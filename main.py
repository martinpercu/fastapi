from fastapi import FastAPI

app = FastAPI()
app.title = "An app with FastAPI"
app.version = "0.1"

@app.get('/', tags=['Home'])
def message():
    return "Bonjour monde"