from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, crud, models
from ..database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/reservas/", response_model=schemas.Reserva)
def crear_reserva(reserva: schemas.ReservaCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_reserva(db, reserva)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/canchas/", response_model=list[schemas.Cancha])
def obtener_canchas(db: Session = Depends(get_db)):
    return crud.get_canchas(db)
    
@router.get("/canchas/paginadas/", response_model=list[schemas.Cancha])
def obtener_canchas(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_canchas(db, skip=skip, limit=limit)

@router.post("/canchas/", response_model=schemas.Cancha)
def crear_cancha(cancha: schemas.CanchaCreate, db: Session = Depends(get_db)):
    return crud.create_cancha(db, cancha)

@router.get("/reservas/", response_model=list[schemas.Reserva])
def obtener_reservas(db: Session = Depends(get_db)):
    try:
        return crud.get_reservas(db)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/reservas/paginadas/", response_model=list[schemas.Reserva])
def obtener_reservas(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    try:
        return crud.get_reservas(db, skip=skip, limit=limit)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
