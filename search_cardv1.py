"""
First version of the search card module which allows users to
search and modify stats for different creatures, no error message, no quit option.
"""

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


def change_card(card_name, msg_=""):
    # Global varaible prevent errors
    global creature_dict
    if msg_ == "":
        # If user doesnt pass in a custom message use the default
        msg_ == f"Change card for {card_name}"
    raw_dict_data = creature_dict[card_name]
    enterbox_values = [card_name]
    enterbox_fields = ["Monster name"]

    # Interating through all the attributes and values
    for attribute, value in raw_dict_data.items():
        enterbox_values.append(attribute)
        enterbox_values.append(value)

    for num in range(0, 4):
        enterbox_fields.append(f"Attribute {num}")
        enterbox_fields.append(f"Attribute {num} value")
    msg_ = ""
    enterbox_title = "Edit card data"
    while True:
        error = False
        error_text = ""
        changed_data = eg.multenterbox(fields=enterbox_fields,
                                       values=enterbox_values, title=enterbox_title)

        for item in changed_data:
            if item == "":
                error = True

        if error is True:
            eg.msgbox("You left a item blank", title="Error")

    # Shortened name for tidyness
    cd = changed_data
    creature_dict[cd[0]] = {cd[1]: cd[2], cd[3]: cd[4], cd[5]: cd[6]}


monster_string = ""
for creature in creature_dict:
    monster_string = f"{creature}\n{monster_string}"

msg_ = f"What card do you want to search these are all of the creatures: {monster_string}"
to_search = eg.enterbox(msg=msg_, title="Monster search")
change_card(card_name=to_search)
print(creature_dict)