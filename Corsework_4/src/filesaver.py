from abc import ABC, abstractmethod
import json
from src.vacancy import Vacancy
from src.apifile import Apihh

class BaseSaver(ABC):
    pass
    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

class JSONSaver(BaseSaver):

    def __init__(self, file_name):
        self.file_name = file_name

    def add_vacancy(self, vacancy):
        data_list = []
        for temp_list in vacancy:
            data_list.append(temp_list.to_json())
        #     # data = json.dumps(data_list, ensure_ascii=False,  indent=4)
        with open (self.file_name, 'w', encoding='UTF-8') as file_json:
                json.dump(data_list, file_json, ensure_ascii=False,  indent=2)

    def del_vacancy(self, vacancy):
        with open(self.file_name, 'r', encoding='UTF-8') as file_json:
            obj = json.load(file_json)
            print(obj)
            minimal = 0
            for temp in obj:
                if temp["title"] == vacancy:
                    obj.pop(minimal)
                minimal += 1

        with open(self.file_name, 'w', encoding='UTF-8') as out_file:
            json.dump(obj, out_file, ensure_ascii=False, indent=2)


# b = JSONSaver('Gh.json')
# # b.add_vacancy()
# b.del_vacancy("Начинающий специалист/стажер в копицентр (ул.Космонавтов)")

# a = Apihh()
# v_list = Vacancy.get_vacancies(a.get_vacancies('Менеджер', 99)['items'])
# v_list.sort(reverse=True)
# b = JSONSaver('Gh.json')
# b.add_vacancy(v_list)

# for i in v_list:
#     print(str(i))