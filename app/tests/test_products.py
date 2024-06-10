from fastapi.testclient import TestClient
 
from app.api import app

client = TestClient(app)

def test_products(): 
    #-----cea_banque-------
    # create a cea_banque
    response = client.post(
        "/products/",
        json = {
            "name": "string",
            "color": "string",
            "weight": 0,
            "height": 0,
            "quantity": 0,
            "price": 0
        }
    )
    
    data = response.json()
    product_id = data["id"]
    assert response.status_code == 201


    # get all cea_banque 

    response = client.get("/products/")
    assert response.status_code == 200

    # Get one cea_banque

    response = client.get(f"/products/{product_id}/")
    assert response.status_code == 200


    # Update one cea_banque

    response = client.put(
            f"/products/{product_id}",
            json = {
                "name": "string",
                "color": "string",
                "weight": 0,
                "height": 0,
                "quantity": 0,
                "price": 0
            }
        )
    assert response.status_code == 200

    # Delete one cea_banque
    response = client.delete(f"/products/{product_id}")
    assert response.status_code == 200

