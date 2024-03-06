from src.apifile import Apihh
from src.vacancy import Vacancy
from src.filesaver import JSONSaver
import json
import os
from config import root_path

hh_vacancies = Apihh()
json_saver = JSONSaver('vacancies.json')


def user_interaction():
    """
    Функция, которая взаимодействует с классами и их методами, а так с файлом json,
    имеет запуск основого кода через цикл
    """

    error_action = str
    search_query = input("Введите ключевое слово профессии:\n")
    search_areas = input(
        "Введите город с помощью индекса,\nузнать нужный индекс можно по ссылке https://api.hh.ru/areas:\n ")
    class_list = Vacancy.get_vacancies(hh_vacancies.get_vacancies(search_query.title(), search_areas)['items'])
    class_list.sort(reverse=True)
    vacancies_list = json_saver.write_list_to_joisn(class_list)
    json_saver.add_vacancy(vacancies_list)

    while True:
        Enter_select = input("\nВыберите действие:\n"
                             "1. Вывести все найденные вакансии\n"
                             "2. Вывести топ N вакансии по зарплат\n"
                             "3. Редактор файла\n")
        сhoosing_action(Enter_select)
        further_action = input('\n\nЕсли желаете продолжить дальше - введите команду "Y/N"\n')
        if further_action == "Y":
            continue
        elif further_action == "N":
            print("\nСпасибо, что воспользовались нашими услугами")
            break
        else:
            while error_action != "Y" and error_action != "N":
                error_action = input('Введите правильную команду "Y/N"\n')
                if error_action == "Y":
                    continue
                elif further_action == "N":
                    print("\nСпасибо, что воспользовались нашими услугами")
                else:
                    print("Неверно выбрана команда")


def сhoosing_action(number):
    """Функция описывает ветку при выборе команды действия
    """
    if int(number) == 1:
        with open(os.path.join(root_path, 'vacancies.json'), 'r', encoding="utf-8") as json_file:
            raw_json = json_file.read()
            data = json.loads(raw_json)
            for temp in data:
                print(f"({temp['title']}, {temp['id']},"
                      f" {temp['url']}, {temp['salary_from']} - {temp['salary_to']},"
                      f" {temp['company_name']})")

    elif int(number) == 2:
        top_n = int(input("Введите количество вакансий для вывода в топ N:\n"))
        with open(os.path.join(root_path, 'vacancies.json'), 'r', encoding="utf-8") as json_file:
            raw_json = json_file.read()
            data = json.loads(raw_json)
            for number in range(top_n):
                print(f"({data[number]['title']}, {data[number]['id']},"
                      f" {data[number]['url']}, {data[number]['salary_from']} - {data[number]['salary_to']},"
                      f" {data[number]['company_name']})")

    elif int(number) == 3:
        vacancy_del = input("Введите id вакансии, которой хотите удалить:\n")
        if json_saver.del_vacancy(vacancy_del) == 1:
            json_saver.del_vacancy(vacancy_del)
            print("Вакансия удалена")
        elif json_saver.del_vacancy(vacancy_del) == 0:
            print("Вакансия не удалена, так как не найдена в хранилище списков")
    else:
        print("Неверный выбор действия")
