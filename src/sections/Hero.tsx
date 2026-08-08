import { motion } from 'framer-motion';
import { Github, Linkedin, Mail, MapPin } from 'lucide-react';
import {
  PROFILE,
  ABOUT,
  HACKATHONS,
  NVIDIA_CERTIFICATES,
  DATACAMP_CERTIFICATES,
  KAGGLE_CERTIFICATES,
} from '../data/content';
import { assetUrl } from '../lib/utils';
import { Stat } from '../components/Stat';
import { VisitorBadge } from '../components/VisitorBadge';

const HERO_IMG = assetUrl('/assets/images/profile/anis.jpg');
const TOTAL_CERTS =
  NVIDIA_CERTIFICATES.length + DATACAMP_CERTIFICATES.length + KAGGLE_CERTIFICATES.length;

const EDITION_DATE = new Date().toLocaleDateString('en-US', {
  weekday: 'long',
  year: 'numeric',
  month: 'long',
  day: 'numeric',
});

const fade = (delay: number) => ({
  initial: { opacity: 0, y: 16 },
  animate: { opacity: 1, y: 0 },
  transition: { duration: 0.6, delay, ease: [0.22, 1, 0.36, 1] as const },
});

export function Hero() {
  return (
    <header id="hero" className="section !pt-8">
      <div className="shell">
        {/* Folio / dateline */}
        <motion.div {...fade(0)} className="flex flex-wrap items-center justify-between gap-2 pb-2">
          <span className="meta">Vol. I · The Engineering Broadsheet</span>
          <span className="meta hidden sm:inline">{EDITION_DATE}</span>
          <VisitorBadge />
        </motion.div>
        <hr className="rule-double" />

        {/* Nameplate */}
        <motion.h1
          {...fade(0.05)}
          className="headline mt-5 text-center text-[clamp(3rem,13vw,10rem)] leading-[0.86]"
        >
          Anis Mselmi
        </motion.h1>

        <motion.div
          {...fade(0.12)}
          className="mt-4 flex flex-wrap items-center justify-center gap-x-3 gap-y-1 text-center"
        >
          <span className="kicker">Java Developer</span>
          <span className="text-accent">✦</span>
          <span className="kicker">AI · RAG · LLM Engineer</span>
          <span className="text-accent">✦</span>
          <span className="kicker">AI Engineering</span>
        </motion.div>

        <hr className="rule mt-5" />

        {/* Lede grid */}
        <div className="mt-8 grid gap-8 lg:grid-cols-[1.05fr_0.95fr]">
          {/* Left: editorial lede */}
          <motion.div {...fade(0.18)}>
            <span className="meta">Sousse, Tunisia — Special Report</span>
            <p className="lede dropcap mt-3">
              A Java developer and AI-engineering student building robust backend
              services and intelligent AI systems — from RAG pipelines and conversational
              agents to Dockerized, CI/CD-driven deployments.
            </p>

            <div className="mt-6 flex flex-wrap gap-3">
              <a href={PROFILE.github} target="_blank" rel="noreferrer" className="btn btn-solid">
                <Github size={16} /> GitHub
              </a>
              <a href={PROFILE.linkedin} target="_blank" rel="noreferrer" className="btn">
                <Linkedin size={16} /> LinkedIn
              </a>
              <a
                href="#contact"
                onClick={(e) => {
                  e.preventDefault();
                  document.getElementById('contact')?.scrollIntoView({ behavior: 'smooth' });
                }}
                className="btn btn-accent"
              >
                <Mail size={16} /> Correspond
              </a>
            </div>

            {/* By the numbers */}
            <div className="mt-8 grid grid-cols-3 gap-4 border-t-2 border-ink pt-5">
              <Stat end={TOTAL_CERTS} suffix="+" label="Certs" />
              <Stat end={HACKATHONS.length} suffix="+" label="Wins" />
              <Stat end={8} suffix="+" label="Projects" />
            </div>
          </motion.div>

          {/* Right: halftone portrait plate */}
          <motion.figure
            initial={{ opacity: 0, scale: 0.98 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ duration: 0.7, delay: 0.25 }}
            className="print-card self-start p-2.5"
          >
            <div className="halftone overflow-hidden">
              <img src={HERO_IMG} alt="Anis Mselmi" className="w-full object-cover" loading="eager" />
            </div>
            <figcaption className="meta mt-2 flex items-center justify-between">
              <span className="flex items-center gap-1">
                <MapPin size={11} /> {PROFILE.location.split(',')[0]}
              </span>
              <span>Fig. 1 — The Developer</span>
            </figcaption>
          </motion.figure>
        </div>

        {/* About briefs */}
        <div className="mt-12 grid gap-px border border-ink bg-ink sm:grid-cols-2 lg:grid-cols-4">
          {ABOUT.slice(0, 8).map((item, i) => (
            <motion.div
              key={item.title}
              initial={{ opacity: 0 }}
              whileInView={{ opacity: 1 }}
              viewport={{ once: true }}
              transition={{ duration: 0.4, delay: (i % 4) * 0.06 }}
              className="bg-card p-4"
            >
              <div className="meta text-accent-deep">{String(i + 1).padStart(2, '0')}</div>
              <div className="headline mt-1 text-base">{item.title}</div>
              <p className="mt-1 text-[0.82rem] leading-snug text-ink-soft">{item.text}</p>
            </motion.div>
          ))}
        </div>
      </div>
    </header>
  );
}
