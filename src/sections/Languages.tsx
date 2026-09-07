import { motion } from 'framer-motion';
import { sectionIndex } from '../lib/utils';
import { SectionHeader } from '../components/SectionHeader';
import { useContent } from '../i18n/content';

export function Languages() {
  const { languages, ui } = useContent();
  return (
    <section id="languages" className="section">
      <div className="shell">
        <SectionHeader
          index={sectionIndex('languages')}
          title={ui.sections.languages.title}
          standfirst={ui.sections.languages.standfirst}
        />

        <div className="grid gap-px border border-ink bg-ink md:grid-cols-3">
          {languages.map((lang, i) => (
            <motion.div
              key={lang.name}
              initial={{ opacity: 0, y: 16 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.45, delay: i * 0.1 }}
              className="bg-card p-6"
            >
              <div className="flex items-center justify-between">
                <img
                  src={lang.flagSrc}
                  alt={lang.flagAlt}
                  className="h-10 w-14 border border-ink object-cover grayscale"
                />
                <span className="tag tag-accent">{lang.badge}</span>
              </div>
              <h3 className="headline mt-4 text-3xl">{lang.name}</h3>
              <p className="mt-2 text-sm text-ink-soft">{lang.detail}</p>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  );
}
