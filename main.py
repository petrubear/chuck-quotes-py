from fastapi import FastAPI
from contextlib import asynccontextmanager
import httpx
from infrastructure.controller.quote_controller import router as quote_router
from infrastructure.configuration.config import Settings

@asynccontextmanager
async def lifespan(app: FastAPI):
    settings = Settings()
    timeout = httpx.Timeout(
        connect=settings.http_connect_timeout,
        read=settings.http_read_timeout,
        write=settings.http_write_timeout,
        pool=settings.http_pool_timeout,
    )
    limits = httpx.Limits(
        max_keepalive_connections=settings.http_max_keepalive_connections,
        max_connections=settings.http_max_connections,
    )
    app.state.http_client = httpx.AsyncClient(timeout=timeout, limits=limits)
    try:
        yield
    finally:
        await app.state.http_client.aclose()

app = FastAPI(title="Quote API", version="1.0", lifespan=lifespan)

app.include_router(quote_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
