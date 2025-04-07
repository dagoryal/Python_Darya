from random import randint
from DbTable import DbTable

db = DbTable("postgresql://postgres:1234@localhost:5432/QA")

def test_get_subject():
    res = db.get_subject()
    assert isinstance(res, list)

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
    new = db.create(subject_title, subject_id)
    prj = new["subject_id"]

    new_name = "updated"
    edited = db.edit(new_name, prj)

    db.delete(prj)
    assert edited["subject_title"] == new_name
    assert edited['subject_id'] == prj

def test_delete_subject():
    db.create('delete_me', 888)
    sub = db.get_max_id()
    len_list = len(db.get_subject())

    db.delete(sub)
    len_after = len(db.get_subject())

    assert len_after - len_list == -1
