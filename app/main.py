from fastapi import FastAPI

app = FastAPI(
    title="GYM-X Backend",
    description="AI-based Sports Performance Analysis and Injury Prevention System",
    version="0.1.0",
)


@app.get("/health", tags=["system"])
def health_check() -> dict:
    """Return the current backend service status."""
    return {
        "status": "ok",
        "project": "GYM-X",
        "version": "0.1.0",
    }
