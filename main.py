import argparse


from db_operations import create_record, list_records, update_record, remove_record


parser = argparse.ArgumentParser(description='CLI програма для CRUD операцій з базою даних')


parser.add_argument('--action', '-a', choices=['create', 'list', 'update', 'remove'], help='Тип операції: create, list, update або remove', required=True)
parser.add_argument('--model', '-m', choices=['Teacher', 'Group', 'Student', 'Subject', 'Grade'], help='Модель для виконання операції', required=True)
parser.add_argument('--id', type=int, help='ID запису для оновлення або видалення')
parser.add_argument('--name', '-n', help='Ім\'я для створення або оновлення')


args = parser.parse_args()


if args.action == 'create':
    create_record(args.model, args.name)
elif args.action == 'list':
    list_records(args.model)
elif args.action == 'update':
    update_record(args.model, args.id, args.name)
elif args.action == 'remove':
    remove_record(args.model, args.id)