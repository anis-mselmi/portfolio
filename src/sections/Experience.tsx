import { SectionHeader } from '../components/SectionHeader';
import { sectionIndex } from '../lib/utils';
import { GitLog, type Commit } from '../components/GitLog';
import { useContent } from '../i18n/content';

function slug(s: string) {
  return s
    .toLowerCase()
    .normalize('NFD')
    .replace(/[̀-ͯ]/g, '')
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-|-$/g, '');
}

export function Experience() {
  const { work, volunteering, ui } = useContent();

  const commits: Commit[] = work.map((job, i) => ({
    title: `${job.role} @ ${job.org}`,
    refs: i === 0 ? 'HEAD -> main' : undefined,
    meta: job.period,
    body: (
      <div>
        {job.points.map((p) => (
          <div key={p} className="flex gap-2">
            <span className="text-accent">+</span>
            <span>{p}</span>
          </div>
        ))}
        {job.tags && (
          <div className="mt-2 text-[color:var(--t-dim)]">
            <span className="term-punct"># </span>
            {job.tags.map((t) => slug(t)).join('  ')}
          </div>
        )}
      </div>
    ),
  }));

  const trailer = (
    <div className="mt-2 border-t border-[rgba(236,229,212,0.12)] pt-4">
      <div className="mb-3">
        <span className="term-user">anis@portfolio</span>
        <span className="term-punct">:</span>
        <span className="term-path">~/experience</span>
        <span className="term-punct">$ </span>
        <span>git tag --list 'service/*'</span>
      </div>
      <div className="text-[color:var(--t-dim)]" aria-label={ui.experience.serviceHeader}>
        {volunteering.map((v) => (
          <div key={`${v.org}-${v.role}`} className="flex flex-wrap items-baseline gap-x-3">
            <span className="git-ref">service/{slug(v.org)}</span>
            <span className="text-[color:var(--t-body)]">{v.role}</span>
            <span className="term-punct">—</span>
            <span>{v.org}</span>
            {v.period && <span className="ml-auto text-[color:var(--t-dim)]">{v.period}</span>}
          </div>
        ))}
      </div>
    </div>
  );

  return (
    <section id="experience" className="section">
      <div className="shell">
        <SectionHeader
          index={sectionIndex('experience')}
          title={ui.sections.experience.title}
          standfirst={ui.sections.experience.standfirst}
        />
        <GitLog
          path="experience"
          cmd="git log --graph --oneline --stat"
          commits={commits}
          trailer={trailer}
        />
      </div>
    </section>
  );
}
