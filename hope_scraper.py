import requests
from bs4 import BeautifulSoup
from datetime import datetime
from dateutil.parser import parse
import pytz

tz = pytz.timezone('America/Chicago')
now = datetime.now(tz)


def get_saturday_menu():

    menu_objects = []
    page = requests.get(
        'http://www.lutheranchurchofhope.org/west-des-moines/about-us/food-service/saturday-evening-menu/')

    soup = BeautifulSoup(page.text, 'html.parser')

    menu_div = soup.find(class_='first group_2of3')

    menu = menu_div.find_all('p')

    for menu_row in menu[1:]:
        if len(menu_row) > 0:
            menu_date = parse(
                menu_row.contents[0].contents[0] + ' ' + str(now.year))
            menu_date = menu_date.replace(tzinfo=tz)
            menu_date.replace(tzinfo=tz)
            menu_objects.append(
                {"date": menu_date, "menu": menu_row.contents[2]})
            # print(menu_row.contents)

    return menu_objects


def next_saturday_menu():

    menu_objects = get_saturday_menu()
    next_menu = {}

    for menu_object in menu_objects:
        if now.year == menu_object["date"].year and now.month == menu_object["date"].month and now.day == menu_object["date"].day:
            next_menu = menu_object
            break
        elif now < menu_object["date"]:
            next_menu = menu_object
            break

    return next_menu


def saturday_night_menu_rest_of_month():
    menu_objects = get_saturday_menu()
    next_menus = []

    for menu_object in menu_objects:
        if now.year == menu_object["date"].year and now.month == menu_object["date"].month and now.day == menu_object["date"].day:
            next_menus.append(menu_object)
        elif now < menu_object["date"]:
            next_menus.append(menu_object)

    return next_menus
