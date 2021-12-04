# Flask
from flask import Response, request

# flask restfull
from flask_restful import Resource

# Injection repository
from src.context.course.infrastructure.persistence.MariaDBCourseRepository import MariaDBCourseRepository

# Use case
from src.context.course.application.CourseCreator import CourseCreator

# SqlAlchemy
from sqlalchemy.exc import SQLAlchemyError, InternalError


class CoursePutController(Resource):
    _course_repository = MariaDBCourseRepository()
    _use_case = CourseCreator(_course_repository)

    def put(self, course_id):
        # try:
            body = request.get_json()
            course = {
                'course_id': course_id,
                'name': body['name'],
                'description': body['description'],
                'teacher_id': body['teacher_id']
            }
            course_response = self._use_case.run(**course)
            return course_response
        # except SQLAlchemyError:
        #     return Response(
        #         "Id existente",
        #         status=400, mimetype='application/json'
        #     )
        # except InternalError:
        #     return Response(
        #         "INTERNAL_ERROR_SERVER",
        #         status=500, mimetype='application/json'
        #     )
