import streamlit as st


def inject_styles() -> None:
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
                cursor: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='32' height='32' style='font-size:24px'><text y='24'>🍰</text></svg>"), auto !important;
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
                padding-top: 1rem;
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

            /* Hero Card wrapper styled on the columns container */
            div[data-testid="stVerticalBlock"] > div:has(#hero) + div {
                position: relative;
                background:
                    radial-gradient(ellipse 80% 60% at 70% 0%, rgba(87,224,255,0.07) 0%, transparent 60%),
                    radial-gradient(ellipse 60% 80% at 0% 100%, rgba(124,156,255,0.09) 0%, transparent 55%),
                    linear-gradient(160deg, rgba(124,156,255,0.10) 0%, rgba(87,224,255,0.04) 100%);
                border: 1px solid rgba(124,156,255,0.18);
                border-radius: 28px;
                padding: 2.5rem 2.5rem 2.2rem;
                box-shadow:
                    0 24px 60px rgba(3, 9, 20, 0.55),
                    0 0 0 1px rgba(87,224,255,0.06) inset;
                animation: heroFadeUp 0.7s cubic-bezier(0.2,0.8,0.2,1) both;
            }

            /* Align columns to the top */
            div[data-testid="stVerticalBlock"] > div:has(#hero) + div > div[data-testid="stHorizontalBlock"] {
                align-items: flex-start !important;
            }

            @keyframes heroFadeUp {
                from { opacity: 0; transform: translateY(22px); }
                to   { opacity: 1; transform: translateY(0); }
            }

            .hero-name {
                font-size: 3.2rem;
                font-weight: 800;
                letter-spacing: -0.03em;
                line-height: 1.1;
                margin-bottom: 0.6rem;
                background: linear-gradient(110deg, #ffffff 30%, #57e0ff 65%, #7c9cff 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
            }

            .hero-role-row {
                margin-bottom: 0.55rem;
            }

            .hero-role-badge {
                display: inline-flex;
                align-items: center;
                gap: 0.45rem;
                padding: 0.3rem 0.9rem 0.3rem 0.65rem;
                border-radius: 999px;
                background: rgba(87, 224, 255, 0.07);
                border: 1px solid rgba(87, 224, 255, 0.22);
                font-size: 0.88rem;
                font-weight: 600;
                color: var(--accent-2);
                letter-spacing: 0.01em;
            }

            .hero-role-dot {
                display: inline-block;
                width: 7px;
                height: 7px;
                border-radius: 50%;
                background: #57e0ff;
                box-shadow: 0 0 8px #57e0ff;
                animation: visitorPulse 2s ease-in-out infinite;
                flex-shrink: 0;
            }

            .hero-location {
                font-size: 0.88rem;
                color: var(--muted);
                margin-bottom: 1rem;
            }

            .hero-about-list {
                list-style-type: none;
                padding-left: 0;
                margin-top: 1rem;
                margin-bottom: 0;
                font-size: 1.14rem;
                color: #c8d8ea;
                line-height: 1.75;
            }

            .hero-about-list li {
                margin-bottom: 0.85rem;
                position: relative;
            }

            .hero-about-list li:last-child {
                margin-bottom: 0;
            }

            .hero-actions {
                display: flex;
                gap: 0.75rem;
                margin-top: 1.5rem;
                flex-wrap: wrap;
                align-items: center;
            }

            .hero-photo-wrap {
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100%;
                padding-top: 0.5rem;
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

            .hero-social-btn {
                display: inline-flex;
                align-items: center;
                justify-content: center;
                gap: 0.45rem;
                padding: 0.55rem 1.15rem;
                border-radius: 12px;
                font-weight: 600;
                font-size: 0.85rem;
                text-decoration: none !important;
                transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
                color: #ffffff !important;
                width: fit-content;
                letter-spacing: 0.01em;
            }

            .hero-social-btn:hover {
                transform: translateY(-3px) scale(1.04);
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

            .btn-cv {
                background: linear-gradient(135deg, #7c3aed 0%, #4f1fc8 100%);
                border: 1px solid rgba(124, 58, 237, 0.5);
                box-shadow: 0 6px 18px rgba(124, 58, 237, 0.35);
            }

            .btn-cv:hover {
                box-shadow: 0 10px 24px rgba(124, 58, 237, 0.6);
                border-color: rgba(167, 139, 250, 0.7);
                background: linear-gradient(135deg, #8b5cf6 0%, #6d28d9 100%);
            }

            /* ── Visitor Badge ── */
            .visitor-badge {
                display: inline-flex;
                align-items: center;
                gap: 0.5rem;
                padding: 0.28rem 0.9rem 0.28rem 0.65rem;
                border-radius: 999px;
                background: rgba(34, 197, 94, 0.07);
                border: 1px solid rgba(34, 197, 94, 0.22);
                font-size: 0.8rem;
                color: var(--muted);
                margin-bottom: 0.75rem;
                width: fit-content;
            }

            .visitor-dot {
                display: inline-block;
                width: 8px;
                height: 8px;
                border-radius: 50%;
                background: #22c55e;
                box-shadow: 0 0 6px #22c55e;
                animation: visitorPulse 2s ease-in-out infinite;
            }

            .visitor-label {
                color: var(--text);
            }

            @keyframes visitorPulse {
                0%, 100% { opacity: 1; transform: scale(1); }
                50% { opacity: 0.6; transform: scale(0.85); }
            }

            /* ── GitHub Activity Feed ── */
            .gh-feed {
                display: flex;
                flex-direction: column;
                gap: 0.55rem;
                margin-top: 0.75rem;
            }

            .gh-event-card {
                display: flex;
                align-items: flex-start;
                gap: 0.85rem;
                padding: 0.75rem 1rem;
                border-radius: 14px;
                background: linear-gradient(180deg, var(--panel) 0%, var(--panel-2) 100%);
                border: 1px solid var(--border);
                transition: transform 0.25s ease, box-shadow 0.25s ease;
            }

            .gh-event-card:hover {
                transform: translateX(4px);
                box-shadow: 0 4px 18px rgba(87, 224, 255, 0.1);
                border-color: rgba(87, 224, 255, 0.2);
            }

            .gh-event-icon {
                font-size: 1.3rem;
                flex-shrink: 0;
                margin-top: 0.1rem;
            }

            .gh-event-body {
                flex: 1;
                min-width: 0;
            }

            .gh-event-type {
                font-size: 0.78rem;
                font-weight: 700;
                text-transform: uppercase;
                letter-spacing: 0.08em;
                color: var(--accent-2);
                margin-bottom: 0.15rem;
            }

            .gh-repo-link {
                font-size: 0.88rem;
                font-weight: 600;
                color: var(--text) !important;
                text-decoration: none !important;
                white-space: nowrap;
                overflow: hidden;
                text-overflow: ellipsis;
                display: block;
            }

            .gh-repo-link:hover {
                color: var(--accent-2) !important;
                text-decoration: underline !important;
            }

            .gh-commit-msg {
                font-size: 0.78rem;
                color: var(--muted);
                margin-top: 0.2rem;
                white-space: nowrap;
                overflow: hidden;
                text-overflow: ellipsis;
            }

            .gh-event-date {
                font-size: 0.75rem;
                color: var(--muted);
                white-space: nowrap;
                flex-shrink: 0;
                margin-top: 0.15rem;
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
                display: flex;
                justify-content: center;
                align-items: center;
                flex-wrap: wrap;
                gap: 0.55rem;
                max-width: fit-content;
                margin: 0 auto;
            }

            .nav-link {
                display: block;
                width: auto;
                min-width: 125px;
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

            /* Collapse spacing around scroll anchors */
            div[data-testid="element-container"]:has(.anchor-target) {
                height: 0px !important;
                margin: 0px !important;
                padding: 0px !important;
            }

            .cover-banner-wrap {
                margin: 0 0 1.75rem;
                border-radius: 28px;
                overflow: hidden;
                box-shadow: 0 20px 50px rgba(3, 9, 20, 0.5);
                transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            }

            .cover-banner-wrap:hover {
                transform: translateY(-4px) scale(1.005);
            }

            .cover-banner {
                width: 100%;
                display: block;
                height: 240px;
                max-height: 240px;
                object-fit: cover;
                object-position: center;
                transition: filter 0.5s ease;
                filter: brightness(0.92) saturate(1.1);
            }

            .cover-banner-wrap:hover .cover-banner {
                filter: brightness(1.05) saturate(1.15);
            }

            .hero-frame {
                margin: 2.2rem auto 0;
                width: 290px;
                max-width: 100%;
                aspect-ratio: 1 / 1;
                padding: 6px;
                border-radius: 60% 40% 30% 70% / 60% 30% 70% 40%;
                background: linear-gradient(120deg, rgba(124, 156, 255, 0.95), rgba(87, 224, 255, 0.6), rgba(124, 156, 255, 0.95));
                background-size: 200% 200%;
                animation:
                    heroBorderShift 8s ease-in-out infinite,
                    heroMorph 12s ease-in-out infinite;
                box-shadow:
                    0 16px 38px rgba(3, 9, 20, 0.5),
                    0 0 25px rgba(87, 224, 255, 0.25),
                    inset 0 0 12px rgba(255, 255, 255, 0.2);
                transition: transform 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275), box-shadow 0.5s ease;
            }


            .hero-frame:hover {
                transform: scale(1.05) rotate(1.5deg);
                box-shadow: 
                    0 22px 48px rgba(3, 9, 20, 0.6),
                    0 0 35px rgba(87, 224, 255, 0.45),
                    0 0 15px rgba(124, 156, 255, 0.3);
            }

            .hero-image {
                display: block;
                width: 100%;
                height: 100%;
                aspect-ratio: 1 / 1;
                object-fit: cover;
                border-radius: inherit;
                border: 1px solid rgba(15, 22, 38, 0.7);
                transition: filter 0.5s ease;
            }

            .hero-frame:hover .hero-image {
                filter: saturate(1.08) brightness(1.02);
            }

            @keyframes heroMorph {
                0% {
                    border-radius: 60% 40% 30% 70% / 60% 30% 70% 40%;
                }
                50% {
                    border-radius: 40% 60% 70% 30% / 50% 60% 30% 65%;
                }
                100% {
                    border-radius: 60% 40% 30% 70% / 60% 30% 70% 40%;
                }
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
                margin-bottom: 1.5rem;
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
                font-size: 0.85rem;
                line-height: 1.4;
                display: -webkit-box;
                -webkit-line-clamp: 3;
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
                transform: translateY(0) scale(1);
                transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275), box-shadow 0.4s ease;
                height: 100%;
            }

            .lang-tone-arabic {
                background: linear-gradient(130deg, rgba(34, 197, 94, 0.4), rgba(12, 18, 32, 0.1), rgba(16, 185, 129, 0.4)) !important;
                box-shadow: 0 10px 25px rgba(2, 28, 12, 0.3) !important;
            }
            .lang-tone-english {
                background: linear-gradient(130deg, rgba(59, 130, 246, 0.4), rgba(12, 18, 32, 0.1), rgba(87, 224, 255, 0.4)) !important;
                box-shadow: 0 10px 25px rgba(2, 12, 28, 0.3) !important;
            }
            .lang-tone-french {
                background: linear-gradient(130deg, rgba(239, 68, 68, 0.4), rgba(12, 18, 32, 0.1), rgba(59, 130, 246, 0.4)) !important;
                box-shadow: 0 10px 25px rgba(28, 2, 2, 0.3) !important;
            }

            @media (hover: hover) {
                .lang-glass-card:hover {
                    transform: translateY(-8px) scale(1.03) !important;
                }
                .lang-tone-arabic:hover {
                    box-shadow: 0 18px 38px rgba(2, 28, 12, 0.45), 0 0 20px rgba(34, 197, 94, 0.25) !important;
                    background: linear-gradient(130deg, rgba(34, 197, 94, 0.8), rgba(12, 18, 32, 0.3), rgba(16, 185, 129, 0.8)) !important;
                }
                .lang-tone-english:hover {
                    box-shadow: 0 18px 38px rgba(2, 12, 28, 0.45), 0 0 20px rgba(59, 130, 246, 0.25) !important;
                    background: linear-gradient(130deg, rgba(59, 130, 246, 0.8), rgba(12, 18, 32, 0.3), rgba(87, 224, 255, 0.8)) !important;
                }
                .lang-tone-french:hover {
                    box-shadow: 0 18px 38px rgba(28, 2, 2, 0.45), 0 0 20px rgba(239, 68, 68, 0.25) !important;
                    background: linear-gradient(130deg, rgba(239, 68, 68, 0.8), rgba(12, 18, 32, 0.3), rgba(59, 130, 246, 0.8)) !important;
                }
            }

            .lang-glass-card-inner {
                position: relative;
                border-radius: 21px;
                height: 100%;
                min-height: 165px;
                padding: 1rem;
                display: flex;
                flex-direction: column;
                justify-content: space-between;
                gap: 0.5rem;
                background: linear-gradient(180deg, var(--panel) 0%, var(--panel-2) 100%);
                border: 1px solid rgba(255, 255, 255, 0.05);
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
                width: 44px;
                height: 44px;
                border-radius: 50%;
                background: rgba(255, 255, 255, 0.05);
                border: 1px solid rgba(255, 255, 255, 0.15);
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.35);
                overflow: hidden;
            }

            .lang-flag-img {
                width: 100% !important;
                height: 100% !important;
                object-fit: cover !important;
                transition: transform 0.35s ease;
            }

            .lang-glass-card:hover .lang-flag-img {
                transform: scale(1.15);
            }

            .lang-flag-img--us {
                object-fit: cover !important;
            }

            .lang-badge {
                display: inline-flex;
                align-items: center;
                justify-content: center;
                padding: 0.22rem 0.65rem;
                border-radius: 999px;
                font-size: 0.68rem;
                letter-spacing: 0.06em;
                text-transform: uppercase;
                font-weight: 800;
            }

            .lang-tone-arabic .lang-badge {
                background: rgba(34, 197, 94, 0.12);
                border: 1px solid rgba(34, 197, 94, 0.35);
                color: #4ade80;
            }

            .lang-tone-english .lang-badge {
                background: rgba(59, 130, 246, 0.12);
                border: 1px solid rgba(59, 130, 246, 0.35);
                color: #60a5fa;
            }

            .lang-tone-french .lang-badge {
                background: rgba(239, 68, 68, 0.12);
                border: 1px solid rgba(239, 68, 68, 0.35);
                color: #f87171;
            }

            .lang-name {
                font-size: 1.15rem;
                font-weight: 800;
                color: #ffffff;
                letter-spacing: -0.01em;
                line-height: 1.1;
                margin-top: 0.1rem;
            }

            .lang-note {
                font-size: 0.84rem;
                color: var(--muted);
                line-height: 1.4;
                margin-top: 0.05rem;
            }

            .lang-accent {
                display: none;
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
                    height: 160px;
                    max-height: 160px;
                }
            }

            @media (max-width: 900px) {
                .block-container {
                    padding-top: 1.2rem;
                    padding-bottom: 2rem;
                }

                div[data-testid="stVerticalBlock"] > div:has(#hero) + div {
                    padding: 1.15rem;
                    border-radius: 18px;
                }

                .cover-banner-wrap {
                    margin: 4.5rem 0 1.25rem;
                    padding: 0;
                    border-radius: 18px;
                }

                .cover-banner {
                    border-radius: 18px;
                    height: 200px;
                    max-height: 200px;
                    object-position: center;
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
                    min-width: 110px;
                }

                .nav-link-inner {
                    padding: 0.45rem 0.5rem;
                    font-size: 0.85rem;
                }

                .sidebar-nav {
                    max-width: 100%;
                }
            }

            @media (max-width: 640px) {
                .sticky-navbar {
                    padding: 0.4rem 0.5rem;
                }

                .sidebar-nav {
                    gap: 0.25rem;
                    max-width: 100%;
                }

                .nav-link {
                    min-width: 80px;
                    flex-grow: 1;
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
                    height: 100px;
                    max-height: 100px;
                    object-position: center;
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
                border-radius: 16px;
                padding: 1.5px;
                overflow: hidden;
                background: linear-gradient(135deg, rgba(124, 156, 255, 0.2), rgba(87, 224, 255, 0.2));
                box-shadow: 0 10px 30px rgba(3, 9, 20, 0.25);
                transform: translateY(0);
                transition: transform 0.4s cubic-bezier(0.165, 0.84, 0.44, 1), box-shadow 0.4s ease, background 0.4s ease;
                height: 100%;
                min-height: 280px;
                display: flex;
                flex-direction: column;
                margin-bottom: 1rem;
            }

            .education-card:hover {
                transform: translateY(-8px);
                background: linear-gradient(135deg, var(--accent) 0%, var(--accent-2) 100%);
                box-shadow: 0 15px 35px rgba(3, 9, 20, 0.45), 0 0 25px rgba(87, 224, 255, 0.2);
            }

            .education-card-inner {
                border-radius: 15px;
                background: rgba(18, 24, 38, 0.82);
                backdrop-filter: blur(12px);
                -webkit-backdrop-filter: blur(12px);
                padding: 1.5rem;
                flex-grow: 1;
                width: 100%;
                display: flex;
                flex-direction: column;
                gap: 0.75rem;
                height: 100%;
            }

            .education-card-header {
                display: flex;
                align-items: center;
                justify-content: space-between;
                width: 100%;
                margin-bottom: 0.25rem;
            }

            .education-emoji-wrapper {
                display: flex;
                align-items: center;
                justify-content: center;
                width: 46px;
                height: 46px;
                border-radius: 50%;
                background: rgba(124, 156, 255, 0.08);
                border: 1px solid rgba(124, 156, 255, 0.15);
                font-size: 1.35rem;
                box-shadow: inset 0 2px 6px rgba(124, 156, 255, 0.1);
                transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275), background 0.4s ease, border-color 0.4s ease;
            }

            .education-card:hover .education-emoji-wrapper {
                transform: scale(1.1) rotate(5deg);
                background: rgba(87, 224, 255, 0.15);
                border-color: rgba(87, 224, 255, 0.3);
            }

            .education-years-badge {
                background: rgba(87, 224, 255, 0.08);
                color: var(--accent-2);
                font-size: 0.75rem;
                font-weight: 600;
                padding: 0.3rem 0.75rem;
                border-radius: 20px;
                border: 1px solid rgba(87, 224, 255, 0.15);
                letter-spacing: 0.05em;
                transition: background 0.3s ease, border-color 0.3s ease;
            }

            .education-card:hover .education-years-badge {
                background: rgba(87, 224, 255, 0.15);
                border-color: rgba(87, 224, 255, 0.35);
            }

            .education-card .education-title {
                font-size: 1.15rem;
                font-weight: 700;
                color: #ffffff;
                line-height: 1.35;
                margin: 0;
            }

            .education-card .education-school {
                color: var(--accent);
                font-size: 0.92rem;
                font-weight: 500;
                line-height: 1.4;
                margin-top: -0.25rem;
            }

            .education-card .education-detail {
                color: var(--muted);
                font-size: 0.85rem;
                line-height: 1.5;
                margin: 0;
                margin-top: auto;
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
                max-width: 1100px;
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

            /* Custom Interactive AI Terminal Console */
            .terminal-window {
                background: linear-gradient(135deg, rgba(13, 21, 37, 0.85) 0%, rgba(7, 12, 22, 0.95) 100%) !important;
                border: 1px solid rgba(87, 224, 255, 0.25) !important;
                border-radius: 16px !important;
                box-shadow: 0 16px 40px rgba(3, 9, 20, 0.65), 0 0 20px rgba(87, 224, 255, 0.1) !important;
                padding: 1.25rem !important;
                font-family: 'Courier New', Courier, monospace !important;
                margin: 1.5rem 0 !important;
                backdrop-filter: blur(12px) !important;
                -webkit-backdrop-filter: blur(12px) !important;
            }

            .terminal-header {
                display: flex;
                align-items: center;
                justify-content: space-between;
                border-bottom: 1px solid rgba(87, 224, 255, 0.2);
                padding-bottom: 0.75rem;
                margin-bottom: 1rem;
            }

            .terminal-dots {
                display: flex;
                gap: 0.4rem;
            }

            .terminal-dot {
                width: 11px;
                height: 11px;
                border-radius: 50%;
                display: inline-block;
            }

            .dot-red { background: #ff5f56 !important; }
            .dot-yellow { background: #ffbd2e !important; }
            .dot-green { background: #27c93f !important; }

            .terminal-title {
                color: var(--muted);
                font-size: 0.82rem;
                font-weight: 600;
                letter-spacing: 0.05em;
            }

            .terminal-badges {
                display: flex;
                gap: 0.55rem;
                flex-wrap: wrap;
                align-items: center;
            }

            .terminal-badge {
                font-size: 0.72rem !important;
                padding: 0.2rem 0.55rem !important;
                border-radius: 6px !important;
                font-weight: 700 !important;
                text-transform: uppercase !important;
                letter-spacing: 0.04em !important;
                display: inline-flex !important;
                align-items: center !important;
                border: 1px solid rgba(255, 255, 255, 0.1) !important;
            }

            .status-online {
                background: rgba(39, 201, 63, 0.15) !important;
                color: #27c93f !important;
                border-color: rgba(39, 201, 63, 0.35) !important;
                box-shadow: 0 0 10px rgba(39, 201, 63, 0.2) !important;
            }

            .status-local {
                background: rgba(87, 224, 255, 0.12) !important;
                color: var(--accent-2) !important;
                border-color: rgba(87, 224, 255, 0.3) !important;
                box-shadow: 0 0 10px rgba(87, 224, 255, 0.15) !important;
            }

            .badge-mode {
                background: rgba(124, 156, 255, 0.12) !important;
                color: var(--accent) !important;
                border-color: rgba(124, 156, 255, 0.3) !important;
            }

            .terminal-body {
                max-height: 580px;
                overflow-y: auto;
                display: flex;
                flex-direction: column;
                gap: 0.85rem;
                padding-right: 0.5rem;
                font-size: 0.92rem;
            }

            .terminal-body::-webkit-scrollbar {
                width: 6px;
            }
            .terminal-body::-webkit-scrollbar-track {
                background: transparent;
            }
            .terminal-body::-webkit-scrollbar-thumb {
                background: rgba(87, 224, 255, 0.2);
                border-radius: 99px;
            }

            .terminal-row {
                line-height: 1.6;
                word-wrap: break-word;
                white-space: pre-wrap;
            }

            .terminal-user {
                color: var(--accent-2) !important;
                font-weight: bold;
            }

            .terminal-prompt {
                color: var(--accent) !important;
                font-weight: bold;
                margin-right: 0.4rem;
            }

            .terminal-output {
                color: #e6ecf2 !important;
            }

            .terminal-output a {
                color: var(--accent-2) !important;
                text-decoration: underline !important;
            }

            .terminal-cursor {
                display: inline-block;
                color: #a6e22e;
                font-weight: 400;
                margin-left: 1px;
                animation: cursorBlink 0.75s step-start infinite;
            }

            @keyframes cursorBlink {
                0%, 100% { opacity: 1; }
                50% { opacity: 0; }
            }

            /* NVIDIA Certifications Section Styling */
            .cert-grid {
                display: grid;
                grid-template-columns: repeat(4, 1fr);
                gap: 1rem;
                margin-bottom: 2rem;
                width: 100%;
            }
            @media (max-width: 1400px) {
                .cert-grid {
                    grid-template-columns: repeat(3, 1fr);
                }
            }
            @media (max-width: 992px) {
                .cert-grid {
                    grid-template-columns: repeat(2, 1fr);
                }
            }
            @media (max-width: 768px) {
                .cert-grid {
                    grid-template-columns: 1fr;
                }
            }

            .cert-card {
                --brand-color: #76b900;
                --brand-chip-color: #b3ea5c;
                --brand-bg-glow: rgba(118, 185, 0, 0.35);
                --brand-gradient-start: rgba(118, 185, 0, 0.55);
                --brand-gradient-hover-start: rgba(118, 185, 0, 1);
                --brand-btn-gradient: linear-gradient(90deg, #76b900 0%, #a6e22e 100%);
                --brand-badge-bg: rgba(118, 185, 0, 0.1);
                --brand-chip-bg: rgba(118, 185, 0, 0.08);
                --brand-chip-border: rgba(118, 185, 0, 0.15);
                --brand-badge-border: rgba(118, 185, 0, 0.25);
                --brand-logo-glow: rgba(118, 185, 0, 0.4);

                position: relative;
                margin-bottom: 0;
                border-radius: 20px;
                padding: 1px;
                overflow: hidden;
                background: linear-gradient(130deg, var(--brand-gradient-start), rgba(124, 156, 255, 0.2), rgba(87, 224, 255, 0.45));
                box-shadow: 0 12px 32px rgba(3, 9, 20, 0.38);
                transform: translateY(0) scale(1);
                transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275), box-shadow 0.4s ease, filter 0.4s ease;
                height: 100%;
                display: flex;
                flex-direction: column;
            }

            .cert-card.brand-datacamp {
                --brand-color: #03ef90;
                --brand-chip-color: #03ef90;
                --brand-bg-glow: rgba(3, 239, 144, 0.35);
                --brand-gradient-start: rgba(3, 239, 144, 0.55);
                --brand-gradient-hover-start: rgba(3, 239, 144, 1);
                --brand-btn-gradient: linear-gradient(90deg, #03ef90 0%, #02965b 100%);
                --brand-badge-bg: rgba(3, 239, 144, 0.1);
                --brand-chip-bg: rgba(3, 239, 144, 0.08);
                --brand-chip-border: rgba(3, 239, 144, 0.15);
                --brand-badge-border: rgba(3, 239, 144, 0.25);
                --brand-logo-glow: rgba(3, 239, 144, 0.4);
            }

            .cert-card.brand-kaggle {
                --brand-color: #20beff;
                --brand-chip-color: #20beff;
                --brand-bg-glow: rgba(32, 190, 255, 0.35);
                --brand-gradient-start: rgba(32, 190, 255, 0.55);
                --brand-gradient-hover-start: rgba(32, 190, 255, 1);
                --brand-btn-gradient: linear-gradient(90deg, #20beff 0%, #008abc 100%);
                --brand-badge-bg: rgba(32, 190, 255, 0.1);
                --brand-chip-bg: rgba(32, 190, 255, 0.08);
                --brand-chip-border: rgba(32, 190, 255, 0.15);
                --brand-badge-border: rgba(32, 190, 255, 0.25);
                --brand-logo-glow: rgba(32, 190, 255, 0.4);
            }

            @media (hover: hover) {
                .cert-card:hover {
                    transform: translateY(-8px) scale(1.02);
                    box-shadow: 0 18px 42px rgba(3, 9, 20, 0.5), 0 0 25px var(--brand-bg-glow);
                    background: linear-gradient(130deg, var(--brand-gradient-hover-start), rgba(124, 156, 255, 0.5), rgba(87, 224, 255, 0.8));
                    filter: saturate(1.05);
                }
            }

            .cert-card-inner {
                position: relative;
                border-radius: 19px;
                background: linear-gradient(180deg, var(--panel) 0%, var(--panel-2) 100%);
                padding: 1rem;
                height: 100%;
                flex-grow: 1;
                display: flex;
                flex-direction: column;
                gap: 0.5rem;
            }

            .cert-head {
                display: flex;
                align-items: center;
                justify-content: space-between;
                gap: 0.5rem;
            }

            .cert-logo {
                width: 26px;
                height: 26px;
                object-fit: contain;
                filter: drop-shadow(0 0 8px var(--brand-logo-glow));
            }

            .cert-badge {
                display: inline-flex;
                align-items: center;
                border-radius: 999px;
                padding: 0.18rem 0.45rem;
                font-size: 0.65rem;
                font-weight: 700;
                letter-spacing: 0.05em;
                text-transform: uppercase;
                color: var(--brand-color);
                background: var(--brand-badge-bg);
                border: 1px solid var(--brand-badge-border);
            }

            .cert-title {
                font-size: 0.98rem;
                font-weight: 700;
                color: #ffffff;
                line-height: 1.3;
            }

            .cert-meta {
                font-size: 0.78rem;
                color: var(--muted);
                display: flex;
                flex-direction: column;
                gap: 0.1rem;
            }

            .cert-chips {
                display: flex;
                flex-wrap: wrap;
                gap: 0.25rem;
                margin-top: 0.1rem;
            }

            .cert-chip {
                display: inline-block;
                padding: 0.15rem 0.4rem;
                border-radius: 999px;
                background: var(--brand-chip-bg);
                border: 1px solid var(--brand-chip-border);
                color: var(--brand-chip-color);
                font-size: 0.68rem;
            }

            .cert-btn {
                margin-top: auto;
                width: 100%;
                display: inline-flex;
                align-items: center;
                justify-content: center;
                padding: 0.5rem 0.8rem;
                border-radius: 10px;
                font-weight: 700;
                font-size: 0.78rem;
                text-decoration: none !important;
                background: var(--brand-btn-gradient);
                color: #0b0f17 !important;
                border: 1px solid rgba(255, 255, 255, 0.2);
                box-shadow: 0 4px 14px var(--brand-bg-glow);
                transition: transform 0.25s ease, box-shadow 0.25s ease, color 0.25s ease;
            }

            .cert-btn:hover {
                transform: translateY(-2px);
                box-shadow: 0 8px 20px var(--brand-bg-glow);
                color: #0b0f17 !important;
            }

            .cert-fade-in {
                opacity: 0;
                transform: translateY(16px);
                animation: certReveal 650ms cubic-bezier(0.2, 0.7, 0.2, 1) forwards;
                animation-delay: var(--delay, 0ms);
            }

            @keyframes certReveal {
                to {
                    opacity: 1;
                    transform: translateY(0);
                }
            }

            /* ── Contact Section ── */
            .contact-success {
                display: flex;
                align-items: flex-start;
                gap: 0.85rem;
                padding: 1rem 1.25rem;
                border-radius: 14px;
                background: rgba(34, 197, 94, 0.08);
                border: 1px solid rgba(34, 197, 94, 0.25);
                margin-top: 0.75rem;
                animation: heroFadeUp 0.4s ease both;
            }

            .contact-fallback {
                padding: 0.85rem 1.1rem;
                border-radius: 12px;
                background: rgba(124, 156, 255, 0.07);
                border: 1px solid rgba(124, 156, 255, 0.22);
                color: var(--muted);
                font-size: 0.9rem;
                margin-top: 0.75rem;
                line-height: 1.6;
            }

            .contact-info-card {
                background: linear-gradient(180deg, var(--panel) 0%, var(--panel-2) 100%);
                border: 1px solid var(--border);
                border-radius: 20px;
                padding: 1.5rem 1.75rem;
                box-shadow: 0 10px 28px rgba(3, 9, 20, 0.35);
                height: 100%;
            }

            .contact-info-title {
                font-size: 0.78rem;
                font-weight: 700;
                color: var(--accent-2);
                letter-spacing: 0.14em;
                text-transform: uppercase;
                margin-bottom: 1.25rem;
            }

            .contact-info-item {
                display: flex;
                align-items: center;
                gap: 0.75rem;
                padding: 0.6rem 0;
                border-bottom: 1px solid rgba(31, 42, 59, 0.5);
                font-size: 0.88rem;
            }

            .contact-info-item:last-child {
                border-bottom: none;
            }

            .contact-info-icon {
                font-size: 1.1rem;
                flex-shrink: 0;
                width: 28px;
                text-align: center;
            }

            .contact-info-link {
                color: var(--accent) !important;
                text-decoration: none !important;
                transition: color 0.2s ease;
                word-break: break-all;
            }

            .contact-info-link:hover {
                color: var(--accent-2) !important;
                text-decoration: underline !important;
            }

            .contact-info-divider {
                height: 1px;
                background: linear-gradient(90deg, rgba(124,156,255,0.3), transparent);
                margin: 0.35rem 0;
            }

            /* Hackathon Wins Styling */
            .hackathon-card {
                background: linear-gradient(130deg, rgba(255, 215, 0, 0.45), rgba(124, 156, 255, 0.2), rgba(87, 224, 255, 0.45)) !important;
                box-shadow: 0 12px 32px rgba(3, 9, 20, 0.38) !important;
                margin-bottom: 1.5rem;
                position: relative;
                border-radius: 20px;
                padding: 1px;
                overflow: hidden;
                height: 325px !important;
                display: flex;
                flex-direction: column;
            }

            @media (hover: hover) {
                .hackathon-card:hover {
                    transform: translateY(-8px) scale(1.02) !important;
                    box-shadow: 0 18px 42px rgba(3, 9, 20, 0.5), 0 0 25px rgba(255, 215, 0, 0.25) !important;
                    background: linear-gradient(130deg, rgba(255, 215, 0, 0.85), rgba(124, 156, 255, 0.5), rgba(87, 224, 255, 0.8)) !important;
                }
            }

            .hackathon-card-inner {
                border-radius: 19px;
                background: linear-gradient(180deg, var(--panel) 0%, var(--panel-2) 100%);
                padding: 0.65rem;
                height: 100%;
                flex-grow: 1;
                display: flex;
                flex-direction: column;
                gap: 0.3rem;
            }

            .hackathon-badge-container {
                position: absolute;
                top: 0.95rem;
                right: 0.95rem;
                z-index: 10;
            }

            .hackathon-award-badge {
                display: inline-flex;
                align-items: center;
                border-radius: 999px;
                padding: 0.2rem 0.5rem;
                font-size: 0.65rem;
                font-weight: 800;
                letter-spacing: 0.05em;
                text-transform: uppercase;
                color: #ffd700;
                background: rgba(0, 0, 0, 0.65);
                border: 1px solid rgba(255, 215, 0, 0.5);
                backdrop-filter: blur(8px);
                -webkit-backdrop-filter: blur(8px);
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.4);
            }

            .hackathon-image {
                height: 160px !important;
                aspect-ratio: auto !important;
                border-radius: 13px;
                object-fit: cover;
                width: 100%;
                flex-shrink: 0;
            }

            .hackathon-body {
                padding: 0.2rem 0.15rem 0.1rem 0.15rem;
                display: flex;
                flex-direction: column;
                flex-grow: 1;
                justify-content: space-between;
                gap: 0.25rem !important;
            }

            .hackathon-title {
                font-size: 0.98rem;
                font-weight: 700;
                color: #ffffff;
                margin-bottom: 0.05rem;
                white-space: nowrap;
                overflow: hidden;
                text-overflow: ellipsis;
            }

            .hackathon-desc {
                font-size: 0.82rem;
                color: var(--muted);
                line-height: 1.35;
                margin-bottom: 0.15rem;
                display: -webkit-box;
                -webkit-line-clamp: 1;
                -webkit-box-orient: vertical;
                overflow: hidden;
                text-overflow: ellipsis;
                height: 1.35em;
            }

            .hackathon-tags {
                display: flex;
                flex-wrap: wrap;
                gap: 0.25rem;
                margin-top: auto;
            }

            /* ═══════════════════════════════════
               MOBILE RESPONSIVE — clean stacked layout
               ═══════════════════════════════════ */

            @media (max-width: 768px) {

                /* ── Navbar: 2-row wrap on tablet ── */
                .sticky-navbar {
                    padding: 0.35rem 0.6rem !important;
                }
                .sidebar-nav {
                    flex-wrap: wrap !important;
                    justify-content: center !important;
                    gap: 0.3rem !important;
                    max-width: 100% !important;
                }
                .nav-link {
                    min-width: 100px !important;
                }
                .nav-link-inner {
                    padding: 0.42rem 0.45rem !important;
                    font-size: 0.78rem !important;
                }

                /* ── Cover banner ── */
                .cover-banner {
                    height: 130px !important;
                    max-height: 130px !important;
                }
                .cover-banner-wrap {
                    margin-top: 5rem !important;
                }

                /* ── Hero frame ── */
                .hero-frame {
                    width: 160px !important;
                    height: 160px !important;
                    margin: 0 auto 1rem !important;
                }

                /* ── Project / hackathon cards: auto height on mobile ── */
                .project-card,
                .project-card-inner {
                    height: auto !important;
                }
                .hackathon-card {
                    height: auto !important;
                    min-height: 260px !important;
                }

                /* ── Language cards: 1-column on mobile ── */
                .lang-cards-grid {
                    grid-template-columns: 1fr !important;
                }

                /* ── Certs: 1-column on mobile ── */
                .cert-grid {
                    grid-template-columns: 1fr !important;
                }

                /* ── Contact card padding ── */
                .contact-info-card {
                    padding: 1.5rem 1.25rem !important;
                    margin-top: 1rem !important;
                }
                .contact-icon-box {
                    width: 38px !important;
                    height: 38px !important;
                }
                .contact-info-item {
                    padding: 0.75rem 0.9rem !important;
                }

                /* ── Typography scale ── */
                h1 { font-size: 1.9rem !important; }
                h2, .section-title { font-size: 1.5rem !important; }
                h3 { font-size: 1.1rem !important; }
                .section-kicker {
                    font-size: 0.7rem !important;
                    letter-spacing: 0.12em !important;
                }

                /* ── Block container ── */
                .block-container {
                    padding-left: 1rem !important;
                    padding-right: 1rem !important;
                }
            }

            /* ── Small phones (< 480px) ── */
            @media (max-width: 480px) {
                .nav-link {
                    min-width: 85px !important;
                    flex-grow: 1 !important;
                }
                .nav-link-inner {
                    font-size: 0.7rem !important;
                    padding: 0.38rem 0.3rem !important;
                    white-space: normal !important;
                    text-align: center !important;
                }
                .hero-frame {
                    width: 130px !important;
                    height: 130px !important;
                }
                .block-container {
                    padding-left: 0.7rem !important;
                    padding-right: 0.7rem !important;
                }
                h1 { font-size: 1.6rem !important; }
                h2, .section-title { font-size: 1.3rem !important; }
                .cover-banner {
                    height: 100px !important;
                    max-height: 100px !important;
                }
            }

        </style>
        """,
        unsafe_allow_html=True,
    )
