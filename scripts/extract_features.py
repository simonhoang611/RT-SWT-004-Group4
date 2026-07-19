import pandas as pd
import os
import shutil
import glob
import argparse

def main():
    parser = argparse.ArgumentParser(description="Extract exact 261 feature files based on the ground truth manifest.")
    parser.add_argument("--manifest", default=os.path.join("data", "full_ground_truth.csv"), help="Path to the sample manifest (ground truth CSV)")
    parser.add_argument("--repos", default=os.path.join("tmp", "repos"), help="Path to cloned repositories")
    parser.add_argument("--output", default=os.path.join("data", "raw"), help="Output directory for extracted feature files")
    args = parser.parse_args()

    BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    manifest_path = os.path.abspath(args.manifest)
    raw_dir = os.path.abspath(args.output)
    repo_dir = os.path.abspath(args.repos)

    if not os.path.exists(manifest_path):
        print(f"Error: Manifest file not found at {manifest_path}")
        return

    df = pd.read_csv(manifest_path)

    proj_to_repo = {
        'Sylius': 'Sylius',
        'Apache Fineract': 'fineract',
        'Diaspora': 'diaspora'
    }

    proj_to_raw = {
        'Sylius': 'Sylius_Ecommerce',
        'Apache Fineract': 'Apache_Fineract_Finance',
        'Diaspora': 'Diaspora_Social_Network'
    }

    print("Cleaning up old files in data/raw/ ...")
    for raw_folder in proj_to_raw.values():
        folder_path = os.path.join(raw_dir, raw_folder)
        if os.path.exists(folder_path):
            for f in glob.glob(os.path.join(folder_path, '*.feature')):
                os.remove(f)

    count = 0
    not_found = 0

    print("Extracting files based on manifest...")
    for idx, row in df.iterrows():
        proj = row['project_name']
        url = row['github_file_url']
        
        if pd.isna(url):
            continue
            
        parts = url.split('/blob/')
        if len(parts) < 2:
            continue
        
        branch_and_path = parts[1]
        rel_path = branch_and_path.split('/', 1)[1]
        rel_path = rel_path.replace('/', os.sep)
        
        src_file = os.path.join(repo_dir, proj_to_repo.get(proj, ""), rel_path)
        
        if os.path.exists(src_file):
            out_name = row['expert_filename']
            dest_file = os.path.join(raw_dir, proj_to_raw[proj], out_name)
            
            # Handle duplicates
            if os.path.exists(dest_file):
                name, ext = os.path.splitext(out_name)
                dest_file = os.path.join(raw_dir, proj_to_raw[proj], f"{name}_{row['id']}{ext}")
                
            os.makedirs(os.path.dirname(dest_file), exist_ok=True)
            shutil.copy2(src_file, dest_file)
            count += 1
        else:
            print(f"File not found in repos: {src_file}")
            not_found += 1

    print(f"Successfully extracted {count} files from repos to {raw_dir}.")
    if not_found > 0:
        print(f"WARNING: {not_found} files were not found in the cloned repositories.")

if __name__ == "__main__":
    main()
