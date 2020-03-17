import random
from fastapi import APIRouter


router = APIRouter()


@router.get('/aggs')
def get_aggs():
    return {'data': [
        {'x': i, 'y': random.randint(1, 10)} for i in range(100)
    ]}
