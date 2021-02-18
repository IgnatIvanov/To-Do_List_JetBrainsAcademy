# Write your code here
# print("Today:")
# print("1) Do yoga")
# print("2) Make breakfast")
# print("3) Learn basics of SQL")
# print("4) Learn what is ORM")

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker
from datetime import datetime

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
2) Add task
0) Exit"""

Base.metadata.create_all(engine)  # Create datamodel in our DB

Session = sessionmaker(bind=engine)
session = Session()  # Creating a session with DB

while main_option != 0:
    print(main_menu)
    main_option = int(input())
    print()

    if main_option == 1:  # Today task menu option
        rows = session.query(Table).all()
        # first_row = rows[0]

        count = 0
        print("Today:")
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

    if main_option == 2:  # Add task menu option
        print('Enter task')
        new_task = str(input())

        # new_row = Table(task='new_task', deadline=datetime.strptime('01-24-2020', '%m-%d-%Y').date())
        new_row = Table(task=new_task, deadline=datetime.today())
        session.add(new_row)
        session.commit()

        print('The task has been added!')
        print()

print("Bye!")