import subprocess
import time
import os

file_path = 'C:\\OSSW4\\hyunyoolim\\your_file.txt'  # 파일 경로
repo_path = 'C:\\OSSW4\\hyunyoolim'                 # 저장소 경로
commit_message = 'hyunyoolim'           # 커밋 메시지
branch_name = 'new-hyun'                # 브랜치 이름

try:
    subprocess.run(['git', 'checkout', branch_name], cwd=repo_path, check=True)
    print(f"Checked out to branch {branch_name}")
except subprocess.CalledProcessError as e:
    print(f"오류: {e}")

while True:
    if not os.path.exists(file_path):
        open(file_path, 'w').close()
        print(f"Created file {file_path}")

    with open(file_path, 'a') as f:
        f.write('#\n')
        print(f"Appended to file {file_path}")

    try:
        subprocess.run(['git', 'pull', 'origin', branch_name], cwd=repo_path, check=True)
        print("Pulled latest changes")
        subprocess.run(['git', 'add', file_path], cwd=repo_path, check=True)
        print("Added changes")
        subprocess.run(['git', 'commit', '-m', commit_message], cwd=repo_path, check=True)
        print("Committed changes")
        subprocess.run(['git', 'push', 'origin', branch_name], cwd=repo_path, check=True)
        print("Pushed changes")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

    time.sleep(10)  # 커밋 쿨타임
