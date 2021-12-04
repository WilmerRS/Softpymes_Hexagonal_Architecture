from flask import Response
from flask_restful import Resource

# Injection repository
from src.context.course.infrastructure.persistence.MariaDBCourseRepository import MariaDBCourseRepository

# Use cases
from src.context.course.application.CourseSearchAll import CourseSearchAll

# Error
from sqlalchemy.exc import SQLAlchemyError


class CourseGetAllController(Resource):
    _course_repository = MariaDBCourseRepository()
    _use_case = CourseSearchAll(_course_repository)

    def get(self):
        try:
            courses_response = self._use_case.run()
            return courses_response
        except SQLAlchemyError:
            return Response(
                "Error courses",
                status=400,
                mimetype="application/json"
            )
