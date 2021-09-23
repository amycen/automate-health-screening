import json
import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://healthscreening.schools.nyc/'
GUEST_URL = BASE_URL + '?type=G'
SUBMIT_URL = BASE_URL + 'home/submit/'
GUEST_FORM_PARAMS = '?type=G&IsOther=False&'


def get_request_token():
    r = requests.get(GUEST_URL)
    soup = BeautifulSoup(r.text, 'html.parser')
    request_token = soup.find(attrs={"name": "__RequestVerificationToken"})['value']
    return request_token

def build_request(user):
    params = GUEST_FORM_PARAMS
    for key in user.keys():
        params += f'{key}={user[key]}&'
    request_token = get_request_token()
    request = f'{SUBMIT_URL}{params}ConsentType=&__RequestVerificationToken={request_token}'
    return request

def submit_request(request):
    r = requests.post(request)
    print(f'Sending...{request}\n')
    print(f'{r.text}\n\n')


if __name__ == "__main__":
    # import users from json file
    f = open('user_info.json')
    users = json.load(f)
    for user in users:
        request = build_request(user)
        submit_request(request)

