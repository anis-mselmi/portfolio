import type {
  Profile,
  AboutItem,
  EducationItem,
  Skill,
  Project,
  Language,
  Certificate,
  Hackathon,
  ExperienceItem,
  VolunteerItem,
} from './types';

export const PROFILE: Profile = {
  name: 'Anis Mselmi',
  role: 'Java Developer | AI Engineering Student | AI, DevOps, RAG & LLM Enthusiast',
  location: 'Khzema Ouest, Sousse, Tunisia',
  email: 'anismselmi490@gmail.com',
  phone: '+216 25 141 636',
  github: 'https://github.com/anis-mselmi',
  linkedin: 'https://www.linkedin.com/in/anis-mselmi-441b39326/',
  x: 'https://x.com/anismsalmi',
  // Read-only Google Drive view link. Edit the Doc in place — the link stays the same.
  cv: 'https://docs.google.com/document/d/1xWY5GQe9aXmcVKnHEvEuuF1BacYiZBB_nB13NWiQdlg/preview',
};

export const ROLE_WORDS = [
  'Java Developer',
  'AI Builder',
  'RAG & LLM Engineer',
  'DevOps Enthusiast',
  'AI Engineering Student',
];

export const ABOUT: AboutItem[] = [
  {
    emoji: '☕',
    title: 'Java Developer',
    text: 'Passionate about building robust backend services, scalable applications, and object-oriented solutions.',
  },
  {
    emoji: '🧠',
    title: 'AI Engineering Student',
    text: 'At École Polytechnique de Sousse, focused on AI, DevOps, machine learning, and LLMs.',
  },
  {
    emoji: '⚡',
    title: 'AI Builder',
    text: 'Turning complex ideas into reliable AI systems by building intelligent Python models, RAG pipelines, and conversational agents.',
  },
  {
    emoji: '🐳',
    title: 'DevOps & Automation',
    text: 'Hands-on with Docker containerization, configuring automated CI/CD pipelines, and streamlining deployment workflows.',
  },
  {
    emoji: '🛠️',
    title: 'Infrastructure & Git',
    text: 'Proficient in Linux system administration, advanced Git collaboration workflows, and shell scripting.',
  },
  {
    emoji: '📜',
    title: 'NVIDIA Certified',
    text: 'Specialized credentials in advanced Deep Learning, RAG Agent architectures, and Prompt Engineering.',
  },
  {
    emoji: '🌐',
    title: 'IEEE Congresses',
    text: 'Attended multiple events including CSTAM 1.0, SDC 3.0, WIE ACT 4.0, and TSYP 13.',
  },
  {
    emoji: '🌍',
    title: 'Driven & Hands-on',
    text: 'Experienced with Jupyter/Colab workflows, data visualization, and rapid experimentation with a builder’s mindset.',
  },
];

export const EDUCATION: EducationItem[] = [
  {
    title: 'AI Engineering Student',
    school: 'École Polytechnique de Sousse',
    years: '2025 – 2028',
    detail:
      'Focused on Artificial Intelligence, Machine Learning, and Large Language Models (LLMs). Hands-on building intelligent Python models, RAG pipelines, and conversational agents.',
    icon: 'cpu',
  },
  {
    title: 'Integrated Preparatory Studies',
    school: 'École Polytechnique de Sousse',
    years: '2023 – 2025',
    detail:
      'Underwent rigorous training in Mathematics, Physics, and foundational engineering principles to develop strong Analytical and Problem-Solving capabilities.',
    icon: 'compass',
  },
  {
    title: 'High School Diploma (Baccalauréat)',
    school: 'Lycée Les Lumières Sousse',
    years: '2022 – 2023',
    detail:
      'Completed secondary education with a science-focused curriculum, establishing a solid foundation in Mathematics and Sciences.',
    icon: 'cap',
  },
];

