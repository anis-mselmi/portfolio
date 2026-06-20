# 🌌 Anis Mselmi | Futuristic Portfolio

[![Streamlit App](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io)
[![Python 3.10+](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Mobile Ready](https://img.shields.io/badge/Mobile-Responsive-57e0ff?style=for-the-badge&logoColor=white)](#-mobile-responsive-design)

> [!NOTE]
> ### 🌐 Deployment & Hosting Details
> * **Domain Name:** [https://anismselmi.me](https://anismselmi.me)
> * **Render Host:** [https://anismselmi.onrender.com](https://anismselmi.onrender.com)
> * **Streamlit Host:** [https://anis-mselmi-portfolio.streamlit.app/](https://anis-mselmi-portfolio.streamlit.app/)



<p align="center">
  <img src="assets/images/profile/hero.webp" alt="Anis Mselmi Profile" width="200" style="border-radius: 24px; border: 3px solid #7c9cff; box-shadow: 0 4px 25px rgba(124, 156, 255, 0.45); object-fit: cover;" />
</p>

A **premium, highly interactive personal portfolio** application showcasing a futuristic cyber-console design. Built with **Streamlit** and powered by professional vanilla CSS — featuring fluid scroll behaviors, intersection observers, and glassmorphic UI components.

---

## ✨ Features

### 🧭 7-Button Sticky Centered Navbar
* A sticky navigation bar with **7 section buttons** all displayed on a single centered line: **🛠 Skills · 🎓 Education · 📜 Certs · 🚀 Projects · 🏆 Hackathons · 🌍 Languages · 📬 Contact**
* Smooth scroll-to-section behavior with active-link highlighting via `IntersectionObserver`.
* Horizontally scrollable on mobile — all buttons remain on one line.

---

### 🛠️ Interactive Skills Showcase
* **Skill Category Grid:** Structured glassmorphic cards with interactive hover animations and custom tech tags.
* **Interactive Competence Charts:** 3 custom Plotly dark-themed charts side-by-side:
  1. *Top Skills* — Horizontal bar chart with a cyan-to-purple gradient.
  2. *Domain Mix* — Donut chart showing category distribution.
  3. *Languages* — Vertical bar chart of programming language proficiencies.

---

### 🎓 Structured Education Timeline
* **Glassmorphic Cards:** 3-column glassmorphism layout with `backdrop-filter: blur(12px)`, animated glowing borders on hover.
* **Header Badges:** Circular emoji badges with hover rotation and pill date badges.
* **Direct PDF CV Download:** Local PDF encoded in base64 and served directly to the browser.

---

### 🎖️ Verified NVIDIA Certifications Registry
* **Responsive 4-Column CSS Grid** displaying 8 professional NVIDIA Certificates of Competency.
* **Instant Verification Redirects** — each card links directly to `learn.nvidia.com` for credential verification.

---

### 🚀 Projects Grid
* Multi-column display of core engineering projects with project image cards, tech-stack tags, and GitHub links.
* **NovaChess** project features a custom chess board image (`assets/images/projects/chess.png`).

---

### 🏆 Hackathon Wins
* Dedicated **Hackathons** section showcasing competition achievements with event photos.
* **Fixed-height cards** (325px) with prominent 160px event banner images.
* Each card displays: event name, award badge (🥇 **Top 6**, etc.), organizer, date, and tech tags.
* Gold-to-cyan gradient glassmorphic borders with animated hover lift effect.
* **IEEE WIE ACT 4.0** properly featured alongside other IEEE congresses.

---

### 🌍 Languages Section
* **Glassmorphic language cards** with circular full-bleed flag images (Arabic, English, French, Saudi flag).
* Language proficiency displayed with badge chips per card.
* 2-column responsive grid layout (3-column on wide screens).

---

### 📬 Premium Contact Section
* **Two-column layout** — contact form on the left, Contact Details card on the right.
* **Redesigned Contact Details Card:**
  - Glassmorphic dark card with `backdrop-filter: blur(12px)`.
  - Each contact row has a **color-coded glowing icon box** (blue for email, green for phone, red for location, LinkedIn blue, GitHub white).
  - **Label + Value structure** — small muted label above the actual value.
  - Smooth slide-right hover animation with border glow per row.
  - Gradient accent underline below the "Contact Details" title.
* **Contact Form** with direct email sending via SMTP and a mailto fallback.

---

### 📱 Mobile Responsive Design
* **Streamlit columns stay horizontal** on mobile — `stHorizontalBlock` is forced to `flex-direction: row` so the layout never stacks.
* **Horizontally scrollable navbar** — all 7 buttons visible in a single swipeable strip.
* **Hackathon / Project cards** maintain side-by-side layout with touch-friendly horizontal scroll.
* **Language and Certificate grids** drop to 2-column on tablet, 1-column on very small screens.
* Smooth scaling of typography (`h1`, `h2`, `h3`) and component sizes at 768px and 480px breakpoints.

---

## 🗂️ Codebase Architecture

```
portfolio/
├── app.py              # Entrypoint — page config & section orchestration
├── sections.py         # Modular component renderers (Navbar, Hero, Hackathons, Languages, Contact, etc.)
├── styles.py           # Complete responsive stylesheet (dark glassmorphic theme, animations, mobile CSS)
├── data.py             # Centralized data (profile, education, certs, projects, hackathons, languages)
├── utils.py            # Image optimization pipelines, circular masks & element wrappers
├── requirements.txt    # Python dependencies
└── assets/
    ├── CV de Anis Mselmi.pdf          # PDF Resume (base64-served for download)
    └── images/
        ├── profile/                   # Hero photo, banner
        ├── projects/
        │   └── chess.png              # NovaChess project image
        └── hackathons/                # IEEE & competition event photos
```

---

## 🚀 Getting Started

### 1. Prerequisites
Ensure you have **Python 3.10+** installed.

### 2. Installation
Clone the repository and install dependencies:
```bash
git clone https://github.com/anis-mselmi/portfolio.git
cd portfolio
pip install -r requirements.txt
```

### 3. Running the Portfolio
```bash
streamlit run app.py
```
Opens at **`http://localhost:8501`** by default.

---

## 🛠️ Customization Guide

The codebase is **fully modular** and easy to adapt:

| File | What to change |
|---|---|
| `data.py` | Profile info, projects, education, certs, hackathons, languages |
| `styles.py` | Colors, glow effects, grids, animations, mobile breakpoints |
| `sections.py` | Layout of every section, HTML structure |
| `app.py` | Section order, page config |
| `assets/` | Images, CV PDF |

---

## 📄 License
MIT — free to fork, adapt, and deploy as your own portfolio.
