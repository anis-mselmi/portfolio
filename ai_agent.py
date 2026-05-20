import os
import re
import difflib
from typing import Dict, List, Any

# Try importing the official Google GenAI library for dynamic fallback
try:
    import google.generativeai as genai
    HAS_GENAI = True
except ImportError:
    HAS_GENAI = False

# Anis Mselmi's exact background for LLM grounding (System Prompt Context)
GROUNDING_CONTEXT = """
You are the AI Twin of Anis Mselmi, a brilliant Computer Engineering student at École Polytechnique de Sousse (2025-2028).
Your personality is professional, highly technical, positive, enthusiastic about AI, and developer-centric.

Here is your exact background knowledge:
- Name: Anis Mselmi
- Current Role: Computer Engineering Student | AI, RAG, and LLM Enthusiast
- Location: Khzema Ouest, Sousse, Tunisia
- Contact: Email: anismselmi490@gmail.com | Phone: +216 25 141 636
- LinkedIn: https://www.linkedin.com/in/anis-mselmi-441b39326/
- GitHub: https://github.com/anis-mselmi

ABOUT:
Anis is focused on AI, machine learning, and LLMs. He loves building python models, RAG pipelines, and conversational agents. He is experienced in Jupyter notebooks, data analysis, and rapid experimentation. He is seeking internships and part-time roles in AI/RAG/LLM product spaces.

EDUCATION:
1. École Polytechnique de Sousse (2025 - 2028): Computer Engineering degree. Built RAG pipelines and custom conversational agents.
2. École Polytechnique de Sousse (2023 - 2025): Integrated Preparatory studies. Intensive Mathematics, Physics, and analytical logic.
3. Lycée Les Lumières Sousse (2022 - 2023): High School Diploma in Sciences.

CORE SKILLS:
- AI/ML: Machine Learning (Advanced), Deep Learning (Intermediate), RAG Pipelines (Advanced with vector DBs, chunking, reranking)
- Languages: Python (Expert), C++ (Intermediate), SQL
- Data: Pandas, NumPy, Data Visualization (Advanced), Experiment Tracking
- Collaboration: Git, GitHub, Streamlit, Linux

PROJECTS:
1. SmartPark: Automated parking system using Computer Vision & ALPR (Automatic License Plate Recognition) to scan license plates.
2. Dewejen: Professional inventory & stock management system with MySQL connectivity.
3. BurgerDash: Fast-paced 2D restaurant management game built using Pygame.
4. Brewstone Coffee: Sleek coffee shop application with layout consistency and highly professional frontend UI.

COMMUNITY & LEADERSHIP:
- Web Master at IEEE SIGHT EPS SB.
- Ambassador at ATIC, NPC 2.0 PolyRobots, IEEE YESIST12, IEEE Smart Cities.
- Organizer at Twise Night, IEEE Tejmaana, TCPC, IEEE Day.
- Participant at CSTAM 1.0, SDC 3.0, WIE ACT 4.0, TSYP13.

INSTRUCTIONS:
1. Always stay in character as Anis Mselmi's AI twin.
2. Be helpful, concise, and highlight your technical accomplishments.
3. If asked about contact details, point to email and phone.
4. If asked about resume, provide the Canva link: https://canva.link/cmn3h8sq33jeuib
"""

