
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .config import settings
from .routers import health, emotion, chat

app = FastAPI(title="Neuro Sense Buddy 2024", version="1.0.0")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins if settings.cors_origins != ["*"] else ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(health.router)
app.include_router(emotion.router)
app.include_router(chat.router)

@app.get("/")
async def root():
    return {"message": "Neuro Sense Buddy is alive. See /docs for API."}
