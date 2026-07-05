# 🔍 AI-Powered Social Media Post Filter

## Project Overview

An intelligent AI/ML-based application that filters social media posts from multiple platforms (Instagram, Facebook, LinkedIn) using Natural Language Processing (NLP) and semantic search.

## Features

- **Semantic Search**: Uses NLP to find posts based on meaning, not just keywords
- **Multi-Platform Support**: Processes posts from Instagram, Facebook, and LinkedIn
- **Intelligent Filtering**: Distinguishes between relevant and irrelevant posts
- **User-Friendly Interface**: Streamlit-based web interface with real-time search
- **Relevance Scoring**: Shows relevance score (0-100%) for each result

## Tech Stack

- **Language**: Python 3.14
- **NLP Model**: sentence-transformers (all-MiniLM-L6-v2)
- **Frontend**: Streamlit
- **Data Format**: JSON
- **Version Control**: Git & GitHub

## Project Structure

```
ai-ml-social-post-filter/
├── mock_data.json              # 40 fake social media posts
├── filter_posts.py             # AI filtering logic
├── app.py                      # Streamlit web interface
├── load_data.py                # Data loader script
├── test.py                     # Test script
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

## Installation & Setup

### Prerequisites

- Python 3.10+
- pip (Python package manager)

### Steps

1. Clone the repository:

```bash
git clone https://github.com/gautamdabhi09/ai-ml-social-post-filter.git
cd ai-ml-social-post-filter
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
python -m streamlit run app.py
```

4. Open browser and go to `http://localhost:8501`

## How It Works

### Data

- Mock dataset contains 40 realistic social media posts
- 20 posts related to AI/ML/Internship topics
- 20 unrelated posts for testing accuracy

### Filtering Algorithm

1. **Query Encoding**: Converts user search query to vector embedding
2. **Content Encoding**: Converts each post content to vector embedding
3. **Similarity Calculation**: Uses cosine similarity to find relevant posts
4. **Ranking**: Returns top results sorted by relevance score

### Example Searches

- "AI internship" → Returns AI/ML posts
- "Machine Learning" → Returns ML/Data Science posts
- "Pizza recipe" → Returns food/cooking posts

## Performance

- Response time: < 2 seconds
- Accuracy: Successfully filters relevant vs irrelevant posts
- Handles 40+ posts efficiently

## Testing

Run the test script:

```bash
python filter_posts.py
```

This tests the semantic search with predefined queries.

## Learning Outcomes

- NLP implementation with sentence-transformers
- Semantic search using cosine similarity
- Web app development with Streamlit
- Git/GitHub workflow
- AI/ML model integration

---

**Created as part of AI/ML Internship Task**
