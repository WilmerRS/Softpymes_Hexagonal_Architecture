from ..domain.Teacher import Teacher

# Interface repository
from ..domain.TeacherRepository import TeacherRepository


class TeacherSearchAll:

    def __init__(self, repository: TeacherRepository):
        self._repository = repository

    def run(self):
        teachers = Teacher.query.all()
        return self._repository.get_all(teachers=teachers)
