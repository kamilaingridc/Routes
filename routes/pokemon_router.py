from fastapi import APIRouter

router = APIRouter()

@router.get('/api/v1/pokemons')
async def get_pokemons():
    return{'info':'Retornou todos os pokemons.' }
