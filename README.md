<h1 align="center">Anis Mselmi</h1>

<p align="center">
  <img src="Gemini_Generated_Image_vilfj9vilfj9vilf.png" alt="Project Image" width="500"/>
</p>

A modern, responsive personal portfolio built with Streamlit. The app highlights a hero section, skills, education, experience, projects, languages, and contact form, all styled with a custom dark UI.

## ✨ Features
- Polished hero section with logo and CTA buttons
- Projects grid with images, tags, and GitHub links
- Skills, education, experience, and languages sections
- Sidebar navigation for fast browsing
- Custom theming and card-based layout

## 🧰 Tech Stack
- Python 3.10+
- Streamlit
- Pillow (optional, for image processing)

## ✅ Getting Started
1. Install dependencies:
   ```bash
   pip install streamlit pillow
   ```
2. Run the app:
   ```bash
   streamlit run app.py
   ```

## 🖼️ Assets
Place image assets in the project root (same folder as `app.py`). The current assets include:
- Project images (e.g., `PHP_Logo.png`, `téléchargement.jpg`, `caption.jpg`)
- Hero logo (`Logo-Polytec-Eurace-bleu-01 (1).png`)

If an image is missing, the app will show a placeholder.

## 🧩 Customize Content
Open `app.py` and edit the **Data** section:
- `PROFILE` (name, role, contacts)
- `ABOUT` (summary text)
- `SKILLS`, `EDUCATION`, `EXPERIENCE`, `LANGUAGES`
- `PROJECTS` (name, description, tags, image, GitHub link)

## 🛠️ Styling
All UI styles live in the CSS block near the top of `app.py`. You can adjust:
- Colors (`:root` variables)
- Typography and spacing
- Card layouts
- Button styles

## 📦 Deployment
You can deploy this Streamlit app on:
- Streamlit Community Cloud
- Render, Railway, or any platform that supports Python web apps

---

If you need help customizing or deploying, feel free to reach out.
