# Flask
from flask import Response

# flask restfull
from flask_restful import Resource

# use cases
from src.context.teacher.aplication.TeacherSearchAll import TeacherSearchAll

# Repository injection
from src.context.teacher.infrastructure.persistence.MariaDBTeacherRepository import MariaDBTeacherRepository

# SqlAlchemy
from sqlalchemy.exc import SQLAlchemyError, InternalError


class TeacherGetAll(Resource):
    _teacher_repository = MariaDBTeacherRepository()
    _use_case = TeacherSearchAll(_teacher_repository)

    def get(self):
        try:
            teacher_response = self._use_case.run()
            return teacher_response
        except SQLAlchemyError:
            return Response(
                "Id existente",
                status=400, mimetype='application/json'
            )
        except InternalError:
            return Response(
                "INTERNAL_ERROR_SERVER",
                status=500, mimetype='application/json'
            )
