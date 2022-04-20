import os.path
import random
import time
import pyautogui
import asyncio
import subprocess
import utils


def wait_until_locate(image_path: str, downtime=1):
    probably_point = None
    while probably_point is None:
        time.sleep(downtime)
        probably_point = pyautogui.locateOnScreen(image_path)
    return probably_point


async def start_browser():
    subprocess.Popen(['C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe', '-inprivate',
                      'https://www.reddit.com/register/'])


async def sign_up(username: str, password: str):
    email_textbox_location = pyautogui.center(wait_until_locate('images\\reddit_new_email_textbox_image.png'))
    pyautogui.click(email_textbox_location.x, email_textbox_location.y)
    print('email textbox entered')

    generated_email = utils.generate_email()
    pyautogui.write(generated_email)
    print('email printed')

    pyautogui.press('enter')

    username_textbox_location = pyautogui.center(
        wait_until_locate('images\\reddit_choose_a_username_textbox_image.png'))
    pyautogui.click(username_textbox_location.x, username_textbox_location.y)
    print('username textbox entered')

    pyautogui.write(username)
    print('username printed')
    password_textbox_location = pyautogui.center(wait_until_locate('images\\reddit_password_textbox_image.png'))
    pyautogui.click(password_textbox_location.x, password_textbox_location.y)
    print('password textbox entered')

    pyautogui.write(password)
    print('password printed')
    pyautogui.press('enter')
    print('file closed')

    time.sleep(3)
    reCaptcha_location = pyautogui.center(wait_until_locate('images\\reddit_reCAPTCHA_image.png', downtime=2))
    pyautogui.click(reCaptcha_location)
    time.sleep(5)
    wait_until_locate('images\\reddit_reCaptcha_completed_image.png')
    sign_up_location = pyautogui.center(
        wait_until_locate('images\\reddit_finishing_sign_up_button_image.png', downtime=2))
    pyautogui.click(sign_up_location)
    time.sleep(3)
    if pyautogui.locateOnScreen('images\\reddit_join_button_image.png') is not None:
        if os.path.exists('reddit_accounts.txt'):
            reddit_accounts_file = open('reddit_accounts.txt', 'a')
        else:
            reddit_accounts_file = open('reddit_accounts.txt', 'w')
        reddit_accounts_file.write(username + " - " + password + '\n')
        reddit_accounts_file.close()
        print('username and password written to file')
    else:
        print('sign up failed, username and password weren\'t written to file')
    pyautogui.hotkey('alt', 'f4')


random_location = random.choice(open('windscribe_locations.txt', 'r').readlines())

if random_location.find('\n') != -1:
    random_location = random_location[:len(random_location) - 1]

print('selected location: ' + random_location)
utils.windscribe_connect(random_location)

username = utils.generate_name()
password = utils.generate_password()
print(f'username: {username} password: {password}')

asyncio.run(start_browser())
print('browser opened')

asyncio.run(sign_up(username, password))
print('done')
