from src.sorting import sort_by

jobs_mock = [
    {"min_salary": 1000, "max_salary": 10000, "date_posted": "2022-11-01"},
    {"min_salary": 1200, "max_salary": 12000, "date_posted": "2022-10-11"},
    {"min_salary": 5000, "max_salary": 120000, "date_posted": "2022-10-13"},
    {"min_salary": 500, "max_salary": 8123, "date_posted": "2022-08-01"},
    {"min_salary": 654, "max_salary": 9571, "date_posted": "2022-11-01"},
]

keys = ["min_salary", "max_salary", "date_posted"]


def test_sort_by_criteria():
    for criteria in keys:
        sort_by(jobs_mock, criteria)
        if criteria == "max_salary":
            assert jobs_mock[0][criteria] >= jobs_mock[1][criteria]
        else:
            assert jobs_mock[0][criteria] <= jobs_mock[1][criteria]
