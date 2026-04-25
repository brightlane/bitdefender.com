import json
import requests
from datetime import datetime
import os

QUEUE_FILE = "queue.json"

MASTODON_INSTANCE = os.environ["MASTODON_INSTANCE"]
MASTODON_TOKEN = os.environ["MASTODON_TOKEN"]

def load_queue():
    with open(QUEUE_FILE, "r") as f:
        return json.load(f)

def save_queue(queue):
    with open(QUEUE_FILE, "w") as f:
        json.dump(queue, f, indent=2)

# -----------------------------
# REAL SOCIAL MEDIA POST
# -----------------------------
def post_to_social_media(text):
    url = f"{MASTODON_INSTANCE}/api/v1/statuses"

    headers = {
        "Authorization": f"Bearer {MASTODON_TOKEN}"
    }

    data = {
        "status": text
    }

    response = requests.post(url, headers=headers, data=data)

    if response.status_code != 200:
        raise Exception(f"Failed to post: {response.text}")

    return response.json()

def run_poster():
    queue = load_queue()

    for item in queue:
        if item["status"] == "pending":

            result = post_to_social_media(item["text"])

            item["status"] = "posted"
            item["posted_at"] = str(datetime.now())
            item["post_id"] = result.get("id")

            save_queue(queue)

            print("POSTED SUCCESSFULLY:", result.get("url"))
            break

if __name__ == "__main__":
    run_poster()
