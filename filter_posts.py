import json
from sentence_transformers import SentenceTransformer, util
import torch

# Load the pre-trained NLP model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load mock dataset
def load_posts():
    with open('mock_data.json', 'r', encoding='utf-8') as f:
        posts = json.load(f)
    return posts

# Semantic search function
def search_posts(query, posts, top_k=10):
    """
    Search posts based on semantic similarity
    Returns top_k most relevant posts for the query
    """
    if not query.strip():
        return []
    
    try:
        # Encode the search query
        query_embedding = model.encode(query, convert_to_tensor=True)
        
        # Encode all post contents
        post_contents = [post['post_content'] for post in posts]
        post_embeddings = model.encode(post_contents, convert_to_tensor=True)
        
        # Calculate cosine similarity
        cos_scores = util.pytorch_cos_sim(query_embedding, post_embeddings)[0]
        
        # Get top_k results
        top_results = torch.topk(cos_scores, k=min(top_k, len(posts)))
        
        filtered_posts = []
        for idx, score in zip(top_results[1], top_results[0]):
            post = posts[int(idx)]
            post['relevance_score'] = float(score)
            filtered_posts.append(post)
        
        return filtered_posts
    
    except Exception as e:
        print(f"Error in search: {e}")
        return []

# Test function
def test_search():
    posts = load_posts()
    test_queries = ["AI internship", "Machine Learning", "Pizza recipe"]
    
    print("=" * 60)
    print("TESTING SEMANTIC SEARCH")
    print("=" * 60)
    
    for query in test_queries:
        results = search_posts(query, posts, top_k=3)
        print(f"\n🔍 Query: '{query}'")
        print(f"Found {len(results)} relevant posts:\n")
        
        for i, post in enumerate(results, 1):
            print(f"{i}. [{post['platform']}] {post['poster_name']}")
            print(f"   Score: {post['relevance_score']:.4f}")
            print(f"   Content: {post['post_content'][:80]}...")
            print()

if __name__ == "__main__":
    test_search()