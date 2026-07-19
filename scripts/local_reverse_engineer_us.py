import os
import time
import pandas as pd
from getpass import getpass
from openai import OpenAI
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn

console = Console()

def main():
    console.print("[bold cyan]=== Reverse Engineering User Stories ===[/bold cyan]")
    
    # Check for API key
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        console.print("[yellow]Mẹo: Bạn có thể click chuột phải để dán (paste) Key vào terminal.[/yellow]")
        api_key = input("Vui lòng nhập OpenAI API Key: ").strip()
        
    client = OpenAI(api_key=api_key)
    
    gt_path = os.path.join("data", "extended_ground_truth.csv")
    tpl_us_path = os.path.join("data", "full_user_stories_261_template.csv")
    out_path = os.path.join("data", "full_user_stories_261.csv")
    
    if not os.path.exists(gt_path) or not os.path.exists(tpl_us_path):
        console.print("[bold red]Lỗi: Không tìm thấy file dữ liệu đầu vào![/bold red]")
        return
        
    df_gt = pd.read_csv(gt_path)
    
    # Đọc file đang làm dở nếu có, không thì đọc template gốc
    if os.path.exists(out_path):
        df_tpl = pd.read_csv(out_path)
        console.print("[green]Tìm thấy file chạy dở, sẽ tự động chạy tiếp![/green]")
    else:
        df_tpl = pd.read_csv(tpl_us_path)
        console.print("[green]Bắt đầu chạy từ đầu bằng file template.[/green]")
    
    # Identify missing or ERROR user stories
    missing_mask = df_tpl['user_story'].isna() | (df_tpl['user_story'] == 'ERROR')
    df_missing = df_gt[missing_mask].copy()
    
    console.print(f"Tổng số mẫu: {len(df_tpl)}")
    console.print(f"Số mẫu cần sinh mới: [bold yellow]{len(df_missing)}[/bold yellow]")
    
    if len(df_missing) == 0:
        console.print("[bold green]Không có mẫu nào cần sinh mới![/bold green]")
        return
        
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TaskProgressColumn(),
        console=console
    ) as progress:
        task = progress.add_task("[cyan]Đang gọi API GPT-5.4-mini...", total=len(df_missing))
        
        for idx, row in df_missing.iterrows():
            prompt = f"""You are a product owner. Given the following BDD Gherkin file from a project named {row['project_name']} (Domain: {row['domain']}), write the original User Story that would have generated these tests.
Format strictly as:
As a [role],
I want to [action],
So that [benefit].

Acceptance Criteria:
- [Criterion 1]
- [Criterion 2]
- ... (Extract as many Acceptance Criteria as necessary to fully cover all the Scenarios in the Gherkin file)

GHERKIN CODE:
{str(row['gherkin_content'])[:15000].replace('\\n', '\n')}
"""
            success = False
            while not success:
                try:
                    response = client.chat.completions.create(
                        model="gpt-5.4-mini-2026-03-17",
                        messages=[
                            {"role": "system", "content": "You write concise Connextra format user stories based on BDD tests."},
                            {"role": "user", "content": prompt}
                        ],
                        temperature=0
                    )
                    story_text = response.choices[0].message.content.strip()
                    success = True
                except Exception as e:
                    console.print(f"[red]Rate Limit/Lỗi ở ID {row['id']} - Đợi 60s để OpenAI nạp lại Token... Lỗi: {str(e)[:100]}[/red]")
                    time.sleep(60) # Wait 60s for TPM reset and retry
                
            # Fill the generated story into the template dataframe
            df_tpl.loc[idx, 'user_story'] = story_text
            
            # Save incrementally just in case it crashes
            df_tpl.to_csv(out_path, index=False, encoding='utf-8')
            
            progress.advance(task)
            time.sleep(1) # Base delay to avoid hitting TPM too fast
            
    console.print(f"[bold green]Hoàn tất! Đã lưu file {out_path}[/bold green]")

if __name__ == "__main__":
    main()
