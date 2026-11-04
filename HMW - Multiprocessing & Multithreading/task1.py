import math
import multiprocessing
import time


def compute_factorial(n):
  return math.factorial(n)

if __name__ == "__main__":

  number = 50000

  numbers = [number] * 8

  start_time = time.time()
  single_results = [compute_factorial(n) for n in numbers]
  single_duration = time.time() - start_time
  print(f"Single-process დრო: {single_duration:.4f} წამი")

  start_time = time.time()
  with multiprocessing.Pool() as pool:
    multi_results = pool.map(compute_factorial, numbers)
  multi_duration = time.time() - start_time
  print(f"Multiprocessing დრო: {multi_duration:.4f} წამი")

  print(f"სწრაფია Multiprocessing-ი {single_duration / multi_duration:.2f}-ჯერ"
      if multi_duration > 0
      else "")

