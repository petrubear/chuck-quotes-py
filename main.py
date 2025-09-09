from fastapi import FastAPI
from contextlib import asynccontextmanager
import httpx
from infrastructure.controller.quote_controller import router as quote_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    timeout = httpx.Timeout(5.0, connect=5.0, read=5.0)
    limits = httpx.Limits(max_keepalive_connections=20, max_connections=100)
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
