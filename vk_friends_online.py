import getpass

import vk


APP_ID = 6005016  # чтобы получить app_id, нужно зарегистрировать своё приложение на https://vk.com/dev


def get_user_login():
    user_login = None
    while not user_login:
        user_login = input('User login: ')
    return user_login


def get_user_password():
    user_password = None
    while not user_password:
        user_password = getpass.getpass(prompt='Password: ')
    return user_password


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends'
    )
    api = vk.API(session)
    # например, api.friends.get()
    online_friends = api.friends.getOnline()
    online_friends_info = api.friends.get(user_id=online_friends)
    return online_friends_info


def output_friends_to_console(friends_online):
    print('Online friens: {}'.format(len(friends_online)))
    for friend in friends_online:
        print('{} {}'.format(friend['first_name'], friend['last_name']))

if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    print(friends_online)
    output_friends_to_console(friends_online)
    
