import json
from msvcrt import getch
import os

class jsonAddressBook(object):
"""
JSON based address book. User enters a First name, Last name, and Address.
User also inputs a target directory to either create a new file containing the contact information, 
or, update an existing file if it exists. 
"""

    def new_contact(self):
        output_dict = {}
        user_continue = bool
        while user_continue:
            name_first = input(print("Please enter your contact's first name."))
            name_last =  input(print("Please enter your contact's last name."))
            full_name = name_first + " " + name_last
            address =  input(print("Please enter " + name_first + "\'s" + " address."))
            output_dict = {full_name:address}
            jsonAddressBook().add_to_file(output_dict)
            print("Press enter to continue, or any other key to quit")
            keypress = ord(getch())
            if keypress == '13':
                pass
            else:
                break
        return output_dict

    def add_to_file(self, person):
        filePath = input("Please enter your desired output or existing directory.")
        if os.path.exists(filePath):
            with open(filePath, 'a') as outfile:
                json.dump(person, outfile)
        else:
            with open(filePath, 'w') as outfile:
                json.dump(person, outfile)


if __name__ == "__main__":
    run = jsonAddressBook()
    contact = run.new_contact()
