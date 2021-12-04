# python
from datetime import datetime

# db sqlalchemy
from src.main.database import db


class Course(db.Model):
    __tablename__ = 'Course'
    course_id = db.Column('course_id', db.String(50), primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.Text)

    teacher_id = db.Column(
        db.String(50),
        db.ForeignKey("Teacher.teacher_id")
    )
    current_teacher = db.relationship('Teacher', back_populates="courses")

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, course_id, name, description, teacher_id):
        self.course_id = course_id
        self.name = name
        self.description = description
        self.teacher_id = teacher_id

    def __repr__(self):
        return f'<Course: {self.name} >'

    def __str__(self):
        return f'<Course: {self.name} >'
