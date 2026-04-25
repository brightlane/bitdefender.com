import json
import random
import time
from datetime import datetime

# -----------------------------
# Load posts
# -----------------------------
def load_posts():
    with open("posts.json", "r") as file:
        return json.load(file)

# -----------------------------
# Replace this with real API call
# -----------------------------
def post_to_social_media(text):
    """
    Replace this function with:
    - X (Twitter) API (tweepy)
    - Facebook Graph API
    - Instagram Graph API
    """

    print("\n========================")
    print(f"POST TIME: {datetime.now()}")
    print("------------------------")
    print(text)
    print("========================\n")

# -----------------------------
# Choose and post one message
# -----------------------------
def run_post():
    posts = load_posts()
    post = random.choice(posts)
    post_to_social_media(post["text"])

# -----------------------------
# Run daily loop
# -----------------------------
def start_scheduler(interval_seconds=86400):
    while True:
        run_post()

        # 24 hours = 86400 seconds
        time.sleep(interval_seconds)

if __name__ == "__main__":
    start_scheduler()
