from fastapi import FastAPI
from routes import pokebolas_router, pokemon_router

app = FastAPI()

app.include_router(pokemon_router.router, tags='Pokemon')
app.include_router(pokebolas_router.router, tags='Pokebolas')

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', host='127.0.0.1', port=8000, log_level='info', reload=True)
