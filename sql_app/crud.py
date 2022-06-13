from sqlalchemy.orm import Session
from typing import List
from . import models, schemas
def get_db_user(db: Session, username : str):
    return db.query(models.User).filter_by(username=username).first()
def get_db_candidates(db: Session):
    return db.query(models.Candidate).all()
def get_db_candidates_by_position(db: Session,positionid : int ):
    return db.query(models.Candidate).filter_by(position_id = positionid).all()
def get_db_candidates_filter(db: Session,positionid : int, countyid : int ):
    if(countyid == 0):
        return db.query(models.Candidate).filter_by(position_id = positionid).all()
    else:
        return db.query(models.Candidate).filter_by(position_id = positionid, county_id = countyid).all()
    
def get_db_candidate(db: Session, codestr : str):
    return db.query(models.Candidate).filter_by(short_code =codestr).first()
def get_db_parties(db: Session):
    return db.query(models.Party).order_by(models.Party.name).all()
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
def update_candidate(db: Session, candi: schemas.CandidateUpdate):
    storeobj = db.query(models.Candidate).filter_by(id=candi.id).first()
    candi_data = candi.dict(exclude_unset=True)
    for key, value in candi_data.items():
            setattr(storeobj, key, value)
    db.add(storeobj)
    db.commit()
    db.refresh(storeobj)
    return storeobj
def create_candidate(db: Session, candi: schemas.CandidateCreate):
    db_candidate= models.Candidate(**candi.dict())
    db.add(db_candidate)
    db.commit()
    db.refresh(db_candidate)
    return db_candidate
def del_candidate(db: Session,id : int):
    delobj = db.query(models.Candidate).filter_by(id=id).first()
    db.delete(delobj)
    db.commit()
    return id
def create_party(db: Session, party: schemas.PartyCreate):
    db_party= models.Party(**party.dict())
    db.add(db_party)
    db.commit()
    db.refresh(db_party)
    return db_party
def create_county(db: Session, county: schemas.CountyCreate):
    db_county= models.County(**county.dict())
    db.add(db_county)
    db.commit()
    db.refresh(db_county)
def create_counties(db: Session, counties: List[schemas.CountyCreate]):
    for county in counties:
        db_county = models.County(**county.dict())
        db.add(db_county)
    db.commit()
    return db.query(models.County).all()
def get_db_counties(db: Session):
    return db.query(models.County).all()