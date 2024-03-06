import sys
import pytest
from D:Python.Project.Corsework_4.src.apifile import Apihh
@pytest.fixture
def example():
    return Apihh()

def test_get_vacancies(example):
    for data in  example.get_vacancies("Космонавт", 99)["items"]:
        assert data['salary']['from'] != None
        assert 'Космонавт' in data["name"]
        assert data['area']['id'] == '99'