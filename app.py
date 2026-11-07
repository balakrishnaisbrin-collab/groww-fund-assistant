import streamlit as st
import os
import re

# Page Configuration - Wide layout for a clean dashboard feel
st.set_page_config(page_title="Groww SBI MF Pro Assistant", layout="wide")

# Custom CSS for Groww Theme & UI Enhancements
def apply_custom_styles():
    st.markdown("""
        <style>
        /* Main background */
        .stApp {
            background-color: #212529;
        }
        /* Custom Header Banner */
        .header-banner {
            background-color: #00D09C;
            padding: 30px;
            border-radius: 15px;
            color: white;
            text-align: center;
            margin-bottom: 30px;
        }
        .header-banner h1 {
            color: white !important;
            font-size: 3em !important;
            margin-bottom: 10px;
        }
        /* Metric Card Styling */
        div[data-testid="stMetricValue"] {
            font-size: 35px !important;
            color: #00D09C !important;
        }
        /* Result Container Styling */
        div.stContainer {
            background-color: white;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.08);
            margin-bottom: 20px;
            border-left: 6px solid #00D09C;
        }
        /* Highlight matched text */
        .highlight {
            background-color: #28a745;
            color: white;
            font-weight: bold;
            padding: 2px 6px;
            border-radius: 4px;
        }
        </style>
    """, unsafe_allow_html=True)

apply_custom_styles()

# Header Banner
st.markdown("""
    <div class="header-banner">
        <h1>🌱 Groww SBI MF Pro Assistant</h1>
        <p>Institutional Grade Fact Retrieval Engine • High Precision • Zero Hallucination</p>
    </div>
""", unsafe_allow_html=True)

# Sidebar for Knowledge Base Overview
with st.sidebar:
    st.header("📊 Knowledge Base")
    st.info("Loaded with verified scheme documents.")
    
    txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]
    for idx, file in enumerate(txt_files, 1):
        clean_name = file.replace('.txt', '').replace('_', ' ')
        st.write(f"{idx}. {clean_name}")
        
    st.divider()
    st.warning("⚠️ **Disclaimer:** Facts-only. No investment advice. Verify all data before investing.")

# Load Data Safely
def load_files():
    data = {}
    for file in txt_files:
        try:
            with open(file, 'r', encoding='utf-8') as f:
                data[file] = f.read()
        except Exception as e:
            st.error(f"Error reading {file}: {e}")
    return data

files_data = load_files()

# Top Metrics Row
col_m1, col_m2, col_m3 = st.columns([1, 1, 2])
with col_m1:
    st.metric(label="INDEXED SCHEMES", value=len(files_data))
with col_m2:
    total_chars = sum(len(c) for c in files_data.values())
    st.metric(label="DATA POINTS", value=f"{total_chars:,}")
with col_m3:
    st.success("✨ System Status: Online & Optimized. Ask anything about Expense Ratio, Exit Load, or Returns.")

st.markdown("---")

# Quick Example Buttons
st.subheader("💡 Try an example query")
example_cols = st.columns(3)

if "search_query" not in st.session_state:
    st.session_state.search_query = ""

examples = [
    ("What is the expense ratio of SBI Large Cap Fund?", "expense ratio SBI Large Cap"),
    ("What is the lock-in period for SBI ELSS Tax Saver?", "lock-in period ELSS"),
    ("What is the exit load of SBI Mid Cap Fund?", "exit load Mid Cap")
]

for i, (btn_text, query_val) in enumerate(examples):
    with example_cols[i]:
        if st.button(btn_text, use_container_width=True):
            st.session_state.search_query = query_val
            st.rerun()

# Search Input Section
st.subheader("🔍 Query Console")
user_query = st.text_input(
    "Enter your question below:", 
    value=st.session_state.search_query, 
    placeholder="e.g., What is the riskometer level of SBI Small Cap Fund?"
)

col_action1, col_action2 = st.columns([1, 6])
with col_action1:
    search_clicked = st.button("Ask Assistant", type="primary", use_container_width=True)
with col_action2:
    if st.button("Clear Console", use_container_width=True):
        st.session_state.search_query = ""
        st.rerun()

# Processing Search Results
if search_clicked or user_query:
    if not user_query.strip():
        st.warning("Please enter a valid question.")
    else:
        st.markdown(f"### Results for: **'{user_query}'**")
        query_terms = [w.lower() for w in user_query.split() if len(w) > 2]
        matches_found = 0
        
        for filename, content in files_data.items():
            content_lower = content.lower()
            
            # Check relevance
            if any(term in content_lower for term in query_terms) or any(term in filename.lower() for term in query_terms):
                matches_found += 1
                clean_header = filename.replace('.txt', '').replace('_', ' ').upper()
                
                with st.container():
                    st.markdown(f"#### 📑 {clean_header}")
                    
                    # Highlight matching sentences
                    lines = content.split('\n')
                    highlighted_lines = []
                    for line in lines:
                        if any(term in line.lower() for term in query_terms):
                            for term in query_terms:
                                pattern = re.compile(re.escape(term), re.IGNORECASE)
                                line = pattern.sub(r'<span class="highlight">\g<0></span>', line)
                            highlighted_lines.append(line)
                    
                    if highlighted_lines:
                        for hl in highlighted_lines[:6]:
                            st.markdown(f"• {hl}", unsafe_allow_html=True)
                    else:
                        st.write(content[:350] + "...")
                    
                    # Extract URL
                    urls = re.findall(r'(https?://\S+)', content)
                    if urls:
                        st.markdown(f"🔗 **Verified Source:** [{urls[0]}]({urls[0]})")
                    
                    with st.expander("View Full Raw Document"):
                        st.text(content)
        
        if matches_found == 0:
            st.error("No direct matches found. Try searching for broader terms like 'expense', 'exit load', or 'lock-in'.")
