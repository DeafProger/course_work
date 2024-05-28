from .base import VacancyAPIClient
import requests, json


class HeadHunterAPI(VacancyAPIClient):

    def get_vacancies(self, search_text):
        url = f"https://api.hh.ru/vacancies?currency=RUR&text={search_text}&per_page=100&page="
        vacancies = []
        k = 0
        while True:
            res = requests.get(url + str(k))
            if not res.ok: break
            items = res.json()['items']

            for item in items:
                dic = dict.fromkeys(['id', 'name', 'salary_min', 'salary_max', 'url'])
                salary_min, salary_max = 0, 0

                if item['salary'] is not None:
                    if item['salary']['currency'] != 'RUR': continue
                    if item['salary']['from'] is not None: salary_min = item['salary']['from']
                    if item['salary']['to'] is not None: salary_max = item['salary']['to']

                dic['id'] = item['id']
                dic['name'] = item['name']
                dic['salary_min'] = salary_min
                dic['salary_max'] = salary_max
                dic['url'] = item['url']

                vacancies.append(dic)
            k += 1

        return vacancies

