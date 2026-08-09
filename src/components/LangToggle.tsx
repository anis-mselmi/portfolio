import { useLang } from '../i18n/LanguageContext';
import { useContent } from '../i18n/content';
import { cx } from '../lib/utils';

/** Editorial EN / FR segmented pill for switching the site language. */
export function LangToggle({ className }: { className?: string }) {
  const { lang, setLang } = useLang();
  const { ui } = useContent();

  return (
    <div
      className={cx(
        'inline-flex select-none items-stretch border-2 border-ink font-mono text-[0.7rem] font-bold uppercase tracking-widest',
        className
      )}
      role="group"
      aria-label="Language"
    >
      <button
        type="button"
        onClick={() => setLang('en')}
        aria-pressed={lang === 'en'}
        aria-label={ui.toggle.toEnglish}
        className={cx(
          'px-2 py-0.5 transition-colors',
          lang === 'en' ? 'bg-accent text-paper' : 'bg-transparent text-ink hover:bg-paper-2'
        )}
      >
        EN
      </button>
      <span className="w-px self-stretch bg-ink" aria-hidden="true" />
      <button
        type="button"
        onClick={() => setLang('fr')}
        aria-pressed={lang === 'fr'}
        aria-label={ui.toggle.toFrench}
        className={cx(
          'px-2 py-0.5 transition-colors',
          lang === 'fr' ? 'bg-accent text-paper' : 'bg-transparent text-ink hover:bg-paper-2'
        )}
      >
        FR
      </button>
    </div>
  );
}
