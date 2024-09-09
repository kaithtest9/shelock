import subprocess
from fastapi import FastAPI

app = FastAPI()

@app.get("/sherlock")
def sherlock(q: str):
    name = q.split(' ')[0]
    subprocess.run(['sherlock', name], capture_output=True, text=True)
    with open(f'./{name}.txt', 'r') as f:
        result = f.read()
    return result

@app.get("/")
def main():
    return "success"
