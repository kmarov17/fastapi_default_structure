from fastapi import HTTPException

from app.models.tables import Products


async def create_product(product, db):
    product = Products(**product)

    db.add(product)
    db.commit()
    db.refresh(product)

    return product

async def update_product(product_id: int, product_data, db):    
    # Récupérer le product existant à mettre à jour
    product = db.query(Products).filter(Products.id == product_id).first()
    if product is None:
        raise HTTPException(status_code=404, detail=f"Product with id {product_id} not found")

    # Mettre à jour les champs du product
    for key, value in product_data.items():
        setattr(product, key, value)
        
    db.commit()
    db.refresh(product)

    return product

async def get_products(limit, page, search, db):
    try:
        skip = (page - 1) * limit

        datas = db.query(Products)

        # Filtrer by product name
        datas = datas.filter(Products.name.ilike(f'%{search}%'))

        if page > 0:
            products = datas.limit(limit).offset(skip).all()
        else :
            products = datas.all() # Return all datas if page == 0

        return products
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"{e}")

async def get_product(item_id, db):
    try:
        product = db.query(Products).filter(Products.id == item_id).first()

        if product is None:
            raise HTTPException(status_code=404, detail=f"Product with id {item_id} not found")
        
        return product
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
async def delete_product(product_id: int, db):
    # Récupérer le product existante à supprimer
    product = db.query(Products).filter(Products.id == product_id).first()
    if product is None:
        raise HTTPException(status_code=404, detail=f"Product with id {product_id} not found")

    # Supprimer le product lui même
    db.delete(product)
    db.commit()

    return {"message": f"Product with id {product_id} deleted successfully"}