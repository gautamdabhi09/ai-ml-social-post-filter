import streamlit as st
import json
from filter_posts import search_posts, load_posts

# Page config
st.set_page_config(
    page_title="Social Media Post Filter",
    page_icon="🔍",
    layout="wide"
)

# Title
st.title("🔍 AI-Powered Social Media Post Filter")
st.markdown("Search across Instagram, Facebook, and LinkedIn using intelligent AI filtering")

# Load posts
@st.cache_resource
def get_posts():
    return load_posts()

posts = get_posts()

# Sidebar
st.sidebar.header("📊 Statistics")
st.sidebar.metric("Total Posts", len(posts))
st.sidebar.markdown("---")
st.sidebar.info("This app uses NLP to find semantically relevant posts, not just keyword matches.")

# Search section
st.markdown("---")
col1, col2 = st.columns([4, 1])

with col1:
    search_query = st.text_input(
        "🔎 Search Posts",
        placeholder="e.g., 'AI Internship', 'Machine Learning', 'Python Developer'",
        help="Enter your search query"
    )

with col2:
    num_results = st.selectbox("Results", [5, 10, 15, 20], index=1)

# Display results
if search_query:
    st.markdown("---")
    st.subheader(f"Search Results for: '{search_query}'")
    
    # Search
    results = search_posts(search_query, posts, top_k=num_results)
    
    if results:
        st.success(f"✅ Found {len(results)} relevant posts")
        
        # Display each result
        for idx, post in enumerate(results, 1):
            # Create columns for better layout
            col1, col2 = st.columns([1, 4])
            
            with col1:
                st.image(post['poster_image'], width=100)
            
            with col2:
                # Post header
                st.markdown(f"**{idx}. {post['poster_name']}** · {post['platform']}")
                st.markdown(f"*Posted on: {post['timestamp'][:10]}*")
                
                # Post content
                st.write(post['post_content'])
                
                # Relevance score
                score = post['relevance_score']
                st.metric("Relevance Score", f"{score:.2%}")
            
            st.markdown("---")
    else:
        st.warning("❌ No relevant posts found for your search.")

else:
    st.info("👆 Enter a search query above to get started!")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
    <p><small>AI/ML Internship Task | Social Media Post Filtering System</small></p>
</div>
""", unsafe_allow_html=True)