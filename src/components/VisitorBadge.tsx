import { useEffect, useState } from 'react';

const SEED = 140;
const KEY = 'am_visitor_count';
const SESSION_KEY = 'am_counted';

/** "Circulation" counter, styled as a print run number. */
export function VisitorBadge() {
  const [count, setCount] = useState<number>(SEED);

  useEffect(() => {
    try {
      const stored = Number(localStorage.getItem(KEY));
      let value = Number.isFinite(stored) && stored >= SEED ? stored : SEED;
      if (!sessionStorage.getItem(SESSION_KEY)) {
        value += 1;
        localStorage.setItem(KEY, String(value));
        sessionStorage.setItem(SESSION_KEY, '1');
      }
      setCount(value);
    } catch {
      setCount(SEED);
    }
  }, []);

  return (
    <span className="meta">
      Circulation: <strong className="text-ink">{count.toLocaleString()}</strong>
    </span>
  );
}
