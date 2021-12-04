# from src.context.teacher.infrastructure.persistence.MariaDBTeacherRepository import MariaDBTeacherRepository
from ..domain.Teacher import Teacher

# Interface repository
from ..domain.TeacherRepository import TeacherRepository


class TeacherCreator:

    def __init__(self, repository: TeacherRepository):
        self._repository = repository

    def run(self, teacher_id, teacher_name):
        teacher = Teacher(teacher_id=teacher_id, teacher_name=teacher_name)
        return self._repository.save(teacher=teacher)
