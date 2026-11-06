import asyncio
import aiohttp


async def fetch_posts():
  url = "https://jsonplaceholder.typicode.com/posts"
  async with aiohttp.ClientSession() as session:
    async with session.get(url) as response:
      return await response.json()


async def main_task2():
  posts = await fetch_posts()

  filtered_posts = [
      post for post in posts[:20] if post.get("userId") == 1
  ]

  print("მომხმარებლის (userId = 1) პოსტების სათაურები:\n" + "-" * 40)
  for index, post in enumerate(filtered_posts, 1):
    print(f"{index}. {post['title']}")

asyncio.run(main_task2())