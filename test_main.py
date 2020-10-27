from main import User


def test_user_has_name():

    A = User()
    assert A.parent is None
    assert A.children == set()


def test_user_has_children():
    A = User()
    B = User()

    A.set_link(child=B)

    assert A.parent is None
    assert A.children == {B}

    assert B.parent == A
    assert B.children == set()
