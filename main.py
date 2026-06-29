import time
from datetime import datetime

print("파이썬 애플리케이션이 시작되었습니다.")

while True:
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"[{now}] Hello World! 젠킨스 배포 테스트 중...")
    time.sleep(5)

