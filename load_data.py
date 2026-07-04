import json

# Read the mock dataset
with open('mock_data.json', 'r', encoding='utf-8') as f:
    posts = json.load(f)

print(f"✅ Total posts loaded: {len(posts)}")
print(f"\n📌 First post preview:")
print(f"   Platform: {posts[0]['platform']}")
print(f"   Poster: {posts[0]['poster_name']}")
print(f"   Content: {posts[0]['post_content'][:80]}...")