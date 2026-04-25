import time
import json
import random
from datetime import datetime
import subprocess

POSTS_FILE = "posts.json"
QUEUE_FILE = "queue.json"

def load_posts():
    with open(POSTS_FILE, "r") as f:
        return json.load(f)["posts"]

def load_queue():
    with open(QUEUE_FILE, "r") as f:
        return json.load(f)

def save_queue(queue):
    with open(QUEUE_FILE, "w") as f:
        json.dump(queue, f, indent=2)

def generate_and_queue():
    posts = load_posts()
    queue = load_queue()

    post = random.choice(posts)

    queue.append({
        "text": post,
        "status": "pending",
        "created_at": str(datetime.now())
    })

    save_queue(queue)

def run_daily(interval_seconds=86400):
    while True:
        print("[1] Generating post...")
        generate_and_queue()

        print("[2] Posting to X...")
        subprocess.run(["python", "poster.py"])

        print("[DONE] Sleeping 24h...\n")
        time.sleep(interval_seconds)

if __name__ == "__main__":
    run_daily()
