import { motion } from 'framer-motion';
import { SKILLS_BY_CATEGORY } from '../data/content';
import type { Skill } from '../data/types';
import { SectionHeader } from '../components/SectionHeader';
import { Icon } from '../lib/icons';

const LEVEL_BLOCKS: Record<string, number> = {
  Expert: 4,
  Advanced: 3,
  Intermediate: 2,
  Beginner: 1,
};
const LEVEL_PCT: Record<string, number> = {
  Expert: 96,
  Advanced: 80,
  Intermediate: 60,
  Beginner: 35,
};

function Blocks({ level }: { level: string }) {
  const n = LEVEL_BLOCKS[level] ?? 2;
  return (
    <span className="inline-flex gap-1" aria-label={level}>
      {[0, 1, 2, 3].map((i) => (
        <span
          key={i}
          className="inline-block h-2.5 w-2.5"
          style={{
            background: i < n ? 'var(--accent)' : 'transparent',
            border: '1px solid var(--ink)',
          }}
        />
      ))}
    </span>
  );
}

function SkillEntry({ skill, i }: { skill: Skill; i: number }) {
  return (
    <motion.div
      initial={{ opacity: 0, y: 14 }}
      whileInView={{ opacity: 1, y: 0 }}
      viewport={{ once: true, margin: '0px 0px -8% 0px' }}
      transition={{ duration: 0.4, delay: (i % 3) * 0.05 }}
      className="flat-cell flex flex-col p-4"
    >
      <div className="flex items-start justify-between gap-2">
        <div className="flex items-center gap-2.5">
          <span className="grid h-9 w-9 shrink-0 place-items-center border border-ink bg-paper text-ink">
            <Icon name={skill.icon} size={18} />
          </span>
          <span className="headline text-lg leading-tight">{skill.name}</span>
        </div>
        <Blocks level={skill.level} />
      </div>
      <div className="meta mt-2">{skill.level}</div>
      <p className="mt-1 text-sm text-ink-soft">{skill.subtitle}</p>
      <div className="mt-3 flex flex-wrap gap-1.5">
        {skill.tags.slice(0, 3).map((t) => (
          <span key={t} className="tag">{t}</span>
        ))}
      </div>
    </motion.div>
  );
}

export function Skills() {
  // flat top list for the proficiency figure
  const top = Object.values(SKILLS_BY_CATEGORY)
    .flat()
    .map((s) => ({ name: s.name, pct: LEVEL_PCT[s.level] ?? 60 }))
    .sort((a, b) => b.pct - a.pct)
    .slice(0, 8);

  return (
    <section id="skills" className="section">
      <div className="shell">
        <SectionHeader
          index="01"
          title="Fields of Expertise"
          standfirst="A working index of technical competencies, from AI systems to backend engineering."
        />

        <div className="grid gap-10 lg:grid-cols-[1.6fr_1fr]">
          {/* Skill index by category */}
          <div className="space-y-8">
            {Object.entries(SKILLS_BY_CATEGORY).map(([category, items]) => (
              <div key={category}>
                <div className="mb-3 flex items-baseline gap-3">
                  <h3 className="font-mono text-xs uppercase tracking-widest text-accent-deep">
                    {category}
                  </h3>
                  <hr className="rule-thin flex-1" />
                </div>
                <div className="grid gap-4 sm:grid-cols-2">
                  {items.map((skill, i) => (
                    <SkillEntry key={skill.name} skill={skill} i={i} />
                  ))}
                </div>
              </div>
            ))}
          </div>

          {/* Proficiency figure — printed bar chart */}
          <figure className="print-card h-fit p-5 lg:sticky lg:top-24">
            <figcaption className="meta mb-4 border-b-2 border-ink pb-2">
              Fig. 2 — Proficiency Index (%)
            </figcaption>
            <div className="space-y-3">
              {top.map((s, i) => (
                <div key={s.name}>
                  <div className="flex items-baseline justify-between">
                    <span className="font-mono text-xs">{s.name}</span>
                    <span className="font-mono text-xs text-muted">{s.pct}</span>
                  </div>
                  <div className="mt-1 h-3 w-full border border-ink bg-paper">
                    <motion.div
                      className="h-full bg-ink"
                      initial={{ width: 0 }}
                      whileInView={{ width: `${s.pct}%` }}
                      viewport={{ once: true }}
                      transition={{ duration: 0.8, delay: i * 0.06, ease: [0.22, 1, 0.36, 1] }}
                      style={{ background: i === 0 ? 'var(--accent)' : 'var(--ink)' }}
                    />
                  </div>
                </div>
              ))}
            </div>
          </figure>
        </div>
      </div>
    </section>
  );
}
