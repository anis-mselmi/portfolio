import { Github, Linkedin, Mail, ArrowUp } from 'lucide-react';
import { PROFILE } from '../data/content';

export function Footer() {
  const year = new Date().getFullYear();
  return (
    <footer className="border-t-2 border-ink">
      <div className="shell py-10">
        <div className="flex flex-col items-center gap-6 text-center">
          <div className="headline text-3xl">Anis<span className="text-accent">.</span>Mselmi</div>

          <div className="flex items-center gap-3">
            <a href={PROFILE.github} target="_blank" rel="noreferrer" className="border border-ink p-2.5 transition-colors hover:bg-ink hover:text-paper" aria-label="GitHub">
              <Github size={16} />
            </a>
            <a href={PROFILE.linkedin} target="_blank" rel="noreferrer" className="border border-ink p-2.5 transition-colors hover:bg-ink hover:text-paper" aria-label="LinkedIn">
              <Linkedin size={16} />
            </a>
            <a href={`mailto:${PROFILE.email}`} className="border border-ink p-2.5 transition-colors hover:bg-ink hover:text-paper" aria-label="Email">
              <Mail size={16} />
            </a>
            <button onClick={() => window.scrollTo({ top: 0, behavior: 'smooth' })} className="border border-ink p-2.5 transition-colors hover:bg-accent hover:border-accent hover:text-paper" aria-label="Back to top">
              <ArrowUp size={16} />
            </button>
          </div>

          <hr className="rule w-full" />

          <p className="meta">
            Colophon — Set in Fraunces, Archivo &amp; Space Mono · Built with React, TypeScript &amp; Vite ·
            © {year} {PROFILE.name}
          </p>
        </div>
      </div>
    </footer>
  );
}
