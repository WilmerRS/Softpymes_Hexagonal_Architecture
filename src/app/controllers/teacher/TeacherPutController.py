# Flask
from flask import Response, request

# flask restfull
from flask_restful import Resource

# use cases
from src.context.teacher.aplication.TeacherCreator import TeacherCreator

# Repository injection
from src.context.teacher.infrastructure.persistence.MariaDBTeacherRepository import MariaDBTeacherRepository

# SqlAlchemy
from sqlalchemy.exc import SQLAlchemyError, InternalError


class TeacherPutController(Resource):
    _teacher_repository = MariaDBTeacherRepository()
    _use_case = TeacherCreator(_teacher_repository)

    def put(self, teacher_id):
        try:
            body = request.get_json()
            teacher = {
                'teacher_id': teacher_id,
                'teacher_name': body['teacher_name']
            }
            teacher_response = self._use_case.run(**teacher)
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
