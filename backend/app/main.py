from fastapi import FastAPI

app = FastAPI(
    title="Personal Finance AI",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "application": "Personal Finance AI",
        "status": "running"
    }