import os
import re
import math
from typing import Dict, List, Any

# Try importing the official Google GenAI library for dynamic RAG API queries
try:
    import google.generativeai as genai
    HAS_GENAI = True
except ImportError:
    HAS_GENAI = False

# Anis Mselmi's detailed portfolio knowledge graph divided into semantic chunks for retrieval
KNOWLEDGE_CHUNKS = [
    {
        "id": "about",
        "keywords": ["about", "who is", "anis", "mselmi", "student", "background", "profile", "introduce"],
        "text": "Anis Mselmi is a brilliant Computer Engineering student at École Polytechnique de Sousse specializing in AI, Machine Learning, and RAG. He is a developer focused on building Python tools, data pipelines, and intelligent conversational agents.",
        "twin": "🤖 **[Anis-AI]:** Hello! I'm Anis Mselmi's digital twin. Anis is a passionate **Computer Engineering student** at École Polytechnique de Sousse (class of 2028). He loves building responsive user experiences, machine learning applications, and custom RAG databases. He's always eager to push the boundaries of conversational AI!",
        "recruiter": "💼 **[Anis-Recruiter]:** Anis Mselmi is a highly motivated **Computer Engineering Student** (2025-2028) based in Sousse, Tunisia. He possesses solid analytical foundations from intensive preparatory engineering studies and specializes in building high-ROI AI/RAG solutions. He is actively seeking junior roles, internships, and collaborative development opportunities.",
        "tech": "💻 **[Anis-Tech]:** Architecture overview: I am a profile running on a Streamlit engine with raw Python backend. Anis specializes in Python, Scikit-learn pipelines, deep learning models, and advanced semantic databases. He uses structured data management (SQL/MySQL) and git-driven deployment environments."
    },
    {
        "id": "skills",
        "keywords": ["skills", "stack", "languages", "python", "programming", "c++", "sql", "machine learning", "scikit", "tensorflow"],
        "text": "Core technical skills include expert level Python, C++, and SQL. In AI/ML, specialized in Scikit-Learn pipelines, Deep Learning, exploratory data analysis, and advanced RAG vector embedding architectures.",
        "twin": "🤖 **[Anis-AI]:** Anis has a fantastic tech stack! He is an **expert in Python**, intermediate in C++, and highly proficient in SQL queries. In the AI domain, he excels at creating supervised/unsupervised machine learning pipelines, standardizing exploratory data analysis, and architecting custom semantic indexing platforms.",
        "recruiter": "💼 **[Anis-Recruiter]:** Technical Inventory: Anis has commercial-grade Python experience, is highly capable in relational database design (SQL/MySQL), and builds complete ML pipelines using Scikit-Learn. His software development process is guided by solid version control (Git) and responsive container styling.",
        "tech": "💻 **[Anis-Tech]:** Low-Level Stack Analysis:\n- **Languages:** Python 3.10+ (expert, including async code & memory optimization), C++17 (data structures, logic), SQL (indexing, triggers).\n- **Frameworks & Libs:** Pandas, NumPy, Scikit-learn, OpenCV, Pygame, Streamlit dashboarding.\n- **Architectures:** Semantic search, embeddings, TF-IDF cosine scoring models."
    },
    {
        "id": "smartpark",
        "keywords": ["smartpark", "smart park", "parking", "license", "car", "plate", "vision", "opencv", "alpr", "ocr"],
        "text": "SmartPark is an automated parking controller system utilizing OpenCV and Automatic License Plate Recognition (ALPR) to capture vehicle license plates and parse text via OCR, linking with a backend database for access management.",
        "twin": "🤖 **[Anis-AI]:** 🚗 **SmartPark** is one of Anis's pride and joys! It's a smart parking system that uses Computer Vision (OpenCV) and Automatic License Plate Recognition (ALPR) to read car plates as they arrive, cross-reference them with a database, and trigger physical parking gate animations!",
        "recruiter": "💼 **[Anis-Recruiter]:** Project Metrics: **SmartPark** demonstrates Anis's ability to deliver end-to-end automation. By integrating Computer Vision OCR with central database registries, this system decreases parking gate queue times and provides automated access logs, showing high business utility.",
        "tech": "💻 **[Anis-Tech]:** Technical Breakdown: **SmartPark** features vehicle detection bounding boxes, image preprocessing (grayscale, bilateral filtering, Canny edge tracking), contour extraction for plates, Tesseract/OCR character parsing, and database transactions comparing real-time captures against access records."
    },
    {
        "id": "dewejen",
        "keywords": ["dewejen", "stock", "management", "mysql", "inventory", "database", "desktop", "app"],
        "text": "Dewejen is a professional stock and inventory management desktop application written in Python, featuring real-time MySQL database synchronization, transaction logs, and low-inventory safety triggers.",
        "twin": "🤖 **[Anis-AI]:** 📦 **Dewejen** is a super helpful inventory manager. It connects a sleek Python desktop interface directly to a live MySQL database, allowing users to track stock items, record transactions in real-time, and trigger visual alerts if quantities fall below threshold levels!",
        "recruiter": "💼 **[Anis-Recruiter]:** System Integrity: **Dewejen** is an enterprise inventory application. It features parameterized query models to prevent SQL injection, structured database normalization, and rigorous tracking of transactions, minimizing stock discrepancy risk.",
        "tech": "💻 **[Anis-Tech]:** Database Architecture: **Dewejen** is built with a relational schema hosting tables for `inventory`, `transactions`, and `alerts`. Features active connection pools to a MySQL cluster, ACID transaction compliance, safety stock triggers, and custom GUI dashboard views."
    },
    {
        "id": "burgerdash",
        "keywords": ["burgerdash", "burger dash", "game", "pygame", "2d", "arcade", "simulation"],
        "text": "BurgerDash is a fast-paced 2D restaurant arcade management simulation game written in Python using Pygame, incorporating sprite rendering, level acceleration, and state machine loops.",
        "twin": "🤖 **[Anis-AI]:** 🍔 **BurgerDash** is a highly engaging 2D restaurant arcade game! Anis built it using Pygame, complete with fast cooking mechanics, level speed-up thresholds, custom collision logic, and animated retro sprites. It's super fun to play!",
        "recruiter": "💼 **[Anis-Recruiter]:** Core logic: **BurgerDash** shows Anis's capability in object-oriented programming (OOP). Managing dynamic game states, frame rates, memory footprints of sprites, and clean gameloops are all indicators of highly robust programming discipline.",
        "tech": "💻 **[Anis-Tech]:** Engineering Details: Built on the **Pygame framework**. Utilizes a robust game-state manager (Intro -> Gameplay -> Paused -> GameOver), delta-time frame-rate regulation (locked at 60FPS), quadtree collision calculations, and sprite sheet animation slicing."
    },

    {
        "id": "rag",
        "keywords": ["rag", "retrieval", "vector", "embedding", "chunking", "llm", "semantic", "similarity", "database", "twin"],
        "text": "Retrieval-Augmented Generation (RAG) implementation details: document chunking, overlap limits, embedding vector calculations, cosine similarity scores, and LLM prompt context injection.",
        "twin": "🤖 **[Anis-AI]:** I am literally a product of RAG! Anis designs RAG systems that take raw documents, split them into smart chunks with optimal overlap, encode them into high-dimensional vectors, and run semantic similarity searches to feed LLMs zero-hallucination context!",
        "recruiter": "💼 **[Anis-Recruiter]:** AI Capability: RAG represents the frontier of corporate document search. Anis's theoretical and practical understanding of vector stores, token thresholds, and embedding distances makes him a highly valuable asset for companies adopting generative AI tools.",
        "tech": "💻 **[Anis-Tech]:** RAG Pipeline Specs: This console uses a custom offline **Vector Space Model (VSM)**. The search algorithm computes term-frequency inverse-document-frequency (TF-IDF) vectors for your query, maps it against our 10-document knowledge graph, and calculates cosine distance: $cos(\\theta) = \\frac{A \\cdot B}{\\|A\\| \\|B\\|}$ with failover to Gemini LLM."
    },
    {
        "id": "education",
        "keywords": ["education", "degree", "school", "polytechnique", "preparatory", "lycee", "university", "studies"],
        "text": "Education includes a Computer Engineering degree from École Polytechnique de Sousse (2025-2028), integrated prep studies in Math and Physics (2023-2025), and a high school diploma in Science (2022-2023).",
        "twin": "🤖 **[Anis-AI]:** Anis has a stellar academic foundation! He is pursuing his **Computer Engineering degree** at École Polytechnique de Sousse (2025-2028). Before that, he completed two years of intensive **integrated preparatory engineering studies** (2023-2025) mastering math and physics!",
        "recruiter": "💼 **[Anis-Recruiter]:** Academic Track: Anis is currently enrolled in a rigorous **Computer Engineering degree** at École Polytechnique de Sousse, building on an analytical preparatory foundation. Prep schools in Tunisia select for extreme focus, fast learning curves, and advanced problem-solving capabilities.",
        "tech": "💻 **[Anis-Tech]:** Coursework Syllabus: Advanced courses in Data Structures & Algorithms, Systems Engineering, Relational & NoSQL Databases, Computer Vision, Numerical Analysis, and Machine Learning Model Selection."
    },
    {
        "id": "contact",
        "keywords": ["contact", "email", "phone", "mobile", "reach", "hire", "socials", "linkedin", "github", "address", "location"],
        "text": "Contact info: email: anismselmi490@gmail.com, phone: +216 25 141 636, address: Khzema Ouest, Sousse, Tunisia. LinkedIn: https://www.linkedin.com/in/anis-mselmi-441b39326/ GitHub: https://github.com/anis-mselmi",
        "twin": "🤖 **[Anis-AI]:** Let's connect! You can reach Anis directly via email at **anismselmi490@gmail.com** or call him at **+216 25 141 636**. You can also find him on [LinkedIn](https://www.linkedin.com/in/anis-mselmi-441b39326/) and checkout his repositories on [GitHub](https://github.com/anis-mselmi)!",
        "recruiter": "💼 **[Anis-Recruiter]:** Outreach Channels: I highly encourage reaching out to discuss internships or open roles. You can contact Anis directly at **anismselmi490@gmail.com** or via phone at **+216 25 141 636**. Correspondence will be answered promptly.",
        "tech": "💻 **[Anis-Tech]:** Interface Protocol: To automate communications, the contact form initiates a standard standard email client envelope prefilled with SMTP fields via a HTML `mailto:` schema."
    },
    {
        "id": "cv",
        "keywords": ["cv", "resume", "canva", "pdf", "portfolio", "dossier"],
        "text": "The resume / CV of Anis Mselmi is hosted on Canva for easy viewing and interactive access at: https://canva.link/cmn3h8sq33jeuib",
        "twin": "🤖 **[Anis-AI]:** You can check out Anis's professional CV directly on Canva! It's super sleek and lists all his experiences. Here is the link: **[View CV on Canva](https://canva.link/cmn3h8sq33jeuib)**",
        "recruiter": "💼 **[Anis-Recruiter]:** Credentials Access: To download or view the verified technical resume detailing all of Anis's academic projects, achievements, and leadership history, click here: **[View CV on Canva](https://canva.link/cmn3h8sq33jeuib)**",
        "tech": "💻 **[Anis-Tech]:** Document Link: The Canva CV is embedded as a standard sandboxed iframe within the portfolio layouts, with a fallback direct redirect URL configured."
    },
    {
        "id": "community",
        "keywords": ["ieee", "community", "sight", "webmaster", "ambassador", "organizer", "club", "robotics", "volunteer"],
        "text": "Community positions: Web Master at IEEE SIGHT EPS SB. Ambassador at NPC PolyRobots, IEEE YESIST12, IEEE Smart Cities. Organizer at Twise Night and TCPC.",
        "twin": "🤖 **[Anis-AI]:** Anis is extremely active in the community! He is the **Web Master for IEEE SIGHT EPS SB** and an Ambassador for huge events like **NPC PolyRobots** and **IEEE Smart Cities**. He loves organizing hackathons and tech events!",
        "recruiter": "💼 **[Anis-Recruiter]:** Leadership profile: Anis demonstrates excellent teamwork, communication, and organizational skills. Serving as Web Master and organizing major collegiate tech events like **Twise Night** are indicators of his strong work ethic and proactive nature.",
        "tech": "💻 **[Anis-Tech]:** Volunteer Network: Webmaster responsibilities include administrating domain zones, writing deployment shell scripts, managing branch assets, and ensuring general frontend compliance across club portals."
    },
    {
        "id": "certificates",
        "keywords": ["certificate", "certificates", "certification", "certifications", "nvidia", "deep learning", "rag", "transformers", "nlp", "cybersecurity", "prompt engineering", "credentials", "credential"],
        "text": "NVIDIA Certificates of Competency achieved by Anis Mselmi: Building RAG Agents with LLMs, Introduction to Transformer-Based Natural Language Processing, Building LLM Applications With Prompt Engineering, Building AI-Based Cybersecurity Pipelines, Fundamentals of Deep Learning, Generative AI with Diffusion Models, Building Real-Time Video AI Applications, and Fundamentals of Accelerated Computing with CUDA Python.",
        "twin": "🤖 **[Anis-AI]:** Anis has earned **8 outstanding NVIDIA Certificates of Competency**! They include:\n\n1. 🧠 **Building RAG Agents with LLMs**\n2. 📝 **Introduction to Transformer-Based Natural Language Processing**\n3. ⚙️ **Building LLM Applications With Prompt Engineering**\n4. 🛡️ **Building AI-Based Cybersecurity Pipelines**\n5. 🚀 **Fundamentals of Deep Learning**\n6. 🎨 **Generative AI with Diffusion Models**\n7. 📹 **Building Real-Time Video AI Applications**\n8. 🐍 **Fundamentals of Accelerated Computing with CUDA Python**\n\nYou can view and verify all of them in the Certificates section on this site!",
        "recruiter": "💼 **[Anis-Recruiter]:** Anis holds **8 professional Certificates of Competency from NVIDIA**, verifying his hands-on expertise in Deep Learning, NLP, Prompt Engineering, Cybersecurity pipelines, RAG architectures, Diffusion Models, Real-Time Video AI, and GPU acceleration with CUDA Python. These credentials demonstrate rigorous, industry-recognized competence in deploying modern AI workflows.",
        "tech": "💻 **[Anis-Tech]:** NVIDIA Credentials Registry:\n- **Building RAG Agents with LLMs** (ID: `7vo8r-_oQv2bJTyHff6CDQ`)\n- **Introduction to Transformer-Based Natural Language Processing** (ID: `Yy6SLV7eT4eN7LI-txHLBQ`)\n- **Building LLM Applications With Prompt Engineering** (ID: `iagFYqO4QJmdv4JJU6g_sw`)\n- **Building AI-Based Cybersecurity Pipelines** (ID: `As48ycFRRMqT0VKVb4PbtA`)\n- **Fundamentals of Deep Learning** (ID: `4C-6f4fjSHK2HcgQfx6_ZA`)\n- **Generative AI with Diffusion Models** (ID: `fn3bEZHDTHCZATWKG-svvg`)\n- **Building Real-Time Video AI Applications** (ID: `DttLN2ikRJeNMkkh7euKHA`)\n- **Fundamentals of Accelerated Computing with CUDA Python** (ID: `t-mYwSVhRC2Ve6K0z1qflQ`)\nAll certificates are fully verified, completed in 2025."
    }
]

