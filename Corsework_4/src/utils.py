from src.apifile import Apihh
from src.vacancy import Vacancy
from src.filesaver import JSONSaver
# from functions import asd
import json
import os
from config import root_path

hh_vacancies = Apihh()
json_saver = JSONSaver('vacancies.json')

def user_interaction():

    # search_query = input("Введите поисковый запрос по профессии: ")
    # search_areas = input("Введите город с помощью индекса,\nузнать нужный индекс можно по ссылке https://api.hh.ru/areas: ")
    # class_list = Vacancy.get_vacancies(hh_vacancies.get_vacancies(search_query, search_areas)['items'])
    json_saver.del_vacancy('Менеджер по продажам в аэропорт')

    class_list = Vacancy.get_vacancies(hh_vacancies.get_vacancies('Менеджер', 99)['items'])
    class_list.sort(reverse=True)
    vacancies_list = json_saver.write_list_to_joisn(class_list)
    json_saver.add_vacancy(vacancies_list)
    error_action = str
    while True:
        Enter_select = input("\nВыберите действие:\n"
                             "1. Вывести все найденные вакансии\n"
                             "2. Вывести топ N вакансии по зарплат\n"
                             "3. Редактор файла\n")
        сhoosing_action(Enter_select)
        further_action = input('\n\nЖелаете продолжить дальше - введите команду "Y/N"\n')
        if further_action == "Y":
            continue
        elif further_action == "N":
            print("\nСпасибо, что воспользовались нашими услугами")
            break
        else:
            while error_action != "Y" and error_action != "N":
                error_action = input("Введите правильную команду\n")
                if error_action == "Y":
                    continue
                elif further_action == "N":
                    print("\nСпасибо, что воспользовались нашими услугами")
def сhoosing_action(number):

    if int(number) == 1:
        with open(os.path.join(root_path, 'vacancies.json'), 'r', encoding="utf-8") as json_file:
            raw_json = json_file.read()
            data = json.loads(raw_json)
            for temp in data:
                print(f"({temp['title']}, {temp['url']}, {temp['salary_from']} - {temp['salary_to']}, {temp['company_name']})")

    elif int(number) == 2:
        top_n = int(input("Введите количество вакансий для вывода в топ N: "))
        with open(os.path.join(root_path, 'vacancies.json'), 'r', encoding="utf-8") as json_file:
            raw_json = json_file.read()
            data = json.loads(raw_json)
            for number in range(top_n):
                print(f"({data[number]['title']}, {data[number]['url']}, {data[number]['salary_from']} - {data[number]['salary_to']}, {data[number]['company_name']})")

    elif int(number) == 3:
        vacancy_del = input("Введите точное наименование вакансии, которое хотите удалить\n")
        boolean_value = bool
        with open(os.path.join(root_path, 'vacancies.json'), 'r', encoding="utf-8") as json_file:
            raw_json = json_file.read()
            data = json.loads(raw_json)
            for temp in data:
                if vacancy_del == temp['title']:
                    boolean_value = True
                else:
                    boolean_value = False
        if boolean_value:
            json_saver.del_vacancy(vacancy_del)
            print("Вакансия удалена\n")
        else:
            print("Вакансия не удалена, так как не найдена\n")


