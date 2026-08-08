import { useEffect, useState } from 'react';

/**
 * Tracks which section id is currently active in the viewport using an
 * IntersectionObserver, mirroring the original Streamlit navbar behavior.
 */
export function useActiveSection(ids: readonly string[], defaultId = 'hero'): string {
  const [active, setActive] = useState(defaultId);

  useEffect(() => {
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting && entry.target.id) {
            setActive(entry.target.id);
          }
        });
      },
      { root: null, rootMargin: '-40% 0px -45% 0px', threshold: 0.01 }
    );

    const targets = ids
      .map((id) => document.getElementById(id))
      .filter((el): el is HTMLElement => el !== null);
    targets.forEach((el) => observer.observe(el));

    return () => observer.disconnect();
  }, [ids]);

  return active;
}
