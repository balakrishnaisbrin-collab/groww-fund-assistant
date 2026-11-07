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
        div[data-testid="stMetricValue"] {
            font-size: 30px !important;
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

# Upgraded Premium Header Banner (Matches Fellowmate's Layout with Your Own Identity)
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
