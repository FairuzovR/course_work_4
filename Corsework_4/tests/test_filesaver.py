import pytest
import json
import os
from config import root_path
from src.filesaver import JSONSaver

@pytest.fixture
def ass_to_json():
    json_file = [
        {
            "title": "Врач здравпункта",
            "id": "93548977",
            "url": "https://hh.ru/vacancy/93548977",
            "salary_from": 230000,
            "salary_to": 230000,
            "company_name": "Нефтяник-мед"
        },
        {
            "title": "Врач акушер-гинеколог",
            "id": "94143070",
            "url": "https://hh.ru/vacancy/94143070",
            "salary_from": 100000,
            "salary_to": 250000,
            "company_name": "АПБ групп"
        }]

    return json_file
def test_add_vacancy(ass_to_json):
    exm_add_json = JSONSaver("test.json")
    exm_add_json.add_vacancy(ass_to_json)
    with open(os.path.join(root_path, "test.json"), 'r', encoding="utf-8") as json_file:
        raw_json = json_file.read()
        data = json.loads(raw_json)
        assert len(data[0]) == 6
        assert len(data[1]) == 6
        for key in data[0]:
            assert key in ['title', 'url', 'salary_from', 'salary_to', 'company_name', 'id']
        for key in data[1]:
            assert key in ['title', 'url', 'salary_from', 'salary_to', 'company_name', 'id']

def test_del_vacancy(ass_to_json):
    exm_add_json = JSONSaver("test.json")
    exm_add_json.add_vacancy(ass_to_json)
    exm_add_json.del_vacancy('94143070')
    with open(os.path.join(root_path, "test.json"), 'r', encoding="utf-8") as json_file:
        raw_json = json_file.read()
        data = json.loads(raw_json)
        for num in range(len(data)):
            data[num]['id'] != '94143070'