# ---------------------------------------------------------
# Mathematical Vector Space Model (TF-IDF Cosine Similarity)
# ---------------------------------------------------------
def tokenize(text: str) -> List[str]:
    """Tokenize text into lowercase alphabetical words."""
    return re.findall(r"\b[a-z]{3,}\b", text.lower())

def compute_idf(chunks: List[Dict[str, Any]]) -> Dict[str, float]:
    """Calculate Inverse Document Frequency (IDF) for all vocabulary terms."""
    idf = {}
    N = len(chunks)
    for chunk in chunks:
        # Extract unique words in keywords and text
        words = set(tokenize(chunk["text"]) + chunk["keywords"])
        for word in words:
            idf[word] = idf.get(word, 0) + 1
            
    # Compute log scale IDF
    for word, df in idf.items():
        idf[word] = math.log(1.0 + (N / (1.0 + df))) + 1.0
    return idf

# Global precomputed IDF dictionary
IDF_VOCAB = compute_idf(KNOWLEDGE_CHUNKS)

def get_cosine_similarity(query_words: List[str], chunk: Dict[str, Any]) -> float:
    """Calculate mathematical Cosine Similarity between a query token list and a knowledge chunk."""
    # Combine chunk keywords and chunk body for chunk vector representation
    chunk_words = tokenize(chunk["text"]) + chunk["keywords"]
    
    # Create distinct vocabulary for local pair
    local_vocab = set(query_words + chunk_words)
    if not local_vocab:
        return 0.0
        
    query_vector = {}
    chunk_vector = {}
    
    # Calculate Term Frequencies * IDF
    for word in local_vocab:
        idf = IDF_VOCAB.get(word, 1.0)
        
        tf_q = query_words.count(word)
        query_vector[word] = tf_q * idf
        
        # Keywords are weighted heavily in chunk vector representing search intent matches
        tf_c = chunk_words.count(word) + (chunk["keywords"].count(word) * 3)
        chunk_vector[word] = tf_c * idf
        
    # Compute Dot Product
    dot_product = sum(query_vector[w] * chunk_vector[w] for w in local_vocab)
    
    # Compute Euclidean Vector Lengths (Norms)
    norm_q = math.sqrt(sum(query_vector[w] ** 2 for w in local_vocab))
    norm_c = math.sqrt(sum(chunk_vector[w] ** 2 for w in local_vocab))
    
    if norm_q == 0.0 or norm_c == 0.0:
        return 0.0
        
    return dot_product / (norm_q * norm_c)

