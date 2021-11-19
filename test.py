from main import reverse_it


def test_reverse_one_line():
    assert reverse_it(['cba']) == ['abc']


def test_reverse_multi():
    assert reverse_it(['abc', '123123']) == ['cba', '321321']

