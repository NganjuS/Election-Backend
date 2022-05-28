from sqlalchemy.orm import Session
from typing import List
from . import models, schemas
def get_db_user(db: Session, username : str):
    return db.query(models.User).filter_by(username=username).first()
def get_db_candidates(db: Session):
    return db.query(models.Candidate).all()
def get_db_candidate(db: Session, codestr : str):
    return db.query(models.Candidate).filter_by(short_code =codestr).first()
def get_db_parties(db: Session):
    return db.query(models.Party).all()
def get_position(db: Session):
    return db.query(models.Position).all()
def create_parties(db: Session, parties: List[schemas.PartyCreate]):
    for party in parties:
        db_party = models.Party(**party.dict())
        db.add(db_party)
    db.commit()
    return db.query(models.Party).all()
def create_position(db: Session, posi: schemas.PositionCreate):
    db_position= models.Position(**posi.dict())
    db.add(db_position)
    db.commit()
    db.refresh(db_position)
    return db_position
def create_user(db: Session, usr : schemas.UserCreate):
    db_user = models.User(**usr.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
def create_candidate(db: Session, candi: schemas.CandidateCreate):
    db_candidate= models.Candidate(**candi.dict())
    db.add(db_candidate)
    db.commit()
    db.refresh(db_candidate)
    return db_candidate
def create_party(db: Session, party: schemas.PartyCreate):
    db_party= models.Party(**party.dict())
    db.add(db_party)
    db.commit()
    db.refresh(db_party)
    return db_party