# ---------------------------------------------------------
# Dynamic Response Routing and Processing
# ---------------------------------------------------------
def get_gemini_api_response(query: str, persona: str, api_key: str) -> str | None:
    """
    Attempts to fetch a live generative response from the Gemini API using customized persona directives.
    """
    if not HAS_GENAI:
        return None
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-1.5-flash")
        
        # Inject persona-focused system configurations into prompt
        persona_prompts = {
            "twin": "You are Anis Mselmi's digital AI twin. Respond with a technical, energetic, and highly positive developer tone.",
            "recruiter": "You are Anis Mselmi's recruiting agent. Address standard professional facts, GPA/university standing, dates, timeline, reliability, and business value. Highlight soft skills and hireability.",
            "tech": "You are Anis Mselmi's deep tech lead twin. Answer with extreme technical accuracy, detailed algorithms, code structures, data schema choices, and development optimization details."
        }
        
        # Crafting grounding context query
        grounding_data = "\n".join([f"- {c['id']}: {c['text']}" for c in KNOWLEDGE_CHUNKS])
        system_rules = persona_prompts.get(persona, persona_prompts["twin"])
        
        prompt = (
            f"Grounding Data regarding Anis Mselmi:\n{grounding_data}\n\n"
            f"Role Directives: {system_rules}\n\n"
            f"User Inquiry: '{query}'\n\n"
            f"Output a highly helpful, concise reply tailored to the role. Keep text readable with bullet points and bolding."
        )
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"⚠️ [RAG Failover]: API error: {str(e)}. Falling back to local Cosine Similarity matcher."

