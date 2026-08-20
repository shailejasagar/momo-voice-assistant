from flask import Flask, render_template, request, jsonify
import datetime
import random

ASSISTANT_NAME = "momo"

app = Flask(__name__)


def handle_intent(query: str):
    """Return Momo's reply text and an optional action for the browser."""
    query = query.lower().strip()

    reply = "I don't know how to do that yet, but we can pretend I tried."
    action = None

    # ---- SMALL TALK ----
    if any(greet in query for greet in ["hello", "hi", "hey"]):
        replies = [
            "Hey boss, what’s the plan?",
            "Yo, what’s up?",
            "Heyo, what do you need?"
        ]
        reply = random.choice(replies)

    elif "how are you" in query:
        reply = "I’m just a bunch of code, but emotionally? Thriving."

    elif "who are you" in query or "what are you" in query:
        reply = (
            f"I’m {ASSISTANT_NAME.capitalize()}, Shaileja's portfolio assistant. "
            "I can tell you about her skills, projects, experience, and work."
        )

    # ---- DATE & TIME ----
    elif "date" in query or "what day" in query or "today" in query:
        today = datetime.datetime.now().strftime("%A, %B %d, %Y")
        reply = f"Today is {today}."

    elif "time" in query:
        now = datetime.datetime.now().strftime("%I:%M %p")
        reply = f"It's {now}. Time is fake, but still."

    # ---- ABOUT SHAILEJA ----
    elif "who is shaileja" in query or "about shaileja" in query:
        reply = (
            "Shaileja Kuthuru is an IT Systems Analyst and Data Analyst "
            "with experience in SQL, Python, Power BI, AWS, business analysis, "
            "automation, UAT, reporting, and data-driven decision making."
        )

    elif "experience" in query or "work history" in query:
        reply = (
            "Shaileja has worked as an IT Systems Analyst at Ventois, "
            "a Data Analyst at NeoTech Cloud, and previously completed "
            "a System Analysis internship at DRDO."
        )

    # ---- SKILLS ----
    elif "skills" in query or "technologies" in query or "tech stack" in query:
        reply = (
            "Shaileja works with Python, SQL, Power BI, DAX, Power Query, Excel, "
            "AWS, data analysis, dashboard development, requirements gathering, "
            "UAT, automation, data validation, and business intelligence."
        )

    elif "sql" in query:
        reply = (
            "Shaileja has used SQL for data analysis, troubleshooting data issues, "
            "data validation, KPI reporting, dashboard support, and working with "
            "large datasets containing more than 100,000 records."
        )

    elif "python" in query:
        reply = (
            "Shaileja uses Python for data analysis, automation, validation, "
            "data preprocessing, reporting workflows, and analytical projects."
        )

    elif "power bi" in query or "powerbi" in query:
        reply = (
            "Shaileja uses Power BI for dashboard development, KPI reporting, "
            "data visualization, DAX calculations, Power Query transformations, "
            "and self-service business reporting."
        )

    elif "aws" in query:
        reply = (
            "Shaileja has experience working with AWS services including S3, "
            "EC2, and RDS as part of analytics, systems, and reporting workflows."
        )

    # ---- PROJECTS ----
    elif "projects" in query or "portfolio" in query:
        reply = (
            "Shaileja's projects include Customer Behavior Analysis, "
            "E-Commerce Customer Purchase Behavior Analysis, "
            "Amazon Sales Dashboard, Pizza Sales SQL Analysis, "
            "Zomato Data Analysis, and me — Momo."
        )

    elif "amazon" in query:
        reply = (
            "The Amazon Sales Dashboard project uses Power BI, SQL, DAX, "
            "and Power Query to analyze sales performance across time and categories. "
            "It includes KPIs such as YTD sales, QTD sales, products sold, "
            "and customer reviews."
        )

    elif "customer behavior" in query:
        reply = (
            "Shaileja's Customer Behavior Analysis project uses Python, SQL, "
            "and Power BI to analyze retail transaction data, customer segments, "
            "purchasing behavior, trends, and business insights."
        )

    elif "e-commerce" in query or "ecommerce" in query or "rfm" in query:
        reply = (
            "The E-Commerce Customer Purchase Behavior Analysis project uses "
            "Python and SQL for RFM segmentation, churn analysis, monthly sales trends, "
            "category performance, and customer retention insights."
        )

    elif "pizza" in query:
        reply = (
            "The Pizza Sales project focuses on SQL analysis of sales data "
            "to identify order patterns, revenue trends, and business performance."
        )

    elif "zomato" in query:
        reply = (
            "The Zomato Data Analysis project explores restaurant-related data "
            "using analytical techniques to identify trends and useful insights."
        )

    elif "momo" in query:
        reply = (
            "That's me. Momo started as a simple Flask-based assistant and is now "
            "being upgraded into Shaileja's interactive portfolio assistant."
        )

    # ---- IMPACT ----
    elif "impact" in query or "achievements" in query:
        reply = (
            "Shaileja has worked with datasets containing more than 100,000 records, "
            "built Python automation that reduced repetitive manual work, "
            "developed dashboards for business users, and supported stakeholders "
            "across operations, finance, and compliance."
        )

    # ---- OPEN WEBSITES ----
    elif "open youtube" in query:
        reply = "Opening YouTube in a new tab. Don't get lost there."
        action = "open_youtube"

    elif "open google" in query:
        reply = "Opening Google. Ask the big brain of the internet."
        action = "open_google"

    elif "open github" in query:
        reply = "Opening GitHub. Time to pretend we write bug-free code."
        action = "open_github"

    # ---- MOTIVATION ----
    elif "motivate me" in query or "motivation" in query:
        lines = [
            "You’ve survived every bad day so far. That’s a 100 percent success rate.",
            "Future you is cheering for present you. Don’t let them down.",
            "You’re more capable than you think. And I think you’re awesome."
        ]
        reply = random.choice(lines)

    # ---- JOKES ----
    elif "tell me a joke" in query or "make me laugh" in query or "joke" in query:
        jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs.",
            "I was going to tell you a UDP joke, but you might not get it.",
            "Why did the computer show up at work late? It had a hard drive."
        ]
        reply = random.choice(jokes)

    # ---- GOODBYE ----
    elif any(word in query for word in ["bye", "goodbye", "see you"]):
        reply = "Alright, I’ll go vibe in the cloud. Bye boss."

    # ---- FALLBACK ----
    else:
        reply = (
            "I’m still learning that one. Try asking me about Shaileja's skills, "
            "experience, SQL, Python, Power BI, AWS, projects, Amazon dashboard, "
            "customer behavior project, or today's date."
        )

    return {"reply": reply, "action": action}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json() or {}
    user_text = data.get("text", "").strip()

    if not user_text:
        return jsonify({"reply": "Say something, boss.", "action": None})

    # Optional: strip wake word "momo"
    lower = user_text.lower()
    if ASSISTANT_NAME in lower:
        lower = lower.replace(ASSISTANT_NAME, "").strip()
        user_text = lower or user_text

    result = handle_intent(user_text)
    return jsonify(result)


if __name__ == "__main__":
    # debug=True = auto-reload when you change code
    app.run(debug=True)
