def validate_salary(salary):
    """Метод проверяет указана ли зарплата и отдает 0 в случае None"""
    if salary is None:
        return 0
    else:
        return salary


class Vacancy:
    """
    Класс обратывающий полученную информацию
    """

    def __init__(self, title, url, salary_from, salary_to, company_name, id):
        self.title = title
        self.url = url
        self.salary_from = validate_salary(salary_from)
        self.salary_to = validate_salary(salary_to)
        self.company_name = company_name
        self.id = id

    @staticmethod
    def get_vacancies(vacancies):
        """Статический метод, который выбирает нужные параметры
         и создает список экзамляров классов с помощью класс метода'"""
        new_vacancies = []
        for vacancy in vacancies:
            data = {
                'title': vacancy['name'],
                'id': vacancy['id'],
                'url': vacancy['alternate_url'],
                'salary_from': vacancy['salary']['from'],
                'salary_to': vacancy['salary']['to'],
                'company_name': vacancy['employer']['name'],
            }
            new_vacancies.append(Vacancy.from_dict(data))
        return new_vacancies

    @classmethod
    def from_dict(cls, vacancy):
        """Класс метод"""
        return cls(**vacancy)

    def __str__(self):
        return f"({self.title}, {self.id}, {self.url}, {self.salary_from} - {self.salary_to}, {self.company_name})"

    def __lt__(self, other):
        """
        Магический метод сравнения, который понадобится для сортировки списка
        """
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
        """
        Метод для вывода нужно информации в будущем из экземпляра класса
        """
        return {
            "title": self.title,
            'id': self.id,
            "url": self.url,
            "salary_from": self.salary_from,
            "salary_to": self.salary_to,
            "company_name": self.company_name
        }
