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
  { id: 'certificates', label: 'Certs' },
  { id: 'projects', label: 'Projects' },
  { id: 'hackathons', label: 'Hackathons' },
  { id: 'languages', label: 'Languages' },
  { id: 'contact', label: 'Contact' },
] as const;
