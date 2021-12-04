from ..domain.Course import Course
from ..domain.CourseRepository import CourseRepository


class CourseCreator:
    def __init__(self, repository: CourseRepository):
        self._repository = repository

    def run(self, course_id, name, description, teacher_id):
        course = Course(course_id, name, description, teacher_id)
        return self._repository.save(course=course)
