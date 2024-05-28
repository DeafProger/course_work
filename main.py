# Fourth CourseWork. Written by Valentin Ustinov AKA @DeafProger.


from src.hh import HeadHunterAPI
from src.json_saver import JSONSaver
from src.vacancy import Vacancy


# Создание экземпляра класса для работы с API сайтов с вакансиями
hh_api = HeadHunterAPI()

# Получение вакансий с hh.ru в формате списка объектов
vacancies_list = hh_api.get_vacancies("Python")

# Пример работы контструктора класса с одной вакансией
vacancy = Vacancy('777', "C++ developer", 100000, 150000, "https://hh.ru/vacancies/777?host=hh.ru")

# Сохранение информации о вакансиях в файл
json_saver = JSONSaver(vacancies_list)
json_saver.add_vacancy(vacancy)
json_saver.delete_vacancy(vacancy)


def main():
    while True:
        print('''Выбери действие:
        0: Выйти из программы.
        1: Загрузить вакансии в файл по ключевому слову.
        2: Показать топ 10 вакансий из файла.''')
        user_input = input()
        if not user_input.isdigit(): continue
        dig = int(user_input)

        if dig == 2:
            vacancies =[]
            for vac in json_saver.get_vacancies():
                vacancies.append(Vacancy(vac['id'], vac['name'], vac['salary_min'], vac['salary_max'], vac['url']))
            vacancies = sorted(vacancies, reverse=True)
            for i in range(min(10, len(vacancies))):
                print(vacancies[i])

        if dig == 1:
            search_text = input('Ключевые слова для поиска:')
            vacancies = hh_api.get_vacancies(search_text)
            JSONSaver(vacancies)

        if dig == 0: break


if __name__ == "__main__":
    main()

