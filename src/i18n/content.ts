import { useMemo } from 'react';
import type {
  AboutItem,
  EducationItem,
  Skill,
  Project,
  Language,
  Hackathon,
  ExperienceItem,
  VolunteerItem,
} from '../data/types';
import { useLang, type Lang } from './LanguageContext';

/**
 * Localized content + UI strings. Structural / technical fields (icons, tags,
 * flags, URLs, proper nouns, skill `level` keys) are written once; only human
 * copy differs between English and French via the `t(en, fr)` helper.
 */
function buildBundle(lang: Lang) {
  const t = <T,>(en: T, fr: T): T => (lang === 'fr' ? fr : en);

  const about: AboutItem[] = [
    {
      emoji: '☕',
      title: t('Java Developer', 'Développeur Java'),
      text: t(
        'Passionate about building robust backend services, scalable applications, and object-oriented solutions.',
        "Passionné par la création de services back-end robustes, d'applications évolutives et de solutions orientées objet."
      ),
    },
    {
      emoji: '🧠',
      title: t('AI Engineering Student', 'Étudiant en ingénierie IA'),
      text: t(
        'At École Polytechnique de Sousse, focused on AI, DevOps, machine learning, and LLMs.',
        "À l'École Polytechnique de Sousse, spécialisé en IA, DevOps, apprentissage automatique et LLM."
      ),
    },
    {
      emoji: '⚡',
      title: t('AI Builder', "Créateur d'IA"),
      text: t(
        'Turning complex ideas into reliable AI systems by building intelligent Python models, RAG pipelines, and conversational agents.',
        "Transformer des idées complexes en systèmes d'IA fiables en construisant des modèles Python intelligents, des pipelines RAG et des agents conversationnels."
      ),
    },
    {
      emoji: '🐳',
      title: t('DevOps & Automation', 'DevOps & Automatisation'),
      text: t(
        'Hands-on with Docker containerization, configuring automated CI/CD pipelines, and streamlining deployment workflows.',
        "Expérience pratique de la conteneurisation Docker, de la configuration de pipelines CI/CD automatisés et de l'optimisation des déploiements."
      ),
    },
    {
      emoji: '🛠️',
      title: t('Infrastructure & Git', 'Infrastructure & Git'),
      text: t(
        'Proficient in Linux system administration, advanced Git collaboration workflows, and shell scripting.',
        "Maîtrise de l'administration système Linux, des workflows Git collaboratifs avancés et du scripting shell."
      ),
    },
    {
      emoji: '📜',
      title: t('NVIDIA Certified', 'Certifié NVIDIA'),
      text: t(
        'Specialized credentials in advanced Deep Learning, RAG Agent architectures, and Prompt Engineering.',
        "Certifications spécialisées en Deep Learning avancé, architectures d'agents RAG et Prompt Engineering."
      ),
    },
    {
      emoji: '🌐',
      title: t('IEEE Congresses', 'Congrès IEEE'),
      text: t(
        'Attended multiple events including CSTAM 1.0, SDC 3.0, WIE ACT 4.0, and TSYP 13.',
        'Participation à plusieurs événements dont CSTAM 1.0, SDC 3.0, WIE ACT 4.0 et TSYP 13.'
      ),
    },
    {
      emoji: '🌍',
      title: t('Driven & Hands-on', 'Motivé & Opérationnel'),
      text: t(
        'Experienced with Jupyter/Colab workflows, data visualization, and rapid experimentation with a builder’s mindset.',
        "Expérimenté avec les workflows Jupyter/Colab, la visualisation de données et l'expérimentation rapide, avec un esprit de bâtisseur."
      ),
    },
  ];

  const education: EducationItem[] = [
    {
      title: t('AI Engineering Student', 'Étudiant en ingénierie IA'),
      school: 'École Polytechnique de Sousse',
      years: '2025 – 2028',
      detail: t(
        'Focused on Artificial Intelligence, Machine Learning, and Large Language Models (LLMs). Hands-on building intelligent Python models, RAG pipelines, and conversational agents.',
        "Spécialisé en intelligence artificielle, apprentissage automatique et grands modèles de langage (LLM). Construction pratique de modèles Python intelligents, de pipelines RAG et d'agents conversationnels."
      ),
      icon: 'cpu',
    },
    {
      title: t('Integrated Preparatory Studies', 'Cycle préparatoire intégré'),
      school: 'École Polytechnique de Sousse',
      years: '2023 – 2025',
      detail: t(
        'Underwent rigorous training in Mathematics, Physics, and foundational engineering principles to develop strong Analytical and Problem-Solving capabilities.',
        "Formation rigoureuse en mathématiques, physique et principes fondamentaux de l'ingénierie afin de développer de solides capacités d'analyse et de résolution de problèmes."
      ),
      icon: 'compass',
    },
    {
      title: t('High School Diploma (Baccalauréat)', 'Baccalauréat'),
      school: 'Lycée Les Lumières Sousse',
      years: '2022 – 2023',
      detail: t(
        'Completed secondary education with a science-focused curriculum, establishing a solid foundation in Mathematics and Sciences.',
        'Études secondaires achevées avec un cursus scientifique, établissant des bases solides en mathématiques et en sciences.'
      ),
      icon: 'cap',
    },
  ];

  const work: ExperienceItem[] = [
    {
      role: t('Summer Intern', "Stagiaire d'été"),
      org: 'Digicoser',
      period: t('Jul 2026 – Sep 2026', 'Juil. 2026 – Sept. 2026'),
      points: [
        t(
          'Engineered an idempotent synchronization pipeline from MaxStore to FleetPOS, guaranteeing replay-safe, consistent data transfer.',
          "Conception d'un pipeline de synchronisation idempotent de MaxStore vers FleetPOS, garantissant un transfert de données cohérent et rejouable en toute sécurité."
        ),
        t(
          'Consumed and exposed REST APIs with retry and exponential back-off for resilient, fault-tolerant integration.',
          "Consommation et exposition d'API REST avec relance et back-off exponentiel pour une intégration résiliente et tolérante aux pannes."
        ),
        t(
          'Containerized the services with Docker for reproducible builds and streamlined deployment.',
          'Conteneurisation des services avec Docker pour des builds reproductibles et un déploiement simplifié.'
        ),
      ],
      tags: ['Docker', 'REST API', 'Data Sync', 'Integration'],
    },
    {
      role: t('Summer Intern', 'Stagiaire d’été'),
      org: 'Verdanova Solutions',
      period: t('Jun 2026 – Sep 2026', 'Juin 2026 – Sept. 2026'),
      points: [
        t(
          'Design and build AI features across the stack — from data preparation to model integration.',
          "Conception et développement de fonctionnalités d'IA sur toute la chaîne — de la préparation des données à l'intégration des modèles."
        ),
        t(
          'Apply LLM and RAG techniques to turn business requirements into reliable, knowledge-grounded systems.',
          'Application des techniques LLM et RAG pour transformer les besoins métier en systèmes fiables et ancrés dans la connaissance.'
        ),
      ],
      tags: ['AI', 'LLMs', 'RAG', 'Python'],
    },
  ];

  const volunteering: VolunteerItem[] = [
    { role: t('Member', 'Membre'), org: 'IEEE Tunisia Section', period: t('2023 – Present', '2023 – Présent') },
    { role: t('Ambassador — Smart Cities', 'Ambassadeur — Smart Cities'), org: 'IEEE' },
    { role: t('Ambassador — YESIST12', 'Ambassadeur — YESIST12'), org: 'IEEE' },
    { role: 'Webmaster', org: 'IEEE SIGHT EPS SB' },
    { role: t('Ambassador', 'Ambassadeur'), org: 'ATIC' },
    { role: t('Member', 'Membre'), org: 'ACPC' },
  ];

  const skillsByCategory: Record<string, Skill[]> = {
    [t('AI & Machine Learning', 'IA & Apprentissage automatique')]: [
      {
        icon: 'bot',
        name: 'Machine Learning',
        level: 'Advanced',
        subtitle: t('Model training, evaluation, deployment', 'Entraînement, évaluation et déploiement de modèles'),
        tags: ['scikit-learn', 'feature engineering', 'pipelines'],
        details: '',
        tone: 'blue',
      },
      {
        icon: 'brain',
        name: 'Deep Learning',
        level: 'Intermediate',
        subtitle: t('Neural architectures and optimization', 'Architectures neuronales et optimisation'),
        tags: ['CNN', 'transformers', 'fine-tuning'],
        details: '',
        tone: 'blue',
      },
      {
        icon: 'layers',
        name: 'RAG Pipelines',
        level: 'Advanced',
        subtitle: t('Retrieval + generation system design', 'Conception de systèmes de récupération + génération'),
        tags: ['vector DB', 'chunking', 'reranking'],
        details: '',
        tone: 'red',
      },
    ],
    [t('Programming', 'Programmation')]: [
      {
        icon: 'code',
        name: 'Python',
        level: 'Expert',
        subtitle: t('Core language for AI and automation', "Langage principal pour l'IA et l'automatisation"),
        tags: ['clean code', 'APIs', 'scripting'],
        details: '',
        tone: 'blue',
      },
      {
        icon: 'coffee',
        name: 'Java',
        level: 'Advanced',
        subtitle: t('Robust backend & OOP concepts', 'Back-end robuste & concepts POO'),
        tags: ['OOP', 'Spring Boot', 'multi-threading'],
        details: '',
        tone: 'red',
      },
      {
        icon: 'notebook',
        name: 'Jupyter Notebook',
        level: 'Advanced',
        subtitle: t('Experiment-first development workflow', "Workflow de développement axé sur l'expérimentation"),
        tags: ['EDA', 'prototyping', 'visual insight'],
        details: '',
        tone: 'blue',
      },
    ],
    [t('Data & Analytics', 'Données & Analytique')]: [
      {
        icon: 'bar-chart',
        name: 'Data Analysis',
        level: 'Advanced',
        subtitle: t('Insight extraction from raw datasets', "Extraction d'informations à partir de données brutes"),
        tags: ['cleaning', 'profiling', 'statistics'],
        details: '',
        tone: 'blue',
      },
      {
        icon: 'line-chart',
        name: 'Data Visualization',
        level: 'Advanced',
        subtitle: t('Narrative dashboards and reporting', 'Tableaux de bord narratifs et reporting'),
        tags: ['charts', 'storytelling', 'KPIs'],
        details: '',
        tone: 'red',
      },
      {
        icon: 'flask',
        name: 'Experiment Tracking',
        level: 'Intermediate',
        subtitle: t('Metrics, iteration and model comparison', 'Métriques, itération et comparaison de modèles'),
        tags: ['versioning', 'benchmarks', 'ablation'],
        details: '',
        tone: 'blue',
      },
    ],
    [t('Tools & Platforms', 'Outils & Plateformes')]: [
      {
        icon: 'git',
        name: 'Git',
        level: 'Advanced',
        subtitle: t('Version control and clean collaboration', 'Gestion de versions et collaboration propre'),
        tags: ['branching', 'history', 'workflow'],
        details: '',
        tone: 'red',
      },
      {
        icon: 'github',
        name: 'GitHub',
        level: 'Advanced',
        subtitle: t('Repo management and project delivery', 'Gestion de dépôts et livraison de projets'),
        tags: ['PRs', 'issues', 'CI-ready'],
        details: '',
        tone: 'blue',
      },
      {
        icon: 'orbit',
        name: 'Docker',
        level: 'Advanced',
        subtitle: t('Containerization and reproducible environments', 'Conteneurisation et environnements reproductibles'),
        tags: ['containers', 'images', 'compose'],
        details: '',
        tone: 'blue',
      },
    ],
  };

  const projects: Project[] = [
    {
      name: 'SmartPark',
      desc: t(
        'Automates parking access by scanning car license plates.',
        "Automatise l'accès au parking en scannant les plaques d'immatriculation."
      ),
      tags: ['AI', 'Computer Vision', 'ALPR'],
      image: '/assets/images/projects/smartpark.webp',
      fit: 'cover',
      link: 'https://github.com/anis-mselmi/SmartParkTN-D-tection-automatique-des-plaques-tunisiennes-ALPR-pour-parking',
    },
    {
      name: 'PrepAI-TN',
      desc: t(
        'AI corrector for the Tunisian prépa concours — upload an épreuve and get a written corrigé, or just ask.',
        "Correcteur IA pour les concours de prépa tunisiens — déposez une épreuve et obtenez un corrigé rédigé, ou posez simplement votre question."
      ),
      tags: ['Python', 'LLM', 'Hugging Face', 'LoRA'],
      image: '/assets/images/projects/prepai-tn.png',
      fit: 'cover',
      link: 'https://github.com/anis-mselmi/PrepAI-TN',
    },
    {
      name: 'CertTrack',
      desc: t(
        'A Spring Boot app for managing professional certifications.',
        'Une application Spring Boot pour gérer les certifications professionnelles.'
      ),
      tags: ['Java', 'Spring Boot', 'REST API'],
      image: '/assets/images/projects/java-web-app.png',
      fit: 'cover',
      link: 'https://github.com/anis-mselmi/CertTrack',
    },
  ];

  const languages: Language[] = [
    {
      name: t('Arabic', 'Arabe'),
      flagSrc: 'https://flagcdn.com/w80/sa.png',
      flagAlt: 'Saudi Arabia flag',
      badge: t('Native', 'Langue maternelle'),
      detail: t(
        'Native / Fluent communication across personal, academic, and team environments.',
        "Communication native / courante dans les contextes personnels, académiques et d'équipe."
      ),
      tone: 'arabic',
    },
    {
      name: t('English', 'Anglais'),
      flagSrc: 'https://flagcdn.com/w80/us.png',
      flagAlt: 'United States flag',
      badge: t('Professional', 'Professionnel'),
      detail: t(
        'Professional proficiency for technical writing, collaboration, and presentations.',
        'Maîtrise professionnelle pour la rédaction technique, la collaboration et les présentations.'
      ),
      tone: 'english',
    },
    {
      name: t('French', 'Français'),
      flagSrc: 'https://flagcdn.com/w80/fr.png',
      flagAlt: 'France flag',
      badge: t('Professional', 'Professionnel'),
      detail: t(
        'Professional proficiency for communication, documentation, and everyday teamwork.',
        "Maîtrise professionnelle pour la communication, la documentation et le travail d'équipe au quotidien."
      ),
      tone: 'french',
    },
  ];

  const hackathons: Hackathon[] = [
    {
      title: 'AURA 1.0 congress',
      image: '/assets/images/hackathons/1762176420191.jpg',
      badge: t('1st Place', '1re place'),
      desc: t(
        'Designed and programmed an autonomous robot to navigate complex mazes under tight time constraints.',
        "Conception et programmation d'un robot autonome capable de naviguer dans des labyrinthes complexes sous fortes contraintes de temps."
      ),
      tags: ['Java', 'Robotics', 'Arduino', 'Embedded Systems'],
    },
    {
      title: '𝐀𝐈 𝐂𝐚𝐦𝐞𝐫𝐚 𝐂𝐡𝐚𝐥𝐥𝐞𝐧𝐠𝐞 𝟐𝟎𝟐𝟓',
      image: '/assets/images/hackathons/1765102509130.jpg',
      badge: t('Best Innovation', 'Meilleure innovation'),
      desc: t(
        'Built a real-time smart parking locator app to reduce traffic congestion in urban areas. Entry was selective, through a competitive acceptance process.',
        "Développement d'une application de localisation de parking intelligente en temps réel pour réduire les embouteillages urbains. L'accès était sélectif, via un processus d'acceptation compétitif."
      ),
      tags: ['Python', 'Computer Vision', 'IoT', 'Flask'],
    },
    {
      title: 'Space Hack competetion',
      image: '/assets/images/hackathons/1765725484606.jpg',
      badge: t('1st Place', '1re place'),
      desc: t(
        'Developed a predictive model to forecast energy consumption using historical weather data.',
        "Développement d'un modèle prédictif pour estimer la consommation d'énergie à partir de données météorologiques historiques."
      ),
      tags: ['Machine Learning', 'PyTorch', 'Pandas', 'scikit-learn'],
    },
    {
      title: 'IEEE Congress Challenge',
      image: '/assets/images/hackathons/1765748484658.jpg',
      badge: t('Special Prize', 'Prix spécial'),
      desc: t(
        'Built a full-stack app to help women in agriculture in Tunisia during the IEEE WIE ACT 4.0.',
        "Développement d'une application full-stack pour aider les femmes agricultrices en Tunisie lors de l'IEEE WIE ACT 4.0."
      ),
      tags: ['Blockchain', 'Solidity', 'React', 'Node.js'],
    },
    {
      title: 'WIE Wave 2.0',
      image: '/assets/images/hackathons/wie-wave-2.jpg',
      fit: 'contain',
      badge: t('1st Place', '1re place'),
      desc: t(
        'Won first place in the ideathon with team MindMakers at the IEEE WIE Wave 2.0 event.',
        "Première place à l'ideathon avec l'équipe MindMakers lors de l'événement IEEE WIE Wave 2.0."
      ),
      tags: ['Ideathon', 'Pitching', 'Innovation', 'Team Work'],
    },
    {
      title: 'ideathon 4.0',
      image: '/assets/images/hackathons/ideathon.jpg',
      pos: 'center 25%',
      badge: t('6th Place', '6e place'),
      desc: t(
        'Led a team of 4 to build an automated sorting machine prototype, winning the overall competition.',
        "Direction d'une équipe de 4 personnes pour construire un prototype de machine de tri automatisée, remportant la compétition."
      ),
      tags: ['Python', 'Computer Vision', 'Hardware', 'Team Lead'],
    },
  ];

  const ui = {
    nav: {
      skills: t('Skills', 'Compétences'),
      education: t('Education', 'Formation'),
      experience: t('Experience', 'Expérience'),
      projects: t('Projects', 'Projets'),
      hackathons: t('Hackathons', 'Hackathons'),
      certificates: t('Certs', 'Certifs'),
      languages: t('Languages', 'Langues'),
      contact: t('Contact', 'Contact'),
    } as Record<string, string>,
    sections: {
      skills: {
        title: t('Fields of Expertise', "Domaines d'expertise"),
        standfirst: t(
          'A working index of technical competencies, from AI systems to backend engineering.',
          "Un index des compétences techniques, des systèmes d'IA à l'ingénierie back-end."
        ),
      },
      education: {
        title: t('Academic Record', 'Parcours académique'),
        standfirst: t(
          'A dated chronicle of study — from science fundamentals to AI-focused engineering.',
          "Une chronique datée des études — des fondamentaux scientifiques à l'ingénierie axée sur l'IA."
        ),
      },
      experience: {
        title: t('On Assignment', 'En mission'),
        standfirst: t(
          'Professional posts and field service — where the engineering meets the world.',
          "Postes professionnels et engagement sur le terrain — là où l'ingénierie rencontre le monde."
        ),
      },
      certificates: {
        title: t('Credentials Ledger', 'Registre des certifications'),
        standfirst: t(
          'A verified registry of professional certifications. Every entry links to its issuer for authentication.',
          'Un registre vérifié de certifications professionnelles. Chaque entrée renvoie à son émetteur pour authentification.'
        ),
      },
      projects: {
        title: t('Featured Works', 'Travaux sélectionnés'),
        standfirst: t(
          'Selected engineering builds — computer vision, backend systems, and practical tooling.',
          "Réalisations d'ingénierie sélectionnées — vision par ordinateur, systèmes back-end et outils pratiques."
        ),
      },
      hackathons: {
        title: t('Press Clippings', 'Coupures de presse'),
        standfirst: t(
          'Reports from the field — hackathon victories, robotics, and prototype innovation.',
          'Reportages du terrain — victoires en hackathon, robotique et prototypes innovants.'
        ),
      },
      languages: {
        title: t('Languages', 'Langues'),
        standfirst: t(
          'Communication across borders — for writing, collaboration, and presentation.',
          'Communiquer au-delà des frontières — pour la rédaction, la collaboration et la présentation.'
        ),
      },
      contact: {
        title: t('Letters to the Editor', 'Courrier des lecteurs'),
        standfirst: t(
          'Have a proposal, a role, or a question? Send word — replies are prompt.',
          'Une proposition, un poste ou une question ? Écrivez-moi — les réponses sont rapides.'
        ),
      },
    },
    hero: {
      folio: t('Vol. I · The Engineering Broadsheet', "Vol. I · Le Journal de l'Ingénieur"),
      kicker1: t('Java Developer', 'Développeur Java'),
      kicker2: t('AI · RAG · LLM Engineer', 'Ingénieur IA · RAG · LLM'),
      kicker3: t('AI Engineering', 'Ingénierie IA'),
      dateline: t('Sousse, Tunisia — Special Report', 'Sousse, Tunisie — Reportage spécial'),
      lede: t(
        'An AI Engineering student, specializing in Ubuntu and LLMs, but also building RAG pipelines, computer vision systems, and Spring Boot apps.',
        "Étudiant en ingénierie IA, spécialisé dans Ubuntu et les LLM, je développe aussi des pipelines RAG, des systèmes de vision par ordinateur et des applications Spring Boot."
      ),
      cv: t('Résumé', 'Mon CV'),
      statCerts: t('Certs', 'Certifs'),
      statWins: t('Wins', 'Victoires'),
      statProjects: t('Projects', 'Projets'),
      figCaption: t('Fig. 1 — The Developer', 'Fig. 1 — Le Développeur'),
      circulation: t('Circulation:', 'Tirage :'),
    },
    ticker: { label: t('Stack ▸', 'Technos ▸') },
    skills: {
      fig: t('Fig. 2 — Proficiency Index (%)', 'Fig. 2 — Indice de maîtrise (%)'),
      colDiscipline: t('Discipline', 'Discipline'),
      colStack: t('Stack / Notes', 'Stack / Notes'),
      colProficiency: t('Proficiency', 'Maîtrise'),
      statDisciplines: t('Disciplines listed', 'Disciplines listées'),
      statExpert: t('At expert tier', 'Au niveau expert'),
      statPeak: t('Peak index', 'Indice maximal'),
      section: t('Section', 'Section'),
      entries: t('entries', 'entrées'),
    },
    levels: {
      Expert: t('Expert', 'Expert'),
      Advanced: t('Advanced', 'Avancé'),
      Intermediate: t('Intermediate', 'Intermédiaire'),
      Beginner: t('Beginner', 'Débutant'),
    } as Record<string, string>,
    education: {
      current: t('In progress', 'En cours'),
    },
    experience: {
      position: t('Position №', 'Poste №'),
      volunteerHeader: t('Bénévolat — Community & IEEE Service', 'Bénévolat — Communauté & Service IEEE'),
      dispatch: t('Dispatch №', 'Dépêche №'),
      active: t('Active', 'En cours'),
      serviceHeader: t('Service Record — Community & IEEE', 'Registre de service — Communauté & IEEE'),
    },
    certs: {
      all: t('All', 'Tous'),
      colNo: t('№', '№'),
      colCredential: t('Credential', 'Certification'),
      colIssuer: t('Issuer', 'Émetteur'),
      colFocus: t('Focus', 'Domaine'),
      colDate: t('Date', 'Date'),
      colVerify: t('Verify', 'Vérifier'),
      verify: t('Verify ▸', 'Vérifier ▸'),
    },
    projects: { dispatch: t('Repository №', 'Dépôt №') },
    hackathons: { dispatch: t('Dispatch №', 'Dépêche №') },
    contact: {
      nameLabel: t('Your Name', 'Votre nom'),
      namePlaceholder: t('Jane Doe', 'Jean Dupont'),
      emailLabel: t('Your Email', 'Votre e-mail'),
      emailPlaceholder: t('jane@example.com', 'jean@exemple.com'),
      subjectLabel: t('Subject', 'Objet'),
      subjectPlaceholder: t('A proposal…', 'Une proposition…'),
      messageLabel: t('Message', 'Message'),
      messagePlaceholder: t('Dear Anis,…', 'Cher Anis,…'),
      send: t('Send Correspondence ▸', 'Envoyer le message ▸'),
      sending: t('Dispatching…', 'Envoi…'),
      validation: t('Kindly complete Name, Email, and Message.', "Veuillez remplir le nom, l'e-mail et le message."),
      sentStrong: t('Received.', 'Reçu.'),
      sentText: t(' Thank you — a reply is on its way.', ' Merci — une réponse est en route.'),
      fallback: t(
        'Your mail client should have opened. If not, write to ',
        "Votre client de messagerie devrait s'être ouvert. Sinon, écrivez à "
      ),
      directory: t('Directory', 'Répertoire'),
      dirEmail: t('Email', 'E-mail'),
      dirPhone: t('Telephone', 'Téléphone'),
      dirOffice: t('Bureau', 'Bureau'),
      quote: t(
        '“Turning complex ideas into reliable systems, one build at a time.”',
        '« Transformer des idées complexes en systèmes fiables, une réalisation à la fois. »'
      ),
    },
    footer: {
      colophon: t(
        'Colophon — Set in Fraunces, Archivo & Space Mono · Built with React, TypeScript & Vite ·',
        'Colophon — Composé en Fraunces, Archivo & Space Mono · Réalisé avec React, TypeScript & Vite ·'
      ),
    },
    toggle: {
      toEnglish: t('Switch to English', 'Passer en anglais'),
      toFrench: t('Switch to French', 'Passer en français'),
    },
  };

  return {
    about,
    education,
    work,
    volunteering,
    skillsByCategory,
    projects,
    languages,
    hackathons,
    ui,
  };
}

export type Bundle = ReturnType<typeof buildBundle>;

/** Hook returning the localized content bundle for the active language. */
export function useContent(): Bundle {
  const { lang } = useLang();
  return useMemo(() => buildBundle(lang), [lang]);
}