// Professional experience. NOTE: fill in the exact FleetPOS stack
// (language / database) and any impact metrics (terminals, sync frequency)
// where marked — kept honest rather than invented.
export const WORK_EXPERIENCE: ExperienceItem[] = [
  {
    role: 'Summer Intern',
    org: 'Digicoser',
    period: 'Jul 2026 – Sep 2026',
    points: [
      'Engineered an idempotent synchronization pipeline from MaxStore to FleetPOS, guaranteeing replay-safe, consistent data transfer.',
      'Consumed and exposed REST APIs with retry and exponential back-off for resilient, fault-tolerant integration.',
      'Containerized the services with Docker for reproducible builds and streamlined deployment.',
    ],
    tags: ['Docker', 'REST API', 'Data Sync', 'Integration'],
  },
  {
    role: 'Summer Intern',
    org: 'Verdanova Solutions',
    period: 'Jun 2026 – Sep 2026',
    points: [
      'Design and build AI features across the stack — from data preparation to model integration.',
      'Apply LLM and RAG techniques to turn business requirements into reliable, knowledge-grounded systems.',
    ],
    tags: ['AI', 'LLMs', 'RAG', 'Python'],
  },
];

// Volunteering / Bénévolat — IEEE-focused. Descriptions kept minimal
// where none were provided; add a one-line impact per role to strengthen.
export const VOLUNTEERING: VolunteerItem[] = [
  { role: 'Member', org: 'IEEE Tunisia Section', period: '2023 – Present' },
  { role: 'Ambassador — Smart Cities', org: 'IEEE' },
  { role: 'Ambassador — YESIST12', org: 'IEEE' },
  { role: 'Webmaster', org: 'IEEE SIGHT EPS SB' },
  { role: 'Ambassador', org: 'ATIC' },
  { role: 'Member', org: 'ACPC' },
];

export const SKILLS_BY_CATEGORY: Record<string, Skill[]> = {
  'AI & Machine Learning': [
    {
      icon: 'bot',
      name: 'Machine Learning',
      level: 'Advanced',
      subtitle: 'Model training, evaluation, deployment',
      tags: ['scikit-learn', 'feature engineering', 'pipelines'],
      details: 'Production-oriented supervised and unsupervised model building.',
      tone: 'blue',
    },
    {
      icon: 'brain',
      name: 'Deep Learning',
      level: 'Intermediate',
      subtitle: 'Neural architectures and optimization',
      tags: ['CNN', 'transformers', 'fine-tuning'],
      details: 'Focused on practical DL experiments and model iteration.',
      tone: 'blue',
    },
    {
      icon: 'layers',
      name: 'RAG Pipelines',
      level: 'Advanced',
      subtitle: 'Retrieval + generation system design',
      tags: ['vector DB', 'chunking', 'reranking'],
      details: 'Builds robust knowledge-grounded assistants with retrieval chains.',
      tone: 'red',
    },
  ],
  Programming: [
    {
      icon: 'code',
      name: 'Python',
      level: 'Expert',
      subtitle: 'Core language for AI and automation',
      tags: ['clean code', 'APIs', 'scripting'],
      details: 'Primary stack for AI products, experimentation, and tooling.',
      tone: 'blue',
    },
    {
      icon: 'coffee',
      name: 'Java',
      level: 'Advanced',
      subtitle: 'Robust backend & OOP concepts',
      tags: ['OOP', 'Spring Boot', 'multi-threading'],
      details:
        'Proficient in building secure, scalable applications and microservices using Java.',
      tone: 'red',
    },
    {
      icon: 'notebook',
      name: 'Jupyter Notebook',
      level: 'Advanced',
      subtitle: 'Experiment-first development workflow',
      tags: ['EDA', 'prototyping', 'visual insight'],
      details: 'Fast iteration environment for data and model experiments.',
      tone: 'blue',
    },
  ],
  'Data & Analytics': [
    {
      icon: 'bar-chart',
      name: 'Data Analysis',
      level: 'Advanced',
      subtitle: 'Insight extraction from raw datasets',
      tags: ['cleaning', 'profiling', 'statistics'],
      details: 'Transforms noisy data into actionable information.',
      tone: 'blue',
    },
    {
      icon: 'line-chart',
      name: 'Data Visualization',
      level: 'Advanced',
      subtitle: 'Narrative dashboards and reporting',
      tags: ['charts', 'storytelling', 'KPIs'],
      details: 'Builds visuals that communicate decisions clearly.',
      tone: 'red',
    },
    {
      icon: 'flask',
      name: 'Experiment Tracking',
      level: 'Intermediate',
      subtitle: 'Metrics, iteration and model comparison',
      tags: ['versioning', 'benchmarks', 'ablation'],
      details: 'Keeps model experiments measurable and reproducible.',
      tone: 'blue',
    },
  ],
  'Tools & Platforms': [
    {
      icon: 'git',
      name: 'Git',
      level: 'Advanced',
      subtitle: 'Version control and clean collaboration',
      tags: ['branching', 'history', 'workflow'],
      details: 'Maintains clean commit strategy and collaboration standards.',
      tone: 'red',
    },
    {
      icon: 'github',
      name: 'GitHub',
      level: 'Advanced',
      subtitle: 'Repo management and project delivery',
      tags: ['PRs', 'issues', 'CI-ready'],
      details: 'Organizes portfolio projects with professional structure.',
      tone: 'blue',
    },
    {
      icon: 'orbit',
      name: 'Antigravity',
      level: 'Expert',
      subtitle: 'AI-assisted agentic workflow',
      tags: ['AI agent', 'pair-programming', 'productivity'],
      details: 'Primary environment for rapid, autonomous, and collaborative coding.',
      tone: 'blue',
    },
  ],
};

