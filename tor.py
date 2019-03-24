"""

"""

import requests

proxies = {
    'http': 'socks5://127.0.0.1:9050',
    'https': 'socks5://127.0.0.1:9050'
}


def main():
    url = 'https://api.ipify.org'

    # Запрос без проксирования
    response = requests.get(url)
    print(f'ip: {response.text.strip()}')

    # Запрос с TOR проксированием
    response = requests.get(url, proxies=proxies)
    print(f'tor ip: {response.text.strip()}')


if __name__ == '__main__':
    main()
