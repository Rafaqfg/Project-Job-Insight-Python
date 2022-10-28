from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    jobs = read_brazilian_file("tests/mocks/brazilians_jobs.csv")
    keys = set(key for dict in jobs for key in dict.keys())

    expected_keys = ["type", "salary", "title"]

    assert all((key in expected_keys) for key in keys)