export const PROJECTS: Project[] = [
  {
    name: 'SmartPark',
    desc: 'Automates parking access by scanning car license plates.',
    tags: ['AI', 'Computer Vision', 'ALPR'],
    image: '/assets/images/projects/smartpark.webp',
    fit: 'cover',
    link: 'https://github.com/anis-mselmi/SmartParkTN-D-tection-automatique-des-plaques-tunisiennes-ALPR-pour-parking',
  },
  {
    name: 'PrepAI-TN',
    desc: 'AI corrector for the Tunisian prépa concours — upload an épreuve and get a written corrigé, or just ask.',
    tags: ['Python', 'LLM', 'Hugging Face', 'LoRA'],
    image: '/assets/images/projects/prepai-tn.png',
    fit: 'cover',
    link: 'https://github.com/anis-mselmi/PrepAI-TN',
  },
  {
    name: 'CertTrack',
    desc: 'A Spring Boot app for managing professional certifications.',
    tags: ['Java', 'Spring Boot', 'REST API'],
    image: '/assets/images/projects/java-web-app.png',
    fit: 'cover',
    link: 'https://github.com/anis-mselmi/CertTrack',
  },
];

export const LANGUAGES: Language[] = [
  {
    name: 'Arabic',
    flagSrc: 'https://flagcdn.com/w80/sa.png',
    flagAlt: 'Saudi Arabia flag',
    badge: 'Native',
    detail: 'Native / Fluent communication across personal, academic, and team environments.',
    tone: 'arabic',
  },
  {
    name: 'English',
    flagSrc: 'https://flagcdn.com/w80/us.png',
    flagAlt: 'United States flag',
    badge: 'Professional',
    detail: 'Professional proficiency for technical writing, collaboration, and presentations.',
    tone: 'english',
  },
  {
    name: 'French',
    flagSrc: 'https://flagcdn.com/w80/fr.png',
    flagAlt: 'France flag',
    badge: 'Professional',
    detail: 'Professional proficiency for communication, documentation, and everyday teamwork.',
    tone: 'french',
  },
];

