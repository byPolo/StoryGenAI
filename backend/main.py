from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.config import settings
from routers import story, job

app = FastAPI(
    title = "StoryGenAI",
    description="API to generate stories in a game style format",
    version="0.1.00",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.add_middleware( #This middle wear allows ceraing URL to interact with our backend(Later this is how we connect our API to the frontend)
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(story.router, prefix=settings.API_PREFIX)
app.include_router(job.router, prefix= settings.API_PREFIX)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True) 
