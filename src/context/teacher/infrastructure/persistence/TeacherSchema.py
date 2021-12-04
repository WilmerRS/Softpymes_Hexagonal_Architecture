from src.main.database import ma
from ...domain.Teacher import Teacher
from src.context.course.infrastructure.persistence.CourseBasicSchema import CourseBasicSchema


class TeacherSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Teacher

    courses = ma.Nested(CourseBasicSchema, many=True)


teacher_schema = TeacherSchema()
teachers_schema = TeacherSchema(many=True)
