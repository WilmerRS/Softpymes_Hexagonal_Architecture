from src.main.database import ma
from ...domain.Course import Course

from src.context.teacher.infrastructure.persistence.TeacherSchema import TeacherSchema


class CourseSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Course

    current_teacher = ma.Nested(TeacherSchema, many=False, exclude=('courses',))


course_schema = CourseSchema()
courses_schema = CourseSchema(many=True)
