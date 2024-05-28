from abc import ABC, abstractmethod
from .vacancy import Vacancy


class FileConnector(ABC):
    pass

    @abstractmethod
    def get_vacancies(self):
        pass

    @abstractmethod
    def add_vacancy(self, vacancy:Vacancy):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy: Vacancy):
        pass