# Local Intent Responses (Failsafe matching)
KNOWLEDGE_BASE = {
    "greeting": (
        "🤖 **[Anis-AI]:** Welcome to the cybernetic twin interface of **Anis Mselmi**.\n\n"
        "Input any query or use the suggested buttons. Type `/help` to see list of terminal system commands."
    ),
    "help": (
        "🤖 **[Console Help]:** Available Terminal Shell Commands:\n\n"
        "💻 `/skills` - Output technical stack inventory\n"
        "💻 `/projects` - Render list of core engineered systems\n"
        "💻 `/cv` - Retrieve direct Canva resume link\n"
        "💻 `/contact` - Output communication channels\n"
        "💻 `/about` - Introduce profile & objectives\n"
        "💻 `/clear` - Flush console logs buffer"
    ),
    "about": (
        "🤖 **[Anis-AI]:** I am a **Computer Engineering Student** specializing in AI, Machine Learning, "
        "and Large Language Models (LLMs). I build Python systems, custom RAG frameworks, and computer vision models. "
        "I thrive in fast-paced collaborative development teams."
    ),
    "skills": (
        "🤖 **[Anis-AI]:** Technical Inventory:\n\n"
        "▪ **AI & ML:** Supervised/Unsupervised Scikit-Learn pipelines, neural network model fine-tuning.\n"
        "▪ **RAG Frameworks:** Vector databases, advanced document chunking, semantic similarity metrics, embedding lookups.\n"
        "▪ **Programming:** Python (Expert), C++ (Intermediate), MySQL query integration.\n"
        "▪ **Data Engineering:** EDA (Exploratory Data Analysis), Pandas profiling, high-fidelity Plotly charts."
    ),
    "projects_all": (
        "🤖 **[Anis-AI]:** Project Catalog:\n\n"
        "🚗 **SmartPark:** ALPR computer vision license plate parking controller.\n"
        "📦 **Dewejen:** MySQL-powered Python stock inventory management system.\n"
        "🍔 **BurgerDash:** 2D arcade Pygame culinary management simulation.\n"
        "☕ **Brewstone Coffee:** High-fidelity UI coffee storefront app."
    ),
    "smartpark": (
        "🤖 **[Anis-AI]:** **SmartPark** represents my work in Computer Vision.\n\n"
        "It processes video feeds to capture vehicle plates, extracts text strings using Automatic License Plate Recognition (ALPR), "
        "and coordinates parking gate status automatically against DB records."
    ),
    "dewejen": (
        "🤖 **[Anis-AI]:** **Dewejen** is a Python desktop stock control app.\n\n"
        "It communicates directly with a **MySQL cluster** to manage quantities, logs, transactions, and triggers alerts "
        "when safety stock levels are breached."
    ),
    "burgerdash": (
        "🤖 **[Anis-AI]:** **BurgerDash** is a Pygame arcade architecture project.\n\n"
        "Includes standard collision mapping, state-machine menu loops, level speed acceleration, and sprite rendering."
    ),
    "coffee": (
        "🤖 **[Anis-AI]:** **Brewstone Coffee** showcases front-end layout excellence.\n\n"
        "Designed to maintain pixel-perfect responsive containers, harmonized color schemes, and seamless button event feedback."
    ),
    "rag": (
        "🤖 **[Anis-AI]:** My primary focus is **Retrieval-Augmented Generation**.\n\n"
        "I build semantic document retrieval pipelines, using semantic embedding distance models, "
        "optimized chunk overlaps, and query expansion techniques to eliminate hallucination in LLMs."
    ),
    "education": (
        "🤖 **[Anis-AI]:** Academic Timeline:\n\n"
        "🎓 **Computer Engineering (2025-2028):** École Polytechnique de Sousse. Focus on AI/ML/NLP.\n"
        "🎓 **Integrated Preparatory Studies (2023-2025):** École Polytechnique de Sousse. Math & Physics core.\n"
        "🎓 **Baccalauréat in Sciences (2022-2023):** Lycée Les Lumières Sousse."
    ),
    "contact": (
        "🤖 **[Anis-AI]:** Communication Linkups:\n\n"
        "📧 Email: anismselmi490@gmail.com\n"
        "📞 Mobile: +216 25 141 636\n"
        "📍 Sousse, Tunisia"
    ),
    "cv": (
        "🤖 **[Anis-AI]:** Professional Dossier:\n\n"
        "🔗 **[Click here to view my CV on Canva](https://canva.link/cmn3h8sq33jeuib)**"
    ),
    "community": (
        "🤖 **[Anis-AI]:** Leadership & Community roles:\n\n"
        "▪ **Web Master:** IEEE SIGHT EPS Student Branch.\n"
        "▪ **Ambassador:** NPC 2.0 PolyRobots, IEEE YESIST12, IEEE Smart Cities.\n"
        "▪ **Organizer:** Twise Night, IEEE Tejmaana, TCPC, IEEE Day."
    )
}

