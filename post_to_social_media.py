import tweepy
import facebook
from linkedin_api import Linkedin
from datetime import datetime

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

# Define post content
post_content = """
🚨 **Daily Question Time!** 🚨  
Let’s talk **cybersecurity**! 🔐

👉 **Question 1**: *What do you think is the best antivirus software in 2026?*  
With tech always advancing, we need to stay ahead. Which antivirus will dominate the market in a few years? Share your thoughts and predictions!

👉 **Question 2**: *Is Bitdefender worth the hype?*  
I've been hearing a lot about **Bitdefender** lately, but is it actually as good as people say? What’s your experience with it? Pros, cons, and everything in between—let’s discuss!

👉 **Question 3**: *How do you get Bitdefender at the cheapest price?*  
If you’ve got tips on snagging **Bitdefender** for a great deal, drop them below! I’m looking to get the best protection without breaking the bank. 💸  
And for a detailed guide on Bitdefender, check out this page: [https://brightlane.github.io/bitdefender.com/](https://brightlane.github.io/bitdefender.com/)

💬 Let me know what you think in the comments or by DMing me!  
Let’s keep our devices safe and secure together!

#Cybersecurity #Antivirus #Bitdefender #BestAntivirus2026 #TechTips #Security #OnlineProtection #DigitalSafety #SaveOnTech
"""

# Function to post on Twitter
def post_to_twitter():
    auth = tweepy.OAuth1UserHandler(
        twitter_consumer_key, twitter_consumer_secret, 
        twitter_access_token, twitter_access_token_secret
    )
    api = tweepy.API(auth)
    try:
        api.update_status(post_content)
        print(f"Post successfully made to Twitter at {datetime.now()}")
    except tweepy.TweepError as e:
        print(f"Error posting to Twitter: {e}")

# Function to post on Facebook
def post_to_facebook():
    graph = facebook.GraphAPI(access_token=facebook_access_token)
    try:
        graph.put_object(f'{facebook_page_id}/feed', message=post_content)
        print(f"Post successfully made to Facebook at {datetime.now()}")
    except facebook.GraphAPIError as e:
        print(f"Error posting to Facebook: {e}")

# Function to post on LinkedIn
def post_to_linkedin():
    linkedin_api = Linkedin(linkedin_username, linkedin_password)
    try:
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
