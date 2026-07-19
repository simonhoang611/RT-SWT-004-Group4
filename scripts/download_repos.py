import os
import subprocess
import argparse

def run_command(cmd, cwd=None):
    print(f"Running: {' '.join(cmd)}")
    subprocess.run(cmd, cwd=cwd, check=True)

def main():
    parser = argparse.ArgumentParser(description="Download and checkout specific branches of open source repositories.")
    parser.add_argument("--dest", default=os.path.join("tmp", "repos"), help="Destination folder for cloned repositories")
    args = parser.parse_args()

    repos = [
        {"name": "Sylius", "url": "https://github.com/Sylius/Sylius.git", "branch": "2.3"},
        {"name": "fineract", "url": "https://github.com/apache/fineract.git", "branch": "develop"},
        {"name": "diaspora", "url": "https://github.com/diaspora/diaspora.git", "branch": "develop"}
    ]

    base_dir = os.path.abspath(args.dest)
    os.makedirs(base_dir, exist_ok=True)

    for repo in repos:
        repo_dir = os.path.join(base_dir, repo["name"])
        if not os.path.exists(repo_dir):
            print(f"Cloning {repo['name']}...")
            run_command(["git", "clone", "--branch", repo["branch"], repo["url"], repo_dir])
        else:
            print(f"Repository {repo['name']} already exists in {repo_dir}. Checking out branch {repo['branch']}...")
            run_command(["git", "fetch", "origin", repo["branch"]], cwd=repo_dir)
            run_command(["git", "checkout", repo["branch"]], cwd=repo_dir)
            run_command(["git", "pull", "origin", repo["branch"]], cwd=repo_dir)
            
    print("All repositories have been successfully downloaded and checked out to their specific branches.")

if __name__ == "__main__":
    main()
