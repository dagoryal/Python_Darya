from Yougile import Yougile

api = Yougile('https://ru.yougile.com')

def test_key():
    key = api.get_token()
    return key

def test_add_project(): #Создание проекта
    title = "New project"
    result = api.create_project(title)
    pr_id = result["id"]
    assert result["id"] == pr_id

def test_update(): #Изменение проекта
    title = "UpdateMe"
    old_tit = api.create_project(title)
    title_id = old_tit["id"]
    new_tit = "Updated"
    updated = api.edit_project(title_id, new_tit)
    assert updated["id"] == title_id

def test_project_id(): #Получить по айди
    title = "From id"
    res = api.create_project(title)
    self_id = res["id"]
    new_project = api.get_project(self_id)
    assert new_project ["title"] == title

def test_add_negative_project():
    title = ""
    proj = api.create_project(title)
    res = proj['message']
    assert res == ['title should not be empty']

def test_negative_update():
    old_tit = api.create_project("Updatemepls")
    title_id = old_tit['id']
    new_tit = ""
    updated = api.edit_project(title_id, new_tit)
    error_message = updated['message']
    assert error_message == ['title should not be empty']

def test_neg_project_bez_id():
    new_project = api.get_project(None)
    none_project = new_project['message']
    assert none_project == 'Проект не найден'
