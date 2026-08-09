<div align="center">

# 📰 The Engineering Broadsheet
### Anis Mselmi • Portfolio Vol. I

*Java Developer • AI Engineering Student • RAG & LLM Enthusiast*

Sousse, Tunisia

---

[![React](https://img.shields.io/badge/React-18-61DAFB?style=for-the-badge&logo=react&logoColor=black)](https://react.dev)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.x-3178C6?style=for-the-badge&logo=typescript&logoColor=white)](https://www.typescriptlang.org/)
[![Vite](https://img.shields.io/badge/Vite-6.x-646CFF?style=for-the-badge&logo=vite&logoColor=white)](https://vite.dev)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-3.x-38BDF8?style=for-the-badge&logo=tailwindcss&logoColor=white)](https://tailwindcss.com)
[![Framer Motion](https://img.shields.io/badge/Framer_Motion-11.x-F024B6?style=for-the-badge&logo=framer&logoColor=white)](https://www.framer.com/motion/)
[![Bilingual](https://img.shields.io/badge/Bilingual-EN_%2F_FR-dd3a1b?style=for-the-badge)](#-two-editions-enfr)

</div>

---

## ▍ Front Page

A unique single-page portfolio designed as an **editorial print newspaper**—featuring warm newsprint paper (`#f2eee4`), ink-black typography (`#17130d`), and a striking vermilion accent (`#dd3a1b`). 

It trades the standard dark-mode developer template for a curated aesthetic: high-contrast serif headlines (**Fraunces**), elegant self-drawing rules, a live ticker, a halftone press portrait, and a structured ledger for credentials.

The paper prints in **two editions** — English and French — switchable from a single masthead toggle, with a live link to the résumé.

---

## ▍ Two Editions (EN/FR)

The entire broadsheet is bilingual. An editorial **`EN / FR`** pill in the masthead switches every headline, column, label, and byline between English and French.

* **Single source of copy** — all translated content and UI strings live in `src/i18n/content.ts` via a `t(en, fr)` helper; components read them through the `useContent()` hook.
* **English by default** — every visit always opens on the English edition; the toggle switches the language for the current session only and is not persisted across reloads.
* **Language-neutral data** stays untouched — technical tags, proper nouns, certificate titles, and skill-level logic are never mistranslated.
* **Live résumé** — the hero's accent button links to a read-only, always-current Google Drive CV that updates in place without a redeploy.

---

## ▍ The Columns

| № | Section | Aesthetic & Technical Treatment |
| :--- | :--- | :--- |
| — | **Masthead / Lede** | Nameplate, dateline, drop-cap lede, halftone portrait, count-up statistics, EN/FR toggle, live CV link |
| 01 | **Fields of Expertise** | Skill index with a custom hand-built CSS printed proficiency bar |
| 02 | **Academic Record** | Chronological timeline of academic studies |
| 03 | **On Assignment** | Professional experience, volunteer history, and IEEE service records |
| 04 | **Credentials Ledger** | Provider-tabbed table (NVIDIA · DataCamp · Kaggle) with per-issuer verification links |
| 05 | **Featured Works** | Project showcase structured like feature articles with direct links |
| 06 | **Press Clippings** | Hackathon wins highlighted with award bylines and press-style photos |
| 07 | **Languages** | Multilingual proficiency levels |
| 08 | **Letters to the Editor** | Fully interactive contact desk with direct messaging |

---

## ▍ Design Aesthetics

* **The Palette**: A bespoke color palette featuring a warm newsprint background (`#f2eee4`), deep ink type (`#17130d`), and a bold vermilion accent (`#dd3a1b`).
* **Typography**: Beautiful contrast between **Fraunces** (display serif), **Archivo** (body), and **Space Mono** (meta/labels).
* **Print Detailing**: Textured film-grain overlays, fine column dividers, custom halftone-dot rendering, and brutalist hard-offset shadows.
* **Fluid Motion**: Handcrafted Framer Motion entry animations and SVG path-drawn borders. Fully responsive and respects `prefers-reduced-motion`.

---

## ▍ Local Setup & Run

### 1. Run the Development Server
Install dependencies and launch the local environment:
```bash
npm install
npm run dev
```
The server will start at `http://localhost:5173`.

### 2. Build for Production
Bundle the optimized application:
```bash
npm run build
npm run preview
```

---

## ▍ The Contact Desk (EmailJS Setup)

The contact form is configured to work out-of-the-box using a standard `mailto:` fallback. To enable instant, in-app email sending:

1. Create a free account at [EmailJS](https://dashboard.emailjs.com).
2. Configure a new Email Service and Email Template.
3. Create a `.env` file in the root directory using `.env.example` as a template:

```env
VITE_EMAILJS_SERVICE_ID=your_service_id
VITE_EMAILJS_TEMPLATE_ID=your_template_id
VITE_EMAILJS_PUBLIC_KEY=your_public_key
```

> [!IMPORTANT]
> The template should expect the following parameters: `from_name`, `reply_to`, `subject`, `message`, and `to_email`.

---

## ▍ Directory Structure

```
src/
├── main.tsx             # Application entrypoint
├── App.tsx              # Component orchestration & layout
├── index.css            # Custom CSS & design system overrides
├── data/
│   ├── content.ts       # Language-neutral data (profile, links, certificates)
│   └── types.ts         # TypeScript definitions
├── i18n/
│   ├── LanguageContext.tsx  # EN/FR provider, persistence & default language
│   └── content.ts           # Translated content + UI strings (useContent hook)
├── hooks/
│   ├── useActiveSection.ts
│   ├── useCountUp.ts
│   ├── usePrefersReducedMotion.ts
│   └── useScrollProgress.ts
├── lib/
│   ├── email.ts         # EmailJS client wrapper
│   ├── icons.tsx        # Styled SVG lucide-react overrides
│   └── utils.ts         # Class merging helpers
├── components/          # Reusable core layouts (Navbar, LangToggle, Ticker, VisitorBadge, etc.)
└── sections/            # Component files for each section of the broadsheet
```

---

<div align="center">

**Colophon**
*Set in Fraunces, Archivo & Space Mono. Powered by React, TypeScript & Vite.*

© Anis Mselmi • MIT License

</div>
