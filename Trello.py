import requests

def getboards():
    url = "https://api.trello.com/1/members/me/boards?key=83186eec77e3dfdef0c9564133966dc2&token=d4a9295330e07c0fb4fb595bf3df125705ddebcafde74aaf24e03d78709ae13f"
    response = requests.request("get", url)
    url1 = response.url
    print(url1)
    print(response.text)


def getsingleboard():
    url="https://api.trello.com/1/boards/5ed7862b20647c8a7b0834b1?key=83186eec77e3dfdef0c9564133966dc2&token=d4a9295330e07c0fb4fb595bf3df125705ddebcafde74aaf24e03d78709ae13f"
    response = requests.request("get", url)
    print(response.text)

def getfield():
    url ="https://api.trello.com/1/members/me/boards?fields=name,url&key=83186eec77e3dfdef0c9564133966dc2&token=d4a9295330e07c0fb4fb595bf3df125705ddebcafde74aaf24e03d78709ae13f"
    response = requests.request("get", url)
    print(response.text)

def getlist():
    url="https://api.trello.com/1/lists/5ed788d37423d77bfc76213b?key=83186eec77e3dfdef0c9564133966dc2&token=d4a9295330e07c0fb4fb595bf3df125705ddebcafde74aaf24e03d78709ae13f"
    response = requests.request("get", url)
    print(response.text)

def putboard():
    url="https://api.trello.com/1/boards/5ed7862b20647c8a7b0834b1?key=83186eec77e3dfdef0c9564133966dc2&token=d4a9295330e07c0fb4fb595bf3df125705ddebcafde74aaf24e03d78709ae13f"
    name ={
        'name' : 'qapitol'
    }
    response = requests.request("put", url,params=name)
    print(response.text)

def postboard():
    url="https://api.trello.com/1/boards?key=83186eec77e3dfdef0c9564133966dc2&token=d4a9295330e07c0fb4fb595bf3df125705ddebcafde74aaf24e03d78709ae13f"
    name = {
        'name': 'qapitol4'
    }
    response = requests.request("post", url, params=name)
    print(response.text)

def getcard():
    url="https://api.trello.com/1/lists/5ed78df251c9841b3ddb1e0a/cards?key=83186eec77e3dfdef0c9564133966dc2&token=d4a9295330e07c0fb4fb595bf3df125705ddebcafde74aaf24e03d78709ae13f"
    response = requests.request("get", url)
    print(response.text)

getboards()
getsingleboard()
getfield()
getlist()
putboard()
postboard()
getcard()






