import requests
import urllib.parse

clan_tag = urllib.parse.quote_plus('#2802GQRV8')
api_url = 'https://api.clashofclans.com/v1'
API_KEY = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjBkYjNiZWUwLWU0MjUtNDc3ZS05ZDQ1LWQwZmUyOWQ1YTUzOSIsImlhdCI6MTY2OTA0MDU1Mywic3ViIjoiZGV2ZWxvcGVyL2Q2OWE3MzFhLTk1ZTUtYTc1OS01MGMzLWUxMWE0MjQ4ZjAwNCIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjExMy4xMTAuMTY1LjkxIl0sInR5cGUiOiJjbGllbnQifV19.mcfuthM2cO06s_1QCf6DXd9dDdQdF8zQlenyp3Wb3edhVrPRUP1HwRk0CaWNsxxhDXeoWuan8G3oWHZ9cgKMgw'
headers = {
    'Authorization': f'Bearer {API_KEY}'
}


def get_clan_members():
    url = f'{api_url}/clans/{clan_tag}/members'
    r = requests.get(url=url, headers=headers)
    if r.status_code != 200:
        print(r.text)
        return {}
    else:
        return r.json()


def get_users_info(user_tag):
    url = f'{api_url}/players/{urllib.parse.quote_plus(user_tag)}'
    print(url)
    r = requests.get(url=url, headers=headers)
    if r.status_code != 200:
        print(r.text)
        return {}
    else:
        return r.json()


def get_capitalraid_log():
    """ 这个 api 返回比较慢，只取第一个，每周一下午三点十分执行 """
    url = f'{api_url}/clans/{clan_tag}/capitalraidseasons'
    r = requests.get(url=url, headers=headers)
    if r.status_code != 200:
        print(r.text)
        return {}
    else:
        return r.json()


if __name__ == "__main__":
    my_tag = urllib.parse.quote_plus('#UL2GG0QY')
    # get_clan_members()
    get_users_info(user_tag=my_tag)