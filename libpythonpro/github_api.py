import requests


def buscar_avatar(usuario):
    """ teste limite de 120 caracteresflainforma o usuario(param) e (return) retrona o avatar teste limite de 120 caracteres"""
    url = f'https://api.github.com/users/{usuario}'
    resp = requests.get(url)
    return resp.json()['avatar_url']

if __name__ == '__main__':
    print(buscar_avatar('abrbullyz'))



