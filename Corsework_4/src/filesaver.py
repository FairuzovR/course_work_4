from abc import ABC, abstractmethod
import json
import os
from config import root_path


class BaseSaver(ABC):
    """Абстрактный класс для работы с Json файлом"""
    pass

    @abstractmethod
    def add_vacancy(self, vacancies):
        """
        Абстрактный метод с помощью которого происходит запись раннее запрошенных вакансии в Json файл
        """
        pass

    @abstractmethod
    def del_vacancy(self, id_vacancy):
        """
        Абстрактный метод, который удаляет вакансию по заданному id  json файла
        """
        pass


class JSONSaver(BaseSaver):

    def __init__(self, file_name):
        self.file_name = file_name

    def add_vacancy(self, vacancies):
        """
        Метод с помощью которого происходит запись раннее запрошенных вакансии в Json файл
        """
        with open(os.path.join(root_path, self.file_name), 'w', encoding='UTF-8') as file_json:
            data = json.dumps(vacancies, ensure_ascii=False, indent=2)
            file_json.write(data)

    def del_vacancy(self, id_vacancy):
        """
        Метод, который удаляет вакансию по заданному id  json файла
        """
        data_bool = 0
        with open(os.path.join(root_path, self.file_name), 'r', encoding='UTF-8') as file_json:
            obj = json.load(file_json)
            minimal = 0
            for temp in obj:
                if temp["id"] == str(id_vacancy):
                    obj.pop(minimal)
                    data_bool = 1
                minimal += 1

        with open(self.file_name, 'w', encoding='UTF-8') as out_file:
            json.dump(obj, out_file, ensure_ascii=False, indent=2)
        return data_bool

    @staticmethod
    def write_list_to_joisn(vacancy):
        """Метод выводит словари с нужными данными в итерации списка экземпляров класса
        и записывает их в словарь для дальнейший записи в json файл"""
        data_list = []
        for temp_vacancy in vacancy:
            data_list.append(temp_vacancy.to_json())
        return data_list
