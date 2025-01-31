from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()

focus_tips = [
    "Use the Pomodoro technique: 25 min work, 5 min break.",
    "Try deep work: 90 minutes of focused work, 30 min break.",
    "Turn off notifications for better concentration.",
    "Work near natural light to stay alert.",
]

quick_hacks = [
    "Use the '2-minute rule' – if it takes less than 2 mins, do it now.",
    "Write down 3 tasks before bed for a productive tomorrow.",
    "Listen to instrumental music to boost focus.",
    "Use 'Eisenhower Matrix' – prioritize tasks by urgency & importance.",
]

daily_challenges = [
    "No social media for 24 hours.",
    "Wake up 1 hour earlier and plan your day.",
    "Write down 10 new ideas today.",
    "Try working in 90-minute focused blocks."
]

user_hacks = []

class Hack(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "Welcome to RaspAPI - Your Productivity & Life Hacks API!"}

@app.get("/focus-tips")
def get_focus_tip():
    return {"focus_tip": random.choice(focus_tips)}

@app.get("/quick-hacks")
def get_quick_hack():
    return {"quick_hack": random.choice(quick_hacks)}

@app.get("/daily-challenge")
def get_daily_challenge():
    return {"daily_challenge": random.choice(daily_challenges)}

@app.post("/submit-hack")
def submit_hack(hack: Hack):
    user_hacks.append(hack.text)
    return {"message": "Hack added!", "your_hack": hack.text}

