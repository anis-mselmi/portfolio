import { motion } from 'framer-motion';
import { SectionHeader } from '../components/SectionHeader';
import { assetUrl, cx, sectionIndex } from '../lib/utils';
import { useContent } from '../i18n/content';

export function Hackathons() {
  const { hackathons, ui } = useContent();
  return (
    <section id="hackathons" className="section">
      <div className="shell">
        <SectionHeader
          index={sectionIndex('hackathons')}
          title={ui.sections.hackathons.title}
          standfirst={ui.sections.hackathons.standfirst}
        />

        <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
          {hackathons.map((item, i) => (
            <motion.article
              key={item.title}
              initial={{ opacity: 0, y: 20, rotate: i % 2 === 0 ? -0.6 : 0.6 }}
              whileInView={{ opacity: 1, y: 0, rotate: 0 }}
              viewport={{ once: true, margin: '0px 0px -8% 0px' }}
              transition={{ duration: 0.5, delay: (i % 3) * 0.1 }}
              className="print-card group flex flex-col"
            >
              <div className="relative h-56 overflow-hidden border-b-2 border-ink">
                {item.fit === 'contain' && (
                  // Fills the band with a blurred copy so a portrait poster has no empty bars.
                  <img
                    src={assetUrl(item.image)}
                    alt=""
                    aria-hidden="true"
                    loading="lazy"
                    className="absolute inset-0 h-full w-full scale-125 object-cover blur-xl grayscale transition-all duration-500 group-hover:grayscale-0"
                  />
                )}
                <img
                  src={assetUrl(item.image)}
                  alt={item.title}
                  loading="lazy"
                  style={{ objectPosition: item.pos ?? 'center' }}
                  className={cx(
                    'relative h-full w-full grayscale transition-all duration-500 group-hover:scale-105 group-hover:grayscale-0',
                    item.fit === 'contain' ? 'object-contain' : 'object-cover'
                  )}
                />
                <span className="absolute left-0 top-0 bg-accent px-2.5 py-1 font-mono text-xs font-bold uppercase tracking-wider text-paper">
                  ★ {item.badge}
                </span>
              </div>
              <div className="flex flex-1 flex-col p-4">
                <div className="meta text-accent-deep">{ui.hackathons.dispatch} {String(i + 1).padStart(2, '0')}</div>
                <h3 className="headline mt-1 text-xl leading-tight">{item.title}</h3>
                <p className="mt-2 flex-1 text-sm text-ink-soft">{item.desc}</p>
                <div className="mt-4 flex flex-wrap gap-1.5">
                  {item.tags.map((t) => (
                    <span key={t} className="tag">{t}</span>
                  ))}
                </div>
              </div>
            </motion.article>
          ))}
        </div>
      </div>
    </section>
  );
}
