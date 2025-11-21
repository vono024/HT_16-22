import logging
import os

import sentry_sdk
from sentry_sdk.integrations.fastapi import FastApiIntegration
from sentry_sdk.integrations.logging import LoggingIntegration
from sentry_sdk.integrations.starlette import StarletteIntegration


def init_sentry() -> None:
    """Initialize Sentry monitoring with integrations."""
    sentry_dsn = os.getenv("SENTRY_DSN")

    if not sentry_dsn:
        print("WARNING: SENTRY_DSN not found in environment variables")
        return

    print(f"Initializing Sentry with DSN: {sentry_dsn[:30]}...")

    sentry_sdk.init(
        dsn=sentry_dsn,
        integrations=[
            FastApiIntegration(),
            StarletteIntegration(),
            LoggingIntegration(level=logging.INFO, event_level=logging.ERROR),
        ],
        traces_sample_rate=1.0,
        profiles_sample_rate=1.0,
        debug=True,
    )

    print("Sentry initialized successfully!")
