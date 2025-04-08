import requests

class Yougile:
    def __init__(self, url):
        self.url = url

    def get_token(self, login = 'dagoryal@gmail.com', password = 'dagoryal_136',
                  companyId = '3acb8d8e-dfae-4b32-bded-fdbf9103f1a8'):
        creds = {
            'login': login,
            'password': password,
            'companyId': companyId
        }
        headers = {
            'Content-Type': 'application/json'
        }
        key = requests.post(self.url+'/api-v2/auth/keys', json=creds, headers=headers)
        return key.json()

    def create_project(self, title):
        project = {
            "title": title
        }
        my_headers = {
            "Authorization": "Bearer FsFGFgTxkn8E8fopcfxjnwOpaNmLlphT9tir14PImnEA+fdXZX6cUdhCKXbnNtcS",
            'Content-Type': 'application/json'
        }
        resp = requests.post(self.url+'/api-v2/projects',json=project, headers=my_headers)
        return resp.json()

    def edit_project(self, id_proj, new_title):
        project = {
            "title": new_title
        }
        my_headers = {
            "Authorization": "Bearer FsFGFgTxkn8E8fopcfxjnwOpaNmLlphT9tir14PImnEA+fdXZX6cUdhCKXbnNtcS",
            'Content-Type': 'application/json'
        }
        resp = requests.put(self.url+'/api-v2/projects/'+id_proj, json=project, headers=my_headers)
        return resp.json()

    def get_project(self, main_id):
        my_headers = {
            "Authorization": "Bearer FsFGFgTxkn8E8fopcfxjnwOpaNmLlphT9tir14PImnEA+fdXZX6cUdhCKXbnNtcS",
            'Content-Type': 'application/json'
        }
        resp = requests.get(self.url+'/api-v2/projects/'+str(main_id), headers=my_headers)
        return resp.json()
