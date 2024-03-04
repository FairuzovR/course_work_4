from src.apifile import Apihh
from src.vacancy import Vacancy
from src.filesaver import JSONSaver
import os
import json

class_user = Apihh()
def user_interaction():
    # search_query = input("Введите поисковый запрос по профессии: ")
    # search_areas = input("Введите индекс города,\nузнать нужный индекс можно по ссылке https://api.hh.ru/areas: ")
    # top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    # filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    # salary_range = input("Введите диапазон зарплат: ")  # Пример: 100000 - 150000

    hh_vacancies = Apihh()
    # vacancies_list = Vacancy.get_vacancies(hh_vacancies.get_vacancies(search_query, search_areas)['items'])
    vacancies_list = Vacancy.get_vacancies(hh_vacancies.get_vacancies('Космонавт', '99')['items'])
    vacancies_list.sort()
    json_saver = JSONSaver('vacancies.json')
    json_saver.add_vacancy(vacancies_list)

    # with open('vacancies.json') as f:
    #     templates = json.loads(f)
    #     print(templates)


# def open_json(json_name):
#     with open(json_name) as f:
#         templates = json.load(f)







    # filtered_vacancies = filter_vacancies(vacancies_list, filter_words)
    #
    # ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)
    #
    # sorted_vacancies = sort_vacancies(ranged_vacancies)
    # top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    # print_vacancies(top_vacancies)

# def get_vacancy_api(name_vacancy, area):
#     get_search = Apihh.get_vacancies(name_vacancy, area)
#     return get_search
#
# def filter_vacancies(cast_to_object_list, keyword):
#     pass
#     # keyword_example = class_user.get_vacancies(keyword)