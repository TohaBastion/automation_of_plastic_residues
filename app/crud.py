from sqlalchemy.orm import Session
from models import PlasticMaterial, PrintModel

def get_plastic_material_by_type_and_color(db: Session, plastic_type: str, color: str):
    return db.query(PlasticMaterial).filter(
        PlasticMaterial.name == plastic_type, PlasticMaterial.color == color
    ).first()
