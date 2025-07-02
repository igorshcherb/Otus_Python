import uvicorn

from app import app


__all__ = [
    "app",
]


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
