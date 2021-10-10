from loader import bot
from migration import Teacher, Student, session, Quiz


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



