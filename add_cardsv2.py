import easygui as eg

# Dictionary of creatures and their attributes
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


# Function to handle card checking and input
def card_check(enterbox_msg, enterbox_title, enterbox_fields, user_values=[]):
    while True:
        new_user_values = eg.multenterbox(
            msg=enterbox_msg,
            title=enterbox_title,
            fields=enterbox_fields,
            values=user_values
        )

        if new_user_values is None:
            quitting = eg.boolbox(msg="Do you want to quit?")
            if quitting:
                return False, "User quit"
        else:
            user_values = new_user_values

        print("Card creation is complete")
        print(user_values)

        error = ""
        for value in user_values[1:]:
            if value == "" or user_values[0] == "":
                error = "Please fill in all values"
            try:
                int_value = int(value)
                if int_value < 0 or int_value > 25:
                    error = "Stat values must be between 0 and 25"
            except ValueError:
                error = "All stat values must be a number"

        if error:
            eg.msgbox(msg=error)
        else:
            creature_dict[user_values[0]] = {"Strength": user_values[1],
                                             "Speed": user_values[2],
                                             "Stealth": user_values[3],
                                             "Cunning": user_values[4]}

            return True, user_values


# Initial values and fields
input_fields = ["Creature Name", "Strength", "Speed", "Stealth", "Cunning"]


# Call the card_check function
success, final_values = card_check(
    enterbox_fields=input_fields,
    enterbox_msg="Add custom card (Stat values must be between 0 and 25.)",
    enterbox_title="Custom Card Creator",
)
print(creature_dict)





