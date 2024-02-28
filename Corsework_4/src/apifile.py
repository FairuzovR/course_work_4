from abc import ABC, abstractmethod
import requests
import json

class BaseAPI(ABC):
    @abstractmethod
    def get_vacancies(self, keyword, town):
        raise TypeError("Обязательно ввидите ключевое слово наименования вакансии")

class Apihh():
    def __init__(self):  #             "clusters": "true"
        self.base_params = {
            "only_with_salary": "true",
            "enable_snippets": "true",
            "st": "searchVacancy",
            "text": None,
            "search_field": "name",
            "area": None,
            "per_page": 100,
        }
        self.url = 'https://api.hh.ru/vacancies'

    def get_vacancies(self, keyword, town):
        self.base_params['area'] = town
        self.base_params['text'] = keyword
        response = requests.get(self.url, params=self.base_params)
        data = response.json()
        return data

# a = Apihh()
# print(a.get_vacancies('Космонавт', 99))