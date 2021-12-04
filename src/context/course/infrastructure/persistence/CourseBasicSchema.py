from src.main.database import ma
from ...domain.Course import Course


class CourseBasicSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Course
