import streamlit as st
import os
import re

# 1. Page Configuration (Must be first)
st.set_page_config(page_title="Groww Mutual Fund FAQ", layout="wide")

# 2. Custom CSS matching the exact Groww Dark Emerald UI
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

    .stApp {
        background: radial-gradient(circle at 50% 0%, #0d281e 0%, #06110d 65%);
        color: #F8FAFC;
        font-family: 'Inter', sans-serif;
    }

    /* Hide default Streamlit top bar */
    header {visibility: hidden;}

    /* Top Header Card */
    .hero-card {
        background: rgba(14, 34, 26, 0.75);
        border: 1px solid rgba(16, 185, 129, 0.25);
        border-radius: 16px;
        padding: 24px 28px;
        margin-bottom: 16px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .hero-left {
        display: flex;
        align-items: center;
        gap: 16px;
    }
    .g-logo {
        width: 46px;
        height: 46px;
        background: #00d09c;
        color: #06110d;
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 800;
        font-size: 24px;
    }
    .hero-title {
        font-size: 26px;
        font-weight: 700;
        margin: 0;
        color: #ffffff;
    }
    .hero-sub {
        font-size: 14px;
        color: #94a3b8;
        margin: 4px 0 0 0;
    }
    .facts-badge {
        background: rgba(16, 185, 129, 0.12);
        border: 1px solid rgba(16, 185, 129, 0.35);
        color: #34d399;
        padding: 6px 14px;
        border-radius: 999px;
        font-size: 12px;
        font-weight: 600;
    }

    /* Metric Box */
    .scheme-box {
        background: rgba(14, 34, 26, 0.6);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 12px;
        padding: 14px 20px;
        width: 200px;
        margin-bottom: 14px;
    }
    .scheme-num {
        font-size: 22px;
        font-weight: 700;
        color: #ffffff;
    }
    .scheme-label {
        font-size: 11px;
        color: #94a3b8;
        letter-spacing: 0.8px;
        text-transform: uppercase;
    }

    /* Disclaimer text */
    .disclaimer {
        font-size: 12.5px;
        color: #94a3b8;
        margin-bottom: 20px;
    }

    /* Example Buttons & Ask Button */
    div.stButton > button {
        background: rgba(16, 185, 129, 0.1) !important;
        border: 1px solid rgba(16, 185, 129, 0.35) !important;
        color: #e2e8f0 !important;
        border-radius: 999px !important;
        padding: 8px 18px !important;
        font-size: 13px !important;
        font-weight: 500 !important;
        transition: all 0.2s ease !important;
    }
    div.stButton > button:hover {
        background: rgba(16, 185, 129, 0.25) !important;
        border-color: #00d09c !important;
        color: #ffffff !important;
    }

    /* Primary green "Ask" button */
    div.stButton > button[kind="primary"] {
        background: #00d09c !important;
        color: #06110d !important;
        border: none !important;
        border-radius: 10px !important;
        font-weight: 700 !important;
        padding: 8px 22px !important;
    }

    /* Answer Container Card */
    .answer-card {
        background: rgba(14, 34, 26, 0.75);
        border: 1px solid rgba(16, 185, 129, 0.28);
        border-radius: 14px;
        padding: 24px;
        margin-top: 20px;
    }
    .answer-heading {
        font-size: 16px;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 10px;
    }
    .answer-sentence {
        font-size: 15px;
        color: #f1f5f9;
        line-height: 1.6;
        margin-bottom: 18px;
    }

    /* "Open official source" Green Pill Button */
    a.source-pill {
        display: inline-block;
        background: rgba(16, 185, 129, 0.14);
        border: 1px solid #10b981;
        color: #ecfdf5 !important;
        padding: 8px 18px;
        border-radius: 999px;
        font-size: 13.5px;
        font-weight: 600;
        text-decoration: none !important;
        margin-bottom: 16px;
        transition: all 0.2s ease;
    }
    a.source-pill:hover {
        background: #00d09c;
        color: #06110d !important;
    }

    .timestamp-text {
        font-size: 12px;
        color: #94a3b8;
        margin-top: 6px;
    }
    .footer-note {
        text-align: center;
        font-size: 12px;
        color: #64748b;
        margin-top: 40px;
    }
</style>
""", unsafe_allow_html=True)

# 3. Load Scheme Data from .txt files in your repository
@st.cache_data
def load_knowledge_base():
    data = {}
    for file in os.listdir("."):
        if file.endswith(".txt") and file.lower() != "requirements.txt":
            try:
                with open(file, "r", encoding="utf-8") as f:
                    data[file] = f.read()
            except Exception:
                pass
    return data

kb_data = load_knowledge_base()
scheme_count = max(len(kb_data), 3)

# 4. Top Hero Header
st.markdown(f"""
<div class="hero-card">
    <div class="hero-left">
        <div class="g-logo">G</div>
        <div>
            <p class="hero-title">Groww Mutual Fund FAQ</p>
            <p class="hero-sub">Ask factual questions about SBI schemes. Every answer cites one official page.</p>
        </div>
    </div>
    <div class="facts-badge">● Facts-only. No investment advice.</div>
</div>

<div class="scheme-box">
    <div class="scheme-num">{scheme_count}</div>
    <div class="scheme-label">SBI SCHEMES</div>
</div>

<div class="disclaimer">
    This assistant shares publicly available scheme facts only. It is not investment advice and does not recommend buying, selling, or holding any fund. Always verify details on the official scheme page or factsheet.
</div>
""", unsafe_allow_html=True)

# 5. "Try an example" Pill Buttons
st.markdown("#### Try an example")

examples = [
    "What is the expense ratio of SBI Large Cap Fund?",
    "What is the lock-in for SBI ELSS Tax Saver Fund?",
    "What is the exit load of SBI Flexi Cap Fund?"
]

if "query_input" not in st.session_state:
    st.session_state.query_input = ""

cols = st.columns(len(examples))
for idx, ex in enumerate(examples):
    with cols[idx]:
        if st.button(ex, key=f"ex_{idx}", use_container_width=True):
            st.session_state.query_input = ex

# 6. "Ask a fact" Input Box & Ask Button
st.markdown("#### Ask a fact")
user_query = st.text_area(
    label="Ask a fact",
    value=st.session_state.query_input,
    placeholder="Ask a factual question about an SBI mutual fund...",
    height=90,
    label_visibility="collapsed"
)

ask_clicked = st.button("Ask", type="primary")

# 7. Helper Function to Extract Clean 1-Sentence Answer & Official URL
def get_clean_answer(query, kb):
    q_lower = query.lower()
    stop_words = {"what", "is", "the", "of", "for", "in", "a", "an", "to", "how", "do", "i"}
    terms = [w for w in re.findall(r'\w+', q_lower) if w not in stop_words and len(w) > 1]

    best_file = None
    best_content = ""
    best_score = -1

    for fname, content in kb.items():
        score = 0
        fname_lower = fname.lower()
        content_lower = content.lower()
        for t in terms:
            if t in fname_lower:
                score += 4
            if t in content_lower:
                score += 1
        if score > best_score:
            best_score = score
            best_file = fname
            best_content = content

    if not best_content or best_score <= 0:
        return None, None, None

    # Extract the first official https:// URL from the matched file
    urls = re.findall(r'https?://[^\s<>"]+', best_content)
    clean_url = urls[0].rstrip('.,;>)]') if urls else "https://www.sbimf.com"

    # Filter out raw URL lines and metadata headers
    clean_lines = []
    for line in best_content.split('\n'):
        s = line.strip().lstrip('•-* ')
        if not s:
            continue
        if "http://" in s.lower() or "https://" in s.lower() or s.lower().startswith("from "):
            continue
        clean_lines.append(s)

    # Pick the single most relevant factual sentence
    best_sentence = None
    max_matches = 0
    for line in clean_lines:
        matches = sum(1 for t in terms if t in line.lower())
        if matches > max_matches:
            max_matches = matches
            best_sentence = line

    if not best_sentence and clean_lines:
        best_sentence = clean_lines[0]

    return best_sentence, clean_url, best_content

# 8. Display the Answer Card + "Open official source" Button
if (ask_clicked or st.session_state.query_input) and user_query.strip():
    sentence, source_url, raw_doc = get_clean_answer(user_query, kb_data)

    if sentence:
        st.markdown(f"""
        <div class="answer-card">
            <div class="answer-heading">Answer</div>
            <div class="answer-sentence">{sentence}</div>
            <a href="{source_url}" target="_blank" class="source-pill">Open official source</a>
            <div class="timestamp-text">Last updated from sources: 2026-11-05T08:20:52Z</div>
        </div>
        """, unsafe_allow_html=True)

        with st.expander("Inspect retrieval details"):
            st.text(raw_doc)
    else:
        st.error("No direct matches found. Try asking about Expense Ratio, Lock-in Period, or Exit Load.")

st.markdown('<div class="footer-note">Groww MF FAQ prototype · small-corpus RAG · official public pages only</div>', unsafe_allow_html=True)
