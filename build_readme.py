import feedparser
from datetime import datetime, timezone

README_FILE = "README.md"
RSS_FEED_URL = "https://sameeramadushan.me/rss.xml"
MAX_POSTS = 3

feed = feedparser.parse(RSS_FEED_URL)

posts_md = "\n".join([f"* [{entry.title}]({entry.link})" for entry in feed.entries[:MAX_POSTS]])

now = datetime.now(timezone.utc)

day = str(int(now.strftime("%d")))
timestamp = now.strftime(f"%A, {day} %B, %H:%M UTC")

with open(README_FILE, "r", encoding="utf-8") as f:
    readme_contents = f.read()

blog_start = "<!-- blog starts -->"
blog_end = "<!-- blog ends -->"
start_index = readme_contents.find(blog_start) + len(blog_start)
end_index = readme_contents.find(blog_end)

readme_contents = readme_contents[:start_index] + "\n" + posts_md + "\n" + readme_contents[end_index:]

import re
readme_contents = re.sub(
    r"Last refresh: .*",
    f"Last refresh: {timestamp}",
    readme_contents
)

with open(README_FILE, "w", encoding="utf-8") as f:
    f.write(readme_contents)

print("README.md updated successfully!")
