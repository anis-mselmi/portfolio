import { useState } from 'react';
import { motion } from 'framer-motion';
import { CERT_PROVIDERS } from '../data/content';
import { SectionHeader } from '../components/SectionHeader';
import { cx } from '../lib/utils';
import { useContent } from '../i18n/content';

interface Row {
  title: string;
  issuer: string;
  date: string;
  skills: string[];
  url: string;
}

const ALL: Row[] = CERT_PROVIDERS.flatMap((p) =>
  p.data.map((c) => ({
    title: c.title,
    issuer: p.label,
    date: c.date,
    skills: c.skills,
    url: c.url,
  }))
);

const FILTERS = CERT_PROVIDERS.map((p) => p.label);

export function Certifications() {
  const { ui } = useContent();
  const [filter, setFilter] = useState(FILTERS[0]);
  const rows = ALL.filter((r) => r.issuer === filter);

  return (
    <section id="certificates" className="section">
      <div className="shell">
        <SectionHeader
          index="04"
          title={ui.sections.certificates.title}
          standfirst={ui.sections.certificates.standfirst}
        />

        {/* Filter */}
        <div className="mb-5 flex flex-wrap gap-2">
          {FILTERS.map((f) => (
            <button
              key={f}
              onClick={() => setFilter(f)}
              className={cx(
                'font-mono text-xs uppercase tracking-widest',
                'border border-ink px-3 py-1 transition-colors',
                filter === f ? 'bg-ink text-paper' : 'bg-transparent hover:bg-paper-2'
              )}
            >
              {f}{' '}
              <span className="opacity-60">({ALL.filter((r) => r.issuer === f).length})</span>
            </button>
          ))}
        </div>

        {/* Ledger */}
        <div className="overflow-x-auto border-2 border-ink">
          <table className="w-full min-w-[720px] border-collapse text-left">
            <thead>
              <tr className="border-b-2 border-ink bg-ink text-paper">
                <th className="meta !text-paper px-3 py-2 w-10">{ui.certs.colNo}</th>
                <th className="meta !text-paper px-3 py-2">{ui.certs.colCredential}</th>
                <th className="meta !text-paper px-3 py-2">{ui.certs.colIssuer}</th>
                <th className="meta !text-paper px-3 py-2">{ui.certs.colFocus}</th>
                <th className="meta !text-paper px-3 py-2">{ui.certs.colDate}</th>
                <th className="meta !text-paper px-3 py-2 text-right">{ui.certs.colVerify}</th>
              </tr>
            </thead>
            <tbody>
              {rows.map((r, i) => (
                <motion.tr
                  key={r.title}
                  initial={{ opacity: 0 }}
                  whileInView={{ opacity: 1 }}
                  viewport={{ once: true }}
                  transition={{ duration: 0.3, delay: Math.min(i * 0.03, 0.3) }}
                  className="group border-b border-ink/20 align-top transition-colors last:border-0 hover:bg-card"
                >
                  <td className="px-3 py-3 font-mono text-xs text-muted">{String(i + 1).padStart(2, '0')}</td>
                  <td className="px-3 py-3">
                    <span className="headline text-base leading-tight">{r.title}</span>
                  </td>
                  <td className="px-3 py-3">
                    <span className="tag">{r.issuer}</span>
                  </td>
                  <td className="px-3 py-3">
                    <span className="font-mono text-[0.68rem] text-ink-soft">
                      {r.skills.slice(0, 3).join(' · ')}
                    </span>
                  </td>
                  <td className="px-3 py-3 font-mono text-xs whitespace-nowrap">{r.date}</td>
                  <td className="px-3 py-3 text-right">
                    <a
                      href={r.url}
                      target="_blank"
                      rel="noreferrer"
                      className="link-underline font-mono text-xs uppercase tracking-widest text-accent-deep"
                    >
                      {ui.certs.verify}
                    </a>
                  </td>
                </motion.tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </section>
  );
}
