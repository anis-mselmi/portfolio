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
    page_icon="🧠",
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

        section[data-testid="stSidebar"] {
            background: linear-gradient(180deg, #0f1522 0%, #0b0f17 100%);
            border-right: 1px solid var(--border);
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
            grid-template-columns: repeat(7, minmax(0, 1fr));
            gap: 0.55rem;
        }

        .nav-link {
            display: block;
            width: 100%;
            text-decoration: none;
            color: var(--text) !important;
            background: #111a2b;
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 0.6rem 0.75rem;
            font-size: 0.96rem;
            font-weight: 600;
            text-align: center;
            white-space: nowrap;
            transition: all 0.25s ease;
        }

        .nav-link:hover {
            transform: translateX(2px);
            border-color: rgba(124, 156, 255, 0.55);
            box-shadow: 0 8px 20px rgba(3, 9, 20, 0.38);
        }

        .nav-link.active {
            background: linear-gradient(90deg, rgba(124,156,255,0.26) 0%, rgba(87,224,255,0.16) 100%);
            border-color: rgba(124, 156, 255, 0.65);
            color: #f3f7ff !important;
        }

        .anchor-target {
            display: block;
            position: relative;
            top: -0.7rem;
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
            aspect-ratio: 16 / 4;
            object-fit: cover;
            object-position: center;
            background: #0d1422;
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
            background: linear-gradient(180deg, var(--panel) 0%, var(--panel-2) 100%);
            border: 1px solid var(--border);
            border-radius: 18px;
            padding: 1rem;
            height: 100%;
            display: flex;
            flex-direction: column;
            gap: 0.85rem;
            box-shadow: 0 10px 28px rgba(3, 9, 20, 0.35);
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
            font-size: 0.95rem;
            line-height: 1.5;
        }

        .project-tags {
            margin-top: auto;
        }

        .st-link-button {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            padding: 0.6rem 1.1rem;
            border-radius: 12px;
            background: linear-gradient(90deg, var(--accent) 0%, var(--accent-2) 100%);
            color: #06101a;
            font-weight: 700;
            font-size: 0.95rem;
            letter-spacing: 0.02em;
            text-decoration: none;
            width: fit-content;
            border: 1px solid rgba(255, 255, 255, 0.35);
            box-shadow: 0 10px 24px rgba(87, 224, 255, 0.25);
        }

        .st-link-button:hover {
            transform: translateY(-1px);
            box-shadow: 0 14px 30px rgba(87, 224, 255, 0.35);
        }

        .skill-card {
            background: #0f1626;
            border: 1px solid rgba(124, 156, 255, 0.25);
            border-radius: 16px;
            padding: 1rem 1.1rem;
            box-shadow: 0 10px 26px rgba(3, 9, 20, 0.4);
            margin-bottom: 0.35rem;
        }

        .skill-head {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 0.5rem;
        }

        .skill-name {
            font-weight: 600;
            color: var(--text);
        }

        .skill-value {
            color: var(--muted);
            font-size: 0.9rem;
            font-weight: 600;
        }

        .skill-bar {
            position: relative;
            height: 8px;
            border-radius: 999px;
            background: #0c1422;
            border: 1px solid var(--border);
            overflow: hidden;
        }

        .skill-bar > span {
            position: absolute;
            left: 0;
            top: 0;
            bottom: 0;
            border-radius: 999px;
            background: linear-gradient(90deg, var(--accent) 0%, var(--accent-2) 100%);
        }

        @media (max-width: 900px) {
            .nav-link {
                padding: 0.55rem 0.65rem;
                font-size: 0.92rem;
            }

            .cover-banner {
                aspect-ratio: 16 / 7;
            }

            .sidebar-nav {
                grid-template-columns: repeat(2, minmax(0, 1fr));
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
    },
    {
        "title": "Integrated Preparatory Studies",
        "school": "École Polytechnique de Sousse",
        "years": "2023 – 2025",
    },
    {
        "title": "High School Diploma (Baccalauréat)",
        "school": "Lycée Les Lumières Sousse",
        "years": "2022 – 2023",
    },
]

EXPERIENCE = [
    "Web Master at IEEE SIGHT EPS SB",
    "Ambassador at ATIC, NPC 2.0 PolyRobots",
    "Organizer at Twise Night, IEEE Tejmaana, TCPC, IEEE Day",
    "Participant at CSTAM 1.0, SDC 3.0, WIE ACT 4.0",
]

SKILLS = [
    ("Machine Learning & Deep Learning (AI)", 75),
    ("Python, Jupyter Notebook, Google Colab", 85),
    ("RAG Pipelines & LLM Apps", 75),
    ("Data Analysis & Visualization", 70),
    ("C++", 65),
    ("Git & GitHub", 75),
    ("Problem Solving & Innovation", 80),
]

PROJECTS = [
    {
        "name": "Prototype-de-chatbot-intelligent",
        "desc": "An intelligent chatbot prototype with contextual responses and natural language understanding.",
        "tags": ["AI", "NLP", "Python"],
        "image": "chatbot.jpg",
        "logo": "logo-php-blog.svg",
        "link": "https://github.com/anis-mselmi/Prototype-de-chatbot-intelligent",
        "fit": "cover",
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
    ("Arabic", "Native / Fluent", 100),
    ("English", "Professional Proficiency", 80),
    ("French", "Professional Proficiency", 75),
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
            if image.mode in {"RGBA", "P"}:
                image = image.convert("RGB")
            image.save(buffer, format="JPEG", quality=80)
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
            <div class="section-kicker">Section</div>
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
    cover_path = Path(__file__).parent / "Copie de photo de couverture LinkedIn (1).png"
    cover_data = image_to_data_uri(cover_path, max_width=1600)

    if cover_data:
        st.markdown(
            f"""
            <div class='cover-banner-wrap'>
                <img src='{cover_data}' class='cover-banner' alt='LinkedIn cover image' />
            </div>
            """,
            unsafe_allow_html=True,
        )


# -----------------------------
# Sections
# -----------------------------

def hero_section() -> None:
    section_start("hero", hero=True)
    section_title("Welcome", "👋")
    st.markdown('<div class="hero-card">', unsafe_allow_html=True)
    col1, col2 = st.columns([2, 1], gap="large")

    with col1:
        st.markdown(f"# {PROFILE['name']}")
        st.markdown(f"**{PROFILE['role']}**")
        st.markdown(f"📍 {PROFILE['location']}")
        st.markdown(ABOUT)

        cta_col1, cta_col2 = st.columns(2)
        with cta_col1:
            st.link_button("GitHub 🐙", PROFILE["github"])
        with cta_col2:
            st.link_button("💼 LinkedIn", PROFILE["linkedin"])

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


def render_skills() -> None:
    section_start("skills")
    section_title("Skills", "🛠")
    st.caption("Skill levels are indicative and continuously evolving.")

    cols = st.columns(2, gap="large")
    for index, (skill, level) in enumerate(SKILLS):
        with cols[index % 2]:
            st.markdown(
                f"""
                <div class="skill-card">
                    <div class="skill-head">
                        <span class="skill-name">{skill}</span>
                        <span class="skill-value">{level}%</span>
                    </div>
                    <div class="skill-bar"><span style="width:{level}%"></span></div>
                </div>
                """,
                unsafe_allow_html=True,
            )
    section_end()


def render_education() -> None:
    section_start("education")
    section_title("Education", "🎓")
    for item in EDUCATION:
        st.markdown(f"### {item['title']}")
        st.markdown(f"**{item['school']}**")
        st.markdown(item["years"])
        st.markdown("---")
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
            with st.container(border=True):
                st.markdown(f"### {item['emoji']} {item['title']}")
                st.caption(item["detail"])
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
            link_html = (
                f"<a class='st-link-button' href='{project['link']}' target='_blank'>View on GitHub</a>"
                if project.get("link")
                else ""
            )
            card_html = f"""
                <div class="project-card">
                    {image_html}
                    <div class="project-body">
                        <div class="project-title">{project['name']}</div>
                        <div class="project-desc">{project['desc']}</div>
                        <div class="project-tags">{tags_html}</div>
                        {link_html}
                    </div>
                </div>
            """
            st.markdown(card_html, unsafe_allow_html=True)
    section_end()


def render_languages() -> None:
    section_start("languages")
    section_title("Languages", "🌍")
    st.caption("Communication strengths across native and professional proficiency.")
    cols = st.columns(2, gap="large")
    for index, (lang, level, score) in enumerate(LANGUAGES):
        with cols[index % 2]:
            with st.container(border=True):
                st.markdown(f"### {lang}")
                st.caption(level)
                st.progress(score)
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

    hero_section()
    render_skills()
    render_education()
    render_experience()
    render_projects()
    render_languages()
    render_contact()


if __name__ == "__main__":
    main()
