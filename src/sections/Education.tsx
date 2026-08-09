import { motion } from 'framer-motion';
import { SectionHeader } from '../components/SectionHeader';
import { Icon } from '../lib/icons';
import { useContent } from '../i18n/content';

export function Education() {
  const { education, ui } = useContent();
  return (
    <section id="education" className="section">
      <div className="shell">
        <SectionHeader
          index="02"
          title={ui.sections.education.title}
          standfirst={ui.sections.education.standfirst}
        />

        <div className="border-t-2 border-ink">
          {education.map((item, i) => (
            <motion.article
              key={item.title}
              initial={{ opacity: 0, y: 16 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true, margin: '0px 0px -8% 0px' }}
              transition={{ duration: 0.5, delay: i * 0.08 }}
              className="grid gap-4 border-b border-ink/30 py-6 md:grid-cols-[auto_1fr] md:gap-10"
            >
              <div className="flex items-center gap-3 md:flex-col md:items-start md:gap-3">
                <span className="grid h-12 w-12 place-items-center border-2 border-ink bg-card text-ink">
                  <Icon name={item.icon} size={24} strokeWidth={1.6} />
                </span>
                <span className="font-mono text-sm text-accent-deep">{item.years}</span>
              </div>
              <div>
                <h3 className="headline text-2xl md:text-3xl">{item.title}</h3>
                <div className="meta mt-1">{item.school}</div>
                <p className="mt-3 max-w-3xl text-ink-soft">{item.detail}</p>
              </div>
            </motion.article>
          ))}
        </div>
      </div>
    </section>
  );
}
