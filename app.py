import streamlit as st
from googlesearch import search

# Page configuration
st.set_page_config(page_title="🔍 Google Search Bot", layout="centered")
st.markdown("""
    <style>
    .search-box {
        padding: 2rem;
        background-color: #f0f2f6;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        text-align: center;
    }
    .result-card {
        padding: 1rem;
        margin-bottom: 1rem;
        background-color: #ffffff;
        border-radius: 10px;
        box-shadow: 0 3px 8px rgba(0,0,0,0.05);
    }
    .footer {
        margin-top: 2rem;
        font-size: 0.85rem;
        color: #888;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🤖 Google Search App")
st.write("Search Google results right from this app using Python + Streamlit!")

# Input area in styled div
with st.container():
    st.markdown('<div class="search-box">', unsafe_allow_html=True)
    query = st.text_input("🔍 Type your search query", placeholder="e.g., What is DevOps?")
    num_results = st.slider("🔢 Number of results", min_value=1, max_value=20, value=5)
    search_button = st.button("🚀 Search Now")
    st.markdown('</div>', unsafe_allow_html=True)

# Perform search and show results
if search_button:
    if not query.strip():
        st.warning("⚠️ Please enter a valid search query.")
    else:
        try:
            with st.spinner("🔎 Searching Google..."):
                results = list(search(query, num_results=num_results))

            st.success(f"📌 Found {len(results)} results for **'{query}'**:")

            for i, result in enumerate(results, start=1):
                st.markdown(f"""
                <div class="result-card">
                    <b>{i}. <a href="{result}" target="_blank">{result}</a></b>
                </div>
                """, unsafe_allow_html=True)

        except Exception as e:
            st.error(f"❌ An error occurred: {str(e)}")

# Footer
st.markdown('<div class="footer">Powered by Python & googlesearch • Created by Pradeep 🧠</div>', unsafe_allow_html=True)
