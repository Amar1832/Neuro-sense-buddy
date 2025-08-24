🤖 Neuro Sense Buddy 2024

An emotion-aware chatbot that integrates DeepFace for facial emotion recognition and Groq API for adaptive LLM responses. Built with FastAPI, OpenCV, and prompt engineering, it processes real-time inputs and tailors responses dynamically based on detected emotions, making interactions more human-like and empathetic.

✨ Features

🎭 Facial Emotion Recognition using DeepFace on images or video frames

🧠 Adaptive Chatbot Responses with Groq API powered by Llama models

⚡ Real-time Processing with asynchronous FastAPI backend

🧩 Prompt Engineering Layer to adjust tone/style based on detected emotions

🎥 OpenCV Integration for handling image & video input

🛠️ Configurable via .env for API keys and runtime settings

📂 Project Structure

Neuro-sense-buddy-2024/
├─ app/              # FastAPI backend (routers, services, utils)
├─ examples/         # Demo client & sample prompts
├─ tests/            # Basic test cases
├─ requirements.txt  # Dependencies
└─ README.md         # Project documentation


⚡ Quickstart
1. Clone & Setup
git clone https://github.com/Amar1832/Neuro-sense-buddy.git
cd Neuro-sense-buddy
cp .env.example .env

2. Add your keys

Edit .env and add:

GROQ_API_KEY=your_api_key_here

3. Install & Run
./run.sh


Server will run at: http://localhost:8000

Docs available at: http://localhost:8000/docs

🚀 Example Usage

Health Check

curl http://localhost:8000/health


Analyze Emotion (image upload)

curl -F "image=@face.jpg" http://localhost:8000/v1/emotion/analyze


Chat with Text

curl -X POST http://localhost:8000/v1/chat \
     -H "Content-Type: application/json" \
     -d '{"message":"Hello, I feel nervous"}'


Chat with Image + Text

curl -F "image=@face.jpg" -F "message=hi" \
     http://localhost:8000/v1/chat-with-image

🛠️ Tech Stack

Python

FastAPI

DeepFace (emotion recognition)

Groq API (LLM responses)

OpenCV

Prompt Engineering

📜 License

This project is licensed under the MIT License – see the LICENSE
 file for details.

⚡ Neuro Sense Buddy — an AI that not only talks, but listens to your emotions.
