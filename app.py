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
        "skills, experience, education, certifications, projects, "
        "Python, SQL, Power BI, AWS, or portfolio."
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
                "Hey! I'm Momo. What would you like to know about Shaileja?",
                "Yo. Portfolio assistant online. What can I help you explore?",
                "Hey there. Ask me about Shaileja's projects, experience, or skills.",
            ]
        )

    elif "how are you" in query:
        reply = "I'm just a bunch of code, but emotionally? Thriving."

    elif "who are you" in query or "what are you" in query:
        reply = (
            "I'm Momo, Shaileja's voice-enabled portfolio assistant. "
            "I can answer questions about her experience, technical skills, "
            "projects, education, certifications, and portfolio."
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
    ):
        reply = (
            "Shaileja Kuthuru is a software and systems-focused technology "
            "professional with experience in Python, SQL, AWS, automation, "
            "data analytics, business intelligence, application troubleshooting, "
            "and technical problem solving."
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
            "Shaileja has worked as an IT Systems Analyst at Ventois, "
            "a Data Analyst at NeoTech Cloud, and previously completed "
            "a System Analysis internship at DRDO."
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
            "from Clark University and a bachelor's degree in Electronics "
            "and Communication Engineering from Gurunanak Institute of Technology. "
            "She is currently pursuing a Doctor of Education in Leadership "
            "and Artificial Intelligence at Anderson University."
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
            "Shaileja holds the AWS Certified Solutions Architect Associate, "
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
    ):
        reply = (
            "Shaileja works with Python, SQL, MySQL, Power BI, DAX, "
            "Power Query, AWS, Git, automation, data validation, "
            "application troubleshooting, analytics, and business intelligence."
        )

    elif "python" in query:
        reply = (
            "Shaileja uses Python for automation, data analysis, "
            "data validation, preprocessing, troubleshooting workflows, "
            "and application development."
        )

    elif "sql" in query:
        reply = (
            "Shaileja uses SQL for data analysis, troubleshooting, "
            "data validation, KPI reporting, customer analytics, and "
            "working with datasets containing more than 100,000 records."
        )

    elif "power bi" in query or "powerbi" in query:
        reply = (
            "Shaileja uses Power BI for dashboard development, "
            "KPI reporting, visualization, DAX calculations, "
            "and Power Query transformations."
        )

    elif "aws" in query:
        reply = (
            "Shaileja has experience with AWS services including "
            "S3, EC2, and RDS across systems, analytics, cloud, "
            "and reporting workflows."
        )

    # -------------------------------------------------
    # PROJECTS
    # -------------------------------------------------

    elif "documind" in query or "rag" in query:
        reply = (
            "DocuMind AI is Shaileja's local multi-document RAG assistant. "
            "It supports semantic document retrieval, conversational question answering, "
            "local LLM inference, and source-aware answers with filename "
            "and page-level citations."
        )

    elif "amazon" in query:
        reply = (
            "The Amazon Sales Analysis project uses SQL, Power BI, DAX, "
            "and Power Query to analyze sales performance. It includes "
            "KPIs such as YTD sales, QTD sales, products sold, "
            "and customer-review metrics."
        )

    elif "customer behavior" in query:
        reply = (
            "The Customer Behavior Analysis project uses Python, SQL, "
            "and Power BI to analyze transactional retail data, "
            "customer segments, purchasing patterns, and business trends."
        )

    elif (
        "e-commerce" in query
        or "ecommerce" in query
        or "rfm" in query
    ):
        reply = (
            "The E-Commerce Customer Purchase Behavior Analysis project "
            "uses Python, SQL, and MySQL for RFM segmentation, churn patterns, "
            "monthly sales trends, category performance, and retention analysis."
        )

    elif "zomato" in query:
        reply = (
            "The Zomato Data Analysis project uses Python and exploratory "
            "data analysis to identify restaurant trends, customer preferences, "
            "and useful business insights."
        )

    elif "momo" in query:
        reply = (
            "That's me. Momo started as a Flask-based portfolio assistant "
            "and later evolved into a React and Next.js assistant integrated "
            "directly into Shaileja's production portfolio."
        )

    elif (
        "projects" in query
        or "portfolio projects" in query
        or "what has she built" in query
    ):
        reply = (
            "Shaileja's projects include Momo, DocuMind AI, "
            "Customer Behavior Analysis, E-Commerce Customer Purchase "
            "Behavior Analysis, Amazon Sales Analysis, and Zomato Data Analysis."
        )

    # -------------------------------------------------
    # IMPACT
    # -------------------------------------------------

    elif (
        "impact" in query
        or "achievement" in query
        or "achievements" in query
    ):
        reply = (
            "Shaileja has worked with datasets containing more than "
            "100,000 records, built Python automation that reduced repetitive "
            "manual work, developed analytical dashboards, and supported "
            "technical stakeholders across multiple business functions."
        )

    # -------------------------------------------------
    # PORTFOLIO ACTIONS
    # -------------------------------------------------

    elif "portfolio" in query or "website" in query:
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
        reply = "Opening Shaileja's resume."
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
            "Alright. I'll go vibe in the cloud. "
            "Thanks for exploring Shaileja's portfolio."
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
                "reply": "Say something. I'm listening.",
                "action": None,
            }
        )

    result = handle_intent(user_text)

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)