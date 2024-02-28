from src.apifile import Apihh
class Vacancy:
    def __init__(self, title, url, salary_from, company_name):
        self.title = title
        self.url = url
        self.salary_from = salary_from
        self.company_name = company_name

    @classmethod
    def cast_to_object_list(cls, hh_vacancies):
        vacancies = []
        for vac_data in hh_vacancies:
            title = vac_data['name']
            url = vac_data['alternate_url']
            salary_from = vac_data['salary']['from']
            company_name = vac_data['employer']['name']
            instance = cls(title, url, salary_from, company_name)
            vacancies.append(instance)
        return vacancies

    def __str__(self):
        return f"({self.title}, {self.url}, {self.salary_from}, {self.company_name})"
    def __lt__(self, other):
        self.temp = 0
        if self.salary_from == None:
            self.salary_from = 0
        return self.salary_from < other.salary_from


a = Apihh()
v_list = Vacancy.cast_to_object_list(a.get_vacancies('Космонавт', 99)['items'])
v_list.sort()
print(type(v_list))
for i in v_list:
    print(str(i))