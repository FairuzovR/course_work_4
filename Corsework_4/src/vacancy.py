from src.apifile import Apihh
class Vacancy:
    def __init__(self, title, url, salary_from, salary_to, company_name):
        self.title = title
        self.url = url
        self.salary_from = self.validate_salary(salary_from)
        self.salary_to = self.validate_salary(salary_to)
        self.company_name = company_name

    def validate_salary(self, salary):
        if salary == None:
            return 0
        else:
            return salary


    @staticmethod
    def get_vacancies(vacancies):
        new_vacancies = []
        for vacancy in vacancies:
            data = {
                'title': vacancy['name'],
                'url': vacancy['alternate_url'],
                'salary_from': vacancy['salary']['from'],
                'salary_to': vacancy['salary']['to'],
                'company_name': vacancy['employer']['name'],
            }
            new_vacancies.append(Vacancy.from_dict(data))
        return new_vacancies

    @classmethod
    def from_dict(cls, vacancy):
        return cls(**vacancy)

    def __str__(self):
        return f"({self.title}, {self.url}, {self.salary_from} - {self.salary_to}, {self.company_name})"

    def __lt__(self, other):
        if self.salary_to != 0 and self.salary_from != 0:
            return (int(self.salary_to) + int(self.salary_from) / 2) < (
                    int(other.salary_to) + int(other.salary_from) / 2)
        elif self.salary_to == 0 and self.salary_from != 0:
            return int(self.salary_from) < int(other.salary_from)
        elif self.salary_to != 0 and self.salary_from == 0:
            return int(self.salary_to) < int(other.salary_to)
        else:
            return int(self.salary_to) < int(other.salary_to)

    def to_json(self):
        return {
            "title": self.title,
            "url": self.url,
            "salary_from": self.salary_from,
            "salary_to": self.salary_to,
            "company_name": self.company_name
        }


# a = Apihh()
# v_list = Vacancy.get_vacancies(a.get_vacancies('Менеджер', 99)['items'])
# v_list.sort(reverse=True)
# for i in v_list:
#     print(str(i))