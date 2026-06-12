# 🌌 Anis Mselmi | Futuristic Agentic Portfolio

[![Streamlit App](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io)
[![Python 3.10+](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Google Gemini](https://img.shields.io/badge/Google%20Gemini-8E75C2?style=for-the-badge&logo=googlegemini&logoColor=white)](https://deepmind.google/technologies/gemini/)
[![Vector Search & RAG](https://img.shields.io/badge/RAG-Agentic-008080?style=for-the-badge&logo=vector&logoColor=white)](#-ask-my-ai-twin-console)

A premium, highly interactive personal portfolio application showcasing a futuristic cyber-console design. Built with **Streamlit** and optimized with professional vanilla CSS styles, fluid scroll behaviors, intersection observers, and a custom **AI Twin RAG Terminal Console**!

---

## ✨ Primary Features

### 🤖 Ask My AI Twin Console
An interactive developer-themed terminal mimicking a live **Retrieval-Augmented Generation (RAG)** engine.
* **Intelligent Query Parser:** Employs high-precision fuzzy keyword matching and sequence metrics to locate portfolio details instantly.
* **Developer Shell Commands:** Fully supports Unix-style console slash-commands:
  * `/about` — Introduce Anis's professional objective
  * `/skills` — Print technical stack inventory
  * `/projects` — List engineered software systems
  * `/certificates` (or `/certs`) — Output verified NVIDIA certificates registry
  * `/cv` — Print direct resume Canva URL
  * `/contact` — Display communications channels
  * `/clear` — Flush console buffer
  * `/help` — Print command registry
* **Gemini LLM Failover:** Connects dynamically with **Google Gemini 1.5 Flash** if a `GEMINI_API_KEY` is provided, answering arbitrary technical questions with real-time semantic grounding.
* **Suggested Prompts:** Includes fast-access click triggers to run prompt queries instantly.

### 🛠️ Interactive Skills Showcase & Competence Charts
A modern grid displaying specialized computer engineering and software skills.
* **Skill Categories:** Structured grid with interactive hover animations, custom tags, and categories.
* **Interactive Competence Charts:** Integrates 3 custom dark-themed interactive Plotly charts side-by-side showing:
  1. *Top Skills:* A horizontal bar chart of top skills with a cyan-to-purple gradient.
  2. *Domain Mix:* A donut chart representing skill category distribution.
  3. *Languages:* A vertical bar chart indicating programming language proficiencies.

### 🎓 Structured Education Timeline
A responsive, side-by-side 3-column education timeline detailing academic path milestones.
* **Glassmorphic Cards:** Transformed into beautiful 3-column glassmorphism cards with 12px backdrop-blur and a glowing border gradient that turns into a bright neon purple-to-cyan border on hover.
* **Header Badges:** Includes circular floating emoji badges with hover rotation and modern pill date badges.
* **Direct PDF Resume Download:** Integrates a local PDF CV (`assets/CV de Anis Mselmi (1) (1).pdf`) which is automatically encoded in base64 on startup and served directly to the user's browser for download.

### 🧭 Sticky Centered Navbar
* A sticky 5-button top navigation bar allowing users to jump directly to sections: **🛠 Skills**, **🎓 Education**, **📜 Certs**, **🚀 Projects**, and **📬 Contact**.
* Styled with flexbox to group all 5 buttons next to each other in the center with a tight fit, wrapping responsively on mobile.

### 🎖️ Verified NVIDIA Certifications & Registry
A premium, highly interactive dashboard registry showcasing Anis's professional credentials from NVIDIA.
* **Compact CSS Grid Layout:** Displays 8 professional Certificates of Competency in an elegant, responsive 4-column glassmorphic grid with custom technology tags.
* **Perfect Equal-Sizing Alignment:** Designed using CSS Grid stretch properties and flex-direction models, ensuring all certificate cards and "Verify Credential" buttons align with identical dimensions across all rows.
* **Instant Verification Redirects:** Each card features a direct, secure verify button connecting to NVIDIA's credentials verification system (`learn.nvidia.com`).
* **Chatbot Grounding:** The AI Twin terminal console understands slash-commands (`/certificates`, `/certs`) and naturally details the verification status of all 8 certificates across different personas (Twin, Recruiter, Tech Lead).

### 🚀 Projects Grid
Premium multi-column display of core engineering projects.
* Features project cards with fully optimized images and tag badges.
* Connects directly to external repositories.

### 🌍 Languages
* **Languages Showcase:** Display of linguistic capabilities utilizing glassmorphic card layouts, flag graphics, and custom proficiency badges.


---

## 🗂️ Codebase Architecture

```filepath
├── app.py           # Entrypoint — page configuration & section orchestration
├── sections.py      # Core modular component renderers (Navbar, Hero, Projects, etc.)
├── styles.py        # Complete custom responsive stylesheet (cyberpunk dark-theme, animations)
├── ai_agent.py      # Fuzzy intent parser & Google Gemini API RAG twin engine
├── data.py          # Centralized configuration data (profile, academic, lists)
├── utils.py         # Image optimization pipelines, circular masks & element wrappers
└── assets/
    ├── CV de Anis Mselmi (1) (1).pdf  # Local PDF CV / Resume file
    └── images/
        └── profile/ # Optimized profile images, web banners & project assets
```

---

## 🚀 Getting Started

### 1. Prerequisites
Ensure you have **Python 3.10+** installed on your system.

### 2. Installation
Clone the repository, navigate to the folder, and install the dependencies:
```bash
pip install -r requirements.txt
```
*(Or install manually: `pip install streamlit pillow`)*

### 3. Running the Portfolio
Fire up the local Streamlit application server:
```bash
streamlit run app.py
```
By default, the server will launch at **`http://localhost:8501`**.

---

## 🔑 Activating Live LLM Agent Capabilities
To transition the **Ask My AI Twin Console** from a local search matcher to a live conversational assistant using **Google Gemini**:

1. Obtain a free API key from [Google AI Studio](https://aistudio.google.com/).
2. Add your key to the Streamlit secrets block:
   * Create a file at `.streamlit/secrets.toml` in your project folder.
   * Add the following entry:
     ```toml
     GEMINI_API_KEY = "your_actual_api_key_here"
     ```
3. Alternatively, export the API key in your terminal shell:
   * **Windows (PowerShell):** `$env:GEMINI_API_KEY="your_api_key"`
   * **Linux/macOS:** `export GEMINI_API_KEY="your_api_key"`

---

## 🛠️ Personal Customization

The codebase is built to be modular and incredibly easy to adapt:
* **Update Personal Details:** Simply edit the fields in `data.py` to change titles, project names, education timelines, or skill sets.
* **Modify Styles & Theme:** Open `styles.py` to adjust colors, glowing effects, grid containers, or keyframe animations.
* **Update Layout Flow:** Rearrange or modify render elements inside `sections.py` and `app.py`.
