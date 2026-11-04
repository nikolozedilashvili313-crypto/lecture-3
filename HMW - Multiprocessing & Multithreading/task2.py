import threading
import time
import requests

URL = "https://jsonplaceholder.typicode.com/posts"


def send_request(post_id):
  requests.get(f"{URL}/{post_id}")

if __name__ == "__main__":
  threads = []
  start_time = time.time()

  for i in range(1, 101):
    thread = threading.Thread(target=send_request, args=(i,))
    threads.append(thread)
    thread.start()

  for thread in threads:
    thread.join()

  task2_time = time.time() - start_time
  print(f"Task 2 (100 Threads) შესრულების დრო: {task2_time:.4f} წამი")