import requests

def test_public_ip():
    with open('ip.txt', 'r') as f:
        stored_ip = f.read()

    assert stored_ip.strip() == requests.get('http://ipinfo.io/ip').text.strip()
