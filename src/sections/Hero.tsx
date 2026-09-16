import { motion } from 'framer-motion';
import { Github, Linkedin, MapPin, FileText } from 'lucide-react';
import { PROFILE, HACKATHONS } from '../data/content';
import { assetUrl } from '../lib/utils';
import { Stat } from '../components/Stat';
import { useContent } from '../i18n/content';
import { useLang } from '../i18n/LanguageContext';

const HERO_IMG = assetUrl('/assets/images/profile/anis.jpg');

/** Current X (formerly Twitter) brand mark — lucide only ships the old bird. */
function XIcon({ size = 16 }: { size?: number }) {
  return (
    <svg
      width={size}
      height={size}
      viewBox="0 0 24 24"
      fill="currentColor"
      aria-hidden="true"
    >
      <path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24h-6.66l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z" />
    </svg>
  );
}
const TOTAL_CERTS = 20;

const fade = (delay: number) => ({
  initial: { opacity: 0, y: 16 },
  animate: { opacity: 1, y: 0 },
  transition: { duration: 0.6, delay, ease: [0.22, 1, 0.36, 1] as const },
});

export function Hero() {
  const { lang } = useLang();
  const { ui } = useContent();
  const editionDate = new Date().toLocaleDateString(lang === 'fr' ? 'fr-FR' : 'en-US', {
    weekday: 'long',
    year: 'numeric',
    month: 'long',
    day: 'numeric',
  });

  return (
    <header id="hero" className="section !pt-8">
      <div className="shell">
        {/* Folio / dateline */}
        <motion.div {...fade(0)} className="flex flex-wrap items-center justify-between gap-2 pb-2">
          <span className="meta">{ui.hero.folio}</span>
          <span className="meta hidden sm:inline">{editionDate}</span>
        </motion.div>
        <hr className="rule-double" />

        {/* Nameplate */}
        <motion.h1
          {...fade(0.05)}
          className="headline mt-5 text-center text-[clamp(3rem,13vw,10rem)] leading-[0.86]"
        >
          Anis Mselmi
        </motion.h1>

        <motion.div
          {...fade(0.12)}
          className="mt-4 flex flex-wrap items-center justify-center gap-x-3 gap-y-1 text-center"
        >
          <span className="kicker">{ui.hero.kicker1}</span>
          <span className="text-accent">✦</span>
          <span className="kicker">{ui.hero.kicker2}</span>
          <span className="text-accent">✦</span>
          <span className="kicker">{ui.hero.kicker3}</span>
        </motion.div>

        <hr className="rule mt-5" />

        {/* Lede grid */}
        <div className="mt-8 grid gap-8 lg:grid-cols-[1.05fr_0.95fr]">
          {/* Left: editorial lede */}
          <motion.div {...fade(0.18)}>
            <span className="meta">{ui.hero.dateline}</span>
            <p className="lede dropcap mt-3">{ui.hero.lede}</p>

            <div className="mt-6 flex flex-wrap gap-3">
              <a href={PROFILE.github} target="_blank" rel="noreferrer" className="btn btn-solid">
                <Github size={16} /> GitHub
              </a>
              <a href={PROFILE.linkedin} target="_blank" rel="noreferrer" className="btn btn-linkedin">
                <Linkedin size={16} /> LinkedIn
              </a>
              <a
                href={PROFILE.cv}
                target="_blank"
                rel="noreferrer"
                className="btn btn-accent"
              >
                <FileText size={16} /> {ui.hero.cv}
              </a>
              <a
                href={PROFILE.x}
                target="_blank"
                rel="noreferrer"
                className="btn"
                aria-label="X (Twitter)"
              >
                <XIcon size={15} />
              </a>
            </div>

            {/* By the numbers */}
            <div className="mt-8 grid grid-cols-3 gap-4 border-t-2 border-ink pt-5">
              <Stat end={TOTAL_CERTS} suffix="+" label={ui.hero.statCerts} />
              <Stat end={HACKATHONS.length} suffix="+" label={ui.hero.statWins} />
              <Stat end={8} suffix="+" label={ui.hero.statProjects} />
            </div>
          </motion.div>

          {/* Right: halftone portrait plate */}
          <motion.figure
            initial={{ opacity: 0, scale: 0.98 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ duration: 0.7, delay: 0.25 }}
            className="print-card self-start p-2.5"
          >
            <div className="halftone overflow-hidden">
              <img src={HERO_IMG} alt="Anis Mselmi" className="w-full object-cover" loading="eager" />
            </div>
            <figcaption className="meta mt-2 flex items-center justify-between">
              <span className="flex items-center gap-1">
                <MapPin size={11} /> {PROFILE.location.split(',')[0]}
              </span>
              <span>{ui.hero.figCaption}</span>
            </figcaption>
          </motion.figure>
        </div>
      </div>
    </header>
  );
}
