from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from main import tokenize_string


app = FastAPI()


# Pydantic model for request validation
class SourceCode(BaseModel):
    code: str


# Add CORS middleware to allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],    # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],    # Allows all methods
    allow_headers=["*"],    # Allows all headers
)


@app.get("/")
async def root():
    return {
        "message": "Welcome to the Square's tokenizer API!",
        "endpoints": {
            "/": "This welcome message",
            "/tokenize": "POST endpoint to tokenize source code"
        }
    }


@app.post("/tokenize")
async def tokenize(source: SourceCode):
    try:
        tokens = tokenize_string(source.code)
        return {"tokens": tokens}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
