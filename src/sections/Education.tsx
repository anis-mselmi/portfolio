import { SectionHeader } from '../components/SectionHeader';
import { sectionIndex } from '../lib/utils';
import { GitLog, type Commit } from '../components/GitLog';
import { useContent } from '../i18n/content';

export function Education() {
  const { education, ui } = useContent();

  const commits: Commit[] = education.map((item, i) => ({
    title: item.title,
    refs: i === 0 ? 'HEAD -> main, origin/main' : undefined,
    meta: `${item.school}  ·  ${item.years}`,
    body: item.detail,
  }));

  return (
    <section id="education" className="section">
      <div className="shell">
        <SectionHeader
          index={sectionIndex('education')}
          title={ui.sections.education.title}
          standfirst={ui.sections.education.standfirst}
        />
        <GitLog path="academic" cmd="git log --graph --stat" commits={commits} />
      </div>
    </section>
  );
}