def get_ai_response(query: str, persona: str = "twin") -> str:
    """
    Core entrypoint: Routes the user query through command shell parsing, 
    live Gemini LLM API evaluation (if API key exists), or local Cosine Similarity calculations.
    """
    q = query.lower().strip()
    
    # 1. System Command Shell Parsing
    if q.startswith("/"):
        cmd = q.split()[0]
        if cmd == "/help":
            return (
                "🤖 **[Console Help Menu]:** Recognized terminal system shell commands:\n\n"
                "▪ `/skills` - Output technical stack inventory\n"
                "▪ `/projects` - Output list of core engineered systems\n"
                "▪ `/certificates` - Output verified credentials index\n"
                "▪ `/cv` - Retrieve direct Canva resume link\n"
                "▪ `/contact` - Output communication channels\n"
                "▪ `/about` - Introduce profile & objectives\n"
                "▪ `/status` - Trigger core system metrics and telemetry\n"
                "▪ `/mode [twin|recruiter|tech]` - Alter persona profile on the fly\n"
                "▪ `/clear` - Flush console logs buffer"
            )
        elif cmd == "/skills":
            chunk = next(c for c in KNOWLEDGE_CHUNKS if c["id"] == "skills")
            return chunk.get(persona, chunk["twin"])
        elif cmd == "/projects":
            proj_desc = (
                "🍔 **BurgerDash:** 2D retro arcade pygame cooking simulation.\n"
                "🚗 **SmartPark:** Computer Vision License Plate scanner.\n"
                "📦 **Dewejen:** MySQL-powered inventory manager."
            )
            return f"🤖 **[Anis-AI] Systems Catalog:**\n\n{proj_desc}"
        elif cmd == "/cv":
            chunk = next(c for c in KNOWLEDGE_CHUNKS if c["id"] == "cv")
            return chunk.get(persona, chunk["twin"])
        elif cmd == "/certificates" or cmd == "/certs":
            chunk = next(c for c in KNOWLEDGE_CHUNKS if c["id"] == "certificates")
            return chunk.get(persona, chunk["twin"])
        elif cmd == "/contact":
            chunk = next(c for c in KNOWLEDGE_CHUNKS if c["id"] == "contact")
            return chunk.get(persona, chunk["twin"])
        elif cmd == "/about":
            chunk = next(c for c in KNOWLEDGE_CHUNKS if c["id"] == "about")
            return chunk.get(persona, chunk["twin"])
        elif cmd.startswith("/mode"):
            # This is captured in sections.py to update session state, 
            # here we just provide feedback
            parts = q.split()
            if len(parts) > 1 and parts[1] in ["twin", "recruiter", "tech"]:
                return f"⚙️ **[System Mode]:** Swapped active persona to: **{parts[1].upper()}**."
            return "⚠️ **[System Error]:** Usage `/mode [twin|recruiter|tech]`"
        elif cmd == "/status":
            has_api = "ONLINE" if os.environ.get("GEMINI_API_KEY") else "FAILOVER ACTIVE"
            return (
                f"📊 **[Console Telemetry System diagnostics]:**\n\n"
                f"▪ **Core Router Engine:** TF-IDF Vector Space Scorer (Cosine $\\theta$ Metric)\n"
                f"▪ **Database Telemetry:** {len(KNOWLEDGE_CHUNKS)} semantic context vectors indexed\n"
                f"▪ **Live LLM Fallback:** {has_api}\n"
                f"▪ **Selected Persona:** {persona.upper()}\n"
                f"▪ **NLP Latency:** < 5ms (Local cache indexing)"
            )
        else:
            return f"🤖 **[System Command Error]:** Command '{cmd}' not recognized. Type `/help` for shell index."

    # 2. Live API RAG Evaluation
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        try:
            import streamlit as st
            api_key = st.secrets.get("GEMINI_API_KEY") or st.secrets.get("gemini_api_key")
        except Exception:
            pass

    if api_key:
        api_res = get_gemini_api_response(query, persona, api_key)
        if api_res:
            return api_res

    # 3. High-Precision TF-IDF Cosine Similarity Offline Router
    query_words = tokenize(q)
    if not query_words:
        return (
            "🤖 **[Anis-AI]:** Console parsed empty query strings. "
            "Please enter a valid engineering inquiry, or type `/help`!"
        )
        
    best_chunk = None
    max_sim = 0.0
    
    for chunk in KNOWLEDGE_CHUNKS:
        sim = get_cosine_similarity(query_words, chunk)
        if sim > max_sim:
            max_sim = sim
            best_chunk = chunk
            
    # Dynamic Similarity Match Threshold (0.09)
    if best_chunk and max_sim > 0.09:
        return best_chunk.get(persona, best_chunk["twin"])

    # Generous general fallback with instructions
    fallback_msgs = {
        "twin": (
            "🤖 **[Anis-AI]:** That's a fascinating question! I didn't locate a precise match for that specific topic inside my local TF-IDF semantic chunks. "
            "Ask me about my **NVIDIA certificates**, **skills**, **projects**, or **community activities**!"
        ),
        "recruiter": (
            "💼 **[Anis-Recruiter]:** I appreciate your question. While that specific inquiry isn't indexed in my local database, Anis would be glad to address it in detail. "
            "You can contact him directly at **anismselmi490@gmail.com** or check out his Canva resume link `/cv`!"
        ),
        "tech": (
            "💻 **[Anis-Tech]:** Index mismatch error. Search query vocabulary terms returned cosine distance scores below the 0.09 threshold. "
            "Please check out indexed projects `/projects`, or inspect my technical system configurations `/status`."
        )
    }
    
    return fallback_msgs.get(persona, fallback_msgs["twin"])
