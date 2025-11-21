from dotenv import load_dotenv

load_dotenv()

import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.core.logging.logging_config import setup_logging
from src.core.logging.sentry import init_sentry

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan events."""
    init_sentry()
    setup_logging()
    logger.info("Application starting up...")
    yield
    logger.info("Application shutting down...")


app = FastAPI(
    title="Lab 16-22 Project",
    description="Lab project with logging, tests, linter, CI/CD with Pre-commit",
    version="0.1.0",
    lifespan=lifespan,
)


@app.get("/")
async def read_root():
    """Root endpoint."""
    logger.info("Root endpoint accessed")
    return {"message": "Welcome to Lab 16-22!", "status": "running"}


@app.get("/healthcheck")
async def healthcheck():
    """Health check endpoint."""
    logger.info("Health check called")
    return {"status": "ok", "message": "Service is running"}


@app.get("/time")
async def get_time():
    """Get server time."""
    from datetime import datetime

    now = datetime.now()
    logger.info(f"Time endpoint accessed at {now}")
    return {"server_time": now.isoformat()}


@app.get("/sentry-debug")
async def trigger_error():
    """Test endpoint to trigger Sentry error tracking."""
    logger.error("Triggering manual Sentry exception")
    division_by_zero = 1 / 0
    return {"division_by_zero": division_by_zero}
