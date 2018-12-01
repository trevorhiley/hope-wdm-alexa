import requests
from bs4 import BeautifulSoup
from datetime import datetime
from dateutil.parser import parse
import pytz

tz = pytz.timezone('America/Chicago')
now = datetime.now(tz)


def get_saturday_menu():


    page = requests.get(
        'http://www.lutheranchurchofhope.org/west-des-moines/about-us/food-service/saturday-evening-menu/')

    soup = BeautifulSoup(page.text, 'html.parser')

    menu_div = soup.find(class_='first group_2of3')

    menu = menu_div.find_all('p')

    menu_objects = parse_menu_div(menu)

    print(menu_objects)

    return menu_objects


def saturday_night_menu_next():

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

def parse_menu_div(menu):
    menu_objects = []
    for menu_row in menu[1:]:
        if len(menu_row) > 0:
            menu_date = parse_menu_date(menu_row)
            menu_objects.append(
                {"date": menu_date, "menu": menu_row.contents[2]})

    return menu_objects

def parse_menu_date(menu_row):
    date_content = ""
    if "&" in menu_row.contents[0].contents[0]:
        and_position = menu_row.contents[0].contents[0].index('&')
        date_content = menu_row.contents[0].contents[0][0:and_position]
    else:
        date_content = menu_row.contents[0].contents[0]
    menu_date = parse(
                date_content + ' ' + str(now.year))
    menu_date = menu_date.replace(tzinfo=tz)
    menu_date.replace(tzinfo=tz)
    return menu_date

get_saturday_menu()