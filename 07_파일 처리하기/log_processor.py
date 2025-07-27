import logging
import pandas as pd

log_filename = "app.log"

log_format = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename=log_filename, level=logging.DEBUG, format=log_format, encoding='utf-8')

logging.info("프로그램이 시작되었습니다")
logging.warning("메모리 사용량이 높습니다")
logging.error("데이터베이스 연결 실패")
logging.debug("디버깅 메시지입니다")
logging.warning("디스크 공간 부족")
logging.error("파일을 찾을 수 없음")

print("로그 파일이 생성되었습니다.\n")

error_logs = []
warning_logs = []

with open(log_filename, 'r', encoding='utf-8') as f:
    for line in f:
        if " - ERROR - " in line:
            error_logs.append(line.strip())
        elif " - WARNING - " in line:
            warning_logs.append(line.strip())

print("ERROR 레벨 로그들:")
for log in error_logs:
    print(log)

print("\nWARNING 레벨 로그들:")
for log in warning_logs:
    print(log)