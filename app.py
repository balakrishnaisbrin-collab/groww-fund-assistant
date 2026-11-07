import streamlit as st
import os
import re

# Page Configuration - Must be the very first Streamlit command
st.set_page_config(page_title="Groww SBI MF Pro Assistant", layout="wide")

# Custom CSS for Premium Glassmorphism & Neon Glow UI
def apply_custom_styles():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

        /* 1. Main Background with Top Radial Spotlight */
        .stApp {
            background-color: #070913;
            background-image: 
                radial-gradient(at 50% 0%, rgba(99, 102, 241, 0.18) 0px, transparent 55%),
                radial-gradient(at 85% 15%, rgba(6, 182, 212, 0.12) 0px, transparent 45%);
            color: #F8FAFC;
            font-family: 'Inter', sans-serif;
        }

        /* 2. Glassmorphic Hero Banner with Inner Lighting */
        .header-banner {
            background: linear-gradient(135deg, rgba(30, 27, 75, 0.75) 0%, rgba(15, 23, 42, 0.85) 50%, rgba(8, 51, 68, 0.7) 100%);
            backdrop-filter: blur(16px);
            border: 1px solid rgba(99, 102, 241, 0.35);
            padding: 28px 34px;
            border-radius: 20px;
            margin-bottom: 24px;
            box-shadow: 0 20px 40px -15px rgba(0, 0, 0, 0.7), 
                        0 0 35px rgba(99, 102, 241, 0.15) inset;
            display: flex;
            align-items: center;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 16px;
        }
        .header-left {
            display: flex;
            align-items: center;
            gap: 18px;
        }
        .logo-box {
            width: 54px;
            height: 54px;
            border-radius: 14px;
            background: linear-gradient(135deg, #6366F1, #06B6D4);
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 700;
            font-size: 24px;
            color: white;
            box-shadow: 0 0 20px rgba(6, 182, 212, 0.5);
        }
        .header-banner h1 {
            color: #FFFFFF !important;
            font-size: 2.1rem !important;
            font-weight: 700 !important;
            margin: 0 !important;
            letter-spacing: -0.5px;
        }
        .header-banner p {
            color: #94A3B8 !important;
            font-size: 0.95rem !important;
            margin: 4px 0 0 0 !important;
        }
        .status-pill {
            background: rgba(6, 182, 212, 0.12);
            border: 1px solid rgba(6, 182, 212, 0.45);
            color: #22D3EE;
            padding: 8px 16px;
            border-radius: 999px;
            font-size: 0.85rem;
            font-weight: 500;
            box-shadow: 0 0 15px rgba(6, 182, 212, 0.2);
            white-space: nowrap;
        }

        /* 3. Frosted Glass Metric Cards */
        div[data-testid="stMetric"] {
            background: rgba(30, 41, 59, 0.45);
            border: 1px solid rgba(255, 255, 255, 0.08);
            padding: 16px 22px;
            border-radius: 16px;
            backdrop-filter: blur(10px);
            transition: all 0.3s ease;
        }
        div[data-testid="stMetric"]:hover {
            border-color: rgba(99, 102, 241, 0.45);
            box-shadow: 0 0 20px rgba(99, 102, 241, 0.15);
        }
        div[data-testid="stMetricLabel"] p {
            color: #94A3B8 !important;
            font-weight: 600 !important;
            letter-spacing: 0.5px;
        }
        div[data-testid="stMetricValue"] {
            font-size: 32px !important;
            font-weight: 700 !important;
            color: #38BDF8 !important;
        }

        /* 4. Pill-Shaped Example Buttons with Hover Lighting */
        div.stButton > button {
            background: rgba(15, 23, 42, 0.75) !important;
            color: #E2E8F0 !important;
            border: 1px solid rgba(99, 102, 241, 0.4) !important;
            border-radius: 999px !important;
            padding: 10px 20px !important;
            font-size: 0.88rem !important;
            font-weight: 500 !important;
            transition: all 0.25s ease-in-out !important;
            box-shadow: 0 0 12px rgba(99, 102, 241, 0.1) inset !important;
        }
        div.stButton > button:hover {
            border-color: #22D3EE !important;
            color: #FFFFFF !important;
            background: rgba(99, 102, 241, 0.2) !important;
            box-shadow: 0 0 20px rgba(6, 182, 212, 0.45), 
                        0 0 12px rgba(99, 102, 241, 0.3) inset !important;
            transform: translateY(-2px);
        }

        /* Primary 'Ask Assistant' Button */
        div.stButton > button[kind="primary"] {
            background: linear-gradient(135deg, #6366F1 0%, #06B6D4 100%) !important;
            color: #FFFFFF !important;
            border: none !important;
            font-weight: 600 !important;
            box-shadow: 0 4px 20px rgba(6, 182, 212, 0.4) !important;
        }

        /* 5. Glowing Input Box on Click/Focus */
        div[data-baseweb="input"] {
            background-color: rgba(15, 23, 42, 0.85) !important;
            border: 1px solid rgba(255, 255, 255, 0.14) !important;
            border-radius: 14px !important;
            transition: all 0.25s ease !important;
        }
        div[data-baseweb="input"]:focus-within {
            border-color: #22D3EE !important;
            box-shadow: 0 0 22px rgba(6, 182, 212, 0.35) !important;
        }

        /* 6. Result Container & Highlight Tags */
        div[data-testid="stVerticalBlockBorderWrapper"] {
            background: rgba(30, 41, 59, 0.45) !important;
            border: 1px solid rgba(255, 255, 255, 0.1) !important;
            border-radius: 16px !important;
            padding: 18px !important;
        }
        .highlight {
            background: rgba(6, 182, 212, 0.2);
            color: #67E8F9;
            border: 1px solid rgba(6, 182, 212, 0.45);
            font-weight: 600;
            padding: 2px 8px;
            border-radius: 6px;
        }

        /* Sidebar Styling */
        section[data-testid="stSidebar"] {
            background-color: #0B0F19;
            border-right: 1px solid rgba(255, 255, 255, 0.06);
        }
        </style>
    """, unsafe_allow_html=True)

apply_custom_styles()

# Upgraded Premium Header Banner
st.markdown("""
    <div class="header-banner">
        <div class="header-left">
            <div class="logo-box">S</div>
            <div>
                <h1>Groww SBI MF Pro Assistant</h1>
                <p>Ask factual questions about SBI schemes. Every answer cites verified official data.</p>
            </div>
        </div>
        <div class="status-pill">● Facts-only. No investment advice.</div>
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
                
                with st.container(border=True):
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
                    \'st.link\_button("Verified Source", urls\[O ])
                    if urls:
                        st.markdown(f"🔗 **Verified Source:** [{urls[0]}]({urls[0]})")
                    
                    with st.expander("View Full Raw Document"):
                        st.text(content)
        
        if matches_found == 0:
            st.error("No direct matches found. Try searching for broader terms like 'expense', 'exit load', or 'lock-in'.")
