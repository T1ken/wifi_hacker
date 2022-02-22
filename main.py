import subprocess


def extract_wifi_passwords():
    profiles_data = subprocess.check_output('netsh wlan show profiles').decode('CP866').split('\n')
    profiles = [i.split(':')[1] for i in profiles_data if 'Все профили пользователей' in i]

    for profile in profiles:
        profile_right_name = profile.split('\r')[0]
        profile_info = subprocess.check_output('netsh wlan show profile {} key=clear'.format(profile_right_name)).decode('CP866').split('\n')
        try:
            password = [i.split(':')[1].split('\t')[0].strip() for i in profile_info if 'Содержимое ключа' in i][0]
        except IndexError:
            password = None

        with open('wifi_passwords.txt', 'a', encoding='CP866') as file:
            file.write('Profile: {}Password: {}\n{}\n'.format(profile, password, "#" * 20))


def main():
    extract_wifi_passwords()
    print('I hate niggas')


if __name__ == '__main__':
    main()
