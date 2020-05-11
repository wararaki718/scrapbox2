from app.module import module

def test_answer():
    x = 2
    y = 2
    assert module(x, y) == 4
