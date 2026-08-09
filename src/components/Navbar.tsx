import { useEffect, useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { Menu, X } from 'lucide-react';
import { NAV_ITEMS, cx } from '../lib/utils';
import { useActiveSection } from '../hooks/useActiveSection';
import { useContent } from '../i18n/content';
import { LangToggle } from './LangToggle';

const IDS = ['hero', ...NAV_ITEMS.filter((i) => !('href' in i)).map((i) => i.id)];

/** Sticky editorial masthead bar (appears after scrolling past the nameplate). */
export function Navbar() {
  const { ui } = useContent();
  const active = useActiveSection(IDS);
  const [open, setOpen] = useState(false);
  const [shown, setShown] = useState(false);

  useEffect(() => {
    const onScroll = () => setShown(window.scrollY > 320);
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
    return () => window.removeEventListener('scroll', onScroll);
  }, []);

  const go = (id: string) => (e: React.MouseEvent) => {
    e.preventDefault();
    setOpen(false);
    const el = document.getElementById(id);
    if (!el) return;
    // Land the section's heading just below the fixed navbar, accounting for
    // both the navbar height and the section's own top padding.
    const navH = document.querySelector('header.fixed')?.getBoundingClientRect().height ?? 0;
    const style = getComputedStyle(el);
    const padTop = parseFloat(style.paddingTop) || 0;
    const top = el.getBoundingClientRect().top + window.scrollY - navH - 16 + padTop;
    window.scrollTo({ top, behavior: 'smooth' });
  };

  return (
    <AnimatePresence>
      {shown && (
        <motion.header
          initial={{ y: -70 }}
          animate={{ y: 0 }}
          exit={{ y: -70 }}
          transition={{ duration: 0.35, ease: [0.22, 1, 0.36, 1] }}
          className="fixed inset-x-0 top-0 z-50 border-b-2 border-ink bg-paper/95 backdrop-blur-sm"
        >
          <div className="shell flex items-center justify-between py-2.5">
            <a href="#hero" onClick={go('hero')} className="headline text-xl tracking-tight">
              Anis<span className="text-accent">.</span>Mselmi
            </a>

            <nav className="hidden items-center gap-5 md:flex">
              {NAV_ITEMS.map((item, i) =>
                'href' in item ? (
                  <a
                    key={item.id}
                    href={item.href}
                    target="_blank"
                    rel="noreferrer"
                    className="link-underline font-mono text-xs uppercase tracking-widest text-accent transition-colors hover:text-accent-deep"
                  >
                    <span className="text-muted">{String(i + 1).padStart(2, '0')}</span> {ui.nav[item.id]}
                  </a>
                ) : (
                  <a
                    key={item.id}
                    href={`#${item.id}`}
                    onClick={go(item.id)}
                    className={cx(
                      'link-underline font-mono text-xs uppercase tracking-widest transition-colors',
                      active === item.id ? 'text-accent' : 'text-ink hover:text-accent'
                    )}
                  >
                    <span className="text-muted">{String(i + 1).padStart(2, '0')}</span> {ui.nav[item.id]}
                  </a>
                )
              )}
              <LangToggle className="ml-1" />
            </nav>

            <div className="flex items-center gap-2 md:hidden">
              <LangToggle />
              <button
                onClick={() => setOpen((v) => !v)}
                className="border-1.5 border border-ink p-1.5"
                aria-label="Menu"
              >
                {open ? <X size={18} /> : <Menu size={18} />}
              </button>
            </div>
          </div>

          <AnimatePresence>
            {open && (
              <motion.nav
                initial={{ height: 0, opacity: 0 }}
                animate={{ height: 'auto', opacity: 1 }}
                exit={{ height: 0, opacity: 0 }}
                className="overflow-hidden border-t border-ink bg-paper md:hidden"
              >
                <div className="shell grid grid-cols-2 gap-px py-2">
                  {NAV_ITEMS.map((item, i) =>
                    'href' in item ? (
                      <a
                        key={item.id}
                        href={item.href}
                        target="_blank"
                        rel="noreferrer"
                        onClick={() => setOpen(false)}
                        className="py-2 font-mono text-xs uppercase tracking-widest text-accent"
                      >
                        <span className="text-accent">{String(i + 1).padStart(2, '0')}</span> {ui.nav[item.id]}
                      </a>
                    ) : (
                      <a
                        key={item.id}
                        href={`#${item.id}`}
                        onClick={go(item.id)}
                        className="py-2 font-mono text-xs uppercase tracking-widest"
                      >
                        <span className="text-accent">{String(i + 1).padStart(2, '0')}</span> {ui.nav[item.id]}
                      </a>
                    )
                  )}
                </div>
              </motion.nav>
            )}
          </AnimatePresence>
        </motion.header>
      )}
    </AnimatePresence>
  );
}
