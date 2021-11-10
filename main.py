from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    return {'data': {'page': 'Home: Hello Universe'}}


@app.get('/about')
def about():
    return {'data': {'page': 'About Us'}}
