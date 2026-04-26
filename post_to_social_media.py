import tweepy
import facebook
from linkedin_api import Linkedin
from datetime import datetime
import random

# Twitter API credentials
twitter_consumer_key = 'YOUR_TWITTER_CONSUMER_KEY'
twitter_consumer_secret = 'YOUR_TWITTER_CONSUMER_SECRET'
twitter_access_token = 'YOUR_TWITTER_ACCESS_TOKEN'
twitter_access_token_secret = 'YOUR_TWITTER_ACCESS_TOKEN_SECRET'

# Facebook API credentials
facebook_access_token = 'YOUR_FACEBOOK_ACCESS_TOKEN'
facebook_page_id = 'YOUR_FACEBOOK_PAGE_ID'  # You can get this from your Facebook page's settings

# LinkedIn API credentials
linkedin_username = 'YOUR_LINKEDIN_USERNAME'
linkedin_password = 'YOUR_LINKEDIN_PASSWORD'

# Predefined content for variation (keeping the questions intact)
questions = [
    "What do you think is the best antivirus software in 2026?",
    "Is Bitdefender worth the hype?",
    "How do you get Bitdefender at the cheapest price?"
]

# Add variations for dynamic content (such as new hashtags, etc.)
hashtags = [
    "#Cybersecurity", "#Antivirus", "#Bitdefender", "#BestAntivirus2026", 
    "#TechTips", "#Security", "#OnlineProtection", "#DigitalSafety", "#SaveOnTech"
]

# Function to generate dynamic post content
def generate_post_content():
    timestamp = datetime.now().strftime("%B %d, %Y %H:%M:%S")  # Add timestamp for freshness

    # Randomly select 2 out of the 3 questions to add variety
    selected_questions = random.sample(questions, 2)

    # Choose 3 random hashtags from the list
    selected_hashtags = random.sample(hashtags, 3)

    # Construct the post content with Quora reference
    post_content = f"""
    🚨 **Daily Question Time!** 🚨  
    Let’s talk **cybersecurity**! 🔐

    👉 **Question 1**: *{selected_questions[0]}*  
    👉 **Question 2**: *{selected_questions[1]}*  

    💬 Let me know what you think in the comments or by DMing me!  
    Let’s keep our devices safe and secure together!

    ⏰ Posted on: {timestamp}

    🔗 Join the discussion and answer on my Quora page here: [https://www.quora.com/What-is-the-best-antivirus-in-2026](https://www.quora.com/What-is-the-best-antivirus-in-2026)

    {', '.join(selected_hashtags)}
    """

    return post_content

# Function to post on Twitter
def post_to_twitter():
    auth = tweepy.OAuth1UserHandler(
        twitter_consumer_key, twitter_consumer_secret, 
        twitter_access_token, twitter_access_token_secret
    )
    api = tweepy.API(auth)
    try:
        post_content = generate_post_content()
        api.update_status(post_content)
        print(f"Post successfully made to Twitter at {datetime.now()}")
    except tweepy.TweepError as e:
        print(f"Error posting to Twitter: {e}")

# Function to post on Facebook
def post_to_facebook():
    graph = facebook.GraphAPI(access_token=facebook_access_token)
    try:
        post_content = generate_post_content()
        graph.put_object(f'{facebook_page_id}/feed', message=post_content)
        print(f"Post successfully made to Facebook at {datetime.now()}")
    except facebook.GraphAPIError as e:
        print(f"Error posting to Facebook: {e}")

# Function to post on LinkedIn
def post_to_linkedin():
    linkedin_api = Linkedin(linkedin_username, linkedin_password)
    try:
        post_content = generate_post_content()
        linkedin_api.submit_share(post_content)
        print(f"Post successfully made to LinkedIn at {datetime.now()}")
    except Exception as e:
        print(f"Error posting to LinkedIn: {e}")

# Main function to post to all platforms
def post_to_all():
    post_to_twitter()
    post_to_facebook()
    post_to_linkedin()

if __name__ == "__main__":
    post_to_all()
