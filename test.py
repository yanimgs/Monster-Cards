"""
Second version of the add cards module which allows users to
add custom cards to the monster dictionary
this version is the developed outcome as I
found a better way for the user to enter data
than add_cards_v1"""

import easygui as eg

# Dictionary
creature_dict = {
    "Stoneling": {
        "Strength": 7,
        "Speed": 1,
        "Stealth": 25,
        "Cunning": 15
    },
    "Vexscream": {
        "Strength": 1,
        "Speed": 6,
        "Stealth": 21,
        "Cunning": 19
    },
    "Dawnmirage": {
        "Strength": 5,
        "Speed": 15,
        "Stealth": 18,
        "Cunning": 22
    },
    "Blazegolem": {
        "Strength": 15,
        "Speed": 20,
        "Stealth": 23,
        "Cunning": 6
    },
    "Websnake": {
        "Strength": 7,
        "Speed": 15,
        "Stealth": 10,
        "Cunning": 5
    },
    "Moldvine": {
        "Strength": 21,
        "Speed": 18,
        "Stealth": 14,
        "Cunning": 5
    },
    "Vortexwing": {
        "Strength": 19,
        "Speed": 13,
        "Stealth": 19,
        "Cunning": 2
    },
    "Rotthing": {
        "Strength": 16,
        "Speed": 7,
        "Stealth": 4,
        "Cunning": 12
    },
    "Froststep": {
        "Strength": 14,
        "Speed": 14,
        "Stealth": 17,
        "Cunning": 4
    },
    "Wispghoul": {
        "Strength": 17,
        "Speed": 19,
        "Stealth": 3,
        "Cunning": 2
    }
}


def card_check(user_values, enterbox_msg,
               enterbox_title, enterbox_fields):
    while True:
        new_user_values = eg.multenterbox(
            values=user_values,
            title=enterbox_title,
            msg=enterbox_msg,
            fields=enterbox_fields)
        if new_user_values is None:
            quitting = eg.boolbox(msg="Do you want to exit")
            if quitting is True:
                return False, "User exit"
        else:
            user_values = new_user_values

        print("It is finished")
        print(user_values)
        error = ""
        for value in user_values[1:]:
            if value == "" or user_values[0] == "":
                error = "One of the stats is empty"
            try:
                int_value = int(value)
            except ValueError:
                error = "All stats must be a value not a string"
            else:
                if int_value < 0 or int_value > 25:
                    error = "All stats need to be between 0 and 25"
        if error != "":
            eg.msgbox(msg=error)
    return True, user_values

def add_cards():
    enterbox_fields = ["Creature Name"]
    enterbox_values = ["Strength", "Speed", "Stealth", "Cunning"]
    for stat in enterbox_values:
        enterbox_fields.append(f"{stat}")
    enterbox_title = "Edit card data"
    new_card_data = eg.multenterbox(fields=enterbox_fields,
                                    msg="Add custom card (Stat values must be between 1-25)",
                                    title="Add Custom Card")

    changed_data = card_check(new_card_data,
                              "Confirm this is the correct data",
                              "Data confirmation", enterbox_fields)
    cd = changed_data


add_cards()