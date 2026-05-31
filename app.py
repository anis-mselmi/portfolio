import streamlit as st

from styles import inject_styles
from sections import (
    mount_scroll_behavior,
    render_cover_banner,
    render_navbar,
    hero_section,
    render_ai_console,
    render_skills_section,
    render_education,
    render_certificates,
    render_projects,
    render_languages,
    render_visitor_badge,
)

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
# Inject Styles
# -----------------------------
inject_styles()


# -----------------------------
# App
# -----------------------------
def main() -> None:
    mount_scroll_behavior()
    render_visitor_badge()
    render_navbar()

    hero_section()
    render_ai_console()
    render_skills_section()
    render_education()
    render_certificates()
    render_projects()
    render_languages()


if __name__ == "__main__":
    main()

