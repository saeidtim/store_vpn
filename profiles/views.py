from django.shortcuts import render
from .requests import RequestVpn


def index(request):
    import requests
    import json

    username = 'saeidtim'
    password = 'Asli7375918bboy'

    data = {'username': username,
            'password': password}

    url = 'http://tim.unlimitedinternet.online/login'

    response = requests.post(url, data=data)

    cookies = response.cookies

    # get_list = requests.get('http://tim.unlimitedinternet.online/panel/api/inbounds/list', cookies=cookies,
    #                         headers={'Accept': 'application/json'}).json()
    #
    # user_list = list(map(lambda x: x['total']/1073741824, get_list['obj'][0]['clientStats']))

    url_add = 'http://tim.unlimitedinternet.online/panel/api/inbounds/addClient'

    data = {
        "id": 1,
        "settings": "{\"clients\":[{\"id\":\"95e4e1bb-7796-47f7-e8a7-f40151335311\",\"alterId\":0,\"email\":\"test-django\",\"limitIp\":2,\"totalGB\":42949672960,\"expiryTime\":1682864675944,\"enable\":true,\"tgId\":\"\",\"subId\":\"\"}]}"
    }
    res = requests.post(url_add, data=data, cookies=cookies).json()
    return render(request, 'profiles/index.html', context={'user_list':res})

