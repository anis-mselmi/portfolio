import { useState } from 'react';
import { sectionIndex } from '../lib/utils';
import { motion } from 'framer-motion';
import { Mail, Phone, MapPin, Linkedin, Github } from 'lucide-react';
import { PROFILE } from '../data/content';
import { SectionHeader } from '../components/SectionHeader';
import { sendEmail, buildMailto, emailConfigured, type ContactPayload } from '../lib/email';
import { useContent } from '../i18n/content';

type Status = 'idle' | 'sending' | 'sent' | 'fallback' | 'error';
const empty: ContactPayload = { name: '', email: '', subject: '', message: '' };

export function Contact() {
  const { ui } = useContent();
  const [form, setForm] = useState<ContactPayload>(empty);
  const [status, setStatus] = useState<Status>('idle');
  const [error, setError] = useState('');

  const directory = [
    { icon: Mail, label: ui.contact.dirEmail, value: PROFILE.email, href: `mailto:${PROFILE.email}` },
    { icon: Phone, label: ui.contact.dirPhone, value: PROFILE.phone },
    { icon: MapPin, label: ui.contact.dirOffice, value: PROFILE.location },
    { icon: Linkedin, label: 'LinkedIn', value: 'Anis Mselmi', href: PROFILE.linkedin },
    { icon: Github, label: 'GitHub', value: '@anis-mselmi', href: PROFILE.github },
  ];

  const set = (k: keyof ContactPayload) => (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) =>
    setForm((f) => ({ ...f, [k]: e.target.value }));

  const submit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!form.name.trim() || !form.email.trim() || !form.message.trim()) {
      setStatus('error');
      setError(ui.contact.validation);
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
          index={sectionIndex('contact')}
          title={ui.sections.contact.title}
          standfirst={ui.sections.contact.standfirst}
        />

        <div className="grid gap-8 lg:grid-cols-[1.3fr_1fr]">
          {/* Correspondence form */}
          <form onSubmit={submit} className="print-card p-6 sm:p-8">
            <div className="grid gap-4 sm:grid-cols-2">
              <label className="block">
                <span className="meta">{ui.contact.nameLabel}</span>
                <input className={inputCls} value={form.name} onChange={set('name')} placeholder={ui.contact.namePlaceholder} />
              </label>
              <label className="block">
                <span className="meta">{ui.contact.emailLabel}</span>
                <input className={inputCls} type="email" value={form.email} onChange={set('email')} placeholder={ui.contact.emailPlaceholder} />
              </label>
            </div>
            <label className="mt-4 block">
              <span className="meta">{ui.contact.subjectLabel}</span>
              <input className={inputCls} value={form.subject} onChange={set('subject')} placeholder={ui.contact.subjectPlaceholder} />
            </label>
            <label className="mt-4 block">
              <span className="meta">{ui.contact.messageLabel}</span>
              <textarea className={inputCls} rows={6} value={form.message} onChange={set('message')} placeholder={ui.contact.messagePlaceholder} />
            </label>

            <button type="submit" disabled={status === 'sending'} className="btn btn-accent mt-5 w-full justify-center disabled:opacity-60">
              {status === 'sending' ? ui.contact.sending : ui.contact.send}
            </button>

            {status === 'sent' && (
              <p className="mt-4 border-l-4 border-accent bg-card px-4 py-3 text-sm">
                <strong>{ui.contact.sentStrong}</strong>{ui.contact.sentText}
              </p>
            )}
            {status === 'fallback' && (
              <p className="mt-4 border-l-4 border-ink bg-card px-4 py-3 text-sm">
                {ui.contact.fallback}
                <a href={`mailto:${PROFILE.email}`} className="link-underline text-accent-deep">{PROFILE.email}</a>.
              </p>
            )}
            {status === 'error' && (
              <p className="mt-4 border-l-4 border-accent bg-card px-4 py-3 text-sm text-accent-deep">{error}</p>
            )}
          </form>

          {/* Directory */}
          <div>
            <div className="meta mb-3 border-b-2 border-ink pb-2">{ui.contact.directory}</div>
            <div className="divide-y divide-ink/20 border border-ink">
              {directory.map((row) => {
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
                  <a key={row.label} href={row.href} target={/^https?:|\.html$/.test(row.href) ? '_blank' : undefined} rel="noreferrer" className="block">
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
              {ui.contact.quote}
            </motion.p>
          </div>
        </div>
      </div>
    </section>
  );
}
