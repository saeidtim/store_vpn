import requests
import json

class RequestVpn:
    def __int__(self):
        username = 'saeidtim'
        password = 'Asli7375918bboy'

        data = {'username': username,
                'password': password}

        url = 'http://tim.unlimitedinternet.online/login'

        response = requests.post(url, data=data)

        self.cookies = response.cookies

    def get_list(self):
        return requests.get('http://tim.unlimitedinternet.online/panel/api/inbounds/list', cookies=self.cookies, headers= {'Accept':'application/json'}).json()


    def add(self):
        url_add = 'http://tim.unlimitedinternet.online/panel/api/inbounds/addClient'

        data = {
            "id": 4,
            "settings": "{\"clients\":[{\"id\":\"95e4e1bb-7796-47f7-e8a7-f40551945376\",\"alterId\":0,\"email\":\"New Client\",\"limitIp\":2,\"totalGB\":42949672960,\"expiryTime\":1682864675944,\"enable\":true,\"tgId\":\"\",\"subId\":\"\"}]}"
            }
        res = requests.post(url_add, data=data, cookies=cookies).json()
        return res

