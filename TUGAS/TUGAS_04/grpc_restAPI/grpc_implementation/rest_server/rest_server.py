from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/get_data")
def get_data(query: str):
    return {"message": f"Hello from REST, you sent: {query}"}


if __name__ == "__main__":
    uvicorn.run("rest_server:app", host="127.0.0.1", port=8000, reload=True)
