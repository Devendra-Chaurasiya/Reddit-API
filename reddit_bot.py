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

# Dictionary to store predefined phrases and their responses
responses = {
    "best smartphone": "I think the best smartphone right now is the iPhone 15 or the Google Pixel 8.",
    "AI tool": "I recommend trying OpenAI's GPT models or Google’s Vertex AI for machine learning tasks.",
    "good app for names": "You can try using Google Lens or similar apps that help with identifying names in pictures.",
    "latest technology trends": "Some of the latest trends include AI integration, quantum computing, and blockchain technology.",
    "VR gaming recommendations": "For VR gaming, consider trying Half-Life: Alyx or Beat Saber!",
    "best laptop for students": "The MacBook Air M1 is highly recommended for students due to its performance and battery life.",
    "open source software": "Some great open-source software includes GIMP for image editing and Audacity for audio editing.",
    "learning programming languages": "Python is a fantastic starting language due to its simplicity and versatility.",
    "cloud storage solutions": "Google Drive and Dropbox are popular cloud storage solutions for personal and professional use.",
    "best programming language for web development": "JavaScript is widely used for web development alongside HTML and CSS.",
    # Additional phrases can be added here
}

# Function to monitor comments in a subreddit
def monitor_comments(subreddit_name):
    subreddit = reddit.subreddit(subreddit_name)
    print(f"Monitoring comments in r/{subreddit_name}...")

    for comment in subreddit.stream.comments(skip_existing=True):
        try:
            print(f"New comment: {comment.body}")

            # Check for specific phrases and reply
            for phrase, response in responses.items():
                if phrase in comment.body.lower():
                    comment.reply(response)
                    print(f"Replied to a comment about: {phrase}")
                    break  # Exit the loop after replying
            else:
                print("No specific phrase found, moving to the next comment.")

        except UnicodeEncodeError:
            print("A comment contains unsupported characters.")

if __name__ == "__main__":
    subreddit_name = input("Enter the subreddit to monitor (e.g., r/technology or 'all' for all subreddits): ")

    # Start the comment monitoring in a separate thread
    threading.Thread(target=monitor_comments, args=(subreddit_name,), daemon=True).start()

    # Keep the main thread alive to monitor comments
    while True:
        pass
