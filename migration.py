from sqlalchemy import String, Integer, Column, create_engine, DateTime, ForeignKey, MetaData, Table, select
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker, backref
from sqlalchemy.sql import func

meta = MetaData()

engine = create_engine('sqlite:////home/kanagat/PycharmProjects/Telegram bot projects/Chatbot Quiz/manage_quiz.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class Teacher(Base):
    __tablename__ = 'teacher'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    telegram_id = Column(Integer, nullable=False)
    quizzess = relationship('Quiz', backref='owner')
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())


students_and_quiz_table = Table('students_quiz', Base.metadata,
                                Column('student_id', ForeignKey('student.id'), primary_key=True),
                                Column('quiz_id', ForeignKey('quiz.id'), primary_key=True)
                                )


class Student(Base):
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    exploring = relationship('Quiz', secondary=students_and_quiz_table, backref=backref('explorers', lazy='dynamic'))
    telegram_id = Column(Integer, nullable=False)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())


class Quiz(Base):
    __tablename__ = 'quiz'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    owner_id = Column(Integer, ForeignKey('teacher.id'))
    questions = relationship('Questions', backref='topic')
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())


class Questions(Base):
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    wrong_ans1 = Column(String(50), nullable=False)
    wrong_ans2 = Column(String(50), nullable=False)
    wrong_ans3 = Column(String(50), nullable=False)
    correct_ans = Column(String(50), nullable=False)
    quiz_id = Column(Integer, ForeignKey('quiz.id'))
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())


Base.metadata.create_all(engine)
