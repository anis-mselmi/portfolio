import base64
import re
from pathlib import Path
from urllib.parse import quote
from datetime import datetime

import streamlit as st

from data import (
    PROFILE, ABOUT, EDUCATION, SKILLS_BY_CATEGORY,
    PROJECTS, LANGUAGES,
)
from utils import image_to_data_uri, section_title, section_start, section_end
from ai_agent import get_ai_response


def render_cover_banner() -> None:
    cover_path = Path(__file__).parent / "assets" / "images" / "profile" / "cover_banner.webp"
    cover_data = None
    if cover_path.exists():
        cover_data = "data:image/webp;base64," + base64.b64encode(cover_path.read_bytes()).decode("utf-8")

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
                <a href="#ai-agent" class="nav-link" data-target="ai-agent"><span class="nav-link-inner">🤖 Ask AI</span></a>
                <a href="#skills" class="nav-link" data-target="skills"><span class="nav-link-inner">🛠 Skills</span></a>
                <a href="#education" class="nav-link" data-target="education"><span class="nav-link-inner">🎓 Education</span></a>
                <a href="#projects" class="nav-link" data-target="projects"><span class="nav-link-inner">🚀 Projects</span></a>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def hero_section() -> None:
    section_start("hero", hero=True)
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
        icon_path = Path(__file__).parent / "assets" / "images" / "profile" / "hero.webp"

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


