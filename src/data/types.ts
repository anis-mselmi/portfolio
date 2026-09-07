export type SkillLevel = 'Expert' | 'Advanced' | 'Intermediate' | 'Beginner';
export type Tone = 'blue' | 'red';

export interface Profile {
  name: string;
  role: string;
  location: string;
  email: string;
  phone: string;
  github: string;
  linkedin: string;
  x: string;
  cv: string;
}

export interface AboutItem {
  emoji: string;
  title: string;
  text: string;
}

export interface EducationItem {
  title: string;
  school: string;
  years: string;
  detail: string;
  icon: string;
}

export interface Skill {
  icon: string;
  name: string;
  level: SkillLevel;
  subtitle: string;
  tags: string[];
  details: string;
  tone: Tone;
}

export interface Project {
  name: string;
  desc: string;
  tags: string[];
  image: string;
  fit?: 'cover' | 'contain';
  link?: string;
}

export interface Language {
  name: string;
  flagSrc: string;
  flagAlt: string;
  badge: string;
  detail: string;
  tone: 'arabic' | 'english' | 'french';
}

export interface Certificate {
  title: string;
  id: string;
  url: string;
  date: string;
  skills: string[];
}

export interface ExperienceItem {
  role: string;
  org: string;
  period: string;
  location?: string;
  points: string[];
  tags?: string[];
}

export interface VolunteerItem {
  role: string;
  org: string;
  period?: string;
  detail?: string;
}

export interface Hackathon {
  title: string;
  image: string;
  badge: string;
  desc: string;
  tags: string[];
  /** CSS object-position for the cover image, e.g. 'top' or 'center 30%'. Defaults to center. */
  pos?: string;
  /** 'contain' shows the whole image over a blurred backdrop — for portrait posters. */
  fit?: 'cover' | 'contain';
}
