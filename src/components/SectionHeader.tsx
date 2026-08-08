import { motion } from 'framer-motion';

interface SectionHeaderProps {
  index: string; // e.g. "01"
  title: string;
  standfirst?: string;
}

/** Numbered editorial section header with a drawing rule. */
export function SectionHeader({ index, title, standfirst }: SectionHeaderProps) {
  return (
    <div className="mb-10">
      <div className="flex items-baseline gap-4">
        <span className="kicker whitespace-nowrap">N°{index}</span>
        <motion.hr
          className="rule flex-1"
          initial={{ scaleX: 0 }}
          whileInView={{ scaleX: 1 }}
          viewport={{ once: true }}
          transition={{ duration: 0.7, ease: [0.22, 1, 0.36, 1] }}
          style={{ transformOrigin: 'left' }}
        />
      </div>
      <motion.h2
        className="headline mt-4 text-[clamp(2.2rem,5.5vw,4rem)]"
        initial={{ opacity: 0, y: 18 }}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true }}
        transition={{ duration: 0.55 }}
      >
        {title}
      </motion.h2>
      {standfirst && (
        <p className="lede mt-3 max-w-3xl italic">{standfirst}</p>
      )}
    </div>
  );
}
