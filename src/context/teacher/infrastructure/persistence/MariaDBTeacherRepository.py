# Flask
from flask import jsonify

# Local
from src.main.database import db
from src.context.teacher.infrastructure.persistence.TeacherSchema import teacher_schema, teachers_schema
from src.context.teacher.domain.Teacher import Teacher

# Interface repository
from src.context.teacher.domain.TeacherRepository import TeacherRepository


class MariaDBTeacherRepository(TeacherRepository):

    def save(self, teacher: Teacher):
        db.session.add(teacher)
        db.session.commit()
        return teacher_schema.jsonify(teacher)

    def update(self, teacher: Teacher):
        db.session.commit()
        return teacher_schema.jsonify(teacher)

    def get_all(self, teachers):
        result = teachers_schema.dump(teachers)
        return jsonify(result)

    def get(self, teacher):
        return teacher_schema.jsonify(teacher)

    def delete(self, teacher: Teacher):
        db.session.delete(teacher)
        db.session.commit()
        return teacher_schema.jsonify(teacher)
