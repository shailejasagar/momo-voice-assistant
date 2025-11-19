from flask import Flask, render_template, request, jsonify
import datetime
import random

ASSISTANT_NAME = "momo"

app = Flask(__name__)


def handle_intent(query: str):
    """Return Momo's reply text and an optional action for the browser."""
    query = query.lower()
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
        reply = f"I’m {ASSISTANT_NAME.capitalize()}, your chill web assistant. I exist to make your life 0.01 percent easier."

    # ---- TIME ----
    elif "time" in query:
        now = datetime.datetime.now().strftime("%I:%M %p")
        reply = f"It's {now}. Time is fake, but still."

    # ---- OPEN WEBSITES (via browser actions) ----
    elif "open youtube" in query:
        reply = "Opening YouTube in a new tab. Don't get lost there."
        action = "open_youtube"

    elif "open google" in query:
        reply = "Opening Google. Ask the big brain of the internet."
        action = "open_google"

    elif "open github" in query:
        reply = "Opening GitHub. Time to pretend we write bug-free code."
        action = "open_github"

    # ---- NOTES (very simple: just pretend for now, or you can store later) ----
    elif "motivate me" in query or "motivation" in query:
        lines = [
            "You’ve survived every bad day so far. That’s a 100 percent success rate.",
            "Future you is cheering for present you. Don’t let them down.",
            "You’re more capable than you think. And I think you’re awesome."
        ]
        reply = random.choice(lines)

    elif "tell me a joke" in query or "make me laugh" in query:
        jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs.",
            "I was going to tell you a UDP joke, but you might not get it.",
            "Why did the computer show up at work late? It had a hard drive."
        ]
        reply = random.choice(jokes)

    elif any(word in query for word in ["bye", "goodbye", "see you"]):
        reply = "Alright, I’ll go vibe in the cloud. Bye boss."

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
