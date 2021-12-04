from flask import jsonify

# Local
from src.context.course.domain.CourseRepository import CourseRepository
from src.context.course.domain.Course import Course

# db
from src.main.database import db

# Schema
from .CourseSchema import course_schema, courses_schema


class MariaDBCourseRepository(CourseRepository):
    def get_all(self, courses: list[Course]):
        result = courses_schema.dump(courses)
        return jsonify(result)


    def search(self, course: Course):
        return NotImplemented

    def save(self, course: Course):
        db.session.add(course)
        db.session.commit()
        return course_schema.jsonify(course)
