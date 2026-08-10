import { motion } from 'framer-motion';
import type { ReactNode } from 'react';

export interface Commit {
  title: string;
  refs?: string;
  meta: string;
  body: ReactNode;
}

/** Deterministic 7-char hex "sha" from a string. */
function shaOf(s: string): string {
  let h = 0x811c9dc5;
  for (let i = 0; i < s.length; i++) {
    h ^= s.charCodeAt(i);
    h = Math.imul(h, 0x01000193);
  }
  return (h >>> 0).toString(16).padStart(8, '0').slice(0, 7);
}

function Prompt({ path }: { path: string }) {
  return (
    <span>
      <span className="term-user">anis@portfolio</span>
      <span className="term-punct">:</span>
      <span className="term-path">~/{path}</span>
      <span className="term-punct">$ </span>
    </span>
  );
}

export function GitLog({
  path,
  cmd,
  commits,
  trailer,
}: {
  path: string;
  cmd: string;
  commits: Commit[];
  trailer?: ReactNode;
}) {
  return (
    <motion.div
      initial={{ opacity: 0, y: 18 }}
      whileInView={{ opacity: 1, y: 0 }}
      viewport={{ once: true, margin: '0px 0px -8% 0px' }}
      transition={{ duration: 0.55, ease: [0.22, 1, 0.36, 1] }}
      className="terminal"
    >
      <div className="term-bar">
        <span className="term-dot" aria-hidden />
        <span className="term-dot" aria-hidden />
        <span className="term-dot" aria-hidden />
        <span className="ml-1">bash — anis@portfolio: ~/{path}</span>
      </div>

      <div className="term-body">
        <div className="mb-4">
          <Prompt path={path} />
          <span>{cmd}</span>
        </div>

        {commits.map((c, i) => (
          <div key={c.title} className="git-commit pb-5 last:pb-1">
            <span className="git-node" aria-hidden>
              *
            </span>
            {i < commits.length - 1 && <span className="git-spine" aria-hidden />}

            <div className="leading-snug">
              <span className="git-sha">{shaOf(c.title)}</span>{' '}
              {c.refs && <span className="git-ref">({c.refs})</span>}
            </div>
            <div className="git-title">{c.title}</div>
            <div className="git-meta mt-1">{c.meta}</div>
            <div className="git-body mt-2 max-w-2xl">{c.body}</div>
          </div>
        ))}

        {trailer}

        <div className="mt-3">
          <Prompt path={path} />
          <span className="term-cursor" aria-hidden />
        </div>
      </div>
    </motion.div>
  );
}
