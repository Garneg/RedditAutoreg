import time
import pyautogui
import string
import random
import asyncio
import subprocess


def wait_until_locate(image_path: str):
    probably_point = None
    while probably_point is None:
        time.sleep(0.5)
        probably_point = pyautogui.locateOnScreen(image_path)
    return probably_point


async def start_browser():
    subprocess.Popen(['C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe', '-inprivate', 'reddit.com'])


async def sign_up():
    signup_btn_location = pyautogui.center(wait_until_locate('images\\reddit_signin_button_image.png'))
    time.sleep(5)
    pyautogui.click(signup_btn_location.x, signup_btn_location.y)
    print('sign in button clicked')

    email_textbox_location = pyautogui.center(wait_until_locate('images\\reddit_email_textbox_image.png'))
    pyautogui.click(email_textbox_location.x, email_textbox_location.y)
    print('email textbox entered')

    generated_email = str().join(random.choices(string.ascii_lowercase, k=10)) + '@gmail.com'
    pyautogui.write(generated_email)
    print('email printed')

    pyautogui.press('enter')
    reddit_accounts_file = open('reddit_accounts.txt', 'a')

    username_textbox_location = pyautogui.center(wait_until_locate('images\\reddit_choose_a_username_textbox_image.png'))
    pyautogui.click(username_textbox_location.x, username_textbox_location.y)
    print('username textbox entered')

    generated_username = str().join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=20))
    pyautogui.write(generated_username)
    reddit_accounts_file.write(generated_username + " - ")
    print('username printed')

    password_textbox_location = pyautogui.center(wait_until_locate('images\\reddit_password_textbox_image.png'))
    pyautogui.click(password_textbox_location.x, password_textbox_location.y)
    print('password textbox entered')

    generated_password = str().join(
        random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=12))
    pyautogui.write(generated_password)
    reddit_accounts_file.write(generated_password + '\n')
    print('password printed')
    reddit_accounts_file.close()
    print('file closed')

asyncio.run(start_browser())
print('browser opened')
asyncio.run(sign_up())