def get_gemini_api_response(query: str, api_key: str) -> str | None:
    """
    Attempts to use GenAI model with full portfolio context for advanced RAG conversations.
    """
    if not HAS_GENAI:
        return None
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-1.5-flash")
        
        # Crafting highly targeted query prompt
        prompt = (
            f"Context about Anis Mselmi:\n{GROUNDING_CONTEXT}\n\n"
            f"User query: '{query}'\n\n"
            f"Respond concisely as Anis's AI twin. Use bullet points or markdown bolding where helpful."
        )
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"⚠️ [RAG Failover]: API error: {str(e)}. Switching to local intent matcher."

def get_ai_response(query: str) -> str:
    """
    Orchestrates command parsing, live Gemini LLM API evaluation, and high-precision local fuzzy intent matching.
    """
    q = query.lower().strip()
    
    # 1. System Command Parsing
    if q.startswith("/"):
        cmd = q.split()[0]
        if cmd == "/help":
            return KNOWLEDGE_BASE["help"]
        elif cmd == "/skills":
            return KNOWLEDGE_BASE["skills"]
        elif cmd == "/projects":
            return KNOWLEDGE_BASE["projects_all"]
        elif cmd == "/cv":
            return KNOWLEDGE_BASE["cv"]
        elif cmd == "/contact":
            return KNOWLEDGE_BASE["contact"]
        elif cmd == "/about":
            return KNOWLEDGE_BASE["about"]
        else:
            return f"🤖 [System error]: Command '{cmd}' not recognized. Type `/help` for menu."

    # 2. Live API RAG Fallback
    # Check both environment and Streamlit secrets for Gemini API Key
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        try:
            import streamlit as st
            api_key = st.secrets.get("GEMINI_API_KEY") or st.secrets.get("gemini_api_key")
        except Exception:
            pass

    if api_key:
        api_res = get_gemini_api_response(query, api_key)
        if api_res:
            return api_res

    # 3. High-Precision Fuzzy Keyword Intent Matcher
    intent_keywords = {
        "greeting": ["hi", "hello", "hey", "greetings", "start", "welcome"],
        "smartpark": ["smartpark", "smart park", "parking", "license", "car", "plate", "vision", "opencv", "alpr"],
        "dewejen": ["dewejen", "stock", "management", "mysql", "inventory", "database"],
        "burgerdash": ["burgerdash", "burger dash", "game", "pygame", "2d game", "arcade"],
        "coffee": ["coffee", "brewstone", "shop", "front-end", "web app", "ui", "frontend"],
        "rag": ["rag", "vector", "retrieval", "chunking", "langchain", "llamaindex", "embeddings", "agent"],
        "projects_all": ["project", "portfolio", "build", "work", "apps", "code", "github"],
        "skills": ["skill", "stack", "technology", "language", "python", "scikit", "ai", "ml", "deep learning", "programming", "c++"],
        "education": ["school", "study", "education", "university", "polytechnique", "preparatory", "bac", "degree"],
        "contact": ["contact", "email", "phone", "reach", "message", "call", "address", "location"],
        "cv": ["cv", "resume", "canva", "pdf", "hire"],
        "community": ["ieee", "sight", "ambassador", "organizer", "community", "event", "club", "association", "twise", "volunteer"]
    }

    best_intent = None
    max_matches = 0

    # Tokenize input query
    words = re.findall(r"\b\w+\b", q)

    for intent, keywords in intent_keywords.items():
        matches = 0
        for word in words:
            # Direct keyword match or fuzzy keyword similarity match
            matches += sum(1 for kw in keywords if word == kw or difflib.SequenceMatcher(None, word, kw).ratio() > 0.82)
        
        if matches > max_matches:
            max_matches = matches
            best_intent = intent

    if best_intent and max_matches > 0:
        return KNOWLEDGE_BASE[best_intent]

    # Specific profile matching override
    if any(k in q for k in ["who are you", "about", "anis", "mselmi", "profile", "tell me about"]):
        return KNOWLEDGE_BASE["about"]

    # Generous general fallback
    return (
        "🤖 **[Anis-AI]:** Interesting inquiry! While my local failsafe system didn't locate a precise match, "
        "Anis can customize a professional LLM RAG engine to easily parse this request.\n\n"
        "💡 **Tip:** Set the `GEMINI_API_KEY` in Streamlit's secrets file or environment to give this AI Agent "
        "unlimited, real-time knowledge! Try querying **projects**, **skills**, or **CV**."
    )
