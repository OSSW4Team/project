import subprocess
import time
import os

file_path = 'C:\\OSSW4\\your_file.txt'  # 경로 확인
repo_path = 'C:\\OSSW4'                 # 경로 확인
commit_message = 'w'                    # 커밋 메시지
branch_name = 'kyokwan'                 # 브랜치 이름
main_branch = 'main'                    # 메인 브랜치 이름
merge_commit_message = 'Kyokwan'        # 머지 커밋 메시지
log_file = 'commit_log.txt'             # 로그 파일 경로

def log_message(message):
    with open(log_file, 'a') as log:
        log.write(message + '\n')

def run_git_command(commands, repo_path):
    try:
        result = subprocess.run(commands, cwd=repo_path, check=True, capture_output=True, text=True)
        log_message(f"COMMAND: {' '.join(commands)}\nOUTPUT: {result.stdout}\nERROR: {result.stderr}")
    except subprocess.CalledProcessError as e:
        log_message(f"ERROR: {e}\nCOMMAND: {' '.join(commands)}\nOUTPUT: {e.stdout}\nERROR: {e.stderr}")
        return False
    return True

def resolve_conflicts(repo_path):
    try:
        subprocess.run(['git', 'add', '-A'], cwd=repo_path, check=True)
        subprocess.run(['git', 'commit', '-m', 'Resolved conflicts'], cwd=repo_path, check=True)
    except subprocess.CalledProcessError as e:
        log_message(f"충돌 해결 중 오류 발생: {e}")

def main_loop():
    while True:
        if not os.path.exists(file_path):
            open(file_path, 'w').close()

        with open(file_path, 'a') as f:
            f.write('#\n')

        try:
            if not run_git_command(['git', 'pull', 'origin', branch_name], repo_path):
                continue

            if not run_git_command(['git', 'add', file_path], repo_path):
                continue

            if not run_git_command(['git', 'commit', '-m', commit_message], repo_path):
                continue

            if not run_git_command(['git', 'push', 'origin', branch_name], repo_path):
                continue

            if not run_git_command(['git', 'checkout', main_branch], repo_path):
                continue

            if not run_git_command(['git', 'pull', 'origin', main_branch], repo_path):
                continue

            # 병합 커밋 메시지 지정
            merge_command = ['git', 'merge', '--no-ff', '-m', merge_commit_message, branch_name]
            if not run_git_command(merge_command, repo_path):
                resolve_conflicts(repo_path)

            if not run_git_command(['git', 'push', 'origin', main_branch], repo_path):
                continue

            if not run_git_command(['git', 'checkout', branch_name], repo_path):
                continue

        except subprocess.CalledProcessError as e:
            log_message(f"An error occurred: {e}")
        time.sleep(30)  # 커밋 쿨타임

if __name__ == "__main__":
    main_loop()
