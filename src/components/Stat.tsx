import { useCountUp } from '../hooks/useCountUp';

interface StatProps {
  end: number;
  suffix?: string;
  label: string;
}

export function Stat({ end, suffix = '', label }: StatProps) {
  const { value, ref } = useCountUp(end);
  return (
    <div>
      <div className="headline text-4xl sm:text-5xl">
        <span ref={ref}>{value}</span>
        <span className="text-accent">{suffix}</span>
      </div>
      <div className="meta mt-1">{label}</div>
    </div>
  );
}
