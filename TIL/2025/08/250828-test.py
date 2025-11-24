import asyncio
import time


# 비동기 작업 정의
async def fetch_data(name, delay):
    await asyncio.sleep(delay)  # 논블로킹 I/O (delay 초 대기)
    print(f"{name} 완료!")


# main 함수
async def main():
    start = time.time()  # 시작 시간 기록

    await asyncio.gather(
        fetch_data("Task1", 2),  # 2초 지연
        fetch_data("Task2", 1),  # 1초 지연
    )

    end = time.time()  # 종료 시간 기록
    print(f"총 실행 시간: {end - start:.2f}초")


# 이벤트 루프 실행
asyncio.run(main())
