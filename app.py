import base64
import io
import streamlit as st
from datetime import datetime
from pathlib import Path
from urllib.parse import quote

try:
    from PIL import Image, ImageDraw
except ImportError:
    Image = None
    ImageDraw = None

# -----------------------------
# App Config
# -----------------------------
st.set_page_config(
    page_title="Anis Mselmi | Portfolio",
    page_icon="🍰",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# -----------------------------
# Theme / UI Styling
# -----------------------------

st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

        :root {
            --bg: #0b0f17;
            --panel: #121826;
            --panel-2: #0f1522;
            --text: #e6ecf2;
            --muted: #9fb0c3;
            --accent: #7c9cff;
            --accent-2: #57e0ff;
            --border: #1f2a3b;
        }

        html {
            scroll-behavior: smooth;
        }

        html, body, [class*="css"] {
            font-family: 'Inter', system-ui, -apple-system, sans-serif;
        }

        .stApp {
            background: radial-gradient(1200px 600px at 10% -10%, #1c2a4a 0%, transparent 60%),
                        radial-gradient(900px 500px at 90% -20%, #1b3140 0%, transparent 55%),
                        var(--bg);
            color: var(--text);
        }

        header[data-testid="stHeader"] {
            background: transparent;
            box-shadow: none;
        }

        section[data-testid="stSidebar"], 
        header[data-testid="stHeader"] {
            display: none !important;
        }

        section[data-testid="stSidebar"] div[data-testid="stSidebarUserContent"] {
            position: sticky;
            top: 0.6rem;
        }

        button[kind="header"][aria-label="View sidebar"],
        button[kind="header"][aria-label="Close sidebar"] {
            display: none !important;
        }

        section[data-testid="stSidebar"] .stSidebarHeader,
        section[data-testid="stSidebar"] .stSidebarHeader div {
            padding-bottom: 0.25rem;
        }

        section[data-testid="stSidebar"] h1,
        section[data-testid="stSidebar"] h2,
        section[data-testid="stSidebar"] h3 {
            font-size: 1.35rem;
        }

        section[data-testid="stSidebar"] p,
        section[data-testid="stSidebar"] span,
        section[data-testid="stSidebar"] label {
            font-size: 1rem;
        }

        section[data-testid="stSidebar"] .stRadio label {
            gap: 0.6rem;
            padding: 0.2rem 0.15rem;
        }

        section[data-testid="stSidebar"] .stRadio div[role="radiogroup"] {
            gap: 0.4rem;
        }

        .block-container {
            max-width: 1200px;
            padding-top: 2.25rem;
            padding-bottom: 3.5rem;
        }

        h1, h2, h3 {
            letter-spacing: -0.02em;
        }

        h1 {
            font-size: 3rem;
            margin-bottom: 0.35rem;
        }

        h2 {
            font-size: 2rem;
        }

        h3 {
            font-size: 1.35rem;
            margin-top: 0.75rem;
        }

        .stMarkdown p, .stCaption {
            color: var(--muted);
        }

        .section-title {
            font-size: 2rem;
            font-weight: 700;
            margin-bottom: 0.25rem;
        }

        .section-kicker {
            color: var(--muted);
            letter-spacing: 0.18em;
            text-transform: uppercase;
            font-size: 0.75rem;
            font-weight: 600;
        }

        .section-divider {
            height: 1px;
            background: linear-gradient(90deg, rgba(124,156,255,0.5), rgba(87,224,255,0.1));
            margin: 0.85rem 0 1.5rem;
        }

        .hero-card {
            background: linear-gradient(135deg, rgba(124,156,255,0.12), rgba(87,224,255,0.05));
            border: 1px solid var(--border);
            border-radius: 22px;
            padding: 1.75rem 2rem;
            box-shadow: 0 16px 40px rgba(3, 9, 20, 0.45);
        }

        .glass-card {
            background: linear-gradient(180deg, var(--panel) 0%, var(--panel-2) 100%);
            border: 1px solid var(--border);
            border-radius: 18px;
            padding: 1.25rem 1.5rem;
            box-shadow: 0 10px 28px rgba(3, 9, 20, 0.35);
        }

        .stat-card {
            background: #0f1626;
            border: 1px solid var(--border);
            border-radius: 16px;
            padding: 0.85rem 1rem;
        }

        .pill {
            display: inline-flex;
            align-items: center;
            gap: 0.35rem;
            padding: 0.35rem 0.75rem;
            border-radius: 999px;
            border: 1px solid var(--border);
            background: #10192a;
            color: #c7d2e2;
            font-size: 0.85rem;
            margin: 0.25rem 0.35rem 0 0;
        }

        .tag {
            display: inline-block;
            padding: 0.25rem 0.6rem;
            border-radius: 999px;
            background: rgba(124,156,255,0.12);
            border: 1px solid rgba(124,156,255,0.25);
            color: #c9d3ff;
            font-size: 0.78rem;
            margin-right: 0.35rem;
        }

        .stButton > button, .stLinkButton > a {
            border-radius: 12px !important;
            border: 1px solid var(--border) !important;
            padding: 0.6rem 1.05rem !important;
            font-weight: 600 !important;
        }

        .stLinkButton > a {
            background: linear-gradient(90deg, var(--accent) 0%, var(--accent-2) 100%) !important;
            color: #06101a !important;
            border: none !important;
        }

        /* Custom Hero Social Action Buttons */
        .hero-social-btn {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 0.35rem;
            padding: 0.35rem 0.9rem;
            border-radius: 10px;
            font-weight: 600;
            font-size: 0.82rem;
            text-decoration: none !important;
            transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            color: #ffffff !important;
            box-shadow: 0 4px 15px rgba(3, 9, 20, 0.35);
            text-align: center;
            width: fit-content;
        }

        .hero-social-btn:hover {
            transform: translateY(-3px) scale(1.03);
        }

        .btn-gh {
            background: linear-gradient(135deg, #2b3137 0%, #181c20 100%);
            border: 1px solid rgba(255, 255, 255, 0.15);
            box-shadow: 0 6px 18px rgba(24, 28, 32, 0.6);
        }

        .btn-gh:hover {
            box-shadow: 0 10px 24px rgba(24, 28, 32, 0.85);
            border-color: rgba(255, 255, 255, 0.3);
            background: linear-gradient(135deg, #333940 0%, #1e2328 100%);
        }

        .btn-li {
            background: linear-gradient(135deg, #0A66C2 0%, #004182 100%);
            border: 1px solid rgba(10, 102, 194, 0.4);
            box-shadow: 0 6px 18px rgba(10, 102, 194, 0.35);
        }

        .btn-li:hover {
            box-shadow: 0 10px 24px rgba(10, 102, 194, 0.6);
            border-color: rgba(87, 224, 255, 0.6);
            background: linear-gradient(135deg, #0d73d9 0%, #00509e 100%);
        }

        .stProgress > div > div {
            background: linear-gradient(90deg, var(--accent) 0%, var(--accent-2) 100%) !important;
        }

        div[data-testid="stVerticalBlock"] > div:has(> .stContainer) {
            gap: 1.1rem;
        }

        .scroll-progress {
            position: fixed;
            left: 0;
            top: 0;
            height: 4px;
            width: 0%;
            z-index: 9999;
            background: linear-gradient(90deg, var(--accent) 0%, var(--accent-2) 100%);
            box-shadow: 0 0 18px rgba(124, 156, 255, 0.45);
        }

        .sidebar-nav-title {
            font-size: 0.82rem;
            letter-spacing: 0.12em;
            text-transform: uppercase;
            color: var(--muted);
            margin: 0.75rem 0 0.65rem;
            font-weight: 700;
        }

        .sidebar-nav {
            display: grid;
            grid-template-columns: repeat(4, minmax(0, 1fr));
            gap: 0.55rem;
        }

        .nav-link {
            display: block;
            width: 100%;
            text-decoration: none !important;
            border-radius: 16px;
            padding: 1px;
            overflow: hidden;
            background: linear-gradient(130deg, rgba(82, 165, 255, 0.65), rgba(124, 156, 255, 0.3), rgba(87, 224, 255, 0.55));
            box-shadow: 0 4px 15px rgba(3, 9, 20, 0.35);
            transition: all 0.35s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        }

        .nav-link-inner {
            display: block;
            width: 100%;
            border-radius: 15px;
            background: #0d1523;
            padding: 0.6rem 0.65rem;
            text-align: center;
            font-size: 0.95rem;
            font-weight: 600;
            color: #ffffff !important;
            white-space: nowrap;
            transition: background 0.3s ease;
        }

        .nav-link:hover {
            transform: translateY(-4px) scale(1.04);
            box-shadow: 0 8px 22px rgba(87, 224, 255, 0.22);
        }

        .nav-link:hover .nav-link-inner {
            background: rgba(13, 21, 35, 0.82);
        }

        .nav-link.active {
            background: linear-gradient(130deg, rgba(82, 165, 255, 1), rgba(124, 156, 255, 0.8), rgba(87, 224, 255, 0.95));
            box-shadow: 0 8px 25px rgba(87, 224, 255, 0.3);
        }

        .nav-link.active .nav-link-inner {
            background: rgba(13, 21, 35, 0.9);
        }

        .anchor-target {
            display: block;
            position: relative;
            top: -4.8rem;
            visibility: hidden;
        }

        .cover-banner-wrap {
            margin: 0 0 1.35rem;
            border-radius: 24px;
            padding: 6px;
            background: linear-gradient(120deg, rgba(124, 156, 255, 0.75), rgba(87, 224, 255, 0.35));
            box-shadow: 0 16px 38px rgba(3, 9, 20, 0.42);
        }

        .cover-banner {
            width: 100%;
            display: block;
            border-radius: 20px;
            border: 1px solid rgba(255, 255, 255, 0.18);
            height: auto;
            max-height: 260px;
            object-fit: contain;
            object-position: center;
            background: #0a1220;
        }


        .hero-frame {
            margin: 2.2rem auto 0;
            width: 290px;
            max-width: 100%;
            padding: 6px;
            border-radius: 32px;
            background: linear-gradient(120deg, rgba(124, 156, 255, 0.85), rgba(87, 224, 255, 0.4), rgba(124, 156, 255, 0.9));
            background-size: 200% 200%;
            animation: heroBorderShift 10s ease-in-out infinite;
            box-shadow: 0 16px 38px rgba(3, 9, 20, 0.45);
            transform: rotate(-1.5deg);
            transition: transform 0.4s ease, box-shadow 0.4s ease;
        }

        .hero-frame:hover {
            transform: rotate(0deg) translateY(-4px);
            box-shadow: 0 20px 46px rgba(3, 9, 20, 0.55);
        }

        .hero-image {
            display: block;
            width: 100%;
            height: auto;
            border-radius: 26px;
            border: 1px solid rgba(15, 22, 38, 0.7);
        }

        @keyframes heroBorderShift {
            0% {
                background-position: 0% 50%;
            }
            50% {
                background-position: 100% 50%;
            }
            100% {
                background-position: 0% 50%;
            }
        }

        .project-card {
            display: block;
            text-decoration: none !important;
            position: relative;
            border-radius: 20px;
            padding: 1px;
            overflow: hidden;
            background: linear-gradient(130deg, rgba(82, 165, 255, 0.85), rgba(124, 156, 255, 0.5), rgba(87, 224, 255, 0.8));
            box-shadow: 0 12px 30px rgba(3, 9, 20, 0.38);
            height: 340px;
            transform: translateY(0) scale(1);
            transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275), box-shadow 0.4s ease, filter 0.4s ease;
        }

        .project-card::before {
            content: "";
            position: absolute;
            inset: -115% -35%;
            transform: translateX(-45%) rotate(14deg);
            background: linear-gradient(120deg, transparent 30%, rgba(255, 255, 255, 0.33) 50%, transparent 70%);
            opacity: 0;
            transition: opacity 0.35s ease, transform 0.55s ease;
            pointer-events: none;
        }

        @media (hover: hover) {
            .project-card:hover::before {
                opacity: 1 !important;
                transform: translateX(28%) rotate(14deg) !important;
            }

            .project-card:hover {
                transform: translateY(-8px) scale(1.02) !important;
                box-shadow: 0 18px 42px rgba(3, 9, 20, 0.5), 0 0 25px rgba(87, 224, 255, 0.2) !important;
                filter: saturate(1.05) !important;
            }
        }

        div[data-testid="stMarkdownContainer"] .project-card:focus,
        div[data-testid="stMarkdownContainer"] .project-card:active,
        .project-card:focus,
        .project-card:focus-within {
            outline: none !important;
            box-shadow: 0 12px 30px rgba(3, 9, 20, 0.38) !important;
            transform: translateY(0) scale(1) !important;
        }

        /* Prevent press jitter action - match hover look while holding click */
        @media (hover: hover) {
            .project-card:active {
                transform: translateY(-8px) scale(1.02) !important;
                box-shadow: 0 18px 42px rgba(3, 9, 20, 0.5), 0 0 25px rgba(87, 224, 255, 0.2) !important;
            }
        }

        .project-card-inner {
            position: relative;
            border-radius: 19px;
            background: linear-gradient(180deg, var(--panel) 0%, var(--panel-2) 100%);
            padding: 0.85rem;
            height: 100%;
            display: flex;
            flex-direction: column;
            gap: 0.65rem;
        }

        .project-image {
            width: 100%;
            aspect-ratio: 16 / 9;
            height: auto;
            object-fit: cover;
            object-position: center;
            border-radius: 14px;
            border: 1px solid var(--border);
            background: #0b0f17;
            display: block;
            transition: transform 0.4s ease, filter 0.4s ease;
        }

        @media (hover: hover) {
            .project-card:hover .project-image {
                transform: scale(1.04) !important;
                filter: brightness(1.1) !important;
            }
        }

        .project-image--contain {
            object-fit: contain;
            padding: 0.75rem;
            background: #0d1422;
        }

        .project-body {
            display: flex;
            flex-direction: column;
            gap: 0.55rem;
            flex: 1;
        }

        .project-title {
            font-size: 1.15rem;
            font-weight: 600;
            color: var(--text);
        }

        .project-desc {
            color: var(--muted);
            font-size: 0.92rem;
            line-height: 1.42;
            display: -webkit-box;
            -webkit-line-clamp: 2;
            -webkit-box-orient: vertical;
            overflow: hidden;
            text-overflow: ellipsis;
        }

        .project-tags {
            margin-top: auto;
        }

        .st-link-button {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            align-self: center;
            padding: 0.65rem 1rem;
            border-radius: 12px;
            background: linear-gradient(90deg, var(--accent) 0%, var(--accent-2) 100%);
            color: #000000 !important;
            font-weight: 800;
            font-size: 0.95rem;
            letter-spacing: 0.04em;
            text-transform: uppercase;
            text-decoration: none !important;
            width: 100%;
            margin-top: 0.4rem;
            border: 1px solid rgba(255, 255, 255, 0.35);
            box-shadow: 0 10px 24px rgba(87, 224, 255, 0.25);
            transition: transform 0.25s ease, box-shadow 0.25s ease, color 0.25s ease;
        }

        .st-link-button:hover {
            transform: translateY(-1px);
            box-shadow: 0 14px 30px rgba(87, 224, 255, 0.35);
            text-decoration: none !important;
            color: #000000 !important;
        }

        .skills-grid-kicker {
            margin-bottom: 0.35rem;
            font-size: 0.8rem;
            color: #9fb4d3;
            letter-spacing: 0.14em;
            text-transform: uppercase;
            font-weight: 700;
        }

        .skills-grid-note {
            margin-bottom: 0.8rem;
            font-size: 0.93rem;
            color: #b9cae0;
        }

        .skill-card {
            position: relative;
            margin-bottom: 0.75rem;
            border-radius: 19px;
            padding: 1px;
            overflow: hidden;
            background: linear-gradient(135deg, rgba(29, 122, 255, 0.95), rgba(47, 228, 255, 0.84));
            box-shadow: 0 8px 22px rgba(2, 8, 22, 0.32);
            transform: translateY(0) scale(1);
            transition: transform 0.3s ease, box-shadow 0.3s ease, filter 0.3s ease;
        }

        .skill-card.tone-red {
            background: linear-gradient(135deg, rgba(255, 93, 93, 0.9), rgba(255, 255, 255, 0.82));
        }

        .skill-card::before {
            content: "";
            position: absolute;
            inset: -120% -35%;
            background: linear-gradient(120deg, transparent 30%, rgba(255, 255, 255, 0.34) 50%, transparent 70%);
            transform: translateX(-45%) rotate(16deg);
            opacity: 0;
            transition: opacity 0.35s ease, transform 0.55s ease;
            pointer-events: none;
        }

        .skill-card:hover::before {
            opacity: 1;
            transform: translateX(30%) rotate(16deg);
        }

        .skill-card-inner {
            position: relative;
            border-radius: 18px;
            background: rgba(7, 14, 28, 0.62);
            border: 1px solid rgba(170, 210, 255, 0.2);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            padding: 1rem;
            min-height: 190px;
            display: flex;
            flex-direction: column;
            gap: 0.62rem;
        }

        .skill-head {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 0.6rem;
        }

        .skill-icon {
            width: 48px;
            height: 48px;
            border-radius: 14px;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            font-size: 1.42rem;
            color: #f5fbff;
            background: radial-gradient(circle at 30% 20%, rgba(124, 156, 255, 0.42), rgba(87, 224, 255, 0.13));
            border: 1px solid rgba(124, 156, 255, 0.48);
            box-shadow: 0 0 0 rgba(87, 224, 255, 0);
            transition: transform 0.35s ease, box-shadow 0.35s ease, filter 0.35s ease;
        }

        .skill-icon-img {
            width: 24px;
            height: 24px;
            object-fit: contain;
            filter: drop-shadow(0 0 8px rgba(87, 224, 255, 0.3));
        }

        .skill-name {
            font-size: 1.03rem;
            line-height: 1.26;
            font-weight: 700;
            color: #ffffff;
            text-shadow: 0 1px 1px rgba(0, 0, 0, 0.28);
            letter-spacing: 0.01em;
        }

        .skill-subtitle {
            font-size: 0.86rem;
            color: #d2e4ff;
            line-height: 1.45;
            margin-top: -0.15rem;
        }

        .skill-level {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            border-radius: 999px;
            padding: 0.3rem 0.7rem;
            font-size: 0.75rem;
            font-weight: 700;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            white-space: nowrap;
        }

        .level-expert {
            color: #ffffff;
            background: linear-gradient(90deg, rgba(18, 118, 255, 0.56), rgba(45, 232, 255, 0.46));
            border: 1px solid rgba(130, 235, 255, 0.7);
        }

        .level-advanced {
            color: #ffffff;
            background: linear-gradient(90deg, rgba(255, 93, 93, 0.44), rgba(255, 255, 255, 0.22));
            border: 1px solid rgba(255, 205, 205, 0.7);
        }

        .level-intermediate {
            color: #ffffff;
            background: linear-gradient(90deg, rgba(86, 145, 255, 0.32), rgba(107, 218, 255, 0.28));
            border: 1px solid rgba(160, 196, 255, 0.65);
        }

        .skill-chips {
            margin-top: auto;
            display: flex;
            flex-wrap: wrap;
            gap: 0.4rem;
        }

        .skill-chip {
            position: relative;
            overflow: hidden;
            display: inline-flex;
            align-items: center;
            border-radius: 999px;
            padding: 0.23rem 0.58rem;
            font-size: 0.7rem;
            font-weight: 600;
            color: #eff7ff;
            background: rgba(17, 32, 61, 0.78);
            border: 1px solid rgba(141, 185, 255, 0.44);
            animation: chipPulse 3.4s ease-in-out infinite;
        }

        .skill-chip::after {
            content: "";
            position: absolute;
            inset: 0;
            transform: translateX(-105%);
            background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.22), transparent);
            animation: chipSweep 4.2s ease-in-out infinite;
        }

        .skill-card:hover {
            transform: scale(1.05);
            box-shadow: 0 0 0 1px rgba(87, 224, 255, 0.34), 0 18px 36px rgba(22, 186, 255, 0.22);
            filter: saturate(1.08);
        }

        .skill-card:hover .skill-icon {
            transform: translateY(-2px) rotate(-8deg);
            box-shadow: 0 0 22px rgba(87, 224, 255, 0.38);
            filter: brightness(1.1);
        }

        .skill-fade-in {
            opacity: 0;
            transform: translateY(16px);
            animation: skillReveal 650ms cubic-bezier(0.2, 0.7, 0.2, 1) forwards;
            animation-delay: var(--delay, 0ms);
        }

        .skill-fade-in.is-visible {
            opacity: 1;
            transform: translateY(0);
        }

        @keyframes skillReveal {
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        @keyframes chipSweep {
            0%, 65% {
                transform: translateX(-110%);
            }
            100% {
                transform: translateX(120%);
            }
        }

        @keyframes chipPulse {
            0%, 100% {
                box-shadow: 0 0 0 rgba(87, 224, 255, 0);
            }
            50% {
                box-shadow: 0 0 12px rgba(87, 224, 255, 0.2);
            }
        }

        div[data-baseweb="tab-list"] {
            display: flex !important;
            justify-content: center !important;
            align-items: center;
            position: relative;
            isolation: isolate;
            gap: 0.58rem;
            margin: 0 auto 1.05rem;
            width: fit-content;
            max-width: 100%;
            flex-wrap: wrap;
            padding: 0.35rem;
            border-radius: 999px;
            border: 1px solid rgba(124, 156, 255, 0.25);
            background: linear-gradient(120deg, rgba(15, 22, 38, 0.82), rgba(12, 18, 32, 0.74));
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.08), 0 12px 28px rgba(4, 10, 22, 0.28);
        }

        button[data-baseweb="tab"] {
            border-radius: 999px !important;
            border: 1px solid rgba(124, 156, 255, 0.36) !important;
            background: rgba(255, 255, 255, 0.03) !important;
            color: #d7e6f8 !important;
            font-weight: 650 !important;
            padding: 0.45rem 1.05rem !important;
            transition: transform 0.25s ease, box-shadow 0.25s ease, border-color 0.25s ease !important;
            min-height: 42px;
            cursor: pointer !important;
            pointer-events: auto !important;
            user-select: none;
            white-space: nowrap;
            position: relative;
            z-index: 1;
            box-shadow: none !important;
        }

        button[data-baseweb="tab"]::before,
        button[data-baseweb="tab"]::after {
            content: none !important;
            display: none !important;
        }

        /* Remove Streamlit/BaseWeb default tab underline indicator (often red). */
        button[data-baseweb="tab"],
        button[data-baseweb="tab"][aria-selected="true"] {
            border-bottom: 0 !important;
        }

        div[data-baseweb="tab-highlight"] {
            display: none !important;
            height: 0 !important;
            background: transparent !important;
        }

        button[data-baseweb="tab"] * {
            color: inherit !important;
        }

        button[data-baseweb="tab"]:hover {
            transform: translateY(-1px);
            border-color: rgba(87, 224, 255, 0.55) !important;
            box-shadow: 0 0 16px rgba(87, 224, 255, 0.22);
        }

        button[data-baseweb="tab"]:focus-visible {
            outline: 2px solid rgba(130, 235, 255, 0.9) !important;
            outline-offset: 2px;
            box-shadow: 0 0 0 3px rgba(87, 224, 255, 0.22);
        }

        button[data-baseweb="tab"][aria-selected="true"] {
            background: rgba(87, 224, 255, 0.16) !important;
            border-color: rgba(87, 224, 255, 0.5) !important;
            color: #f7fbff !important;
            box-shadow: none !important;
        }

        .skills-grid-note {
            color: #d4e6ff;
        }

        .lang-grid-kicker {
            margin-bottom: 0.65rem;
            font-size: 0.84rem;
            color: #b7c6da;
            letter-spacing: 0.1em;
            text-transform: uppercase;
            font-weight: 700;
        }

        .lang-showcase {
            position: relative;
            margin-top: 0.25rem;
        }

        .lang-cards-grid {
            display: grid;
            grid-template-columns: repeat(2, minmax(0, 1fr));
            gap: 1rem;
        }

        .lang-glass-card {
            position: relative;
            border-radius: 22px;
            padding: 1px;
            overflow: hidden;
            background: linear-gradient(130deg, rgba(82, 165, 255, 0.95), rgba(124, 156, 255, 0.62), rgba(87, 224, 255, 0.92));
            box-shadow: 0 14px 32px rgba(3, 9, 22, 0.42);
            transform: translateY(0) scale(1);
            transition: transform 0.3s ease, box-shadow 0.3s ease, filter 0.3s ease;
            animation: none;
        }

        .lang-glass-card::before {
            content: "";
            position: absolute;
            inset: -115% -35%;
            transform: translateX(-45%) rotate(14deg);
            background: linear-gradient(120deg, transparent 30%, rgba(255, 255, 255, 0.33) 50%, transparent 70%);
            opacity: 0;
            transition: opacity 0.35s ease, transform 0.55s ease;
            pointer-events: none;
        }

        .lang-glass-card:hover::before {
            opacity: 1;
            transform: translateX(28%) rotate(14deg);
        }

        .lang-glass-card:hover {
            transform: translateY(-4px) scale(1.03);
            box-shadow: 0 0 0 1px rgba(159, 227, 255, 0.42), 0 18px 38px rgba(21, 189, 255, 0.3);
            filter: saturate(1.06);
        }

        .lang-glass-card-inner {
            position: relative;
            border-radius: 21px;
            height: 100%;
            min-height: 220px;
            padding: 1rem 1rem 0.95rem;
            display: flex;
            flex-direction: column;
            gap: 0.72rem;
            background: linear-gradient(145deg, rgba(9, 18, 34, 0.76), rgba(11, 21, 39, 0.68));
            border: 1px solid rgba(165, 205, 255, 0.22);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
        }

        .lang-head {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 0.55rem;
        }

        .lang-flag {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: 54px;
            height: 54px;
            border-radius: 16px;
            font-size: 1.9rem;
            background: rgba(255, 255, 255, 0.08);
            border: 1px solid rgba(203, 227, 255, 0.33);
            box-shadow: 0 8px 20px rgba(3, 9, 20, 0.28);
        }

        .lang-flag-img {
            width: 34px;
            height: 24px;
            border-radius: 6px;
            object-fit: cover;
            border: 1px solid rgba(255, 255, 255, 0.45);
            box-shadow: 0 3px 8px rgba(3, 9, 20, 0.28);
        }

        .lang-flag-img--us {
            object-fit: fill !important;
        }

        .lang-badge {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            padding: 0.32rem 0.72rem;
            border-radius: 999px;
            font-size: 0.72rem;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            font-weight: 800;
            color: #f4fbff;
            border: 1px solid rgba(198, 231, 255, 0.5);
            background: linear-gradient(90deg, rgba(82, 165, 255, 0.28), rgba(87, 224, 255, 0.24));
        }

        .lang-name {
            font-size: 1.5rem;
            font-weight: 800;
            color: #f5fbff;
            letter-spacing: -0.01em;
            line-height: 1.1;
        }

        .lang-note {
            font-size: 0.95rem;
            color: #bcd1ea;
            line-height: 1.45;
        }

        .lang-accent {
            margin-top: auto;
            width: 100%;
            height: 8px;
            border-radius: 999px;
            background: linear-gradient(90deg, rgba(82, 165, 255, 0.78), rgba(87, 224, 255, 0.62));
            box-shadow: 0 0 16px rgba(87, 224, 255, 0.26);
            opacity: 0.88;
        }

        .lang-tone-arabic {
            background: linear-gradient(130deg, rgba(22, 176, 129, 0.95), rgba(26, 155, 117, 0.7), rgba(78, 215, 171, 0.88));
        }

        .lang-tone-english {
            background: linear-gradient(130deg, rgba(69, 123, 255, 0.95), rgba(102, 136, 255, 0.72), rgba(89, 205, 255, 0.86));
        }

        .lang-tone-french {
            background: linear-gradient(130deg, rgba(56, 112, 255, 0.95), rgba(255, 255, 255, 0.76), rgba(255, 95, 95, 0.92));
        }

        .lang-fade-in {
            opacity: 1;
            transform: translateY(0);
            animation: none;
        }

        .lang-fade-in.is-visible {
            opacity: 1;
            transform: translateY(0);
        }

        @keyframes langRevealSoft {
            from {
                opacity: 0;
                transform: translateY(12px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        @keyframes langFloat {
            0%,
            100% {
                transform: translateY(0);
            }
            50% {
                transform: translateY(-4px);
            }
        }

        .skill-name {
            font-weight: 700;
            font-size: 1rem;
            color: #eef5ff;
            line-height: 1.25;
            margin-top: 0.2rem;
        }

        .skill-level {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            border-radius: 999px;
            padding: 0.28rem 0.68rem;
            font-size: 0.78rem;
            font-weight: 700;
            letter-spacing: 0.05em;
            text-transform: uppercase;
            white-space: nowrap;
        }

        .level-expert {
            color: #f7fbff;
            background: linear-gradient(90deg, rgba(124, 156, 255, 0.4), rgba(87, 224, 255, 0.35));
            border: 1px solid rgba(87, 224, 255, 0.45);
        }

        .level-advanced {
            color: #f7fbff;
            background: linear-gradient(90deg, rgba(255, 77, 77, 0.34), rgba(255, 255, 255, 0.2));
            border: 1px solid rgba(255, 177, 177, 0.45);
        }

        .level-intermediate {
            color: #f7fbff;
            background: linear-gradient(90deg, rgba(116, 211, 255, 0.26), rgba(124, 156, 255, 0.24));
            border: 1px solid rgba(124, 156, 255, 0.45);
        }

        .skill-card:hover {
            transform: scale(1.05);
            box-shadow: 0 0 0 1px rgba(87, 224, 255, 0.28), 0 14px 34px rgba(23, 182, 255, 0.26);
        }

        .skill-card:hover .skill-icon {
            transform: translateY(-2px) scale(1.08) rotate(-7deg);
            box-shadow: 0 0 20px rgba(87, 224, 255, 0.35);
        }

        .skill-fade-in {
            opacity: 0;
            transform: translateY(16px);
            transition: opacity 0.55s ease, transform 0.55s ease;
        }

        .skill-fade-in.is-visible {
            opacity: 1;
            transform: translateY(0);
        }

        @media (max-width: 900px) {
            .lang-cards-grid {
                grid-template-columns: 1fr;
            }

            .lang-glass-card-inner {
                min-height: 190px;
            }

            div[data-baseweb="tab-list"] {
                width: 100%;
                justify-content: center !important;
                border-radius: 16px;
                padding: 0.42rem;
            }
        }

        @media (min-width: 1200px) {
            .lang-cards-grid {
                grid-template-columns: repeat(3, minmax(0, 1fr));
            }
        }

        @media (max-width: 1024px) {
            .block-container {
                padding-left: 1rem;
                padding-right: 1rem;
            }

            h1 {
                font-size: 2.45rem;
            }

            h2, .section-title {
                font-size: 1.75rem;
            }

            .cover-banner {
                max-height: 220px;
            }
        }

        @media (max-width: 900px) {
            .block-container {
                padding-top: 1.2rem;
                padding-bottom: 2rem;
            }

            .hero-card {
                padding: 1.15rem;
                border-radius: 18px;
            }

            .cover-banner-wrap {
                margin: 4.5rem 0 1.25rem;
                border-radius: 18px;
                padding: 4px;
            }

            .cover-banner {
                border-radius: 14px;
                max-height: 180px;
                object-position: center 46%;
            }

            .hero-frame {
                width: 220px;
                margin: 1rem auto 0.1rem;
            }

            .project-card {
                border-radius: 14px;
                height: auto !important;
            }

            .project-card-inner {
                height: auto !important;
                border-radius: 13px;
            }

            .skill-card,
            .glass-card {
                border-radius: 14px;
            }

            .skill-card-inner {
                min-height: 114px;
            }



            .nav-link {
                padding: 1px;
            }

            .nav-link-inner {
                padding: 0.45rem 0.5rem;
                font-size: 0.85rem;
            }

            .sidebar-nav {
                grid-template-columns: repeat(4, minmax(0, 1fr));
            }
        }

        @media (max-width: 640px) {
            .sticky-navbar {
                padding: 0.4rem 0.5rem;
            }

            .sidebar-nav {
                grid-template-columns: repeat(4, minmax(0, 1fr));
                gap: 0.25rem;
            }

            .nav-link-inner {
                padding: 0.4rem 0.2rem;
                font-size: 0.68rem;
                white-space: normal;
            }

            .cover-banner-wrap {
                margin-top: 4.2rem;
            }

            h1 {
                font-size: 1.85rem;
                line-height: 1.12;
            }

            h2, .section-title {
                font-size: 1.4rem;
            }

            h3 {
                font-size: 1.12rem;
            }

            .section-kicker {
                letter-spacing: 0.12em;
                font-size: 0.68rem;
            }

            .cover-banner {
                max-height: 150px;
                object-position: center 50%;
            }



            .stButton > button,
            .stLinkButton > a,
            .st-link-button {
                width: 100% !important;
                justify-content: center;
            }

            .project-card-inner {
                padding: 0.82rem;
            }

            .skill-icon {
                width: 40px;
                height: 40px;
                font-size: 1.2rem;
            }

            .pill,
            .tag {
                font-size: 0.74rem;
            }

            .experience-card-inner {
                padding: 1.15rem 1.15rem;
            }
            .education-card-inner {
                padding: 1.25rem 1.25rem;
            }
            .experience-card .experience-title,
            .education-card .education-title {
                font-size: 1.15rem;
            }
            .education-card .education-school,
            .experience-card .experience-detail {
                font-size: 0.95rem;
            }
        }

        /* Explicit Contact Form Theme Overrides for All Devices */
        div[data-testid="stForm"] {
            border: 1px solid var(--border) !important;
            background-color: var(--panel) !important;
            border-radius: 16px !important;
            padding: 1.25rem !important;
            box-shadow: 0 8px 32px rgba(3, 9, 20, 0.35) !important;
        }

        /* Inputs & Textareas */
        div[data-testid="stForm"] input,
        div[data-testid="stForm"] textarea {
            background-color: #161c2b !important;
            color: #ffffff !important;
            border: 1px solid var(--border) !important;
            border-radius: 10px !important;
        }

        /* Focus Ring */
        div[data-testid="stForm"] input:focus,
        div[data-testid="stForm"] textarea:focus {
            border-color: var(--accent) !important;
            box-shadow: 0 0 0 1px var(--accent) !important;
        }

        /* Labels alignment and coloring */
        div[data-testid="stForm"] label div, 
        div[data-testid="stForm"] label p {
            color: var(--text) !important;
        }
        /* Experience Cards */
        .experience-card {
            position: relative;
            border-radius: 20px;
            padding: 1px 1px 12px 1px;
            overflow: hidden;
            background: linear-gradient(130deg, rgba(82, 165, 255, 0.75), rgba(124, 156, 255, 0.4), rgba(87, 224, 255, 0.65));
            box-shadow: 0 12px 32px rgba(3, 9, 20, 0.38);
            transform: translateY(0);
            transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275), box-shadow 0.4s ease, border-color 0.4s ease;
            height: 100%;
            min-height: 220px;
            margin-bottom: 1.5rem;
            display: flex;
            flex-direction: column;
        }

        .experience-card:hover {
            transform: translateY(-6px) scale(1.02);
            box-shadow: 0 18px 42px rgba(3, 9, 20, 0.5), 0 0 20px rgba(87, 224, 255, 0.18);
        }

        .experience-card-inner {
            border-radius: 19px;
            background: linear-gradient(180deg, var(--panel) 0%, var(--panel-2) 100%);
            padding: 1.35rem 1.5rem;
            flex-grow: 1;
            width: 100%;
            display: flex;
            flex-direction: column;
            gap: 0.5rem;
        }

        .experience-card .experience-emoji {
            font-size: 1.85rem;
            margin-bottom: 0.3rem;
        }

        .experience-card .experience-title {
            font-size: 1.18rem;
            font-weight: 700;
            color: #ffffff;
            line-height: 1.3;
        }

        .experience-card .experience-detail {
            color: var(--muted);
            font-size: 0.94rem;
            line-height: 1.5;
            margin-top: 0.2rem;
        }
        
        /* Education Cards */
        .education-card {
            position: relative;
            border-radius: 20px;
            padding: 1px 1px 12px 1px;
            overflow: hidden;
            background: linear-gradient(130deg, rgba(82, 165, 255, 0.75), rgba(124, 156, 255, 0.4), rgba(87, 224, 255, 0.65));
            box-shadow: 0 12px 32px rgba(3, 9, 20, 0.38);
            transform: translateY(0);
            transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275), box-shadow 0.4s ease, border-color 0.4s ease;
            height: 100%;
            margin-bottom: 1.5rem;
            display: flex;
            flex-direction: column;
        }

        .education-card:hover {
            transform: translateY(-6px) scale(1.02);
            box-shadow: 0 18px 42px rgba(3, 9, 20, 0.5), 0 0 20px rgba(87, 224, 255, 0.18);
        }

        .education-card-inner {
            border-radius: 19px;
            background: linear-gradient(180deg, var(--panel) 0%, var(--panel-2) 100%);
            padding: 1.5rem 1.75rem;
            flex-grow: 1;
            width: 100%;
            display: flex;
            flex-direction: column;
            gap: 0.3rem;
        }

        .education-card .education-years {
            font-size: 0.88rem;
            color: var(--accent-2);
            font-weight: 700;
            letter-spacing: 0.05em;
            text-transform: uppercase;
            margin-bottom: 0.2rem;
        }

        .education-card .education-title {
            font-size: 1.35rem;
            font-weight: 700;
            color: #ffffff;
            line-height: 1.3;
        }

        .education-card .education-school {
            color: #f1f6fb;
            font-size: 1.05rem;
            line-height: 1.45;
            margin-top: 0.15rem;
            opacity: 0.95;
        }

        .education-card .education-detail {
            color: var(--muted);
            font-size: 1rem;
            line-height: 1.55;
            margin-top: 0.45rem;
        }

        .education-card .education-emoji {
            font-size: 1.85rem;
            margin-bottom: 0.35rem;
        }

        .sticky-navbar {
            position: fixed;
            top: 0px;
            left: 0px;
            width: 100%;
            z-index: 999999;
            background: transparent;
            backdrop-filter: none;
            -webkit-backdrop-filter: none;
            padding: 0.75rem 2rem;
            border-bottom: none;
            box-shadow: none;
            margin: 0;
            display: block;
        }

        .sticky-navbar .sidebar-nav {
            max-width: 1180px;
            margin: 0 auto;
        }

        /* CV Cards — desktop */
        .cv-access-card,
        .cv-preview-card {
            min-height: 380px;
        }

        /* CV Cards — mobile: let content breathe */
        @media (max-width: 640px) {
            .cv-access-card {
                min-height: unset !important;
                height: auto !important;
            }
            .cv-access-card .experience-card-inner {
                padding: 1.5rem !important;
            }
            .cv-preview-card {
                min-height: unset !important;
                height: auto !important;
            }
            .cv-preview-card iframe {
                height: 260px !important;
            }
        }
        
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# Data
# -----------------------------
PROFILE = {
    "name": "Anis Mselmi",
    "role": "Computer Engineering Student | AI, RAG, and LLM Enthusiast",
    "location": "Khzema Ouest, Sousse, Tunisia",
    "email": "anismselmi490@gmail.com",
    "phone": "+216 25 141 636",
    "github": "https://github.com/anis-mselmi",
    "linkedin": "https://www.linkedin.com/in/anis-mselmi-441b39326/",
}

ABOUT = (
    "🧠 Computer Engineering student at École Polytechnique de Sousse, focused on AI, "
    "machine learning, and LLMs. I love turning complex ideas into reliable AI systems "
    "by building intelligent Python models, RAG pipelines, and conversational agents. "
    "⚡ I am hands-on with Jupyter/Colab workflows, data visualization, and rapid "
    "experimentation, and I bring a builder's mindset to every project. 🌍 Curious, "
    "driven, and always learning, I am open to internships and part-time roles where "
    "I can contribute to impactful AI, RAG, and LLM products."
)

EDUCATION = [
    {
        "title": "Computer Engineering Student",
        "school": "École Polytechnique de Sousse",
        "years": "2025 – 2028",
        "detail": "Focused on Artificial Intelligence, Machine Learning, and Large Language Models (LLMs). Hands-on building intelligent Python models, RAG pipelines, and conversational agents.",
        "emoji": "💻",
    },
    {
        "title": "Integrated Preparatory Studies",
        "school": "École Polytechnique de Sousse",
        "years": "2023 – 2025",
        "detail": "Underwent rigorous training in Mathematics, Physics, and foundational engineering principles to develop strong Analytical and Problem-Solving capabilities.",
        "emoji": "📐",
    },
    {
        "title": "High School Diploma (Baccalauréat)",
        "school": "Lycée Les Lumières Sousse",
        "years": "2022 – 2023",
        "detail": "Completed secondary education with a science-focused curriculum, establishing a solid foundation in Mathematics and Sciences.",
        "emoji": "🏫",
    },
]

EXPERIENCE = [
    "Web Master at IEEE SIGHT EPS SB",
    "Ambassador at ATIC, NPC 2.0 PolyRobots",
    "Organizer at Twise Night, IEEE Tejmaana, TCPC, IEEE Day",
    "Participant at CSTAM 1.0, SDC 3.0, WIE ACT 4.0",
]

SKILLS_BY_CATEGORY = {
    "AI & Machine Learning": [
        {
            "icon": "🤖",
            "name": "Machine Learning",
            "level": "Advanced",
            "subtitle": "Model training, evaluation, deployment",
            "tags": ["scikit-learn", "feature engineering", "pipelines"],
            "details": "Production-oriented supervised and unsupervised model building.",
            "tone": "blue",
        },
        {
            "icon": "🧠",
            "name": "Deep Learning",
            "level": "Intermediate",
            "subtitle": "Neural architectures and optimization",
            "tags": ["CNN", "transformers", "fine-tuning"],
            "details": "Focused on practical DL experiments and model iteration.",
            "tone": "blue",
        },
        {
            "icon": "🧩",
            "name": "RAG Pipelines",
            "level": "Advanced",
            "subtitle": "Retrieval + generation system design",
            "tags": ["vector DB", "chunking", "reranking"],
            "details": "Builds robust knowledge-grounded assistants with retrieval chains.",
            "tone": "red",
        },

    ],
    "Programming": [
        {
            "icon": "🐍",
            "name": "Python",
            "level": "Expert",
            "subtitle": "Core language for AI and automation",
            "tags": ["clean code", "APIs", "scripting"],
            "details": "Primary stack for AI products, experimentation, and tooling.",
            "tone": "blue",
        },
        {
            "icon": "⚙️",
            "name": "C++",
            "level": "Intermediate",
            "subtitle": "Performance-focused systems concepts",
            "tags": ["OOP", "memory", "algorithms"],
            "details": "Solid foundation for low-level optimization and logic design.",
            "tone": "red",
        },
        {
            "icon": "📓",
            "name": "Jupyter Notebook",
            "level": "Advanced",
            "subtitle": "Experiment-first development workflow",
            "tags": ["EDA", "prototyping", "visual insight"],
            "details": "Fast iteration environment for data and model experiments.",
            "tone": "blue",
        },

    ],
    "Data & Analytics": [
        {
            "icon": "📊",
            "name": "Data Analysis",
            "level": "Advanced",
            "subtitle": "Insight extraction from raw datasets",
            "tags": ["cleaning", "profiling", "statistics"],
            "details": "Transforms noisy data into actionable information.",
            "tone": "blue",
        },
        {
            "icon": "📈",
            "name": "Data Visualization",
            "level": "Advanced",
            "subtitle": "Narrative dashboards and reporting",
            "tags": ["charts", "storytelling", "KPIs"],
            "details": "Builds visuals that communicate decisions clearly.",
            "tone": "red",
        },
        {
            "icon": "🧪",
            "name": "Experiment Tracking",
            "level": "Intermediate",
            "subtitle": "Metrics, iteration and model comparison",
            "tags": ["versioning", "benchmarks", "ablation"],
            "details": "Keeps model experiments measurable and reproducible.",
            "tone": "blue",
        },
    ],
    "Tools & Platforms": [
        {
            "icon": "🐱",
            "name": "Git",
            "level": "Advanced",
            "subtitle": "Version control and clean collaboration",
            "tags": ["branching", "history", "workflow"],
            "details": "Maintains clean commit strategy and collaboration standards.",
            "tone": "red",
        },
        {
            "icon": "🐱",
            "name": "GitHub",
            "level": "Advanced",
            "subtitle": "Repo management and project delivery",
            "tags": ["PRs", "issues", "CI-ready"],
            "details": "Organizes portfolio projects with professional structure.",
            "tone": "blue",
        },
        {
            "icon": "🌌",
            "name": "Antigravity",
            "level": "Expert",
            "subtitle": "AI-assisted agentic workflow",
            "tags": ["AI agent", "pair-programming", "productivity"],
            "details": "Primary environment for rapid, autonomous, and collaborative coding.",
            "tone": "blue",
        },

    ],
}

PROJECTS = [
    {
        "name": "LLM Chat App",
        "desc": "A production-ready conversational AI application with a modern UI, streaming responses, and advanced LLM integration.",
        "tags": ["AI", "LLM", "Python"],
        "image": "image.png",
        "logo": "logo-php-blog.svg",
        "link": "https://github.com/anis-mselmi/LLM-chat-app",
        "fit": "contain",
    },
    {
        "name": "AI Image Classifier",
        "desc": "A fast, intuitive image classifier with model insights and confidence scoring.",
        "tags": ["AI", "Computer Vision", "Python"],
        "image": "1669108029830.png",
        "logo": "logo-ai-classifier.smavg",
        "link": "https://github.com/anis-mselmi/AI-Image-Classifier",
    },
    {
        "name": "SmartParkTN",
        "desc": "Scans car license plates (matricules) at the parking entrance to automate access and tracking.",
        "tags": ["AI", "Computer Vision", "ALPR"],
        "image": "Gemini_Generated_Image_3ingj23ingj23ing.png",
        "logo": "logo-restaurant-sentiment.svg",
        "link": "https://github.com/anis-mselmi/SmartParkTN-D-tection-automatique-des-plaques-tunisiennes-ALPR-pour-parking",
    },
]

LANGUAGES = [
    {
        "name": "Arabic",
        "flag_src": "https://flagcdn.com/w80/sa.png",
        "flag_alt": "Saudi Arabia flag",
        "badge": "Native",
        "detail": "Native / Fluent communication across personal, academic, and team environments.",
        "tone": "arabic",
    },
    {
        "name": "English",
        "flag_src": "https://flagcdn.com/w80/us.png",
        "flag_alt": "United States flag",
        "flag_class": "lang-flag-img--us",
        "badge": "Professional",
        "detail": "Professional proficiency for technical writing, collaboration, and presentations.",
        "tone": "english",
    },
    {
        "name": "French",
        "flag_src": "https://flagcdn.com/w80/fr.png",
        "flag_alt": "France flag",
        "badge": "Professional",
        "detail": "Professional proficiency for communication, documentation, and everyday teamwork.",
        "tone": "french",
    },
]

SOFT_SKILLS = ["Communication", "Teamwork", "Project Management", "Organization"]
INTERESTS = ["Travelling", "Sports", "Reading"]

# -----------------------------
# Helpers
# -----------------------------

def load_profile_image(image_path: Path):
    if not image_path.exists():
        return None
    if Image is None or ImageDraw is None:
        return str(image_path)

    image = Image.open(image_path).convert("RGBA")
    size = min(image.size)
    left = (image.width - size) // 2
    top = (image.height - size) // 2
    image = image.crop((left, top, left + size, top + size))

    mask = Image.new("L", (size, size), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, size, size), fill=255)
    image.putalpha(mask)
    return image


@st.cache_data(show_spinner=False)
def image_to_data_uri(image_path: Path, max_width: int = 900) -> str | None:
    if not image_path.exists():
        return None
    suffix = image_path.suffix.lower().lstrip(".")
    mime_map = {
        "jpg": "image/jpeg",
        "jpeg": "image/jpeg",
        "png": "image/png",
        "webp": "image/webp",
        "svg": "image/svg+xml",
    }
    mime_type = mime_map.get(suffix, "image/png")

    if suffix == "svg":
        encoded = base64.b64encode(image_path.read_bytes()).decode("utf-8")
        return f"data:{mime_type};base64,{encoded}"

    if Image is not None:
        try:
            image = Image.open(image_path)
            if image.width > max_width:
                ratio = max_width / image.width
                new_size = (max_width, max(1, int(image.height * ratio)))
                image = image.resize(new_size)

            buffer = io.BytesIO()
            has_alpha = image.mode in {"RGBA", "LA"} or (
                image.mode == "P" and "transparency" in image.info
            )

            if has_alpha:
                image.save(buffer, format="PNG", optimize=True)
                encoded = base64.b64encode(buffer.getvalue()).decode("utf-8")
                return "data:image/png;base64," + encoded

            image = image.convert("RGB")
            image.save(buffer, format="JPEG", quality=80, optimize=True)
            encoded = base64.b64encode(buffer.getvalue()).decode("utf-8")
            return f"data:image/jpeg;base64,{encoded}"
        except Exception:
            pass

    encoded = base64.b64encode(image_path.read_bytes()).decode("utf-8")
    return f"data:{mime_type};base64,{encoded}"

def section_title(title: str, icon: str = "") -> None:
    with st.container():
        st.markdown(
            f"""
            <div class="section-title">{icon} {title}</div>
            <div class="section-divider"></div>
            """,
            unsafe_allow_html=True,
        )


def badge(text: str) -> None:
    st.markdown(f"<span class=\"pill\">{text}</span>", unsafe_allow_html=True)


def section_start(anchor: str, hero: bool = False) -> None:
    st.markdown(
        f"<span id='{anchor}' class='anchor-target anchor-section' data-anchor='{anchor}'></span>",
        unsafe_allow_html=True,
    )


def section_end() -> None:
    return


def render_cover_banner() -> None:
    cover_path = Path(__file__).parent / "Copie de photo de couverture LinkedIn (2).png"
    cover_data = None
    if cover_path.exists():
        cover_data = "data:image/png;base64," + base64.b64encode(cover_path.read_bytes()).decode("utf-8")

    if cover_data:
        st.markdown(
            f"""
            <div class='cover-banner-wrap'>
                <img src='{cover_data}' class='cover-banner' alt='LinkedIn cover image' />
            </div>
            """,
            unsafe_allow_html=True,
        )


def render_navbar() -> None:
    st.markdown(
        """
        <div class="sticky-navbar">
            <div class="sidebar-nav">
                <a href="#skills" class="nav-link" data-target="skills"><span class="nav-link-inner">🛠 Skills</span></a>
                <a href="#education" class="nav-link" data-target="education"><span class="nav-link-inner">🎓 Education</span></a>
                <a href="#experience" class="nav-link" data-target="experience"><span class="nav-link-inner">💼 Experience</span></a>
                <a href="#projects" class="nav-link" data-target="projects"><span class="nav-link-inner">🚀 Projects</span></a>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# -----------------------------
# Sections
# -----------------------------

def hero_section() -> None:
    section_start("hero", hero=True)
    # section_title("Welcome", "👋")
    st.markdown('<div class="hero-card">', unsafe_allow_html=True)
    col1, col2 = st.columns([2, 1], gap="large")

    with col1:
        st.markdown(f"# {PROFILE['name']}")
        st.markdown(f"**{PROFILE['role']}**")
        st.markdown(f"📍 {PROFILE['location']}")
        st.markdown(ABOUT)

        st.markdown(
            f"""
            <div style="display: flex; gap: 0.75rem; margin-top: 1rem; flex-wrap: wrap;">
                <a href="{PROFILE['github']}" class="hero-social-btn btn-gh" target="_blank">
                    🐱 GitHub
                </a>
                <a href="{PROFILE['linkedin']}" class="hero-social-btn btn-li" target="_blank">
                    💼 LinkedIn
                </a>
            </div>
            """, 
            unsafe_allow_html=True
        )

    with col2:
        icon_path = Path(__file__).parent / "Gemini_Generated_Image_vilfj9vilfj9vilf.png"

        st.write("")
        if icon_path.exists():
            hero_image = image_to_data_uri(icon_path)
            if hero_image:
                st.markdown(
                    f"""
                    <div class='hero-frame'>
                        <img src='{hero_image}' class='hero-image' alt='Profile photo' />
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
            else:
                st.image(str(icon_path), width=290)
        else:
            st.info("Add hero image: Gemini_Generated_Image_vilfj9vilfj9vilf.png")
    st.markdown("</div>", unsafe_allow_html=True)
    section_end()


def render_skills_section() -> None:
    section_start("skills")
    section_title("Skills", "🛠")
    st.caption("Futuristic AI dashboard cards with neon glow, animated chips, and role-focused depth.")

    tabs = st.tabs(list(SKILLS_BY_CATEGORY.keys()))

    for tab, (category, items) in zip(tabs, SKILLS_BY_CATEGORY.items()):
        with tab:
            st.markdown(f"<div class='skills-grid-kicker'>{category}</div>", unsafe_allow_html=True)
            st.markdown(
                "<div class='skills-grid-note'>Hover cards for glow, motion, and a quick expertise snapshot.</div>",
                unsafe_allow_html=True,
            )
            cols = st.columns(3, gap="large")
            for index, item in enumerate(items):
                level_class = f"level-{item['level'].lower()}"
                tone_class = "tone-red" if item.get("tone") == "red" else ""
                skill_icon = (
                    f"<img src='{item['icon_src']}' class='skill-icon-img' alt='{item['name']} icon' />"
                    if item.get("icon_src")
                    else item["icon"]
                )
                chips_html = "".join(
                    [f"<span class='skill-chip'>{tag}</span>" for tag in item.get("tags", [])[:3]]
                )
                delay_ms = (index % 3) * 90
                with cols[index % 3]:
                    st.markdown(
                        f"""
                        <div class="skill-card skill-fade-in {tone_class}" style="--delay:{delay_ms}ms" title="{item.get('details', '')}">
                            <div class="skill-card-inner" title="{item.get('details', '')}">
                                <div class="skill-head">
                                    <span class="skill-icon">{skill_icon}</span>
                                    <span class="skill-level {level_class}">{item['level']}</span>
                                </div>
                                <div class="skill-name">{item['name']}</div>
                                <div class="skill-subtitle">{item.get('subtitle', '')}</div>
                                <div class="skill-chips">{chips_html}</div>
                            </div>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )
    section_end()


def render_education() -> None:
    section_start("education")
    section_title("Education", "🎓")
    for item in EDUCATION:
        st.markdown(
            f"""
            <div class="education-card">
                <div class="education-card-inner">
                    <div class="education-emoji">{item.get('emoji', '')}</div>
                    <div class="education-years">{item['years']}</div>
                    <div class="education-title">{item['title']}</div>
                    <div class="education-school">{item['school']}</div>
                    <div class="education-detail">{item.get('detail', '')}</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    section_end()


def render_experience() -> None:
    section_start("experience")
    section_title("Experience & Community", "💼")
    st.caption("Leadership, community, and event experience across tech initiatives.")
    cards = [
        {
            "title": "Web Master at IEEE SIGHT EPS SB",
            "emoji": "🧩",
            "detail": "Managed web presence, content updates, and digital visibility.",
        },
        {
            "title": "Ambassador at ATIC, NPC 2.0 PolyRobots, IEEE YESIST12, IEEE Smart Cities",
            "emoji": "🌐",
            "detail": "Represented the community and supported outreach initiatives.",
        },
        {
            "title": "Organizer at Twise Night, IEEE Tejmaana, TCPC, IEEE Day",
            "emoji": "🎯",
            "detail": "Coordinated events, logistics, and volunteer teams.",
        },
        {
            "title": "Participant at CSTAM 1.0, SDC 3.0, WIE ACT 4.0, TSYP13",
            "emoji": "🚀",
            "detail": "Active participant in workshops, challenges, and conferences.",
        },
    ]

    cols = st.columns(2, gap="large")
    for index, item in enumerate(cards):
        with cols[index % 2]:
            st.markdown(
                f"""
                <div class="experience-card">
                    <div class="experience-card-inner">
                        <div class="experience-emoji">{item['emoji']}</div>
                        <div class="experience-title">{item['title']}</div>
                        <div class="experience-detail">{item['detail']}</div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
    section_end()


def render_projects() -> None:
    section_start("projects")
    section_title("Projects", "🚀")
    st.caption("Project placeholders — ready to be replaced with real work samples.")

    cols = st.columns(3, gap="large")
    for idx, project in enumerate(PROJECTS):
        with cols[idx % 3]:
            image_path = Path(__file__).parent / project.get("image", "")
            image_data = image_to_data_uri(image_path)
            fit = project.get("fit", "cover")
            image_class = "project-image project-image--contain" if fit == "contain" else "project-image"
            image_style = f"object-fit:{fit};"
            image_html = (
                f"<img src='{image_data}' alt='{project['name']}' class='{image_class}' style='{image_style}' />"
                if image_data
                else f"<div class='project-image'></div>"
            )
            tags_html = "".join([f"<span class='tag'>#{t}</span>" for t in project["tags"]])
            start_tag = f'<a class="project-card" href="{project["link"]}" target="_blank" style="text-decoration: none; display: block;">' if project.get("link") else '<div class="project-card">'
            end_tag = '</a>' if project.get("link") else '</div>'
            
            card_html = f"""
                {start_tag}
                    <div class="project-card-inner">
                        {image_html}
                        <div class="project-body">
                            <div class="project-title">{project['name']}</div>
                            <div class="project-desc">{project['desc']}</div>
                            <div class="project-tags">{tags_html}</div>
                        </div>
                    </div>
                {end_tag}
            """
            st.markdown(card_html, unsafe_allow_html=True)
    section_end()


def render_languages() -> None:
    section_start("languages")
    section_title("Languages", "🌍")
    st.caption("Communication strengths presented as premium glass cards.")
    st.markdown(
        "<div class='lang-grid-kicker'>Global communication profile</div>",
        unsafe_allow_html=True,
    )

    cols = st.columns(3, gap="large")
    for index, item in enumerate(LANGUAGES):
        delay_ms = min(index * 90, 220)
        float_delay = index * 140
        card_html = (
            f"<div class='lang-showcase'>"
            f"<div class='lang-glass-card lang-tone-{item['tone']} lang-fade-in' "
            f"style='--delay:{delay_ms}ms;--float-delay:{float_delay}ms;'>"
            "<div class='lang-glass-card-inner'>"
            "<div class='lang-head'>"
            f"<span class='lang-flag'><img src='{item['flag_src']}' alt='{item['flag_alt']}' class='lang-flag-img {item.get('flag_class', '')}' /></span>"
            f"<span class='lang-badge'>{item['badge']}</span>"
            "</div>"
            f"<div class='lang-name'>{item['name']}</div>"
            f"<div class='lang-note'>{item['detail']}</div>"
            "</div>"
            "</div>"
            "</div>"
        )
        with cols[index % 3]:
            st.markdown(card_html, unsafe_allow_html=True)
    section_end()


def render_cv() -> None:
    section_start("cv")
    section_title("My CV", "📜")
    st.caption("A glance at my professional background and skills available for direct access.")

    cv_link = "https://drive.google.com/file/d/12FTlWDxiwvmR51csiFUhfn3_HJ9tXjyV/view?usp=sharing"
    direct_download = "https://drive.google.com/uc?export=download&id=12FTlWDxiwvmR51csiFUhfn3_HJ9tXjyV"
    preview_url = "https://drive.google.com/file/d/12FTlWDxiwvmR51csiFUhfn3_HJ9tXjyV/preview"

    col1, col2 = st.columns([1.1, 1], gap="large")
    with col1:
        st.markdown(
            f"""
            <div class="experience-card cv-access-card">
                <div class="experience-card-inner" style="justify-content: center; padding: 2.2rem;">
                    <h3 style="margin-top: 0; margin-bottom: 0.5rem; color: var(--accent-2);">📄 Instant Access to Resume</h3>
                    <p style="margin-bottom: 1.5rem; color: var(--muted); line-height: 1.6; font-size: 0.98rem;">
                        Download or view my updated PDF resume. Inside, you'll find a detailed listing of my academic computer engineering background, complete technical experiences and project snapshots.
                    </p>
                    <div style="display: flex; flex-direction: column; gap: 0.82rem; width: 100%; margin-top: auto;">
                        <a class="st-link-button" href="{cv_link}" target="_blank" style="text-decoration: none !important;">📂 View on Drive</a>
                        <a class="st-link-button" href="{direct_download}" target="_blank" style="text-decoration: none !important;">⬇️ Download Direct PDF</a>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    with col2:
        st.markdown(
            f"""
            <div class="experience-card cv-preview-card">
                <div class="experience-card-inner" style="padding: 0; overflow: hidden; justify-content: center;">
                    <iframe src="{preview_url}" width="100%" height="380" style="border: none; display: block;"></iframe>
                </div>
            </div>
            """, 
            unsafe_allow_html=True
        )
    section_end()


def render_contact() -> None:
    section_start("contact")
    section_title("Contact", "📬")
    st.caption("Send a direct message — it opens your email client with everything pre‑filled.")
    with st.form("contact_form", clear_on_submit=True):
        name = st.text_input("Your Name")
        sender_email = st.text_input("Your Email")
        subject = st.text_input("Subject")
        message = st.text_area("Message", height=160)
        submitted = st.form_submit_button("📨 Send Message")

    if submitted:
        body = f"Name: {name}\nEmail: {sender_email}\n\n{message}"
        mailto = (
            f"mailto:{PROFILE['email']}?subject={quote(subject)}"
            f"&body={quote(body)}"
        )
        st.markdown(f"[Click here to send your email]({mailto})")

    st.markdown("---")
    st.caption(f"© {datetime.now().year} {PROFILE['name']} · Built with Streamlit")
    section_end()


def mount_scroll_behavior() -> None:
    st.markdown("<div class='scroll-progress' id='scroll-progress'></div>", unsafe_allow_html=True)
    st.markdown(
        """
        <script>
            (() => {
                const SIDE_LINK_SELECTOR = '.nav-link';
                const SECTION_SELECTOR = '.anchor-section';
                const duration = 600;

                const easeInOut = (t) => {
                    return t < 0.5 ? 2 * t * t : 1 - Math.pow(-2 * t + 2, 2) / 2;
                };

                const smoothScrollTo = (targetY) => {
                    const startY = window.pageYOffset;
                    const distance = targetY - startY;
                    let startTime = null;

                    const tick = (currentTime) => {
                        if (!startTime) startTime = currentTime;
                        const elapsed = currentTime - startTime;
                        const progress = Math.min(elapsed / duration, 1);
                        const eased = easeInOut(progress);
                        window.scrollTo(0, startY + distance * eased);
                        if (elapsed < duration) {
                            window.requestAnimationFrame(tick);
                        }
                    };

                    window.requestAnimationFrame(tick);
                };

                const updateProgress = () => {
                    const el = document.getElementById('scroll-progress');
                    if (!el) return;
                    const scrollTop = window.pageYOffset;
                    const docHeight = document.documentElement.scrollHeight - window.innerHeight;
                    const ratio = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;
                    el.style.width = `${Math.min(100, Math.max(0, ratio))}%`;
                };

                const links = Array.from(document.querySelectorAll(SIDE_LINK_SELECTOR));
                links.forEach((link) => {
                    link.addEventListener('click', (event) => {
                        event.preventDefault();
                        const targetId = link.dataset.target;
                        const target = document.getElementById(targetId);
                        if (!target) return;
                        const top = target.getBoundingClientRect().top + window.pageYOffset - 10;
                        smoothScrollTo(top);
                    });
                });

                const observeSkillCards = () => {
                    const revealCards = Array.from(
                        document.querySelectorAll('.skill-fade-in, .lang-fade-in')
                    );
                    if (!revealCards.length) return;

                    const skillObserver = new IntersectionObserver(
                        (entries) => {
                            entries.forEach((entry) => {
                                if (entry.isIntersecting) {
                                    entry.target.classList.add('is-visible');
                                    skillObserver.unobserve(entry.target);
                                }
                            });
                        },
                        {
                            root: null,
                            rootMargin: '0px 0px -12% 0px',
                            threshold: 0.08,
                        }
                    );

                    revealCards.forEach((card, index) => {
                        card.style.transitionDelay = `${Math.min(index * 35, 180)}ms`;
                        skillObserver.observe(card);
                    });
                };

                const setActive = (anchor) => {
                    links.forEach((link) => {
                        const isActive = link.dataset.target === anchor;
                        link.classList.toggle('active', isActive);
                    });
                };

                const sections = Array.from(document.querySelectorAll(SECTION_SELECTOR));
                if (sections.length) {
                    const observer = new IntersectionObserver(
                        (entries) => {
                            entries.forEach((entry) => {
                                if (entry.isIntersecting) {
                                    const anchor = entry.target.dataset.anchor;
                                    if (anchor) setActive(anchor);
                                }
                            });
                        },
                        {
                            root: null,
                            rootMargin: '-40% 0px -45% 0px',
                            threshold: 0.01,
                        }
                    );
                    sections.forEach((section) => observer.observe(section));
                }

                setActive('hero');
                updateProgress();
                observeSkillCards();
                setTimeout(observeSkillCards, 350);
                window.addEventListener('scroll', updateProgress, { passive: true });
            })();
        </script>
        """,
        unsafe_allow_html=True,
    )


# -----------------------------
# App
# -----------------------------

def main() -> None:
    mount_scroll_behavior()
    render_cover_banner()
    render_navbar()

    hero_section()
    render_skills_section()
    render_education()
    render_experience()
    render_projects()
    render_languages()
    render_cv()
    render_contact()


if __name__ == "__main__":
    main()
