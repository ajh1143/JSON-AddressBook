# JSON-AddressBook

JSON based address book. 

#### Imports

```Python3
import json
from msvcrt import getch
import os
```

#### Class

```Python3 
class jsonAddressBook(object):
```

#### User is prompted to enter a new contact's First name, Last name, and Address.
```Python3
def new_contact(self):
        filePath = input("Please enter your desired output or existing directory.")
        output_dict = {}
        user_continue = bool
        while user_continue:
            name_first = input(print("Please enter your contact's first name."))
            name_last =  input(print("Please enter your contact's last name."))
            full_name = name_first + " " + name_last
            address =  input(print("Please enter " + name_first + "\'s" + " address."))
            output_dict = {full_name:address}
            jsonAddressBook().add_to_file(output_dict, filepath)
            print("Press enter to continue, or any other key to quit")
            keypress = ord(getch())
            if keypress == '13':
                pass
            else:
                break
```

#### User then inputs a target directory to either create a new file containing the contact information in JSON form

```Python3
    def add_to_file(self, person, fileName):
        if os.path.exists(fileName):
            with open(fileName, 'a') as outfile:
                json.dump(person, outfile)
```

#### If an existing file is detected, it will be updated with the new contact information.

```Python3
        else:
            with open(fileName, 'w') as outfile:
                json.dump(person, outfile)
```
