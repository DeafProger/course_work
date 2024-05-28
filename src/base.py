from abc import ABC, abstractmethod


class VacancyAPIClient(ABC):

    @abstractmethod
    def get_vacancies(self, search_text):
        pass