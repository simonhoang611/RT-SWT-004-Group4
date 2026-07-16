import os
import csv
import json
import time
import urllib.request
import urllib.error
from datetime import datetime

CLAUDE_API_KEY = "YOUR_CLAUDE_API_KEY"
MODEL = "claude-sonnet-5"
DATA_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FEWSHOT_DIR = os.path.join(DATA_DIR, "fewshot")

def extract_project_templates():
    templates = {}
    mapping = {}
    with open(os.path.join(DATA_DIR, 'full_ground_truth.csv'), 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            proj = row['project_name']
            mapping[row['id']] = proj
            if proj not in templates and row['gherkin_content'].strip() != "":
                templates[proj] = row['gherkin_content']
    return templates, mapping

def call_claude_api(messages_content, log_file, sample_id, max_retries=5):
    url = "https://api.anthropic.com/v1/messages"
    headers = {
        "x-api-key": CLAUDE_API_KEY,
        "anthropic-version": "2023-06-01",
        "content-type": "application/json"
    }
    data = {
        "model": MODEL,
        "max_tokens": 2048,
        "messages": [
            {"role": "user", "content": messages_content}
        ]
    }
    
    for attempt in range(max_retries):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            req = urllib.request.Request(url, data=json.dumps(data).encode("utf-8"), headers=headers, method="POST")
            with urllib.request.urlopen(req, timeout=60) as response:
                res_body = response.read().decode("utf-8")
                res_json = json.loads(res_body)
                
                # Extract text
                text = ""
                for block in res_json.get('content', []):
                    if block.get('type') == 'text':
                        text = block['text'].strip()
                        break
                
                # Extract usage for cost calculation
                usage = res_json.get('usage', {})
                input_tokens = usage.get('input_tokens', 0)
                output_tokens = usage.get('output_tokens', 0)
                resp_model = res_json.get('model', MODEL)
                
                # Claude Sonnet pricing: $3/1M input, $15/1M output
                cost_usd = (input_tokens * 3.0 / 1_000_000) + (output_tokens * 15.0 / 1_000_000)
                
                # Log success
                log_file.write(f"[{timestamp}] ID={sample_id} | model={resp_model} | input_tokens={input_tokens} | output_tokens={output_tokens} | cost=${cost_usd:.6f} | status=SUCCESS\n")
                log_file.flush()
                
                return text, cost_usd
                
        except urllib.error.HTTPError as e:
            err_text = e.read().decode('utf-8')
            if e.code == 429:
                wait = 2 ** attempt
                log_file.write(f"[{timestamp}] ID={sample_id} | model={MODEL} | status=RATE_LIMIT | retry_wait={wait}s\n")
                log_file.flush()
                print(f"    [Rate Limit] Waiting {wait}s...", flush=True)
                time.sleep(wait)
            else:
                log_file.write(f"[{timestamp}] ID={sample_id} | model={MODEL} | status=HTTP_ERROR_{e.code} | error={err_text[:200]}\n")
                log_file.flush()
                time.sleep(2)
        except Exception as e:
            log_file.write(f"[{timestamp}] ID={sample_id} | model={MODEL} | status=ERROR | error={str(e)[:200]}\n")
            log_file.flush()
            time.sleep(2)
    
    log_file.write(f"[{timestamp}] ID={sample_id} | model={MODEL} | status=FAILED_ALL_RETRIES\n")
    log_file.flush()
    return "", 0.0

def clean_gherkin(content):
    if content.startswith("```gherkin"):
        content = content[10:]
    elif content.startswith("```"):
        content = content[3:]
    if content.endswith("```"):
        content = content[:-3]
    return content.strip()

def main():
    print("=" * 60)
    print(" STARTING FEW-SHOT EXPERIMENT (Claude Sonnet 5)")
    print("=" * 60)
    
    templates, project_map = extract_project_templates()
    print("Extracted standard templates:")
    for proj, tpl in templates.items():
        print(f" - {proj}: {len(tpl)} chars")
        
    user_stories = []
    with open(os.path.join(DATA_DIR, 'full_user_stories.csv'), 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            user_stories.append(row)
            
    print(f"Loaded {len(user_stories)} User Stories.")
    
    output_csv = os.path.join(FEWSHOT_DIR, 'full_generated_gherkin.csv')
    log_path = os.path.join(FEWSHOT_DIR, 'full_api_log.txt')
    
    total_cost = 0.0
    
    with open(output_csv, 'w', encoding='utf-8', newline='') as f_out, \
         open(log_path, 'w', encoding='utf-8') as f_log:
        
        f_log.write(f"=== FEW-SHOT EXPERIMENT LOG (Claude Sonnet 5) ===\n")
        f_log.write(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f_log.write(f"Model: {MODEL}\n")
        f_log.write(f"Total samples: {len(user_stories)}\n")
        f_log.write(f"{'='*80}\n\n")
        
        writer = csv.writer(f_out)
        writer.writerow(["id", "user_story", "gherkin_generated"])
        
        for idx, row in enumerate(user_stories, 1):
            sid = row['id']
            story = row['user_story']
            proj = project_map.get(sid, "Sylius")
            template = templates.get(proj, "")
            
            print(f"[{idx}/{len(user_stories)}] Generating Gherkin for ID {sid} (Project: {proj})...", flush=True)
            
            user_msg = (
                f"You are an expert Quality Assurance (QA) Automation Engineer.\n\n"
                f"Based on the following User Story, write a comprehensive and valid Gherkin scenario.\n\n"
                f"To help you understand the specific coding style, domain terminology, and tags used in this project, "
                f"here is an example of a good Gherkin file from the same project:\n\n"
                f"=== EXAMPLE GHERKIN ===\n{template}\n=======================\n\n"
                f"Now, write the Gherkin for this User Story:\n\n{story}\n\n"
                f"ONLY output the Gherkin syntax. Do not output markdown blocks like ```gherkin. Just the raw text."
            )
            
            response, cost = call_claude_api(user_msg, f_log, sid)
            clean_res = clean_gherkin(response)
            total_cost += cost
            
            writer.writerow([sid, story, clean_res])
            f_out.flush()
            
            time.sleep(1)  # Respect rate limits
        
        f_log.write(f"\n{'='*80}\n")
        f_log.write(f"Completed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f_log.write(f"Total API cost: ${total_cost:.6f}\n")
        f_log.write(f"{'='*80}\n")

    print("=" * 60)
    print(f" Successfully generated 100 Few-Shot results (Claude).")
    print(f" Total API cost: ${total_cost:.6f}")
    print(f" CSV: {output_csv}")
    print(f" Log: {log_path}")
    
if __name__ == "__main__":
    main()
