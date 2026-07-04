import os
import sys
import subprocess
from datetime import datetime

def get_ordinal(n):
    if 11 <= (n % 100) <= 13:
        return str(n) + 'th'
    return str(n) + {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')

def update_root_readme(day_str, problem_name):
    readme_path = "README.md"
    if not os.path.exists(readme_path):
        pass # We assume it exists now, but just in case, we leave it alone or append normally
    
    now = datetime.now()
    date_str = f"{get_ordinal(now.day)} {now.strftime('%B')}"
    
    with open(readme_path, "a", encoding="utf-8") as f:
        f.write(f"| {day_str} ({date_str}) | [{problem_name}](./day-{day_str}) |\n")

def create_day_folder(day_num_str, problem_name):
    day_folder = f"day-{day_num_str}"
    os.makedirs(day_folder, exist_ok=True)
    
    # Create solution template
    solution_path = os.path.join(day_folder, "solution.py")
    if not os.path.exists(solution_path):
        with open(solution_path, "w", encoding="utf-8") as f:
            f.write(f"# Day {day_num_str}: {problem_name}\n\n")
            f.write("def solve():\n    pass\n\nif __name__ == '__main__':\n    solve()\n")
            
    # Create README template
    readme_path = os.path.join(day_folder, "README.md")
    if not os.path.exists(readme_path):
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(f"# {problem_name}\n\n")
            f.write("## Problem Statement\n\n\n")
            f.write("## Approach / Thought Process\n\n\n")
            f.write("## Complexity\n\n- Time: \n- Space: \n\n")
            f.write("## What I Learned\n\n\n")

def run_git_commands(day_num_str, problem_name):
    commit_message = f"Day {day_num_str}: {problem_name}"
    
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", commit_message], check=True)
    subprocess.run(["git", "push", "origin", "main"], check=True)

def main():
    if len(sys.argv) >= 3:
        day_num = sys.argv[1]
        problem_name = " ".join(sys.argv[2:])
    else:
        day_num = input("Enter Day Number (e.g., 1): ")
        problem_name = input("Enter Problem Name: ")

    try:
        day_num_int = int(day_num)
        day_num_str = f"{day_num_int:02d}"
    except ValueError:
        day_num_str = day_num

    print(f"Setting up Day {day_num_str}: {problem_name}")
    
    create_day_folder(day_num_str, problem_name)
    update_root_readme(day_num_str, problem_name)
    
    print("Files created and root README updated. Committing to git...")
    try:
        run_git_commands(day_num_str, problem_name)
        print("Successfully committed and pushed!")
    except subprocess.CalledProcessError as e:
        print(f"Git command failed: {e}")
        print("Please check your git configuration and ensure you have pushed an initial commit.")

if __name__ == "__main__":
    main()
