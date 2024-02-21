from sqlalchemy.orm import sessionmaker
from db_operations import create_record, list_records, update_record, remove_record
from db import Student, Group, Subject, Teacher, Grade
import argparse
from sqlalchemy import create_engine

# Підключення до бази даних
engine = create_engine('sqlite:///school.db')
Session = sessionmaker(bind=engine)
session = Session()

def main():
    parser = argparse.ArgumentParser(description='CLI Program for CRUD operations with database')
    parser.add_argument('--action', '-a', choices=['create', 'list', 'update', 'remove'], help='CRUD action')
    parser.add_argument('--model', '-m', choices=['Student', 'Group', 'Subject', 'Teacher', 'Grade'], help='Model name')
    parser.add_argument('--name', '-n', help='Name of the model')
    parser.add_argument('--id', '-i', type=int, help='ID of the model')

    args = parser.parse_args()

    if args.action == 'create':
        if args.model == 'Student':
            create_record(session, Student, name=args.name, group_id=args.group_id)
        elif args.model == 'Group':
            create_record(session, Group, name=args.name)
        elif args.model == 'Subject':
            create_record(session, Subject, name=args.name, teacher_id=args.teacher_id)
        elif args.model == 'Teacher':
            create_record(session, Teacher, name=args.name)
        elif args.model == 'Grade':
            create_record(session, Grade, value=args.value, timestamp=args.timestamp, student_id=args.student_id, subject_id=args.subject_id)

    elif args.action == 'list':
        if args.model:
            list_records(session, eval(args.model))
        else:
            print("Please provide model name to list records.")

    elif args.action == 'update':
        if args.model and args.id:
            update_record(session, eval(args.model), args.id, name=args.name, group_id=args.group_id, teacher_id=args.teacher_id, value=args.value, timestamp=args.timestamp, student_id=args.student_id, subject_id=args.subject_id)
        else:
            print("Please provide both model name and id to update record.")

    elif args.action == 'remove':
        if args.model and args.id:
            remove_record(session, eval(args.model), args.id)
        else:
            print("Please provide both model name and id to remove record.")

if __name__ == "__main__":
    main()