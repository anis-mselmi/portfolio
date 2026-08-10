import { useState, type CSSProperties } from 'react';
import { motion } from 'framer-motion';
import { siNvidia, siDatacamp, siKaggle, type SimpleIcon } from 'simple-icons';
import { CERT_PROVIDERS } from '../data/content';
import { SectionHeader } from '../components/SectionHeader';
import { cx } from '../lib/utils';
import { useContent } from '../i18n/content';

interface Theme {
  icon: SimpleIcon;
  tagline: string;
  bg: string;
  fg: string;
  border: string;
  brand: string;
}

/** Each issuer rendered in its own brand identity. */
const THEME: Record<string, Theme> = {
  nvidia: {
    icon: siNvidia,
    tagline: 'Deep Learning Institute',
    bg: '#0b0b0b',
    fg: '#f4f6f0',
    border: 'rgba(118,185,0,0.30)',
    brand: '#76b900',
  },
  datacamp: {
    icon: siDatacamp,
    tagline: 'Career Track Certification',
    bg: '#05192d',
    fg: '#eef4f8',
    border: 'rgba(3,239,98,0.28)',
    brand: '#03ef62',
  },
  kaggle: {
    icon: siKaggle,
    tagline: 'Kaggle Learn',
    bg: '#ffffff',
    fg: '#1a1d21',
    border: '#e0e3e7',
    brand: '#20beff',
  },
};

function Logo({ icon, color, size = 16 }: { icon: SimpleIcon; color: string; size?: number }) {
  return (
    <svg
      role="img"
      aria-hidden
      viewBox="0 0 24 24"
      width={size}
      height={size}
      style={{ fill: color }}
    >
      <path d={icon.path} />
    </svg>
  );
}

export function Certifications() {
  const { ui } = useContent();
  const [key, setKey] = useState<string>(CERT_PROVIDERS[0].key);

  const active = CERT_PROVIDERS.find((p) => p.key === key) ?? CERT_PROVIDERS[0];
  const t = THEME[active.key];

  return (
    <section id="certificates" className="section">
      <div className="shell">
        <SectionHeader
          index="04"
          title={ui.sections.certificates.title}
          standfirst={ui.sections.certificates.standfirst}
        />

        {/* Issuer filter — active tab wears its brand colour */}
        <div className="mb-6 flex flex-wrap gap-2">
          {CERT_PROVIDERS.map((p) => {
            const isActive = p.key === key;
            const pt = THEME[p.key];
            return (
              <button
                key={p.key}
                type="button"
                aria-pressed={isActive}
                onClick={() => setKey(p.key)}
                className={cx(
                  'flex items-center gap-2 border-[1.5px] px-3 py-1.5 font-mono text-xs uppercase tracking-widest transition-colors',
                  !isActive && 'border-ink hover:bg-paper-2'
                )}
                style={
                  isActive
                    ? { background: pt.brand, borderColor: pt.brand, color: '#0b0b0b' }
                    : undefined
                }
              >
                <Logo icon={pt.icon} color={isActive ? '#0b0b0b' : pt.brand} size={13} />
                {p.label}
                <span className="opacity-60">({p.data.length})</span>
              </button>
            );
          })}
        </div>

        {/* Active issuer strip */}
        <div className="mb-4 flex items-center gap-3">
          <span
            className="grid h-9 w-9 shrink-0 place-items-center border-[1.5px]"
            style={{ background: t.bg, borderColor: t.brand }}
          >
            <Logo icon={t.icon} color={t.brand} size={18} />
          </span>
          <span className="meta">{t.tagline}</span>
          <hr className="rule ml-1 flex-1" />
        </div>

        {/* Little brand cards — side by side, wrapping under each other */}
        <div className="grid gap-3 sm:grid-cols-2 xl:grid-cols-3">
          {active.data.map((c, i) => (
            <motion.a
              key={`${active.key}-${c.id}`}
              href={c.url}
              target="_blank"
              rel="noreferrer"
              aria-label={`${c.title} — ${active.label}. ${ui.certs.verify}`}
              initial={{ opacity: 0, y: 10 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.35, delay: Math.min(i * 0.04, 0.25) }}
              className="cert-card"
              style={
                {
                  background: t.bg,
                  color: t.fg,
                  borderColor: t.border,
                  ['--brand']: t.brand,
                } as CSSProperties
              }
            >
              <div className="flex items-center justify-between gap-3">
                <span className="flex items-center gap-2">
                  <Logo icon={t.icon} color={t.brand} size={14} />
                  <span className="cert-issuer">{active.label}</span>
                </span>
                <span className="cert-date">{c.date}</span>
              </div>

              <div className="cert-title">{c.title}</div>

              <div className="cert-skills">
                {c.skills.slice(0, 3).map((s) => (
                  <span key={s} className="cert-chip">
                    {s}
                  </span>
                ))}
              </div>

              <span className="cert-verify">{ui.certs.verify}</span>
            </motion.a>
          ))}
        </div>
      </div>
    </section>
  );
}
