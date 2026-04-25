import os
from datetime import datetime
import random

AFFILIATE = "https://get.bitdefender.com/6949dd39475d"

topics = [
    "Bitdefender Review 2025",
    "Best Antivirus for Windows",
    "How to Remove Malware Fast",
    "Is Free Antivirus Enough?",
    "Ransomware Protection Guide",
    "Best Cybersecurity Tools",
    "VPN Safety Explained",
    "How Hackers Steal Passwords",
    "Identity Theft Protection Guide",
    "Safe Browsing Tips"
]

def generate_post():
    topic = random.choice(topics)
    date = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

    html = f"""
<!DOCTYPE html>
<html>
<head>
<title>{topic}</title>
<meta name="description" content="{topic} with expert cybersecurity insights.">
</head>

<body style="font-family:Arial;background:#0b0f19;color:white;padding:40px;">

<h1>{topic}</h1>

<p>
Bitdefender is one of the strongest cybersecurity tools available today, protecting millions of users worldwide from malware, ransomware, and phishing attacks.
</p>

<h2>Why It Matters</h2>
<p>
Cyber threats are increasing daily. Using a tool like Bitdefender helps prevent identity theft, data loss, and system damage.
</p>

<h2>Key Protection Features</h2>
<ul>
<li>Real-time malware detection</li>
<li>Ransomware shielding</li>
<li>Anti-phishing protection</li>
<li>Secure VPN browsing</li>
</ul>

<a href="{AFFILIATE}" style="display:inline-block;padding:15px 20px;background:#1e90ff;color:white;text-decoration:none;margin-top:20px;">
👉 Try Bitdefender Now
</a>

<h2>Conclusion</h2>
<p>
Bitdefender provides enterprise-level protection for everyday users.
</p>

<p><small>Affiliate link included.</small></p>

</body>
</html>
"""

    filename = f"posts/post-{date}.html"

    os.makedirs("posts", exist_ok=True)

    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)

    print("Generated:", filename)


# FOREVER LOOP (DAILY MODE)
while True:
    generate_post()
    print("Sleeping 24 hours...")
    import time
    time.sleep(86400)
