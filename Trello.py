import requests

def getboards():
    url = "https://api.trello.com/1/members/me/boards?key={yourkey}&token={yourtoken}"
    response = requests.request("get", url)
    url1 = response.url
    print(url1)
    print(response.text)


def getsingleboard():
    url="https://api.trello.com/1/boards/{boardid}?key={yourkey}&token={yourtoken}"
    response = requests.request("get", url)
    print(response.text)

def getfield():
    url ="https://api.trello.com/1/members/me/boards?fields=name,url&key={yourkey}&token={yourtoken}"
    response = requests.request("get", url)
    print(response.text)

def getlist():
    url="https://api.trello.com/1/lists/{listid}?key={yourkey}&token={yourtoken}"
    response = requests.request("get", url)
    print(response.text)

def putboard():
    url="https://api.trello.com/1/boards/{boardid}?key={yourkey}&token={yourtoken}"
    name ={
        'name' : 'qapitol'
    }
    response = requests.request("put", url,params=name)
    print(response.text)

def postboard():
    url="https://api.trello.com/1/boards?key={yourkey}&token={yourtoken}"
    name = {
        'name': 'qapitol4'
    }
    response = requests.request("post", url, params=name)
    print(response.text)

def getcard():
    url="https://api.trello.com/1/lists/{listid}/cards?key={yourkey}&token={yourtoken}"
    response = requests.request("get", url)
    print(response.text)

getboards()
getsingleboard()
getfield()
getlist()
putboard()
postboard()
getcard()






