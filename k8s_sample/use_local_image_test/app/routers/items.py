from fastapi import APIRouter


router = APIRouter()


@router.get('/item')
def get_item():
    return 'item'

@router.get('/items')
def get_items():
    return 'items'
