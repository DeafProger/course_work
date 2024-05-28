from .file_connector import FileConnector
import json


class JSONSaver(FileConnector):

    def __init__(self, vacancies):
        with open("vacancies.json", "w", encoding='utf8') as write_file:
            json.dump(vacancies, write_file, ensure_ascii=False)

    def get_vacancies(self):
        with open("vacancies.json", encoding='utf8') as read_file:
            return json.load(read_file)

    def add_vacancy(self, vacancy):
        vacancies = self.get_vacancies()
        for vac in vacancies:
            if vac['id'] == vacancy.id: return
        dic = dict.fromkeys(['id', 'name', 'salary_min', 'salary_max', 'url'])
        dic['id'] = vacancy.id
        dic['name'] = vacancy.name
        dic['salary_min'] = vacancy.salary_min
        dic['salary_max'] = vacancy.salary_max
        dic['url'] = vacancy.url
        vacancies.append(dic)
        self.__init__(vacancies)

    def delete_vacancy(self, vacancy):
        vacancies = self.get_vacancies()
        for vac in vacancies:
            if vac['id'] == vacancy.id:
                vacancies.remove(vac)
                self.__init__(vacancies)
                return

