import streamlit as st

from styles import inject_styles
from sections import (
    mount_scroll_behavior,
    render_cover_banner,
    render_navbar,
    hero_section,
    render_skills_section,
    render_education,
    render_experience,
    render_projects,
    render_languages,
    render_pacman,
    render_cv,
    render_contact,
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
    render_navbar()

    hero_section()
    render_skills_section()
    render_education()
    render_experience()
    render_projects()
    render_languages()
    render_pacman()
    render_cv()
    render_contact()


if __name__ == "__main__":
    main()
