import { motion } from 'framer-motion';
import { sectionIndex } from '../lib/utils';
import {
  // Languages
  siCplusplus,
  siOpenjdk,
  siJavascript,
  siTypescript,
  // AI / ML / DL
  siScikitlearn,
  siPytorch,
  siTensorflow,
  siOpencv,
  siNvidia,
  siHuggingface,
  siLangchain,
  siGooglegemini,
  siOllama,
  siGradio,
  siWeightsandbiases,
  siMlflow,
  siQdrant,
  // Data
  siApachekafka,
  siDvc,
  siKaggle,
  // Notebooks / envs
  siJupyter,
  siAnaconda,
  siGooglecolab,
  // Backend / web
  siSpringboot,
  siFastapi,
  siFlask,
  siDjango,
  siNodedotjs,
  siReact,
  siStreamlit,
  siVite,
  // Databases
  siMysql,
  siPostgresql,
  siMongodb,
  siRedis,
  siSqlite,
  // DevOps / cloud
  siDocker,
  siKubernetes,
  siGit,
  siGithub,
  siLinux,
  siUbuntu,
  type SimpleIcon,
} from 'simple-icons';
import { SectionHeader } from '../components/SectionHeader';
import { useContent } from '../i18n/content';

/** Ordered set of official brand logos (Simple Icons) — only tools with a logo. */
const TOOLS: SimpleIcon[] = [
  siLinux, siNvidia, siHuggingface, siOpenjdk, siJavascript, siTypescript,
  siScikitlearn, siPytorch, siTensorflow, siGit, siSpringboot, siGithub,
  siUbuntu, siCplusplus, siLangchain, siGooglegemini, siOllama, siGradio,
  siWeightsandbiases, siMlflow, siQdrant,
  siApachekafka, siDvc, siKaggle,
  siJupyter, siAnaconda, siGooglecolab,
  siOpencv, siFastapi, siFlask, siDjango, siNodedotjs, siReact, siStreamlit, siVite,
  siMysql, siPostgresql, siMongodb, siRedis, siSqlite,
  siDocker, siKubernetes,
];

function BrandTile({ icon, delay }: { icon: SimpleIcon; delay: number }) {
  return (
    <motion.div
      initial={{ opacity: 0, y: 12 }}
      whileInView={{ opacity: 1, y: 0 }}
      viewport={{ once: true, margin: '0px 0px -4% 0px' }}
      transition={{ duration: 0.32, delay, ease: [0.22, 1, 0.36, 1] }}
      className="brand-tile"
      style={{ ['--brand' as string]: `#${icon.hex}` }}
      title={icon.title}
      aria-label={icon.title}
    >
      <svg role="img" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
        <path d={icon.path} />
      </svg>
      <span className="brand-name">{icon.title}</span>
    </motion.div>
  );
}

export function Skills() {
  const { ui } = useContent();

  return (
    <section id="skills" className="section">
      <div className="shell">
        <SectionHeader
          index={sectionIndex('skills')}
          title={ui.sections.skills.title}
          standfirst={ui.sections.skills.standfirst}
        />

        {/* Official logos, centered and fitted into one grid */}
        <div className="mx-auto grid max-w-4xl grid-cols-4 justify-items-center gap-x-6 gap-y-12 sm:grid-cols-6 md:grid-cols-7">
          {TOOLS.map((icon, i) => (
            <BrandTile key={icon.title} icon={icon} delay={(i % 7) * 0.03} />
          ))}
        </div>
      </div>
    </section>
  );
}
