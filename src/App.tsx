import { Background } from './components/Background';
import { ScrollProgress } from './components/ScrollProgress';
import { Navbar } from './components/Navbar';
import { Ticker } from './components/Ticker';
import { Hero } from './sections/Hero';
import { Skills } from './sections/Skills';
import { Education } from './sections/Education';
import { Experience } from './sections/Experience';
import { Certifications } from './sections/Certifications';
import { Projects } from './sections/Projects';
import { Hackathons } from './sections/Hackathons';
import { Languages } from './sections/Languages';
import { Contact } from './sections/Contact';
import { Footer } from './sections/Footer';

export default function App() {
  return (
    <div className="relative">
      <Background />
      <ScrollProgress />
      <Navbar />

      <div className="relative z-10">
        <Hero />
        <Ticker />
        <main>
          <Skills />
          <Education />
          <Experience />
          <Certifications />
          <Projects />
          <Hackathons />
          <Languages />
          <Contact />
        </main>
        <Footer />
      </div>
    </div>
  );
}
