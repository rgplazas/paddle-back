from sqlalchemy.orm import Session
from . import models, schemas
from datetime import datetime, timedelta

def get_canchas(db: Session):
    return db.query(models.Cancha).all()
def get_canchas(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Cancha).offset(skip).limit(limit).all()

def create_cancha(db: Session, cancha: schemas.CanchaCreate):
    db_cancha = models.Cancha(**cancha.model_dump())
    db.add(db_cancha)
    db.commit()
    db.refresh(db_cancha)
    return db_cancha

def get_reservas_por_dia_y_cancha(db: Session, cancha_id: int, dia: datetime):
    # Consultar las reservas para la cancha en el rango de fechas del día (24 horas).
    return db.query(models.Reserva).filter(
        models.Reserva.cancha_id == cancha_id,
        models.Reserva.dia >= dia,
        models.Reserva.dia < dia + timedelta(days=1)  # Filtra solo reservas dentro de las 24 horas del día
    ).all()


def create_reserva(db: Session, reserva: schemas.ReservaCreate):
    # Obtener todas las reservas existentes para la cancha y el día especificado
    reservas = get_reservas_por_dia_y_cancha(db, reserva.cancha_id, reserva.dia)
    
    # Verificar que no haya superposición de horarios con las reservas existentes
    for r in reservas:
        # Verifica si la nueva reserva comienza dentro del intervalo de la reserva existente
        if not (reserva.dia + timedelta(hours=reserva.duracion) <= r.dia or reserva.dia >= r.dia + timedelta(hours=r.duracion)):
            raise ValueError(f"La reserva para la cancha {reserva.cancha_id} entra en conflicto con una existente.")
    
    # Si no hay conflictos, crear la nueva reserva
    db_reserva = models.Reserva(**reserva.model_dump())
    db.add(db_reserva)
    db.commit()
    db.refresh(db_reserva)
    return db_reserva

def get_reservas(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Reserva).offset(skip).limit(limit).all()
def get_reservas(db: Session):
    return db.query(models.Reserva).all()
def get_reservas_con_cancha(db: Session):
    return db.query(models.Reserva).join(models.Cancha).all()