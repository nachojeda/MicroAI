from fastapi import FastAPI

app = FastAPI()


@app.get("/first_ednpoint/test")
def test_function():
    return {"message": "Welcome FastAPI Nerds"}