# News Summarizer and Categorizer

A Streamlit web application that fetches news articles based on a user-provided topic, summarizes them using the LLaMA language model and categorizes the summaries into predefined categories such as Technology, Health, Finance, Sports, Entertainment, and Science.

## Features

- **Fetch News**: Retrieve news articles from various sources using the News API.
- **Summarize Articles**: Automatically summarize the content of news articles using the LLaMA language model.
- **Categorize Summaries**: Classify the summarized content into predefined categories for easy organization and analysis.

## Getting Started

Clone the repository and install the necessary dependencies to run the application locally.

### Setting Up Your Environment

1. **Get a News API Key**: 
   - Sign up at [News API](https://newsapi.org/register) to get a free API key.

2. **Hide Your API Key**:
   - Create a file named `.env` in the root directory of the project.
   - Add your API key to this file with the following format:
     ```
     NEWS_API_KEY=your_news_api_key_here
     ```
   - The `.env` file is used to store environment variables securely and should **not** be committed to version control. Ensure your `.gitignore` file includes `.env` to keep your API key safe.

### Running the Application

 **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/news-summarizer.git
   cd news-summarizer
   ```

### Technologies Used

- **Streamlit**: This is for building the web interface.
- **LLaMA Model**: For text summarization and categorization.
- **News API**: For fetching news articles.
- **Python**: For scripting and integration.

### License

This project is licensed under the MIT License, making it free to use, modify, and distribute.

### Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue to improve the project.


