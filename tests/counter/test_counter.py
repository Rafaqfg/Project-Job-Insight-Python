from src.counter import count_ocurrences


def test_counter():
    assert count_ocurrences("src/jobs.py", "Python") == 1639
    assert count_ocurrences("src/jobs.py", "JavaScript") == 122
