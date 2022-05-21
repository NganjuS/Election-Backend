from sqlalchemy.orm import Session
from . import models, schemas
def get_position(db: Session):
    return db.query(models.Position).all()
def create_position(db: Session, posi: schemas.PositionCreate):
    db_position= models.Position(**posi.dict())
    db.add(db_position)
    db.commit()
    db.refresh(db_position)
    return db_position