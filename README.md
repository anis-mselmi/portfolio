<div align="center">

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  T H E   E N G I N E E R I N G   B R O A D S H E E T
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

# Anis Mselmi<span>.</span>

**Vol. I — Java Developer · AI-Engineering Student · RAG & LLM Enthusiast**

*Sousse, Tunisia — A personal portfolio set as a printed periodical.*

[![React 18](https://img.shields.io/badge/React_18-111111?style=flat-square&logo=react&logoColor=57e0ff)](https://react.dev)
[![TypeScript](https://img.shields.io/badge/TypeScript-111111?style=flat-square&logo=typescript&logoColor=3178C6)](https://www.typescriptlang.org/)
[![Vite](https://img.shields.io/badge/Vite-111111?style=flat-square&logo=vite&logoColor=dd3a1b)](https://vite.dev)
[![Tailwind](https://img.shields.io/badge/Tailwind-111111?style=flat-square&logo=tailwindcss&logoColor=38bdf8)](https://tailwindcss.com)
[![Motion](https://img.shields.io/badge/Framer_Motion-111111?style=flat-square&logo=framer&logoColor=ffffff)](https://www.framer.com/motion/)

</div>

---

## ▍ Front Page

A single-page portfolio built as an **editorial print newspaper** — warm newsprint
paper, ink-black type, and a single sharp vermilion accent. It trades the usual
dark-mode developer template for something with a point of view: high-contrast
**Fraunces** headlines, hairline rules that draw themselves in, a running stack
ticker, a halftone press portrait, and a credentials *ledger* instead of yet
another card grid.

> **Read it live →** [anismselmi.me](https://anismselmi.me)

---

## ▍ The Columns

| № | Section | Treatment |
|---|---------|-----------|
| — | **Masthead / Lede** | Nameplate, dateline, drop-cap lede, halftone portrait, count-up stats |
| 01 | **Fields of Expertise** | Skill index + a hand-built printed proficiency bar figure |
| 02 | **Academic Record** | Dated study chronicle |
| 03 | **On Assignment** | Professional posts + Bénévolat / IEEE service |
| 04 | **Credentials Ledger** | Filterable table across NVIDIA · DataCamp · Kaggle |
| 05 | **Featured Works** | Projects as feature articles → GitHub |
| 06 | **Press Clippings** | Hackathon wins with award bylines |
| 07 | **Languages** | Communication index |
| 08 | **Letters to the Editor** | Contact desk + directory |

---

## ▍ Design Direction

- **Palette** — newsprint paper `#f2eee4`, ink `#17130d`, one sharp vermilion `#dd3a1b` (dominant + accent, never a timid gradient).
- **Type** — **Fraunces** (display serif) · **Archivo** (body) · **Space Mono** (labels & meta).
- **Print detailing** — film-grain overlay, faint column rules, hairline dividers, halftone-dot portrait, grayscale→colour photo reveals, and brutalist hard-offset-shadow hovers.
- **Motion** — Framer Motion reveals and drawing rules; fully responsive; honours `prefers-reduced-motion`.

---

## ▍ The Printing Press

```
React 18 · TypeScript · Vite · Tailwind CSS · Framer Motion · lucide-react · EmailJS
```

No chart library — the proficiency figure is hand-built CSS.

---

## ▍ Run the Presses

```bash
npm install
npm run dev        # http://localhost:5173
```

Production build & preview:

```bash
VITE_OUT_DIR=dist npm run build   # bundles to ./dist
npm run preview
```

---

## ▍ The Contact Desk (EmailJS)

The form works out of the box via a `mailto:` fallback. For real in-page sending,
create a free [EmailJS](https://dashboard.emailjs.com) service + template, then copy
`.env.example` → `.env`:

```env
VITE_EMAILJS_SERVICE_ID=your_service_id
VITE_EMAILJS_TEMPLATE_ID=your_template_id
VITE_EMAILJS_PUBLIC_KEY=your_public_key
```

Template fields: `from_name`, `reply_to`, `subject`, `message`, `to_email`.

---

## ▍ Editing the Copy

All content is typed and lives in one place — **`src/data/content.ts`**
(profile, about, education, experience, skills, projects, certifications,
hackathons, languages). Theme tokens & fonts are in `tailwind.config.js` and
`src/index.css` (`:root`).

```
src/
├── main.tsx · App.tsx · index.css
├── data/          # content.ts · types.ts  (single source of truth)
├── hooks/         # active-section, scroll-progress, count-up, reduced-motion
├── lib/           # utils · email · icons
├── components/    # Background · Navbar · Ticker · SectionHeader · Stat · …
└── sections/      # Hero · Skills · Education · Experience · Certifications
                   # Projects · Hackathons · Languages · Contact · Footer
```

---

<div align="center">

**Colophon** — Set in Fraunces, Archivo & Space Mono. Built with React, TypeScript & Vite.

*© Anis Mselmi · MIT License — fork it, reset the type, make it your own.*

</div>
