import {
  Bot,
  Brain,
  Layers,
  Code2,
  Coffee,
  BookOpen,
  BarChart3,
  LineChart,
  FlaskConical,
  GitBranch,
  Github,
  Orbit,
  Cpu,
  Compass,
  GraduationCap,
  Sparkles,
  type LucideIcon,
} from 'lucide-react';

/** Monochrome line-icon registry — replaces color emojis to suit the
 *  ink-on-paper editorial aesthetic. Keys are referenced from data. */
const REGISTRY: Record<string, LucideIcon> = {
  bot: Bot,
  brain: Brain,
  layers: Layers,
  code: Code2,
  coffee: Coffee,
  notebook: BookOpen,
  'bar-chart': BarChart3,
  'line-chart': LineChart,
  flask: FlaskConical,
  git: GitBranch,
  github: Github,
  orbit: Orbit,
  cpu: Cpu,
  compass: Compass,
  cap: GraduationCap,
};

interface IconProps {
  name: string;
  size?: number;
  className?: string;
  strokeWidth?: number;
}

export function Icon({ name, size = 20, className, strokeWidth = 1.75 }: IconProps) {
  const Cmp = REGISTRY[name] ?? Sparkles;
  return <Cmp size={size} className={className} strokeWidth={strokeWidth} />;
}
