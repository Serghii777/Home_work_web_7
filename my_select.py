from sqlalchemy import func, desc
from db import Student, Group, Subject, Teacher, Grade
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


engine = create_engine('sqlite:///my_database.db')
Session = sessionmaker(bind=engine)
session = Session()


def select_1(session):
    return session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .select_from(Grade).join(Student).group_by(Student.id).order_by(desc('avg_grade')).limit(5).all()


def select_2(session):
        query_result = session.query(Student.fullname) \
            .join(Grade).join(Subject) \
            .filter(Subject.name == 'Математика') \
            .group_by(Student.id) \
            .order_by(func.avg(Grade.grade).desc()) \
            .limit(1).scalar()
        return query_result


def select_3(session):
    query_result = session.query(Grade.group_id, func.avg(Grade.grade)) \
        .join(Subject).filter(Subject.name == 'Математика') \
        .group_by(Grade.group_id).all()
    return query_result


def select_4(session):
    query_result = session.query(func.avg(Grade.grade)).scalar()
    return query_result


def select_5(session):
    query_result = session.query(Subject.name).filter(Subject.teacher_id == 1).all()
    return query_result


def select_6(session):
    query_result = session.query(Student.fullname).join(Group).filter(Group.id == 1).all()
    return query_result


def select_7(session):
    query_result = session.query(Grade.grade) \
        .join(Subject).join(Group) \
        .filter(Group.id == 1, Subject.name == 'Математика').all()
    return query_result


def select_8(session):
    query_result = session.query(func.avg(Grade.grade)) \
        .join(Subject) \
        .filter(Subject.teacher_id == 1).scalar()
    return query_result


def select_9(session):
    query_result = session.query(Subject.name) \
        .join(Grade).join(Student) \
        .filter(Student.id == 1).all()
    return query_result


def select_10(session):
    query_result = session.query(Subject.name) \
        .join(Grade).join(Student).join(Teacher) \
        .filter(Student.id == 1, Teacher.id == 1).all()
    return query_result



def select_11(session):

    query_result = session.query(func.avg(Grade.grade)) \
        .filter(Grade.student_id == 1, Grade.teacher_id == 1).scalar()
    return query_result
    

def select_12(session):

    subquery = session.query(func.max(Grade.lesson_number)) \
        .join(Subject).filter(Subject.name == 'Математика')

    query_result = session.query(Grade.grade) \
        .join(Subject).join(Group) \
        .filter(Group.id == 1, Subject.name == 'Математика', Grade.lesson_number == subquery).all()

    return query_result
