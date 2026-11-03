from fastapi import FastAPI

app = FastAPI()
items = []

@app.get('/health')
def health():
    return {'status': 'ok'}

@app.post('/items')
def add_item(name: str):
    items.append(name)
    return {'message': 'Ajouté'}

@app.get('/items')
def get_items():
    return items
