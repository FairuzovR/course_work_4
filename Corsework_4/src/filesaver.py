from abc import ABC, abstractmethod
import json
import os
from config import root_path
from src.vacancy import Vacancy
from src.apifile import Apihh

class BaseSaver(ABC):
    pass
    @abstractmethod
    def add_vacancy(self, vacancies):
        pass

class JSONSaver(BaseSaver):

    def __init__(self, file_name):
        self.file_name = file_name

    def add_vacancy(self, vacancies):
        with open (os.path.join(root_path, self.file_name), 'w', encoding='UTF-8') as file_json:
            data = json.dumps(vacancies, ensure_ascii=False, indent=2)
            file_json.write(data)

    def del_vacancy(self, vacancy):
        with open(os.path.join('../', root_path, self.file_name), 'r', encoding='UTF-8') as file_json:
            obj = json.load(file_json)
            print(type(obj))
            minimal = 0
            for temp in obj:
                if temp["title"] == vacancy:
                    obj.pop(minimal)
                minimal += 1

        with open(self.file_name, 'w', encoding='UTF-8') as out_file:
            json.dump(obj, out_file, ensure_ascii=False, indent=2)

    def write_list_to_joisn(self, vacancy):
        data_list = []
        for temp_vacancy in vacancy:
            data_list.append(temp_vacancy.to_json())
        return data_list




# b = JSONSaver('vacancies.json')
# # # # b.add_vacancy()
# b.del_vacancy("Менеджер по продажам в аэропорт")
#
# # a = Apihh()
# # v_list = Vacancy.get_vacancies(a.get_vacancies('Менеджер', 99)['items'])
# # v_list.sort(reverse=True)
# # b = JSONSaver('Gh.json')
# # b.add_vacancy(v_list)
#
# # for i in v_list:
# #     print(str(i))