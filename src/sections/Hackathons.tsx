import { motion } from 'framer-motion';
import { HACKATHONS } from '../data/content';
import { SectionHeader } from '../components/SectionHeader';
import { assetUrl } from '../lib/utils';

export function Hackathons() {
  return (
    <section id="hackathons" className="section">
      <div className="shell">
        <SectionHeader
          index="06"
          title="Press Clippings"
          standfirst="Reports from the field — hackathon victories, robotics, and prototype innovation."
        />

        <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
          {HACKATHONS.map((item, i) => (
            <motion.article
              key={item.title}
              initial={{ opacity: 0, y: 20, rotate: i % 2 === 0 ? -0.6 : 0.6 }}
              whileInView={{ opacity: 1, y: 0, rotate: 0 }}
              viewport={{ once: true, margin: '0px 0px -8% 0px' }}
              transition={{ duration: 0.5, delay: (i % 3) * 0.1 }}
              className="print-card group flex flex-col"
            >
              <div className="relative overflow-hidden border-b-2 border-ink">
                <img
                  src={assetUrl(item.image)}
                  alt={item.title}
                  loading="lazy"
                  className="h-44 w-full object-cover grayscale transition-all duration-500 group-hover:grayscale-0 group-hover:scale-105"
                />
                <span className="absolute left-0 top-0 bg-accent px-2.5 py-1 font-mono text-xs font-bold uppercase tracking-wider text-paper">
                  ★ {item.badge}
                </span>
              </div>
              <div className="flex flex-1 flex-col p-4">
                <div className="meta text-accent-deep">Dispatch № {String(i + 1).padStart(2, '0')}</div>
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
