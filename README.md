# RaspAPI - Productivity & Life Hacks API

## Overview
RaspAPI is a simple FastAPI-based web service that provides productivity tips, quick hacks, and daily challenges to improve focus and efficiency. Users can also submit their own hacks.

## Features
- Get random focus tips to enhance productivity.
- Retrieve quick hacks for life efficiency.
- Receive a daily challenge to push your limits.
- Submit your own productivity hacks.

## Installation
Ensure you have Python installed, then install FastAPI and Uvicorn:
```sh
pip install fastapi uvicorn
```

## Running the API
To start the FastAPI server, run:
```sh
uvicorn main:app --reload
```

## API Endpoints

### 1. Home Endpoint
**GET /**
- Returns a welcome message.

#### Example Request:
```sh
curl -X GET "http://127.0.0.1:8000/"
```
#### Response:
```json
{
  "message": "Welcome to RaspAPI - Your Productivity & Life Hacks API!"
}
```

### 2. Get a Random Focus Tip
**GET /focus-tips**
- Retrieves a random focus tip.

#### Example Request:
```sh
curl -X GET "http://127.0.0.1:8000/focus-tips"
```
#### Response:
```json
{
  "focus_tip": "Use the Pomodoro technique: 25 min work, 5 min break."
}
```

### 3. Get a Quick Hack
**GET /quick-hacks**
- Returns a random quick hack.

#### Example Request:
```sh
curl -X GET "http://127.0.0.1:8000/quick-hacks"
```
#### Response:
```json
{
  "quick_hack": "Write down 3 tasks before bed for a productive tomorrow."
}
```

### 4. Get a Daily Challenge
**GET /daily-challenge**
- Returns a randomly selected daily challenge.

#### Example Request:
```sh
curl -X GET "http://127.0.0.1:8000/daily-challenge"
```
#### Response:
```json
{
  "daily_challenge": "No social media for 24 hours."
}
```

### 5. Submit a Hack
**POST /submit-hack**
- Allows users to submit their own hacks.

#### Example Request:
```sh
curl -X POST "http://127.0.0.1:8000/submit-hack" -H "Content-Type: application/json" -d '{"text": "Drink water first thing in the morning."}'
```
#### Response:
```json
{
  "message": "Hack added!",
  "your_hack": "Drink water first thing in the morning."
}
```

