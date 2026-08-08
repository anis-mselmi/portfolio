const ITEMS = [
  'JAVA', 'PYTHON', 'MACHINE LEARNING', 'RAG PIPELINES', 'LLMs', 'PYTORCH',
  'DEEP LEARNING', 'DOCKER', 'CI/CD', 'LINUX', 'GIT', 'SPRING BOOT',
  'COMPUTER VISION', 'SCIKIT-LEARN', 'SQL', 'DATA ENGINEERING',
  'PROMPT ENGINEERING', 'CUDA', 'TRANSFORMERS',
];

/** Newspaper-style running headline ticker. */
export function Ticker() {
  return (
    <div className="border-y-2 border-ink bg-ink text-paper">
      <div className="flex items-stretch overflow-hidden">
        <span className="flex shrink-0 items-center bg-accent px-4 font-mono text-xs font-bold uppercase tracking-widest text-paper">
          Stack ▸
        </span>
        <div className="relative flex-1 overflow-hidden py-2">
          <div className="ticker-track">
            {[...ITEMS, ...ITEMS].map((t, i) => (
              <span key={i} className="flex shrink-0 items-center font-mono text-xs tracking-widest">
                <span className="px-6">{t}</span>
                <span className="text-accent">✦</span>
              </span>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}
