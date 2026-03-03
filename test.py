import requests
from bs4 import BeautifulSoup
import urllib.parse
import webbrowser
import re

def play_youtube(video_query):
    search_url = "https://www.youtube.com/results"
    params = {
        "search_query": video_query
    }

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(search_url, params=params, headers=headers)

    # البحث عن أول videoId
    match = re.search(r'"videoId":"([a-zA-Z0-9_-]{11})"', response.text)

    if match:
        video_id = match.group(1)
        video_url = f"https://www.youtube.com/watch?v={video_id}&autoplay=1"
        webbrowser.open(video_url)
        print(f"▶ Playing: {video_query}")
        return

    # Fallback
    webbrowser.open(search_url)
    print(f"🔍 Searching on YouTube: {video_query}")

# ======================
# INPUT من المستخدم
# ======================
video_query = input("🎵 Enter video name to play on YouTube: ")

if video_query.strip():
    play_youtube(video_query)
else:
    print("❌ You must enter a video name!")
