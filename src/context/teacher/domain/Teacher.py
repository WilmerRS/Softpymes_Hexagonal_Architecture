# python
from datetime import datetime

# db sqlalchemy
from src.main.database import db


class Teacher(db.Model):
    __tablename__ = 'Teacher'
    teacher_id = db.Column('teacher_id', db.String(50), primary_key=True)
    teacher_name = db.Column(db.String(100))

    courses = db.relationship('Course', back_populates="current_teacher")

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, teacher_id, teacher_name):
        self.teacher_id = teacher_id
        self.teacher_name = teacher_name

    def __repr__(self):
        return f'<Teacher: {self.teacher_name} >'

    def __str__(self):
        return f'<Teacher: {self.teacher_name} >'
