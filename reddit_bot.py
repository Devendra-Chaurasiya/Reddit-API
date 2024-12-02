import praw
import openai
import re
import threading
import time
import sys, io

# Set the encoding to UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

# Initialize the Reddit API client
reddit = praw.Reddit(
    client_id='your_client_id',
    client_secret='your_client_secret',
    user_agent='AI_Assistant_Bot/1.0',
    username='your_username',
    password='your_password'
)

# OpenAI API configuration
openai.api_key = "your_openai_api_key"

# Function to generate AI responses
def generate_ai_response(comment_text, post_title=None, post_body=None):
    try:
        # Construct context
        context = (
            f"Post Title: {post_title}\nPost Body: {post_body}\n\nUser Comment: {comment_text}"
            if post_title and post_body
            else comment_text
        )

        # Call OpenAI API
        response = openai.Chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant for Reddit comments."},
                {"role": "user", "content": context},
            ],
            max_tokens=150,
            temperature=0.7,
        )

        return response['choices'][0]['message']['content']

    except Exception as e:
        print(f"Error generating AI response: {e}")
        return "I'm sorry, I couldn't generate a response at the moment."


# Function to extract subreddit or post details from URL
def extract_subreddit_or_post(input_url):
    if "reddit.com" in input_url:
        match = re.search(r"reddit\.com/r/([a-zA-Z0-9_]+)", input_url)
        if match:
            subreddit = match.group(1)
            if "/comments/" in input_url:
                post_id_match = re.search(r"/comments/([a-zA-Z0-9]+)/", input_url)
                if post_id_match:
                    return ("post", subreddit, post_id_match.group(1))
            return ("subreddit", subreddit, None)
    else:
        return ("subreddit", input_url, None)


# Function to monitor comments in a subreddit
def monitor_comments(subreddit_name):
    subreddit = reddit.subreddit(subreddit_name)
    print(f"Monitoring comments in r/{subreddit_name}...")

    for comment in subreddit.stream.comments(skip_existing=True):
        try:
            if comment.author == reddit.user.me():
                continue

            print(f"New comment by {comment.author}: {comment.body}")
            response = generate_ai_response(comment.body)
            comment.reply(response)
            print(f"Replied to comment by {comment.author}")

        except praw.exceptions.RedditAPIException as e:
            if "RATELIMIT" in str(e):
                wait_time = int(re.search(r"(\d+)", str(e)).group(1)) + 1
                print(f"Rate limit hit. Waiting for {wait_time} seconds.")
                time.sleep(wait_time)
            else:
                print(f"Reddit API Exception: {e}")

        except Exception as e:
            print(f"Error while replying: {e}")


# Function to monitor a specific post by ID
def reply_to_post(subreddit_name, post_id):
    submission = reddit.submission(id=post_id)
    post_title = submission.title
    post_body = submission.selftext
    print(f"Monitoring the post: {post_title}")

    submission.comments.replace_more(limit=0)

    for comment in submission.comments.list():
        try:
            if comment.author == reddit.user.me():
                continue

            print(f"New comment by {comment.author}: {comment.body}")
            response = generate_ai_response(comment.body, post_title, post_body)
            comment.reply(response)
            print(f"Replied to comment by {comment.author}")

        except praw.exceptions.RedditAPIException as e:
            if "RATELIMIT" in str(e):
                wait_time = int(re.search(r"(\d+)", str(e)).group(1)) + 1
                print(f"Rate limit hit. Waiting for {wait_time} seconds.")
                time.sleep(wait_time)
            else:
                print(f"Reddit API Exception: {e}")

        except Exception as e:
            print(f"Error while replying: {e}")


# Main function
if __name__ == "__main__":
    input_url = input("Enter a subreddit name, subreddit URL, or post URL: ")
    input_type, subreddit_name, post_id = extract_subreddit_or_post(input_url)

    if input_type == "subreddit":
        threading.Thread(target=monitor_comments, args=(subreddit_name,), daemon=True).start()
    elif input_type == "post":
        reply_to_post(subreddit_name, post_id)

    while True:
        pass
