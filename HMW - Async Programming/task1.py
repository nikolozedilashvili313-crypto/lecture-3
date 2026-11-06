
import asyncio
import time
import aiohttp
import requests


start_sync = time.time()

sync_results = []
for i in range(1, 11):
  url = f"https://jsonplaceholder.typicode.com/todos/{i}"
  response = requests.get(url)
  sync_results.append(response.json())

end_sync = time.time()
sync_time = end_sync - start_sync
print(f"სინქრონულმა ვერსიამ იმუშავა: {sync_time:.4f} წამში")

async def fetch_todo(session, todo_id):
  url = f"https://jsonplaceholder.typicode.com/todos/{todo_id}"
  async with session.get(url) as response:
    return await response.json()


async def main_task1():
  start_async = time.time()

  async with aiohttp.ClientSession() as session:
    tasks = [fetch_todo(session, i) for i in range(1, 11)]
    await asyncio.gather(*tasks)

  end_async = time.time()
  return end_async - start_async

async_time = asyncio.run(main_task1())
print(f"აინქრონულმა ვერსიამ იმუშავა: {async_time:.4f} წამში")

difference = sync_time - async_time
print( f"„ასინქრონულმა ვერსიამ {difference:.4f} წამით უფრო სწრაფად იმუშავა!“")