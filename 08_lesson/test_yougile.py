from Yougile import Yougile

api = Yougile('https://ru.yougile.com')

def test_key():
    key = api.get_token()
    return key

def test_add_project():
    title = "New project123"
    result = api.create_project(title)
    return result["id"]

def test_update():
    old_tit = api.create_project("UpdateMe")
    new_tit = "Updated"
    updated = api.edit_project(old_tit, new_tit)
    return updated

def test_project_id():
    title = "From id"
    res = api.create_project(title)
    self_id = res
    new_project = api.get_project(self_id)
    return new_project

def test_add_negative_project():
    title = ""
    result = api.create_project(title)
    return result

def test_negative_update():
    old_tit = api.create_project("")
    new_tit = "Updated"
    updated = api.edit_project(old_tit, new_tit)
    return updated

def test_neg_project_id():
    title = "From id"
    res = api.create_project(title=None)
    self_id = res
    new_project = api.get_project(self_id)
    return new_project