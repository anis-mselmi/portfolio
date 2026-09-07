/** Join class names, skipping falsy values. */
export function cx(...parts: Array<string | false | null | undefined>): string {
  return parts.filter(Boolean).join(' ');
}

/** Safely encode an asset path that may contain spaces or parentheses. */
export function assetUrl(path: string): string {
  // Encode each segment but keep slashes intact.
  return path
    .split('/')
    .map((seg, i) => (i === 0 ? seg : encodeURIComponent(seg)))
    .join('/');
}

export const NAV_ITEMS = [
  { id: 'skills', label: 'Skills' },
  { id: 'education', label: 'Education' },
  { id: 'experience', label: 'Experience' },
  { id: 'projects', label: 'Projects' },
  { id: 'hackathons', label: 'Hackathons' },
  { id: 'certificates', label: 'Certs' },
  { id: 'languages', label: 'Languages' },
  { id: 'contact', label: 'Contact' },
] as const;

/**
 * Editorial number shown in a section header ("N°04"), derived from NAV_ITEMS
 * so the sequence follows page order instead of drifting when sections move.
 */
export function sectionIndex(id: string): string {
  const at = NAV_ITEMS.findIndex((item) => item.id === id);
  return String(at + 1).padStart(2, '0');
}
