import { motion } from 'framer-motion';
import { ArrowUpRight } from 'lucide-react';
import { SectionHeader } from '../components/SectionHeader';
import { assetUrl } from '../lib/utils';
import { useContent } from '../i18n/content';

export function Projects() {
  const { projects, ui } = useContent();
  return (
    <section id="projects" className="section">
      <div className="shell">
        <SectionHeader
          index="05"
          title={ui.sections.projects.title}
          standfirst={ui.sections.projects.standfirst}
        />

        <div className="grid gap-6 md:grid-cols-3">
          {projects.map((project, i) => (
            <motion.a
              key={project.name}
              href={project.link}
              target="_blank"
              rel="noreferrer"
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true, margin: '0px 0px -8% 0px' }}
              transition={{ duration: 0.5, delay: (i % 3) * 0.1 }}
              className="print-card group flex flex-col"
            >
              <div className="relative aspect-[16/11] overflow-hidden border-b-2 border-ink">
                <img
                  src={assetUrl(project.image)}
                  alt={project.name}
                  loading="lazy"
                  className="h-full w-full object-cover grayscale transition-all duration-500 group-hover:grayscale-0"
                  style={{ objectFit: project.fit ?? 'cover' }}
                />
                <span className="absolute right-0 top-0 grid h-9 w-9 place-items-center bg-ink text-paper transition-colors group-hover:bg-accent">
                  <ArrowUpRight size={16} />
                </span>
              </div>
              <div className="flex flex-1 flex-col p-4">
                <div className="meta text-accent-deep">{ui.projects.dispatch} {String(i + 1).padStart(2, '0')}</div>
                <h3 className="headline mt-1 text-2xl leading-tight">{project.name}</h3>
                <p className="mt-2 flex-1 text-sm text-ink-soft">{project.desc}</p>
                <div className="mt-4 flex flex-wrap gap-1.5">
                  {project.tags.map((t) => (
                    <span key={t} className="tag">{t}</span>
                  ))}
                </div>
              </div>
            </motion.a>
          ))}
        </div>
      </div>
    </section>
  );
}
