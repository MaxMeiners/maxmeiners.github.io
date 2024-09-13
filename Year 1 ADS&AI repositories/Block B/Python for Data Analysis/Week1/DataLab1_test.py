import DataLab1;

def test_hello():
    assert DataLab1.hello_world() == "Hello World!"

def test_even_or_odd():
    assert DataLab1.even_or_odd(6) == "even"

def test_adult_or_child():
    assert DataLab1.adult_or_child(6) == "child"

def test_rivm():
    assert DataLab1.rivm("1961 - 1971") == "Groningen"



