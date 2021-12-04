# Repository
from ..domain.CourseRepository import CourseRepository

# model
from ..domain.Course import Course


class CourseSearchAll:
    def __init__(self, repository: CourseRepository):
        self._repository = repository

    def run(self):
        courses = Course.query.all()
        result_courses = self._repository.get_all(courses=courses)
        return result_courses
