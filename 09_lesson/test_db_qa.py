from random import randint
from DbTable import DbTable

db = DbTable("postgresql://postgres:1234@localhost:5432/QA")

def test_get_subject():
    res = db.get_subject()
    assert len(res) is not None

def test_create_subject():
    summ = db.get_subject()
    len_before = len(summ)

    subject_title = "qa"
    subject_id = randint(16, 100)

    db.create(subject_title, subject_id)
    summ = db.get_subject()
    len_after = len(summ)

    max_id = db.get_max_id()
    db.delete(max_id)

    assert len_after - len_before == 1
    assert max_id == subject_id

def test_edit():
    subject_title = "qa"
    subject_id = randint(16, 100)
    db.create(subject_title, subject_id)

    new_name = "updated"
    db.edit(new_name, subject_id)
    sub = db.select_by_id(subject_id)

    db.delete(sub)
    assert sub == subject_id
    assert new_name == "updated"

def test_delete_subject():
    db.create('delete_me', 888)
    sub = db.get_max_id()
    len_list = len(db.get_subject())

    db.delete(sub)
    len_after = len(db.get_subject())

    assert len_after - len_list == -1
