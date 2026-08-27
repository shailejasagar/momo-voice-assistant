from flask import Flask, render_template, request, jsonify
import datetime
import random

ASSISTANT_NAME = "momo"

app = Flask(__name__)


PORTFOLIO_DATA = {
    "name": "Shaileja Kuthuru",
    "portfolio": "https://www.shailejak.com",
    "github": "https://github.com/shailejasagar",
    "linkedin": "https://www.linkedin.com/in/shailejakuthuru123",
    "email": "kuthurushaileja@gmail.com",
    "resume": "https://www.shailejak.com/Shaileja_Kuthuru_Resume.pdf",
}


def random_reply(items):
    return random.choice(items)


def handle_intent(query: str):
    """
    Process a visitor question and return
    Momo's response plus an optional browser action.
    """

    query = query.lower().strip()

    reply = (
        "I'm still learning that one. Try asking about Shaileja's "
        "software engineering experience, AI projects, RAG, technical skills, "
        "education, certifications, AWS, Python, SQL, or portfolio."
    )

    action = None

    # -------------------------------------------------
    # REMOVE WAKE WORD
    # -------------------------------------------------

    query = query.replace(ASSISTANT_NAME, "").strip() or query

    # -------------------------------------------------
    # GREETINGS
    # -------------------------------------------------

    if query in ["hello", "hi", "hey"] or query.startswith(
        ("hello ", "hi ", "hey ")
    ):
        reply = random_reply(
            [
                "Hey! I'm Momo. Ask me about Shaileja's software, AI projects, experience, or technical skills.",
                "Hey there. I'm Momo, Shaileja's interactive portfolio assistant. What would you like to explore?",
                "Momo online. Ask me about DocuMind AI, Shaileja's experience, skills, projects, or education.",
            ]
        )

    elif "how are you" in query:
        reply = (
            "Running smoothly and ready to talk software, AI, and "
            "everything Shaileja has been building."
        )

    elif "who are you" in query or "what are you" in query:
        reply = (
            "I'm Momo 2.0, Shaileja's voice-enabled portfolio assistant. "
            "I help visitors explore her software engineering experience, "
            "Generative AI and RAG projects, technical skills, education, "
            "certifications, resume, and professional links."
        )

    # -------------------------------------------------
    # DATE / TIME
    # -------------------------------------------------

    elif (
        "date" in query
        or "what day" in query
        or "today" in query
    ):
        today = datetime.datetime.now().strftime(
            "%A, %B %d, %Y"
        )

        reply = f"Today is {today}."

    elif "time" in query:
        now = datetime.datetime.now().strftime(
            "%I:%M %p"
        )

        reply = f"It's currently {now}."

    # -------------------------------------------------
    # ABOUT SHAILEJA
    # -------------------------------------------------

    elif (
        "who is shaileja" in query
        or "about shaileja" in query
        or "tell me about shaileja" in query
        or "what does shaileja do" in query
    ):
        reply = (
            "Shaileja Kuthuru is a software engineer and technology professional "
            "with hands-on experience in Python, SQL, AWS, automation, application "
            "development, and data-driven systems. Her current technical focus "
            "includes Generative AI, Retrieval-Augmented Generation, semantic "
            "search, embeddings, local LLM applications, and intelligent software. "
            "Her projects include DocuMind AI and Momo 2.0."
        )

    # -------------------------------------------------
    # CURRENT FOCUS
    # -------------------------------------------------

    elif (
        "current focus" in query
        or "what is she learning" in query
        or "what is she focused on" in query
        or "ai focus" in query
    ):
        reply = (
            "Shaileja is currently focused on software engineering and "
            "AI application development, particularly Generative AI, "
            "Retrieval-Augmented Generation, semantic retrieval, local LLMs, "
            "Python applications, cloud technologies, and modern web development."
        )

    # -------------------------------------------------
    # EXPERIENCE
    # -------------------------------------------------

    elif (
        "experience" in query
        or "work history" in query
        or "where has she worked" in query
    ):
        reply = (
            "Shaileja's experience includes working as a Software Engineer "
            "and Analyst at Ventois, a Data Analyst at NeoTech Cloud, and "
            "a System Analysis Intern at DRDO. Her work has included Python "
            "and SQL development, automation, application troubleshooting, "
            "AWS workflows, data analytics, reporting, and technical collaboration."
        )

    elif "ventois" in query:
        reply = (
            "At Ventois, Shaileja worked as a Software Engineer and Analyst. "
            "She used Python and SQL to support application troubleshooting "
            "and data-validation workflows, automated recurring analysis and "
            "reporting tasks, investigated technical issues, supported AWS-based "
            "workflows, and explored responsible uses of Generative AI for "
            "code analysis, documentation, debugging, and information retrieval."
        )

    elif (
        "neotech" in query
        or "neo tech" in query
    ):
        reply = (
            "At NeoTech Cloud, Shaileja worked as a Data Analyst using SQL, "
            "Python, AWS, and Power BI. Her work included e-commerce reporting, "
            "KPI development, dashboard creation, stakeholder collaboration, "
            "data-quality investigation, and Python-based reporting automation."
        )

    elif "drdo" in query:
        reply = (
            "During her System Analysis internship at DRDO, Shaileja used "
            "Python for data preprocessing and analysis, supported data-cleaning "
            "and validation standards, and investigated recurring dataset-quality "
            "issues such as missing values and duplicates."
        )

    # -------------------------------------------------
    # EDUCATION
    # -------------------------------------------------

    elif (
        "education" in query
        or "degree" in query
        or "university" in query
        or "college" in query
    ):
        reply = (
            "Shaileja earned a Master of Science in Information Technology "
            "from Clark University with a 3.67 GPA and a bachelor's degree "
            "in Electronics and Communication Engineering from Gurunanak "
            "Institute of Technology. She is pursuing a Doctor of Education "
            "in Leadership and Artificial Intelligence at Anderson University."
        )

    # -------------------------------------------------
    # CERTIFICATIONS
    # -------------------------------------------------

    elif (
        "certification" in query
        or "certified" in query
        or "credentials" in query
    ):
        reply = (
            "Shaileja holds the AWS Certified Solutions Architect – Associate, "
            "AWS Certified Cloud Practitioner, and IBM Data Science "
            "Professional Certificate credentials."
        )

    # -------------------------------------------------
    # SKILLS
    # -------------------------------------------------

    elif (
        "skills" in query
        or "technologies" in query
        or "tech stack" in query
        or "technical skills" in query
    ):
        reply = (
            "Shaileja's technical stack includes Python, SQL, MySQL, JavaScript, "
            "TypeScript, React, Next.js, Flask, REST APIs, Git, and AWS. "
            "Her AI skills include Retrieval-Augmented Generation, LLM applications, "
            "semantic search, embeddings, prompt engineering, Ollama, and local "
            "LLM inference. She also works with Power BI, DAX, Power Query, "
            "automation, data transformation, and exploratory data analysis."
        )

    # -------------------------------------------------
    # AI / GENERATIVE AI
    # -------------------------------------------------

    elif (
        "generative ai" in query
        or "gen ai" in query
        or "genai" in query
        or "artificial intelligence" in query
        or "ai skills" in query
    ):
        reply = (
            "Shaileja's Generative AI work focuses on building practical "
            "LLM-powered applications. She has hands-on project experience "
            "with Retrieval-Augmented Generation, semantic embeddings, "
            "similarity-based retrieval, prompt engineering, local LLM inference, "
            "source-grounded responses, and conversational AI."
        )

    elif (
        "rag" in query
        or "retrieval augmented generation" in query
    ):
        reply = (
            "Shaileja has hands-on experience implementing Retrieval-Augmented "
            "Generation through DocuMind AI. The system processes documents, "
            "creates semantic embeddings, retrieves relevant chunks using "
            "similarity search, sends grounded context to a local language model, "
            "and returns answers with filename and page-level citations."
        )

    elif "embedding" in query or "semantic search" in query:
        reply = (
            "Shaileja uses semantic embeddings and similarity-based retrieval "
            "in DocuMind AI to identify document chunks that are most relevant "
            "to a user's question before sending that context to the language model."
        )

    elif (
        "ollama" in query
        or "local llm" in query
        or "gemma" in query
    ):
        reply = (
            "Shaileja has used Ollama for local LLM inference in DocuMind AI, "
            "allowing the RAG workflow to generate conversational answers locally "
            "while grounding responses in retrieved document content."
        )

    # -------------------------------------------------
    # PROGRAMMING / SOFTWARE
    # -------------------------------------------------

    elif "python" in query:
        reply = (
            "Python is one of Shaileja's primary technologies. She uses it "
            "for application development, RAG pipelines, automation, data analysis, "
            "data validation, preprocessing, troubleshooting, and backend development."
        )

    elif "sql" in query:
        reply = (
            "Shaileja uses SQL for data analysis, application troubleshooting, "
            "data validation, KPI reporting, customer analytics, and working "
            "with large structured datasets."
        )

    elif (
        "react" in query
        or "next.js" in query
        or "nextjs" in query
        or "typescript" in query
    ):
        reply = (
            "Shaileja uses React, Next.js, and TypeScript in her portfolio "
            "development work. Momo 2.0 is integrated into her Next.js portfolio "
            "to provide an interactive AI-inspired experience for visitors."
        )

    elif "flask" in query:
        reply = (
            "Shaileja uses Flask for lightweight Python backend development. "
            "Momo's backend uses Flask to process portfolio questions and return "
            "responses and browser actions through a REST-style chat endpoint."
        )

    elif (
        "rest api" in query
        or "api" in query
    ):
        reply = (
            "Shaileja has experience building and integrating REST-style APIs. "
            "For example, Momo connects its frontend interaction layer to a "
            "Python Flask backend through a JSON-based chat endpoint."
        )

    elif "power bi" in query or "powerbi" in query:
        reply = (
            "Shaileja uses Power BI for dashboard development, KPI reporting, "
            "data visualization, DAX calculations, and Power Query transformations."
        )

    elif "aws" in query:
        reply = (
            "Shaileja has experience with AWS services including S3, EC2, "
            "and RDS across cloud, application, analytics, and reporting workflows. "
            "She also holds both AWS Solutions Architect – Associate and "
            "AWS Cloud Practitioner certifications."
        )

    # -------------------------------------------------
    # DOCUMIND AI
    # -------------------------------------------------

    elif "documind" in query:
        reply = (
            "DocuMind AI is Shaileja's multi-document Retrieval-Augmented "
            "Generation assistant built with Python, Streamlit, and Ollama. "
            "It processes PDF documents, creates semantic embeddings, performs "
            "similarity-based retrieval, uses local LLM inference for conversational "
            "question answering, and produces source-grounded responses with "
            "filename and page-level citations."
        )

    # -------------------------------------------------
    # MOMO
    # -------------------------------------------------

    elif (
        "momo 2.0" in query
        or "momo project" in query
        or "tell me about momo" in query
    ):
        reply = (
            "Momo 2.0 is Shaileja's voice-enabled portfolio assistant. "
            "It combines a Python and Flask backend with intent-based query "
            "processing, REST API communication, browser speech recognition, "
            "speech synthesis, and integration with her React and Next.js portfolio. "
            "Visitors can use Momo to explore her experience, skills, projects, "
            "education, certifications, resume, and professional links."
        )

    # -------------------------------------------------
    # ANALYTICS PROJECTS
    # -------------------------------------------------

    elif "amazon" in query:
        reply = (
            "Shaileja's Amazon Sales Analysis project uses SQL, Power BI, "
            "DAX, and Power Query. She built data-transformation and modeling "
            "workflows along with interactive KPIs for YTD and QTD sales, "
            "products sold, customer reviews, and product performance."
        )

    elif "customer behavior" in query:
        reply = (
            "The Customer Behavior Analysis project uses Python, SQL, and "
            "Power BI to analyze transactional retail data, customer segments, "
            "purchasing behavior, and business trends."
        )

    elif (
        "e-commerce" in query
        or "ecommerce" in query
        or "rfm" in query
    ):
        reply = (
            "The E-Commerce Customer Purchase Behavior Analysis project "
            "uses Python, SQL, and MySQL. It applies RFM segmentation and "
            "analyzes customer recency, sales trends, category performance, "
            "churn patterns, and retention opportunities."
        )

    elif "zomato" in query:
        reply = (
            "The Zomato Data Analysis project uses Python and exploratory "
            "data analysis to investigate restaurant trends, customer preferences, "
            "and business patterns."
        )

    # -------------------------------------------------
    # ALL PROJECTS
    # -------------------------------------------------

    elif (
        "projects" in query
        or "portfolio projects" in query
        or "what has she built" in query
        or "what did she build" in query
    ):
        reply = (
            "Shaileja's featured projects include DocuMind AI, a multi-document "
            "RAG assistant; Momo 2.0, a voice-enabled portfolio assistant; "
            "Amazon Sales Analysis; Customer Behavior Analysis; "
            "E-Commerce Customer Purchase Behavior Analysis; and "
            "Zomato Data Analysis. Her newer projects emphasize software "
            "engineering and Generative AI while her analytics projects "
            "demonstrate strong Python, SQL, and business intelligence skills."
        )

    # -------------------------------------------------
    # IMPACT / STRENGTHS
    # -------------------------------------------------

    elif (
        "impact" in query
        or "achievement" in query
        or "achievements" in query
    ):
        reply = (
            "Shaileja has worked with datasets containing more than 100,000 "
            "records, automated recurring analysis and reporting workflows, "
            "reduced repetitive manual analysis, developed dashboards and "
            "data-driven systems, and built AI applications including "
            "a RAG document assistant and a voice-enabled portfolio assistant."
        )

    elif (
        "strength" in query
        or "strengths" in query
        or "why hire" in query
        or "why should we hire" in query
    ):
        reply = (
            "Shaileja combines software development, cloud, data, and emerging "
            "Generative AI skills. Her background spans Python, SQL, AWS, "
            "application troubleshooting, automation, analytics, and hands-on "
            "AI projects, giving her the ability to approach problems from both "
            "software and data perspectives."
        )

    # -------------------------------------------------
    # TARGET ROLES
    # -------------------------------------------------

    elif (
        "role" in query
        or "roles" in query
        or "opportunities" in query
        or "looking for" in query
        or "job" in query
    ):
        reply = (
            "Shaileja is interested in opportunities across software engineering, "
            "AI application development, Generative AI, cloud engineering, "
            "and data-driven technology roles where she can continue building "
            "practical intelligent systems."
        )

    # -------------------------------------------------
    # PORTFOLIO ACTIONS
    # -------------------------------------------------

    elif (
        "portfolio" in query
        or "website" in query
    ):
        reply = "Opening Shaileja's portfolio."
        action = "open_portfolio"

    elif "github" in query:
        reply = "Opening Shaileja's GitHub."
        action = "open_github"

    elif "linkedin" in query:
        reply = "Opening Shaileja's LinkedIn profile."
        action = "open_linkedin"

    elif (
        "resume" in query
        or "cv" in query
    ):
        reply = "Opening Shaileja's updated resume."
        action = "open_resume"

    elif (
        "contact" in query
        or "email" in query
        or "reach shaileja" in query
    ):
        reply = (
            "You can contact Shaileja at "
            "kuthurushaileja@gmail.com."
        )

        action = "open_email"

    # -------------------------------------------------
    # PERSONALITY
    # -------------------------------------------------

    elif (
        "motivate me" in query
        or "motivation" in query
    ):
        reply = random_reply(
            [
                "Future you is cheering for present you. Keep going.",
                "Progress beats perfection. Ship something useful today.",
                "You don't need to know everything. You need to keep learning.",
            ]
        )

    elif (
        "joke" in query
        or "make me laugh" in query
    ):
        reply = random_reply(
            [
                "Why do programmers prefer dark mode? Because light attracts bugs.",
                "I was going to tell you a UDP joke, but you might not get it.",
                "Why did the computer arrive late? It had a hard drive.",
            ]
        )

    elif any(
        word in query
        for word in [
            "bye",
            "goodbye",
            "see you",
        ]
    ):
        reply = (
            "Thanks for exploring Shaileja's portfolio. "
            "I'll be here if you want to talk software, AI, or projects again."
        )

    return {
        "reply": reply,
        "action": action,
    }


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json() or {}

    user_text = data.get(
        "text",
        "",
    ).strip()

    if not user_text:
        return jsonify(
            {
                "reply": "Ask me something about Shaileja. I'm listening.",
                "action": None,
            }
        )

    result = handle_intent(user_text)

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)