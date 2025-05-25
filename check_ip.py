import requests

if __name__ == '__main__':

    # getting the current public ip for the device
    resp = requests.get('http://ipinfo.io/ip')
    curr_public_ip = resp.text

    # getting the stored ip
    with open('ip.txt', 'r') as f:
        stored_public_ip = f.read()

    if curr_public_ip.strip() != stored_public_ip.strip():
        with open('ip.txt', 'w') as f:
            f.write(curr_public_ip)