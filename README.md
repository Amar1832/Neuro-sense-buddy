🤖 Neuro Sense Buddy 2024

Neuro Sense Buddy is a real-time emotion-aware chatbot that works with your webcam. It detects your emotions live using DeepFace, then adapts its replies with the Groq API and prompt engineering — making it feel less like a program and more like a supportive friend.

✨ Features

🎥 Webcam-based live detection (not just video analysis)

🎭 Facial emotion recognition in real time with DeepFace

🧠 Adaptive chatbot replies using Groq API (LLM responses)

🧩 Prompt engineering to tune tone & style to your mood

⚡ FastAPI backend with lightweight endpoints

📂 Project Structure
Neuro-sense-buddy-2024/
│
├── app/              
│
├── examples/         
│
├── tests/            
│
├── requirements.txt  
│
└── README.md         

⚡ Quickstart
git clone https://github.com/your-username/neuro-sense-buddy-2024.git
cd neuro-sense-buddy-2024
cp .env.example .env
pip install -r requirements.txt
uvicorn app.main:app --reload

🛠️ Tech Stack

Python

FastAPI

DeepFace

Groq API

OpenCV

Prompt Engineering

📜 License

Licensed under the MIT License – see the LICENSE file for details.

👉 This way it’s clear it’s not “video analytics,” but a live detection buddy that feels interactive and personal.
