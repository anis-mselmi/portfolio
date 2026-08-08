import emailjs from '@emailjs/browser';
import { PROFILE } from '../data/content';

const SERVICE_ID = import.meta.env.VITE_EMAILJS_SERVICE_ID;
const TEMPLATE_ID = import.meta.env.VITE_EMAILJS_TEMPLATE_ID;
const PUBLIC_KEY = import.meta.env.VITE_EMAILJS_PUBLIC_KEY;

export const emailConfigured = Boolean(SERVICE_ID && TEMPLATE_ID && PUBLIC_KEY);

export interface ContactPayload {
  name: string;
  email: string;
  subject: string;
  message: string;
}

/** Send via EmailJS. Throws on failure so the caller can fall back to mailto. */
export async function sendEmail(payload: ContactPayload): Promise<void> {
  if (!emailConfigured) throw new Error('EmailJS not configured');
  await emailjs.send(
    SERVICE_ID!,
    TEMPLATE_ID!,
    {
      from_name: payload.name,
      reply_to: payload.email,
      subject: payload.subject || 'Portfolio Contact',
      message: payload.message,
      to_email: PROFILE.email,
    },
    { publicKey: PUBLIC_KEY! }
  );
}

/** Build a mailto: URL pre-filled with the form contents. */
export function buildMailto({ name, email, subject, message }: ContactPayload): string {
  const body = `Name: ${name}\nEmail: ${email}\n\nMessage:\n${message}`;
  const params = new URLSearchParams({
    subject: subject || 'Portfolio Contact',
    body,
  });
  return `mailto:${PROFILE.email}?${params.toString()}`;
}
