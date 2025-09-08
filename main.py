from fastapi import FastAPI
from infrastructure.controller.quote_controller import router as quote_router

app = FastAPI(title="Quote API", version="1.0")

app.include_router(quote_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