export const NVIDIA_CERTIFICATES: Certificate[] = [
  {
    title: 'Building RAG Agents with LLMs',
    id: '7vo8r-_oQv2bJTyHff6CDQ',
    url: 'https://learn.nvidia.com/certificates?id=7vo8r-_oQv2bJTyHff6CDQ',
    date: 'Sep 2025',
    skills: ['RAG', 'LLM Agents', 'Vector Databases', 'LangChain'],
  },
  {
    title: 'Introduction to Transformer-Based Natural Language Processing',
    id: 'Yy6SLV7eT4eN7Ll-txHLBQ',
    url: 'https://learn.nvidia.com/certificates?id=Yy6SLV7eT4eN7Ll-txHLBQ',
    date: 'Sep 2025',
    skills: ['Transformers', 'NLP', 'BERT', 'GPT Architecture'],
  },
  {
    title: 'Building LLM Applications With Prompt Engineering',
    id: 'iagFYqO4QJmdv4JJU6g_sw',
    url: 'https://learn.nvidia.com/certificates?id=iagFYqO4QJmdv4JJU6g_sw',
    date: 'Sep 2025',
    skills: ['Prompt Engineering', 'LLM Integration', 'System Prompts'],
  },
  {
    title: 'Building AI-Based Cybersecurity Pipelines',
    id: 'As48ycFRRMqT0VKVb4PbtA',
    url: 'https://learn.nvidia.com/certificates?id=As48ycFRRMqT0VKVb4PbtA',
    date: 'Apr 2025',
    skills: ['Cybersecurity', 'AI Pipelines', 'Anomaly Detection'],
  },
  {
    title: 'Fundamentals of Deep Learning',
    id: '4C-6f4fjSHK2HcgQfx6_ZA',
    url: 'https://learn.nvidia.com/certificates?id=4C-6f4fjSHK2HcgQfx6_ZA',
    date: 'Sep 2025',
    skills: ['Deep Learning', 'Neural Networks', 'Computer Vision', 'PyTorch'],
  },
  {
    title: 'Generative AI with Diffusion Models',
    id: 'fn3bEZHDTHCZATWKG-svvg',
    url: 'https://learn.nvidia.com/certificates?id=fn3bEZHDTHCZATWKG-svvg',
    date: 'Nov 2025',
    skills: ['Diffusion Models', 'Generative AI', 'Denoising', 'Image Generation'],
  },
  {
    title: 'Building Real-Time Video AI Applications',
    id: 'DttLN2ikRJeNMkkh7euKHA',
    url: 'https://learn.nvidia.com/certificates?id=DttLN2ikRJeNMkkh7euKHA',
    date: 'Dec 2025',
    skills: ['DeepStream', 'Video AI', 'Intelligent Video Analytics', 'IVA'],
  },
  {
    title: 'Fundamentals of Accelerated Computing with CUDA Python',
    id: 't-mYwSVhRC2Ve6K0z1qflQ',
    url: 'https://learn.nvidia.com/certificates?id=t-mYwSVhRC2Ve6K0z1qflQ',
    date: 'Dec 2025',
    skills: ['CUDA Python', 'GPU Acceleration', 'Numba', 'Parallel Computing'],
  },
];

export const HACKATHONS: Hackathon[] = [
  {
    title: 'AURA 1.0 congress',
    image: '/assets/images/hackathons/1762176420191.jpg',
    badge: '1st Place',
    desc: 'Designed and programmed an autonomous robot to navigate complex mazes under tight time constraints.',
    tags: ['Java', 'Robotics', 'Arduino', 'Embedded Systems'],
  },
  {
    title: '𝐀𝐈 𝐂𝐚𝐦𝐞𝐫𝐚 𝐂𝐡𝐚𝐥𝐥𝐞𝐧𝐠𝐞 𝟐𝟎𝟐𝟓',
    image: '/assets/images/hackathons/1765102509130.jpg',
    badge: 'Best Innovation',
    desc: 'Built a real-time smart parking locator app to reduce traffic congestion in urban areas.',
    tags: ['Python', 'Computer Vision', 'IoT', 'Flask'],
  },
  {
    title: 'Space Hack competetion',
    image: '/assets/images/hackathons/1765725484606.jpg',
    badge: '1st Place',
    desc: 'Developed a predictive model to forecast energy consumption using historical weather data.',
    tags: ['Machine Learning', 'PyTorch', 'Pandas', 'scikit-learn'],
  },
  {
    title: 'IEEE Congress Challenge',
    image: '/assets/images/hackathons/1765748484658.jpg',
    badge: 'Special Prize',
    desc: 'Built a full-stack app to help women in agriculture in Tunisia during the IEEE WIE ACT 4.0.',
    tags: ['Blockchain', 'Solidity', 'React', 'Node.js'],
  },
  {
    title: 'WIE Wave 2.0',
    image: '/assets/images/hackathons/wie-wave-2.jpg',
    fit: 'contain',
    badge: '1st Place',
    desc: 'Won first place in the ideathon with team MindMakers at the IEEE WIE Wave 2.0 event.',
    tags: ['Ideathon', 'Pitching', 'Innovation', 'Team Work'],
  },
  {
    title: 'ideathon 4.0',
    image: '/assets/images/hackathons/ideathon.jpg',
    badge: '6th Place',
    desc: 'Led a team of 4 to build an automated sorting machine prototype, winning the overall competition.',
    tags: ['Python', 'Computer Vision', 'Hardware', 'Team Lead'],
  },
];

export const SOFT_SKILLS: string[] = ['Communication', 'Teamwork', 'Project Management', 'Organization'];
export const INTERESTS: string[] = ['Travelling', 'Sports', 'Reading'];

export const CERT_PROVIDERS = [
  { key: 'nvidia', label: 'NVIDIA', color: '#76b900', data: NVIDIA_CERTIFICATES },
] as const;
