from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db import Student, Group, Subject, Teacher, Grade


engine = create_engine("postgresql://postgres:test1234@localhost/postgres")
Session = sessionmaker(bind=engine)
session = Session()


fake = Faker()


groups = ['Група 1', 'Група 2', 'Група 3']
for group_name in groups:
    group = Group(name=group_name)
    session.add(group)


for _ in range(3):
    teacher = Teacher(name=fake.name())
    session.add(teacher)


subjects = ['Математика', 'Фізика', 'Хімія', 'Історія', 'Література']
for subject_name in subjects:
    subject = Subject(name=subject_name)
    session.add(subject)


for _ in range(30):
    student = Student(
        name=fake.name(),
        group_id=fake.random_element(elements=(1, 2, 3))
    )
    session.add(student)
    
    for subject_id in range(1, 6):  # від 1 до 5, бо ми маємо 5 предметів
        grade = Grade(
            student_id=student.id,
            subject_id=subject_id,
            teacher_id=fake.random_element(elements=(1, 2, 3)),
            value=fake.random_int(min=1, max=100)
        )
        session.add(grade)


session.commit()


session.close()