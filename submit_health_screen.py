# import mechanicalsoup
# import json

# f = open('user_info.json')
# users = json.load(f)

# #make iterative
# user = users[0]
# print(user)

# browser = mechanicalsoup.StatefulBrowser(
#     soup_config={'features': 'lxml'},
#     raise_on_404=True,
#     user_agent='MyBot/0.1: mysite.example.com/bot_info',
# )

# browser.set_verbose(2)

# browser.open('https://healthscreening.schools.nyc/?type=G')
# browser.select_form('form[action="/home/submit"]')
# browser.form.print_summary()

# browser["Type"] = "G"
# browser["IsOther"] = "False"
# browser["IsStudent"] = "1"
# browser["FirstName"] = "Jamir"
# browser["LastName"] = "Quezada+Cen"
# browser["Email"] = "rofol611@gmail.com"
# browser["State"] = "NY"
# browser["Location"] = "20K768-K747"

# browser["Answer1"] = "0"
# browser["Answer2"] = "0"
# browser["Answer3"] = "0"
# browser["Answer4"] = "0"
# browser["ConsentType"] = ""


# resp = browser.submit_selected()
# # form body
# {
# 	"Type": "G",
# 	"IsOther": "False",
# 	"IsStudent": "1",
# 	"FirstName": "Jamir",
# 	"LastName": "Quezada+Cen",
# 	"Email": "rofol611@gmail.com",
# 	"State": "NY",
# 	"Location": "20K768-K747",
# 	"Floor": "",
# 	"Answer1": "0",
# 	"Answer2": "0",
# 	"Answer3": "0",
# 	"Answer4": "0",
# 	"ConsentType": "",
# 	"__RequestVerificationToken": 
# }

import json
import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://healthscreening.schools.nyc/'
GUEST_URL = BASE_URL + '?type=G'
SUBMIT_URL = BASE_URL + 'home/submit/'


def get_request_token():
    r = requests.get('https://healthscreening.schools.nyc/?type=G')
    soup = BeautifulSoup(r.text, 'html.parser')
    request_token = soup.find(attrs={"name": "__RequestVerificationToken"})['value']
    return request_token

def build_request(user):
    params = "?"
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

