# Automate Health Screen Form

## DISCLAIMER

This should only be used if the questionaire answers are same day to day for healthy guest/student. If conditions changes, please manually fill out a form online prior to entering the building to determine if you are allowed access. Any manual submission or papers filled out on site will supersed this.

Alternatively, editing the user_info.json with the correct questionaire answers and triggering a manual run will generate the latest result.

This does not guarantee any accuracy or user errors when filling out the form. If you are unsure, FILL IT OUT YOURSELF.

We are not responsible for any inaccuracy or misuse of the script.

## Background

Script follows the fields required for [**Guest** health screening form](https://healthscreening.schools.nyc/?type=G). If you want to use the login, this cannot handle it. You can however modify this to login or use the user info as guest.

It will build requests based on the information in json file and sends them out. You can input multiple guests information in the json file.

You should receive an email denoting your screening status after running the script **per person**. If you didn't receive an email, something went wrong! Either the form changed, the request changed, or a field value is incorrect/missing.

## Setup

1. Virtual Environment and Install Package Dependencies

```bash
# create virtual environment
python3 -m venv env

# activate virtual env
# you need to run ONE of theses before running any python commands

.\env\Scripts\Activate.ps1  # ONLY IF WINDOWS POWERSHELL
# OR
source env/bin/activate  # ONLY IF MAC
```

```bash
# Install dependencies
pip install -r requirements.txt
```

2. Fill out info for your users in `user_info.json` or whatever you want to name it. Just make sure to change the filename in `submit_health_screen.py`

3. You should receive an email in your inbox denoting if you can access the building.

## Form Fields

As of September 2021, the below fields and values are available in the form and need to be in the json file.

You can add multiple people by adding them in an array in the json file.

```json
[
  {
    "IsStudent": "1",
    "FirstName": "George",
    "LastName": "Richards",
    "Email": "rrichards029@gmail.com",
    "State": "NY",
    "Location": "XAPN-XAPN",
    "Floor": "",
    "Answer1": "0",
    "Answer2": "0",
    "Answer3": "0",
    "Answer4": "0"
  },
  {
    "IsStudent": "0",
    "FirstName": "Jenny",
    "LastName": "James",
    "Email": "jjames293@gmail.com",
    "State": "NY",
    "Location": "18K818",
    "Floor": "",
    "Answer1": "0",
    "Answer2": "0",
    "Answer3": "0",
    "Answer4": "0"
  }
]
```

### Key Value Mappings

All required unless denoted otherwise

`IsStudent`: What type of guest are you?
| Value | Definition |
|-------|-----------------------------------------|
| 1 | I'm a Student |
| 0 | I'm a Visitor or a Family Member |
| 2 | I'm a non-DOE Staff/Contracted Provider |

`FirstName`: First name
Free form text. `-`(dash) is not supported. Use `+` to replace space, e.g. `Mary Jane` should be `MaryJane` or `Mary+Jane`

`LastName`: Last name
Same as `FirstName` requirements

`Email`: email address where you want to recieve the status/pass

`State`: State abbreviation where the location is at

`Location`: Location code. You can get the `Location` code by going to the website directly and search for your location. The code is the value in parenthesis after the name.

`Floor`: [optional] Which floor are you going to.

`Answer1`: Have you experienced any symptoms of COVID-19, including a fever of 100.0 degrees F or greater, a new cough, new loss of taste or smell or shortness of breath that started in the past 10 days?
| Value | Definition |
|-------|------------|
| 0 | No |
| 1 | Yes |

`Answer2`: In the past 10 days, have you gotten a positive result from a COVID-19 diagnostic test (not a blood test). Please note that 10 days is measured from the day you were tested, not from the day when you got the test result.
| Value | Definition |
|-------|------------|
| 0 | No |
| 1 | Yes |

`Answer3`: Are you considered fully vaccinated against COVID-19 by CDC guidelines?1 Please note that to be considered fully vaccinated by CDC guidelines, two weeks must have passed since you received the second dose in a two-dose series or two weeks must have passed since you received a single-dose vaccine.
| Value | Definition |
|-------|------------|
| 0 | No |
| 1 | Yes |

`Answer4`: To the best of your knowledge, in the past 10 days, have you been in close contact (within 6 feet for at least 10 minutes over a 24 hour period) with anyone who is currently diagnosed with COVID-19 or who has been told they have symptoms of COVID-19? Clinical staff who were in appropriate personal protective equipment (PPE) are not considered close contacts in these scenarios.
| Value | Definition |
|-------|------------|
| 0 | No |
| 1 | Yes |
