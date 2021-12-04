from abc import ABC, abstractmethod
from .Course import Course


class CourseRepository(ABC):
    @abstractmethod
    def get_all(self, courses: list[Course]):
        return NotImplemented

    @abstractmethod
    def search(self, course: Course):
        return NotImplemented

    @abstractmethod
    def save(self, course: Course):
        return NotImplemented
