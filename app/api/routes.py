from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
from app.models import Base, PlasticMaterial, PrintModel
from app.crud import get_plastic_material_by_type_and_color

app = FastAPI()

# Ініціалізація бази даних
Base.metadata.create_all(bind=engine)

# Депенденсі для сесії бази даних
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/check_plastic/")
def check_plastic(order: list[dict], db: Session = Depends(get_db)):
    """
    Перевіряє наявність матеріалів у базі.
    Order: [{model_id: int, quantity: int}, ...]
    """
    for item in order:
        model = db.query(PrintModel).filter(PrintModel.id == item["model_id"]).first()
        if not model:
            raise HTTPException(status_code=404, detail=f"Model ID {item['model_id']} not found")

        plastic = get_plastic_material_by_type_and_color(
            db, model.plastic_type, model.plastic_color
        )
        if not plastic or plastic.quantity_kg < model.plastic_required_kg * item["quantity"]:
            raise HTTPException(
                status_code=400,
                detail=f"Insufficient material: {model.plastic_type}, {model.plastic_color}"
            )
    return {"status": "success", "message": "Enough material available"}
