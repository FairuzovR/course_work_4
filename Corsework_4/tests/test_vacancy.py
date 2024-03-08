import pytest
from src.apifile import Apihh
from src.vacancy import Vacancy

@pytest.fixture
def example_for_apifile():
    return Apihh()

@pytest.fixture
def example_for_apifile():
    return Apihh()

@pytest.fixture
def example_class():
    data = {
            'title': 1,
            'id': 1,
            'url': 1,
            'salary_from': 1,
            'salary_to': 1,
            'company_name': 1
        }
    return data

def test_init():
    with pytest.raises(TypeError):
        Vacancy("Начальник хозяйственного отдела", "94262122", "https://hh.ru/vacancy/94262122",
                140000, 150000)

def test_get_vacancies(example_for_apifile):
    get_vacan = example_for_apifile.get_vacancies("Начальник хозяйственного отдела", 99)['items']
    assert isinstance((Vacancy.get_vacancies(get_vacan)), list)

def test_str():
    str_exp = Vacancy(1, 1, 1, 1, 1, 1,)
    assert str(str_exp) == '(1, 1, 1, 1 - 1, 1)'

def test_lt():
    exp_1 = Vacancy(1, 1, 1000, 2000, 1, 1,)
    exp_2 = Vacancy(1, 1, 2000, 4000, 1, 1,)
    exp_list = [exp_1, exp_2]
    exp_list.sort(reverse=True)
    assert  exp_list[0] == exp_2

def test_to_josn():
    exp_1 = Vacancy(1, 1, 1000, 2000, 1, 1, )
    assert exp_1.to_json() == {
        "title": 1,
        'id': 1,
        "url": 1,
        "salary_from": 1000,
        "salary_to": 2000,
        "company_name": 1
    }
