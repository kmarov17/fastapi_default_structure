from fastapi import Body, Depends, APIRouter
from sqlalchemy.orm import Session

from app.configs.db import get_db
from app.models.products import ProductIn
from app.services.products import get_products, get_product, create_product, update_product, delete_product


router = APIRouter(
    tags=["Products"],
    prefix="/products",
    responses={404: {"description": "Not found"}}
)

# Get all products
@router.get('/')
async def index(db: Session = Depends(get_db), limit: int = 10, page: int = 1, search: str = ""):
    return await get_products(db=db, limit=limit, page=page, search=search)

# Get banque
@router.get("/{id}")
async def show(id: str, db: Session = Depends(get_db)):
    return await get_product(item_id=id, db=db)

# Store product
@router.post('/', status_code=201)
async def store(product: ProductIn = Body(...), db: Session = Depends(get_db)):
    return await create_product(product=product.model_dump(), db=db)

# Update product
@router.put('/{id}', status_code=200)
async def update(id: int, product: ProductIn = Body(...), db: Session = Depends(get_db)):
    return await update_product(product_id=id, product_data=product.model_dump(), db=db)

# Delete product
@router.delete('/{id}', status_code=200)
async def delete(id: int, db: Session = Depends(get_db)):
    return await delete_product(product_id=id, db=db)