import { type CSSProperties } from 'react';
import { sectionIndex } from '../lib/utils';
import { motion } from 'framer-motion';
import { siNvidia, type SimpleIcon } from 'simple-icons';
import { CERT_PROVIDERS } from '../data/content';
import { SectionHeader } from '../components/SectionHeader';
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
  const active = CERT_PROVIDERS[0];
  const t = THEME[active.key];

  return (
    <section id="certificates" className="section">
      <div className="shell">
        <SectionHeader
          index={sectionIndex('certificates')}
          title={ui.sections.certificates.title}
          standfirst={ui.sections.certificates.standfirst}
        />

        {/* Issuer strip */}
        <div className="mb-5 flex items-center gap-3">
          <span
            className="grid h-9 w-9 shrink-0 place-items-center border-[1.5px]"
            style={{ background: t.bg, borderColor: t.brand }}
          >
            <Logo icon={t.icon} color={t.brand} size={18} />
          </span>
          <div className="min-w-0">
            <h3 className="headline text-lg leading-none">{active.label}</h3>
            <div className="meta mt-1">
              {t.tagline} · {active.data.length} credentials
            </div>
          </div>
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
              initial={{ opacity: 0, y: 18 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true, margin: '0px 0px -8% 0px' }}
              transition={{ duration: 0.45, delay: Math.min(i * 0.05, 0.3), ease: [0.22, 1, 0.36, 1] }}
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
