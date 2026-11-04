import time
import requests
from concurrent.futures import ThreadPoolExecutor

URL = "https://jsonplaceholder.typicode.com/posts"


def send_request(post_id):
  requests.get(f"{URL}/{post_id}")

if __name__ == "__main__":
  task2_time = 1.25

  start_time = time.time()

  with ThreadPoolExecutor(max_workers=10) as executor:
    executor.map(send_request, range(1, 101))

  task3_time = time.time() - start_time

  print(f"Task 2 დრო: {task2_time:.4f} წამი")
  print(f"Task 3 (ThreadPoolExecutor) დრო: {task3_time:.4f} წამი")
  print(
      f"შედარება: Task 2 დროა {task2_time:.4f} წამი, ხოლო Task 3 დროა"
      f" {task3_time:.4f} წამი[cite: 1]."
  )