from abc import ABC, abstractmethod
from .Teacher import Teacher


class TeacherRepository(ABC):
    @abstractmethod
    def save(self, teacher: Teacher):
        pass

    @abstractmethod
    def update(self, teacher: Teacher):
        pass

    @abstractmethod
    def get_all(self, teachers: list[Teacher]):
        pass

    @abstractmethod
    def get(self, teacher: Teacher):
        pass

    @abstractmethod
    def delete(self, teacher: Teacher):
        pass
