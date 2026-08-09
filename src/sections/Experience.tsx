import { motion } from 'framer-motion';
import { SectionHeader } from '../components/SectionHeader';
import { useContent } from '../i18n/content';

export function Experience() {
  const { work, volunteering, ui } = useContent();
  return (
    <section id="experience" className="section">
      <div className="shell">
        <SectionHeader
          index="03"
          title={ui.sections.experience.title}
          standfirst={ui.sections.experience.standfirst}
        />

        {/* Professional experience */}
        <div className="border-t-2 border-ink">
          {work.map((job, i) => (
            <motion.article
              key={job.org}
              initial={{ opacity: 0, y: 16 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true, margin: '0px 0px -8% 0px' }}
              transition={{ duration: 0.5, delay: i * 0.08 }}
              className="grid gap-4 border-b border-ink/30 py-7 md:grid-cols-[14rem_1fr] md:gap-10"
            >
              <div>
                <div className="font-mono text-sm text-accent-deep">{job.period}</div>
                <div className="meta mt-1">{ui.experience.position} {String(i + 1).padStart(2, '0')}</div>
              </div>
              <div>
                <h3 className="headline text-2xl md:text-3xl">
                  {job.role} <span className="text-accent">—</span> {job.org}
                </h3>
                <ul className="mt-3 space-y-2">
                  {job.points.map((p) => (
                    <li key={p} className="flex gap-2 text-ink-soft">
                      <span className="mt-1 shrink-0 text-accent">▸</span>
                      <span>{p}</span>
                    </li>
                  ))}
                </ul>
                {job.tags && (
                  <div className="mt-4 flex flex-wrap gap-1.5">
                    {job.tags.map((t) => (
                      <span key={t} className="tag">{t}</span>
                    ))}
                  </div>
                )}
              </div>
            </motion.article>
          ))}
        </div>

        {/* Volunteering */}
        <div className="mt-12">
          <div className="mb-4 flex items-baseline gap-3">
            <h3 className="font-mono text-xs uppercase tracking-widest text-accent-deep">
              {ui.experience.volunteerHeader}
            </h3>
            <hr className="rule-thin flex-1" />
          </div>
          <div className="grid gap-px border border-ink bg-ink sm:grid-cols-2 lg:grid-cols-3">
            {volunteering.map((v, i) => (
              <motion.div
                key={`${v.org}-${v.role}`}
                initial={{ opacity: 0 }}
                whileInView={{ opacity: 1 }}
                viewport={{ once: true }}
                transition={{ duration: 0.4, delay: (i % 3) * 0.06 }}
                className="bg-card p-4"
              >
                <div className="flex items-baseline justify-between gap-2">
                  <span className="meta text-accent-deep">{String(i + 1).padStart(2, '0')}</span>
                  {v.period && <span className="font-mono text-[0.7rem] text-muted">{v.period}</span>}
                </div>
                <div className="headline mt-1 text-lg leading-tight">{v.role}</div>
                <div className="meta mt-0.5">{v.org}</div>
                {v.detail && <p className="mt-2 text-sm text-ink-soft">{v.detail}</p>}
              </motion.div>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
}
