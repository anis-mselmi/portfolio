# Personal Portfolio

A modern, responsive personal portfolio built with Streamlit.

## ✨ Features
- Polished hero section with profile photo and social buttons
- Projects grid with images and tags
- Skills, Education, Experience, Languages, CV, and Contact sections
- Custom dark theme with animated cards and smooth scroll

## 🧰 Tech Stack
- Python 3.10+
- Streamlit
- Pillow

## 📁 Project Structure
| File | Purpose |
|---|---|
| `app.py` | Entry point — page config and section orchestration |
| `styles.py` | All CSS injected via `inject_styles()` |
| `data.py` | Static content: profile, skills, education, projects, languages |
| `utils.py` | Helper functions: image loading, section titles, badges |
| `sections.py` | All page section render functions |

## ✅ Getting Started
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   *(Or simply `pip install streamlit pillow`)*

2. Run the app:
   ```bash
   streamlit run app.py
   ```

## 🧩 Customization
- **Profile, skills, education, projects, languages** → edit `data.py`
- **UI styles and animations** → edit `styles.py`
- **Section layout and rendering logic** → edit `sections.py`
- **Helper utilities** → edit `utils.py`
