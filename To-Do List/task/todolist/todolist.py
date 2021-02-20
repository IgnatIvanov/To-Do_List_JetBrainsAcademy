# Write your code here

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta

engine = create_engine('sqlite:///todo.db?check_same_thread=False')

Base = declarative_base()
main_option = 100  # Variable for user menu handling


class Table(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String, default='default_value')
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return self.deadline


main_menu = """1) Today's tasks
2) Week's tasks
3) All tasks
4) Missed tasks
5) Add task
6) Delete task
0) Exit"""

dict_weeksdays = {
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday'
}

Base.metadata.create_all(engine)  # Create datamodel in our DB

Session = sessionmaker(bind=engine)
session = Session()  # Creating a session with DB

while main_option != 0:
    print(main_menu)
    main_option = int(input())
    print()

    if main_option == 1:  # Today task menu option
        rows = session.query(Table).all()

        count = 0
        today = datetime.today()
        print("Today " + str(datetime.today().day) + ' ' + str(today.strftime('%b')) + ":")
        if len(rows) == 0:
            print('Nothing to do!')

        else:
            for row in rows:

                if row.deadline == datetime.date(datetime.today()):
                    count += 1
                    print(str(count) + ".", row.task)

            if count == 0:
                print('Nothing to do!')
        print()

    if main_option == 2:  # Week`s tasks menu option
        today = datetime.today()

        for x in range(7):
            # Printing date header
            cur_date = today + timedelta(days=x)
            print(dict_weeksdays[cur_date.weekday()], cur_date.day, cur_date.strftime('%b') + ':')

            rows = session.query(Table).filter(Table.deadline == cur_date.date()).all()  # Query to the DB

            count = 0
            if len(rows) == 0:
                print('Nothing to do!')

            else:
                for row in rows:
                    count += 1
                    print(str(count) + ".", row.task)

                if count == 0:
                    print('Nothing to do!')

            print()  # Printing empty line between tasks

    if main_option == 3:  # All tasks menu option
        print('All tasks:')
        rows = session.query(Table).order_by(Table.deadline).all()  # Query to the DB
        count = 0
        for row in rows:
            count += 1
            date = datetime.strptime(str(row.deadline), '%Y-%m-%d')
            print(str(count) + '.', row.task + '.', str(date.day), date.strftime('%b'))

        print()

    if main_option == 4:  # Missed tasks menu option
        print('Missed tasks:')
        rows = session.query(Table).filter(Table.deadline < datetime.today().date()).all()
        if len(rows) == 0:
            print('Nothing is missed!')

        else:
            count = 0
            for row in rows:
                count += 1
                date = datetime.strptime(str(row.deadline), '%Y-%m-%d')
                print(str(count) + '.', row.task + '.', str(date.day), date.strftime('%b'))

        print()

    if main_option == 5:  # Add task menu option
        print('Enter task')
        new_task = str(input())
        print('Enter deadline')
        u_deadline = datetime.strptime(str(input()), '%Y-%m-%d')

        new_row = Table(task=new_task, deadline=u_deadline.date())
        session.add(new_row)
        session.commit()

        print('The task has been added!')
        print()

    if main_option == 6:  # Delete task menu option
        print('Choose the number of the task you want to delete:')
        rows = session.query(Table).order_by(Table.deadline).all()
        count = 0
        for row in rows:
            count += 1
            date = datetime.strptime(str(row.deadline), '%Y-%m-%d')
            print(str(count) + '.', row.task + '.', str(date.day), date.strftime('%b'))

        delete_id = int(input()) - 1
        specific_row = rows[delete_id]
        session.delete(specific_row)
        session.commit()
        print('The task has been deleted!')
        print()

print("Bye!")