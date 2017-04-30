import getpass

import vk


APP_ID = 6005016


def get_user_login():
    user_login = input('User login: ')
    return user_login


def get_user_password():
    user_password = getpass.getpass(prompt='Password: ')
    return user_password


def get_online_friends(login, password):
    try:
        session = vk.AuthSession(app_id=APP_ID,
                                 user_login=login,
                                 user_password=password,
                                 scope='friends')
    except vk.exceptions.VkAuthError:
        print('Authorization error')
    else:
        api = vk.API(session)
        online_friends = api.friends.getOnline()
        online_friends_info = api.users.get(user_ids=online_friends)
        return online_friends_info


def output_friends_to_console(friends_online):
    if friends_online is None:
        return
    print('Online friends: {}'.format(len(friends_online)))
    if friends_online:
        for friend in friends_online:
            print('{} {}'.format(friend['first_name'], friend['last_name']))


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
 