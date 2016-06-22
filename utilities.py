import string
import random
import json


def StringGenerator(length):
    return ''.join(random.choice(string.ascii_lowercase) for i in range(length))


def EmailGenerator():
    email = StringGenerator(5) + "@" + StringGenerator(4) + ".com"
    return email


def PhoneGenerator():
    nums = [x for x in range(7)]
    return "090" + ''.join(str(x) for x in nums)


def UsersGenerator(number):
    users = []
    for i in range(number):
        user = {
            'full_name': StringGenerator(5),
            'phone_number': PhoneGenerator(),
            'user_name': StringGenerator(5),
            'password': '1234567',
            'email': EmailGenerator(),
            'secret_code': '12345',
            'answer': '12345',
            'comfirm_password': '1234567',
            'secret_question': 'whenlove',
            'Address': 'test123412 asdasd'
        }
        users.append(user)
    with open("user.txt", "w") as users_file:
        users_file.write(json.dumps(users))

