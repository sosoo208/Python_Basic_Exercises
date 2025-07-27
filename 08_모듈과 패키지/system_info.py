import os
import sys

env_path = os.environ.get('PATH', '')
file_path = '/Users/username/documents/report.txt'
directory = os.path.dirname(file_path)
filename = os.path.basename(file_path)
name, extension = os.path.splitext(filename)
exists = os.path.exists(file_path)

print(f"현재 작업 디렉토리 : {os.getcwd()}")
print(f"Python 버전 : {sys.version}")
print(f"운영체제 : {os.name}")
print("환경 변수 PATH 일부:", ':'.join(env_path.split(':')[:4]))
print("파일 경로 정보:")
print("- 디렉토리:", directory)
print("- 파일명:", filename)
print("- 확장자:", extension)
print("파일 존재 여부:", exists)
