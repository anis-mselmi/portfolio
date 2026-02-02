import base64
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
    initial_sidebar_state="expanded",
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

        html, body, [class*="css"] {
            font-family: 'Inter', system-ui, -apple-system, sans-serif;
        }

        .stApp {
            background: radial-gradient(1200px 600px at 10% -10%, #1c2a4a 0%, transparent 60%),
                        radial-gradient(900px 500px at 90% -20%, #1b3140 0%, transparent 55%),
                        var(--bg);
            color: var(--text);
        }

        section[data-testid="stSidebar"] {
            background: linear-gradient(180deg, #0f1522 0%, #0b0f17 100%);
            border-right: 1px solid var(--border);
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

        .hero-image {
            margin-top: 3.6rem;
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
            height: 180px;
            object-fit: cover;
            border-radius: 14px;
            border: 1px solid var(--border);
            background: #0b0f17;
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
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# Data
# -----------------------------
PROFILE = {
    "name": "Anis Mselmi",
    "role": "Computer Engineering Student | AI & Web Development Enthusiast",
    "location": "Khzema Ouest, Sousse, Tunisia",
    "email": "anismselmi490@gmail.com",
    "phone": "+216 25 141 636",
    "github": "https://github.com/anis-mselmi",
    "linkedin": "https://www.linkedin.com/in/anis-mselmi-441b39326/",
}

ABOUT = (
    "🧠 Computer Engineering student at École Polytechnique de Sousse, focused on AI, "
    "machine learning, and modern web development. I love turning complex ideas into "
    "clean, user‑friendly experiences—whether that’s building intelligent Python models "
    "or crafting fast, responsive interfaces. ⚡ I’m hands‑on with Jupyter/Colab workflows, "
    "data visualization, and rapid experimentation, and I bring a builder’s mindset to "
    "every project. 🌍 Curious, driven, and always learning, I’m open to internships and "
    "part‑time roles where I can contribute to impactful AI and web products."
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
        "years": "2021 – 2023",
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
    ("Web Development (PHP)", 70),
    ("Data Analysis & Visualization", 70),
    ("C++", 65),
    ("Git & GitHub", 75),
    ("Problem Solving & Innovation", 80),
]

PROJECTS = [
    {
        "name": "Mini Blog (PHP)",
        "desc": "A lightweight PHP blog with clean CRUD, authentication, and a sleek editorial UI.",
        "tags": ["PHP", "MySQL", "Web"],
        "image": "PHP_Logo.png",
        "logo": "logo-php-blog.svg",
        "link": "https://github.com/anis-mselmi/Mini-Blog-PHP",
    },
    {
        "name": "AI Image Classifier",
        "desc": "A fast, intuitive image classifier with model insights and confidence scoring.",
        "tags": ["AI", "Computer Vision", "Python"],
        "image": "téléchargement.jpg",
        "logo": "logo-ai-classifier.svg",
        "link": "https://github.com/anis-mselmi/AI-Image-Classifier",
    },
    {
        "name": "Restaurant Review Sentiment Analysis",
        "desc": "NLP pipeline that analyzes reviews to surface sentiment and key themes.",
        "tags": ["NLP", "Sentiment", "Analytics"],
        "image": "caption.jpg",
        "logo": "logo-restaurant-sentiment.svg",
        "link": "https://github.com/anis-mselmi/Restaurant-Review-Sentiment-Analysis",
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
    if Image is None:
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


def image_to_data_uri(image_path: Path) -> str | None:
    if not image_path.exists():
        return None
    suffix = image_path.suffix.lower().lstrip(".")
    mime_map = {
        "jpg": "image/jpeg",
        "jpeg": "image/jpeg",
        "png": "image/png",
        "webp": "image/webp",
    }
    mime_type = mime_map.get(suffix, "image/png")
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


# -----------------------------
# Sections
# -----------------------------

def hero_section() -> None:
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
        icon_path = Path(__file__).parent / "Logo-Polytec-Eurace-bleu-01 (1).png"

        st.write("")
        if icon_path.exists():
            hero_image = image_to_data_uri(icon_path)
            if hero_image:
                st.markdown(
                    f"<img src='{hero_image}' class='hero-image' width='260' />",
                    unsafe_allow_html=True,
                )
            else:
                st.image(str(icon_path), width=260)
        else:
            st.info("Add hero icon: hero-tech-icon.svg")
    st.markdown("</div>", unsafe_allow_html=True)


def render_skills() -> None:
    section_title("Skills", "🛠")
    st.caption("Skill levels are indicative and continuously evolving.")
    emoji_map = {
        "Machine Learning & Deep Learning (AI)": "🤖",
        "Python, Jupyter Notebook, Google Colab": "🐍",
        "Web Development (PHP)": "🌐",
        "Data Analysis & Visualization": "📊",
        "C++": "⚙️",
        "Git & GitHub": "🧰",
        "Problem Solving & Innovation": "💡",
    }

    cols = st.columns(2, gap="large")
    for index, (skill, level) in enumerate(SKILLS):
        with cols[index % 2]:
            with st.container(border=True):
                emoji = emoji_map.get(skill, "✨")
                st.markdown(f"### {emoji} {skill}")
                st.progress(level)
                st.caption(f"{level}%")


def render_education() -> None:
    section_title("Education", "🎓")
    for item in EDUCATION:
        st.markdown(f"### {item['title']}")
        st.markdown(f"**{item['school']}**")
        st.markdown(item["years"])
        st.markdown("---")


def render_experience() -> None:
    section_title("Experience & Community", "💼")
    st.caption("Leadership, community, and event experience across tech initiatives.")
    cards = [
        {
            "title": "Web Master at IEEE SIGHT EPS SB",
            "emoji": "🧩",
            "detail": "Managed web presence, content updates, and digital visibility.",
        },
        {
            "title": "Ambassador at ATIC, NPC 2.0 PolyRobots",
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


def render_projects() -> None:
    section_title("Projects", "🚀")
    st.caption("Project placeholders — ready to be replaced with real work samples.")

    cols = st.columns(3, gap="large")
    for idx, project in enumerate(PROJECTS):
        with cols[idx % 3]:
            image_path = Path(__file__).parent / project.get("image", "")
            image_data = image_to_data_uri(image_path)
            image_html = (
                f"<img src='{image_data}' alt='{project['name']}' class='project-image' />"
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


def render_languages() -> None:
    section_title("Languages", "🌍")
    st.caption("Communication strengths across native and professional proficiency.")
    cols = st.columns(2, gap="large")
    for index, (lang, level, score) in enumerate(LANGUAGES):
        with cols[index % 2]:
            with st.container(border=True):
                st.markdown(f"### {lang}")
                st.caption(level)
                st.progress(score)


def render_contact() -> None:
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


def render_sidebar() -> str:
    st.sidebar.title("🧭 Navigation")
    st.sidebar.write(PROFILE["name"])
    st.sidebar.caption(PROFILE["role"])
    return st.sidebar.radio(
        "Go to",
        [
            "Hero",
            "Skills",
            "Education",
            "Experience",
            "Projects",
            "Languages",
            "Contact",
        ],
        label_visibility="collapsed",
    )


# -----------------------------
# App
# -----------------------------

def main() -> None:
    selection = render_sidebar()

    if selection == "Hero":
        hero_section()
    elif selection == "Skills":
        render_skills()
    elif selection == "Education":
        render_education()
    elif selection == "Experience":
        render_experience()
    elif selection == "Projects":
        render_projects()
    elif selection == "Languages":
        render_languages()
    elif selection == "Contact":
        render_contact()


if __name__ == "__main__":
    main()
