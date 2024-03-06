from abc import ABC, abstractmethod
import requests


class BaseAPI(ABC):
    """
    Абстрактный класс с работой по запросу информации с hh.ru
    """
    @abstractmethod
    def get_vacancies(self, keyword, town):
        pass


class Apihh(BaseAPI):
    """
    Класс для работы с запросом вакансии с hh.ru
    """

    def __init__(self):
        self.data = None
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
        """Метод класса запроса вакансий по заданным параметрам"""
        self.base_params['area'] = town
        self.base_params['text'] = keyword
        response = requests.get(self.url, params=self.base_params)
        self.data = response.json()
        return self.data
    