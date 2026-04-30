from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root(name: str = "PyCharmH6666ello2013456"):
    """Root endpoint. Optional query param `name` (default: PyCharm)."""
    return {"message": f"Hi, {name}"}


@app.get("/hello/{name}")
def read_hello(name: str):
    """Path endpoint that greets the provided name."""
    return {"message": f"Hi, {name}"}


if __name__ == "__main__":
    # Allow running `python main.py` for quick local testing.
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000)