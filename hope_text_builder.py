import hope_scraper


def saturday_night_menu_next_text():

    current_menu = hope_scraper.saturday_night_menu_next()

    if current_menu:
        current_date = current_menu["date"]
        speak_date = current_date.strftime("%B %d")
        speech_output = "Dinner for " + speak_date + \
            " will be " + current_menu["menu"]
        should_end_session = True
    else:
        speech_output = "The menu for next week has not been posted yet."
        should_end_session = False

    return speech_output, should_end_session


def saturday_night_menu_rest_of_month_text():
    current_menus = hope_scraper.saturday_night_menu_rest_of_month()

    if current_menus:
        speech_output = "Dinner for "
        for current_menu in current_menus:
            current_date = current_menu["date"]
            speak_date = current_date.strftime("%B %d")
            speech_output = speech_output + speak_date + \
                " will be " + current_menu["menu"] + ", "
            should_end_session = True
    else:
        speech_output = "The menu for next week has not been posted yet."
        should_end_session = False

    return speech_output, should_end_session
