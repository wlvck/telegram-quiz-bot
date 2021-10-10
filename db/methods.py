from loader import bot
from migration import Teacher, Student, session, Quiz, students_and_quiz_table


def check_existing_user(first_name, last_name, user_list) -> bool:
    for user in user_list:
        if user.first_name == first_name and user.last_name == last_name:
            return True
    return False


def add_info_about_teacher(telegram_id, first_name, last_name):
    check_user_id = session.query(Teacher).filter_by(telegram_id=telegram_id).first()
    if check_user_id:
        # await bot.send_message(telegram_id, f'{first_name} {last_name} was successfully inserted to database')
        print('You are already in our database')
    else:
        insert = Teacher(first_name=first_name, last_name=last_name, telegram_id=telegram_id)
        session.add(insert)
        session.commit()
        print(f'{first_name} {last_name} was successfully inserted to database')


def edit_info_about_teacher(telegram_id, first_name=None, last_name=None):
    edit = session.query(Teacher).filter_by(telegram_id=telegram_id).first()
    if first_name and last_name:
        edit.first_name = first_name
        edit.last_name = last_name
        session.commit()
    elif first_name:
        edit.first_name = first_name
        session.commit()
    else:
        edit.last_name = last_name
        session.commit()


def check_title_duplicate(quiz_list: list, quiz_title) -> bool:
    for quiz in quiz_list:
        if quiz.title == quiz_title:
            return True
    return False


def add_quiz(user_telegram_id, quiz_title):
    owner_id = session.query(Teacher).filter_by(telegram_id=user_telegram_id).first().id
    check_quiz_title_repeat = session.query(Quiz).filter_by(owner_id=owner_id).all()
    result = check_title_duplicate(check_quiz_title_repeat, quiz_title)
    if result:
        print(f'Please {quiz_title} is already existing, enter another quiz title')
    else:
        insert_new_quiz = Quiz(title=quiz_title, owner_id=owner_id)
        session.add(insert_new_quiz)
        session.commit()
        print(f'{quiz_title} was successfully inserted')


def update_quiz_title(user_telegram_id, new_title):
    owner_id = session.query(Teacher).filter_by(telegram_id=user_telegram_id).first().id
    update_title = session.query(Quiz).filter_by(owner_id=owner_id).first()
    update_title.title = new_title
    session.commit()
    print('Success')


def get_quiz_list(telegram_id) -> list:
    teacher = session.query(Teacher).filter_by(telegram_id=telegram_id).first()
    quiz_list = teacher.quizzess
    return quiz_list


def add_new_student(first_name, last_name, telegram_id):
    student_list = session.query(Student).all()
    check = check_existing_user(first_name, last_name, student_list)
    if check:
        print(f'{first_name} {last_name} is already exists')
    else:
        new_student = Student(first_name=first_name, last_name=last_name, telegram_id=telegram_id)
        session.add(new_student)
        session.commit()
        print('Success')


def edit_student(telegram_id, new_first_name=None, new_last_name=None):
    edit = session.query(Student).filter_by(telegram_id=telegram_id).first()
    if new_first_name and new_last_name:
        edit.first_name = new_first_name
        edit.last_name = new_last_name
        session.commit()
    elif new_first_name:
        edit.first_name = new_first_name
        session.commit()
    else:
        edit.last_name = new_last_name
        session.commit()


def check_students_quiz(student_telegram_id, quiz_id):
    student = session.query(Student).filter_by(telegram_id=student_telegram_id).first().id
    table = session.query(students_and_quiz_table).filter_by(student_id=student).all()
    for index, tuple_ in enumerate(table):
        if tuple_[1] == quiz_id:
            return True
    return False


# print(check_students_quiz(2010, 1))


def join_student_to_quiz(student_telegram_id, quiz_id):
    if check_students_quiz(student_telegram_id=student_telegram_id, quiz_id=quiz_id):
        print('This student was already joined to this quiz')
    else:
        try:
            student = session.query(Student).filter_by(telegram_id=student_telegram_id).first()
            quiz = session.query(Quiz).filter_by(id=quiz_id).first()
            quiz.explorers.append(student)
            session.commit()
            print('Success')
        except Exception as err:
            print(err)


def get_students_quiz_list(telegram_id) -> list:
    student_id = session.query(Student).filter_by(telegram_id=telegram_id).first().id
    get_list = session.query(students_and_quiz_table).filter_by(student_id=student_id).all()
    quiz_list = []
    for index, tuple_ in enumerate(get_list):
        title = session.query(Quiz).filter_by(id=tuple_[1]).first()
        quiz_list.append(title.title)
    return quiz_list

# miras = session.query(Student).filter_by(first_name='Symbat').first()
# quiz1 = session.query(Quiz).filter_by(title='Math').first()
# quiz2 = session.query(Quiz).filter_by(title='HTML').first()
# quiz1.explorers.append(miras)
#
# session.commit()
