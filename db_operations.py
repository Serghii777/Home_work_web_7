from sqlalchemy.orm import Session
from db import Student, Group, Subject, Teacher, Grade

def create_record(session: Session, model, **kwargs):
    """Створення запису у базі даних."""
    record = model(**kwargs)
    session.add(record)
    session.commit()
    return record

def list_records(session: Session, model):
    """Отримання списку всіх записів певної моделі з бази даних."""
    return session.query(model).all()

def update_record(session: Session, model, record_id, **kwargs):
    """Оновлення запису у базі даних за ідентифікатором."""
    record = session.query(model).filter_by(id=record_id).first()
    if record:
        for key, value in kwargs.items():
            setattr(record, key, value)
        session.commit()
        return record
    else:
        return None

def remove_record(session: Session, model, record_id):
    """Видалення запису у базі даних за ідентифікатором."""
    record = session.query(model).filter_by(id=record_id).first()
    if record:
        session.delete(record)
        session.commit()
        return True
    else:
        return False