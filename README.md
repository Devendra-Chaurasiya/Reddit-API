### **AI Reddit Engagement Bot**

---

### **Overview**  
The **AI Reddit Engagement Bot** is a Python-powered script designed to interact with Reddit communities using OpenAI's GPT models. The bot can monitor specified subreddits or individual posts, reply to user comments contextually, and enhance engagement by generating meaningful responses based on the content of posts and discussions.

This tool is ideal for automating Reddit interactions, fostering discussions, and even providing product or service recommendations.

---

### **Key Features**
- **Real-Time Comment Monitoring**:  
  Continuously streams and monitors comments in a subreddit or specific post.

- **AI-Powered Replies**:  
  Uses OpenAI's **GPT-4o-mini** model to generate contextually accurate responses to Reddit comments.

- **Flexible Input Handling**:  
  Works with subreddit URLs, post URLs, or subreddit names.

- **Rate Limit Handling**:  
  Implements Reddit's API rate-limiting mechanisms, ensuring smooth and uninterrupted operation.

---

### **Technical Details**
- **Programming Language**: Python  
- **Libraries Used**:  
  - `praw`: Python Reddit API Wrapper for Reddit interactions.  
  - `openai`: Integration with OpenAI's API for generating responses.  
  - Standard libraries like `re`, `time`, and `threading` for processing.

- **Encodings**: UTF-8 for proper handling of special characters and emojis.

---

### **Setup Instructions**
1. **Clone the Repository**:  
   ```bash
   git clone https://github.com/Devendra-Chaurasiya/Reddit-AI-Bot.git
   cd Reddit-AI-Bot
   ```

2. **Install Dependencies**:  
   Ensure Python 3.10+ is installed and run:  
   ```bash
   pip install praw openai
   ```

3. **Set Up Credentials**:
   - Replace placeholders in the script with your **Reddit API credentials**:  
     ```python
     reddit = praw.Reddit(
         client_id='your_client_id',
         client_secret='your_client_secret',
         user_agent='AI_Assistant_Bot/1.0',
         username='your_username',
         password='your_password'
     )
     ```
   - Add your **OpenAI API key**:  
     ```python
     openai.api_key = "your_openai_api_key"
     ```

4. **Run the Script**:  
   ```bash
   python reddit_bot.py
   ```

5. **Input Subreddit or Post URL**:  
   When prompted, provide either a subreddit name, subreddit URL, or post URL to start monitoring.

---

### **How It Works**
1. **Subreddit Monitoring**:  
   - Streams comments in real time using the PRAW library.
   - Automatically generates replies based on context using GPT-4o-mini.

2. **Post Monitoring**:  
   - Monitors all comments under a specific Reddit post.
   - Generates and posts replies to enhance engagement.

3. **Error Handling**:  
   - Gracefully handles rate limits imposed by Reddit's API.
   - Catches exceptions and logs errors for troubleshooting.

---

### **Future Enhancements**
- Implement **NLP techniques** for more accurate sentiment and context detection.
- Expand support for **multiple OpenAI models** for varied use cases.
- Enable **configurable behaviors** for subreddit-specific rules.

---

### **Disclaimer**
- Use responsibly. Ensure the bot complies with Reddit's [API Terms of Service](https://www.redditinc.com/policies/data-api-terms).
- Avoid spamming or violating subreddit rules.
