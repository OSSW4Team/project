import subprocess
import time
import os

file_path = '/Users/jhg/Desktop/VSVSVSVSCODE/your_file.txt' # C:\\OSSW4 -> 부분만 수정
repo_path = '/Users/jhg/Desktop/VSVSVSVSCODE'                # C:\\OSSW4 -> 부분만 수정
commit_message = 'w'                   # 커밋 메세지
branch_name = 'hwangyu'                # 브랜치 이름
try:
    subprocess.run(['git', 'checkout', branch_name], cwd=repo_path, check=True)
except subprocess.CalledProcessError as e:
    print(f"오류: {e}")

while True:
    if not os.path.exists(file_path):
        open(file_path, 'w').close()

    with open(file_path, 'a') as f:
        f.write('#\n')

    try:
        subprocess.run(['git', 'pull', 'origin', branch_name], cwd=repo_path, check=True)
        subprocess.run(['git', 'add', file_path], cwd=repo_path, check=True)
        subprocess.run(['git', 'commit', '-m', commit_message], cwd=repo_path, check=True)
        subprocess.run(['git', 'push', 'origin', branch_name], cwd=repo_path, check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
    time.sleep(10) # 커밋 쿨타임