def render_projects() -> None:
    section_start("projects")
    section_title("Projects", "🚀")

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

    cv_link = "https://canva.link/cmn3h8sq33jeuib"
    preview_url = "https://www.canva.com/design/DAGzcHTtmzQ/uGneX3fzgU2Q1zRfhlCTRA/view?embed"

    col1, col2 = st.columns([1.1, 1], gap="large")
    with col1:
        st.markdown(
            f"""
            <div class="experience-card cv-access-card">
                <div class="experience-card-inner" style="justify-content: center; padding: 2.2rem;">
                    <h3 style="margin-top: 0; margin-bottom: 0.5rem; color: var(--accent-2);">📄 Instant Access to Resume</h3>
                    <p style="margin-bottom: 1.5rem; color: var(--muted); line-height: 1.6; font-size: 0.98rem;">
                        View my updated CV on Canva. Inside, you'll find a detailed listing of my academic computer engineering background, complete technical experiences and project snapshots.
                    </p>
                    <div style="display: flex; flex-direction: column; gap: 0.82rem; width: 100%; margin-top: auto;">
                        <a class="st-link-button" href="{cv_link}" target="_blank" style="text-decoration: none !important;">🎨 View CV on Canva</a>
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
                    <iframe src="{preview_url}" width="100%" height="380" style="border: none; display: block;" allowfullscreen="allowfullscreen" allow="fullscreen"></iframe>
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


def parse_markdown_to_html(text: str) -> str:
    """
    Translates simple markdown bold stars and hyper-links to responsive HTML safe markup.
    """
    html = text
    # Bold parsing (**text**)
    html = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", html)
    # Hyper-links parsing ([text](url))
    html = re.sub(r"\[(.*?)\]\((.*?)\)", r'<a href="\2" target="_blank" style="color: var(--accent-2); text-decoration: underline;">\1</a>', html)
    # Line breaks to standard HTML
    html = html.replace("\n", "<br>")
    return html


def render_ai_console() -> None:
    section_start("ai-agent")
    section_title("Ask My AI Twin", "🤖")
    st.caption("Interact with a simulated local RAG console trained on my academic background and engineering projects.")

    # Initialize session state variables
    if "terminal_history" not in st.session_state:
        st.session_state.terminal_history = [
            {"role": "system", "content": "Welcome to Anis's Agentic Console [Version 1.0.5]\nInitializing RAG semantic intent scanner...\nSystem ready. Try entering a query, choosing a prompt below, or type /help!"}
        ]
    if "ai_persona" not in st.session_state:
        st.session_state.ai_persona = "twin"

    # Add beautiful Persona Selector Buttons just above the console
    st.markdown("<p style='margin-bottom:0.45rem; font-size:0.92rem; font-weight:700; color:var(--accent-2); text-transform: uppercase; letter-spacing:0.06em;'>Select AI Twin Persona Tone:</p>", unsafe_allow_html=True)
    col_p1, col_p2, col_p3 = st.columns(3)
    with col_p1:
        if st.button("🤖 Cybernetic Twin", key="btn_twin", type="primary" if st.session_state.ai_persona == "twin" else "secondary", use_container_width=True):
            st.session_state.ai_persona = "twin"
            st.session_state.terminal_history.append({"role": "system", "content": "⚙️ System Persona swapped to standard AI Twin. Context set to technical, friendly developer twin."})
            st.rerun()
    with col_p2:
        if st.button("💼 Tech Recruiter", key="btn_recruiter", type="primary" if st.session_state.ai_persona == "recruiter" else "secondary", use_container_width=True):
            st.session_state.ai_persona = "recruiter"
            st.session_state.terminal_history.append({"role": "system", "content": "⚙️ System Persona swapped to Technical Recruiter. Compiling GPA standing, soft skills, and credentials index."})
            st.rerun()
    with col_p3:
        if st.button("💻 Deep Tech Lead", key="btn_tech", type="primary" if st.session_state.ai_persona == "tech" else "secondary", use_container_width=True):
            st.session_state.ai_persona = "tech"
            st.session_state.terminal_history.append({"role": "system", "content": "⚙️ System Persona swapped to Deep Tech Lead. Context set to database schema details and framework parameters."})
            st.rerun()

    # Determine API connection state
    import os
    has_api = os.environ.get("GEMINI_API_KEY")
    if not has_api:
        try:
            has_api = st.secrets.get("GEMINI_API_KEY") or st.secrets.get("gemini_api_key")
        except Exception:
            pass
            
    api_status_text = "● API ONLINE" if has_api else "● COSIM LOCAL ACTIVE"
    api_status_class = "status-online" if has_api else "status-local"

    # Render advanced terminal window with integrated cyber diagnostics
    terminal_html = f"""
    <div class="terminal-window">
        <div class="terminal-header">
            <div class="terminal-dots">
                <span class="terminal-dot dot-red"></span>
                <span class="terminal-dot dot-yellow"></span>
                <span class="terminal-dot dot-green"></span>
            </div>
            <div class="terminal-title">RAG Engine: Cosine Sim Scorer</div>
            <div class="terminal-badges">
                <span class="terminal-badge {api_status_class}">{api_status_text}</span>
                <span class="terminal-badge badge-mode">MODE: {st.session_state.ai_persona.upper()}</span>
            </div>
        </div>
        <div class="terminal-body" id="terminal-body">
    """
    
    # Fill message logs
    for idx, msg in enumerate(st.session_state.terminal_history):
        content_html = parse_markdown_to_html(msg["content"])
        if msg["role"] == "system":
            terminal_html += f'<div class="terminal-row"><span class="terminal-prompt">[sys]:</span> <span style="color:#b9cae0;">{content_html}</span></div>'
        elif msg["role"] == "user":
            terminal_html += f'<div class="terminal-row"><span class="terminal-user">[visitor@lobby]:$</span> <span style="color:#57e0ff; font-weight:bold;">{content_html}</span></div>'
        else:
            prompt_symbol = "twin-ai" if st.session_state.ai_persona == "twin" else ("recruit-ai" if st.session_state.ai_persona == "recruiter" else "tech-ai")
            prompt_color = "#a6e22e" if st.session_state.ai_persona == "twin" else ("#7c9cff" if st.session_state.ai_persona == "recruiter" else "#ffbd2e")
            terminal_html += f'<div class="terminal-row"><span class="terminal-prompt" style="color:{prompt_color};">[{prompt_symbol}]:$</span> <span class="terminal-output">{content_html}</span></div>'
            
    terminal_html += """
        </div>
    </div>
    <script>
        // Auto-scroll the terminal body to the bottom when logs append
        setTimeout(() => {
            const body = document.getElementById("terminal-body");
            if (body) {
                body.scrollTop = body.scrollHeight;
            }
        }, 80);
    </script>
    """
    
    st.markdown(terminal_html, unsafe_allow_html=True)

    # Suggestions row
    suggestions = {
        "🛠 Skills": "Tell me about your tech stack and AI/ML skills.",
        "🚗 SmartPark": "What is the SmartPark CV project?",
        "🧩 RAG / VSM": "How does your local Cosine Similarity VSM model work?",
        "📜 View CV": "How can I view your CV?",
        "📬 Contact": "How can I contact Anis?",
    }

    # Suggestions Pills
    st.markdown("<p style='margin-bottom:0.4rem; font-size:0.9rem; font-weight:600; color:var(--muted);'>Suggested Inquiries:</p>", unsafe_allow_html=True)
    cols = st.columns(len(suggestions))
    for idx, (label, val) in enumerate(suggestions.items()):
        with cols[idx]:
            if st.button(label, key=f"sug_{idx}", use_container_width=True):
                st.session_state.terminal_history.append({"role": "user", "content": val})
                response = get_ai_response(val, st.session_state.ai_persona)
                st.session_state.terminal_history.append({"role": "agent", "content": response})
                st.rerun()

    # Terminal prompt form at the bottom
    with st.form("terminal_input_form", clear_on_submit=True):
        col_input, col_btn = st.columns([5, 1])
        with col_input:
            user_query = st.text_input("Enter command or question...", placeholder="e.g., /status, /skills, /mode recruiter, or custom question...", label_visibility="collapsed")
        with col_btn:
            submit_btn = st.form_submit_button("💻 Send", use_container_width=True)

        if submit_btn and user_query:
            query_str = user_query.strip()
            if query_str.lower() == "/clear":
                st.session_state.terminal_history = [
                    {"role": "system", "content": "Welcome to Anis's Agentic Console [Version 1.0.5]\nConsole buffer cleared.\nSystem ready."}
                ]
            else:
                # Intercept dynamic /mode console commands
                if query_str.lower().startswith("/mode"):
                    parts = query_str.lower().split()
                    if len(parts) > 1 and parts[1] in ["twin", "recruiter", "tech"]:
                        st.session_state.ai_persona = parts[1]
                
                st.session_state.terminal_history.append({"role": "user", "content": query_str})
                response = get_ai_response(query_str, st.session_state.ai_persona)
                st.session_state.terminal_history.append({"role": "agent", "content": response})
            st.rerun()
            
    # Add a Clear Console button
    if st.button("🧹 Clear Terminal Console", key="clear_terminal"):
        st.session_state.terminal_history = [
            {"role": "system", "content": "Welcome to Anis's Agentic Console [Version 1.0.5]\nInitializing RAG semantic intent scanner...\nSystem ready. Try entering a query, choosing a prompt below, or type /help!"}
        ]
        st.rerun()
        
    section_end()


