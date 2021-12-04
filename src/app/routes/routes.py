# Controllers
from src.app.controllers.teacher.TeacherPutController import TeacherPutController
from src.app.controllers.teacher.TeacherGetAll import TeacherGetAll
from src.app.controllers.course.CoursePutController import CoursePutController
from src.app.controllers.course.CourseGetAllController import CourseGetAllController


def register_routes(app):
    # Teachers
    app.add_resource(TeacherPutController, '/v1/teachers/<teacher_id>')
    app.add_resource(TeacherGetAll, '/v1/teachers')

    # Courses
    app.add_resource(CoursePutController, '/v1/courses/<course_id>')
    app.add_resource(CourseGetAllController, '/v1/courses')
