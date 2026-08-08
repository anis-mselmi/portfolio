import { useState } from 'react';
import { motion } from 'framer-motion';
import { Mail, Phone, MapPin, Linkedin, Github } from 'lucide-react';
import { PROFILE } from '../data/content';
import { SectionHeader } from '../components/SectionHeader';
import { sendEmail, buildMailto, emailConfigured, type ContactPayload } from '../lib/email';

type Status = 'idle' | 'sending' | 'sent' | 'fallback' | 'error';
const empty: ContactPayload = { name: '', email: '', subject: '', message: '' };

const DIRECTORY = [
  { icon: Mail, label: 'Email', value: PROFILE.email, href: `mailto:${PROFILE.email}` },
  { icon: Phone, label: 'Telephone', value: PROFILE.phone },
  { icon: MapPin, label: 'Bureau', value: PROFILE.location },
  { icon: Linkedin, label: 'LinkedIn', value: 'Anis Mselmi', href: PROFILE.linkedin },
  { icon: Github, label: 'GitHub', value: '@anis-mselmi', href: PROFILE.github },
];

export function Contact() {
  const [form, setForm] = useState<ContactPayload>(empty);
  const [status, setStatus] = useState<Status>('idle');
  const [error, setError] = useState('');

  const set = (k: keyof ContactPayload) => (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) =>
    setForm((f) => ({ ...f, [k]: e.target.value }));

  const submit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!form.name.trim() || !form.email.trim() || !form.message.trim()) {
      setStatus('error');
      setError('Kindly complete Name, Email, and Message.');
      return;
    }
    setStatus('sending');
    setError('');
    if (!emailConfigured) {
      window.location.href = buildMailto(form);
      setStatus('fallback');
      return;
    }
    try {
      await sendEmail(form);
      setStatus('sent');
      setForm(empty);
    } catch {
      window.location.href = buildMailto(form);
      setStatus('fallback');
    }
  };

  const inputCls =
    'w-full border border-ink bg-paper px-3 py-2.5 font-sans text-sm text-ink outline-none transition-colors placeholder:text-muted focus:bg-white focus:ring-2 focus:ring-accent';

  return (
    <section id="contact" className="section">
      <div className="shell">
        <SectionHeader
          index="08"
          title="Letters to the Editor"
          standfirst="Have a proposal, a role, or a question? Send word — replies are prompt."
        />

        <div className="grid gap-8 lg:grid-cols-[1.3fr_1fr]">
          {/* Correspondence form */}
          <form onSubmit={submit} className="print-card p-6 sm:p-8">
            <div className="grid gap-4 sm:grid-cols-2">
              <label className="block">
                <span className="meta">Your Name</span>
                <input className={inputCls} value={form.name} onChange={set('name')} placeholder="Jane Doe" />
              </label>
              <label className="block">
                <span className="meta">Your Email</span>
                <input className={inputCls} type="email" value={form.email} onChange={set('email')} placeholder="jane@example.com" />
              </label>
            </div>
            <label className="mt-4 block">
              <span className="meta">Subject</span>
              <input className={inputCls} value={form.subject} onChange={set('subject')} placeholder="A proposal…" />
            </label>
            <label className="mt-4 block">
              <span className="meta">Message</span>
              <textarea className={inputCls} rows={6} value={form.message} onChange={set('message')} placeholder="Dear Anis,…" />
            </label>

            <button type="submit" disabled={status === 'sending'} className="btn btn-accent mt-5 w-full justify-center disabled:opacity-60">
              {status === 'sending' ? 'Dispatching…' : 'Send Correspondence ▸'}
            </button>

            {status === 'sent' && (
              <p className="mt-4 border-l-4 border-accent bg-card px-4 py-3 text-sm">
                <strong>Received.</strong> Thank you — a reply is on its way.
              </p>
            )}
            {status === 'fallback' && (
              <p className="mt-4 border-l-4 border-ink bg-card px-4 py-3 text-sm">
                Your mail client should have opened. If not, write to{' '}
                <a href={`mailto:${PROFILE.email}`} className="link-underline text-accent-deep">{PROFILE.email}</a>.
              </p>
            )}
            {status === 'error' && (
              <p className="mt-4 border-l-4 border-accent bg-card px-4 py-3 text-sm text-accent-deep">{error}</p>
            )}
          </form>

          {/* Directory */}
          <div>
            <div className="meta mb-3 border-b-2 border-ink pb-2">Directory</div>
            <div className="divide-y divide-ink/20 border border-ink">
              {DIRECTORY.map((row) => {
                const Icon = row.icon;
                const content = (
                  <div className="group flex items-center gap-3 px-4 py-3 transition-colors hover:bg-card">
                    <Icon size={16} className="shrink-0 text-accent" />
                    <div className="min-w-0">
                      <div className="meta">{row.label}</div>
                      <div className="truncate text-sm font-medium">{row.value}</div>
                    </div>
                  </div>
                );
                return row.href ? (
                  <a key={row.label} href={row.href} target={row.href.startsWith('http') ? '_blank' : undefined} rel="noreferrer" className="block">
                    {content}
                  </a>
                ) : (
                  <div key={row.label}>{content}</div>
                );
              })}
            </div>
            <motion.p
              initial={{ opacity: 0 }}
              whileInView={{ opacity: 1 }}
              viewport={{ once: true }}
              className="lede mt-6 italic"
            >
              “Turning complex ideas into reliable systems, one build at a time.”
            </motion.p>
          </div>
        </div>
      </div>
    </section>
  );
}
