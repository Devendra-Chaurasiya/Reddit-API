import praw
import sys
import io

# Set the encoding to UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Initialize the Reddit API client
reddit = praw.Reddit(
    client_id='YOUR_CLIENT_ID',
    client_secret='YOUR_CLIENT_SECRET',
    user_agent='script:AIChatAssistant:1.0 (by /u/ZealousidealBody6382)',
    username='YOUR_REDDIT_USERNAME',
    password='YOUR_REDDIT_PASSWORD'
)

# Function to monitor comments in a subreddit
def monitor_comments(subreddit_name):
    subreddit = reddit.subreddit(subreddit_name)
    print(f"Monitoring comments in r/{subreddit_name}...")

    for comment in subreddit.stream.comments(skip_existing=True):
        try:
            print(f"New comment: {comment.body}")
        except UnicodeEncodeError:
            print("A comment contains unsupported characters.")

if __name__ == "__main__":
    monitor_comments('all')
