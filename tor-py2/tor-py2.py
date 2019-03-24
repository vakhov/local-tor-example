#!/usr/bin/python2
import requests
import requesocks

check_ip_site = 'http://ifconfig.me/ip'


def get_ip_requests(url):
    print('(+) Sending request with plain ole requests...')
    r = requests.get(url)
    print('(+) IP is: {}'.format(r.text.replace('\n', '')))


def get_ip_requesocks(url):
    print('(+) Sending request with requesocks...')
    session = requesocks.session()
    session.proxies = {
        'http': 'socks5://127.0.0.1:9050',
        'https': 'socks5://127.0.0.1:9050'
    }
    r = session.get(url)
    print('(+) IP is: {}'.format(r.text.replace('\n', '')))


def main():
    print('Running tests...')
    get_ip_requests(check_ip_site)
    get_ip_requesocks(check_ip_site)


if __name__ == '__main__':
    main()
