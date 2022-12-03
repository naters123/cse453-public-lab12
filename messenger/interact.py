########################################################################
# COMPONENT:
#    INTERACT
# Author:
#    Br. Helfrich, Kyle Mueller, Nathan Ricks, Josh Thieme, Emilio Regino
# Summary: 
#    This class allows one user to interact with the system
########################################################################

import messages, control

###############################################################
# USER
# User has a name and a password
###############################################################
class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password

userlist = [
   [ "AdmiralAbe",     "password" ],  
   [ "CaptainCharlie", "password" ], 
   [ "SeamanSam",      "password" ],
   [ "SeamanSue",      "password" ],
   [ "SeamanSly",      "password" ]
]

###############################################################
# USERS
# All the users currently in the system
###############################################################
users = [*map(lambda u: User(*u), userlist)]

ID_INVALID = -1

######################################################
# INTERACT
# One user interacting with the system
######################################################
class Interact:

    ##################################################
    # INTERACT CONSTRUCTOR
    # Authenticate the user and get him/her all set up
    ##################################################
    def __init__(self, username, password, messages):
        self._username = username
        self._p_messages = messages
        self._control = control.Control()
        self._control.authenticate(username, password)
        self._password = password

    ##################################################
    # INTERACT :: SHOW
    # Show a single message
    ##################################################
    def show(self):
        id_ = self._prompt_for_id("display")
        if self._p_messages.exists(id_):
            if self._control.securityConditionRead(self._p_messages.getAssetControl(id_).upper(), self._control.subjectControl):
                self._p_messages.show(id_, self._control)
            else:
                print("\nYou do not have permission to perform this action.")
        else:
            print(f"\nERROR! Message ID \'{id_}\' does not exist")
        print()

    ##################################################
    # INTERACT :: DISPLAY
    # Display the set of messages
    ################################################## 
    def display(self):
        print("Messages:")
        # create a subset of messages that the current user is allowed to see
        tempMessages = []
        for m in self._p_messages.getMessages():
            if self._control.securityConditionRead(self._p_messages.getAssetControl(m.get_id()).upper(), self._control.subjectControl):
                tempMessages.append(m)
        self._p_messages.display(tempMessages, self._control)
        print()

    ##################################################
    # INTERACT :: ADD
    # Add a single message
    ################################################## 
    def add(self):
        self._p_messages.add(self._prompt_for_line("message"),
                             self._username,
                             self._prompt_for_line("date"),
                             self._control.getAuthenticateKey(self._control.authenticate(self._username, self._password))) # get the current user's authentication level

    ##################################################
    # INTERACT :: UPDATE
    # Update a single message
    ################################################## 
    def update(self):
        id_ = self._prompt_for_id("update")
        if self._p_messages.exists(id_):
            if self._control.securityConditionWrite(self._p_messages.getAssetControl(id_).upper(), self._control.subjectControl):
                self._p_messages.show(id_, self._control)
                self._p_messages.update(id_, self._prompt_for_line("message"), self._control)
            else:
                print("\nYou do not have permission to perform this action.")
        else:
            print(f"ERROR! Message ID \'{id_}\' does not exist\n")
        print()
            
    ##################################################
    # INTERACT :: REMOVE
    # Remove one message from the list
    ################################################## 
    def remove(self):
        id_ = self._prompt_for_id("delete")
        if self._p_messages.exists(id_):
            if self._control.securityConditionWrite(self._p_messages.getAssetControl(id_).upper(), self._control.subjectControl):
                self._p_messages.remove(id_, self._control)
            else:
                print("\nYou do not have permission to perform this action.")
        else:
            print(f"ERROR! Message ID \'{id_}\' does not exist\n")
        print()

    ##################################################
    # INTERACT :: PROMPT FOR LINE
    # Prompt for a line of input
    ################################################## 
    def _prompt_for_line(self, verb):
        return input(f"Please provide a {verb}: ")

    ##################################################
    # INTERACT :: PROMPT FOR ID
    # Prompt for a message ID
    ################################################## 
    def _prompt_for_id(self, verb):
        return int(input(f"Select the message ID to {verb}: "))

    # ##################################################
    # # INTERACT :: AUTHENTICATE
    # # Authenticate the user: find their control level
    # ################################################## 
    # def _authenticate(self, username, password):
    #     id_ = self._id_from_user(username)
    #     return ID_INVALID != id_ and password == users[id_].password

    ##################################################
    # INTERACT :: ID FROM USER
    # Find the ID of a given user
    ################################################## 
    def _id_from_user(self, username):
        for id_user in range(len(users)):
            if username == users[id_user].name:
                return id_user
        return ID_INVALID

#####################################################
# INTERACT :: DISPLAY USERS
# Display the set of users in the system
#####################################################
def display_users():
    for user in users:
        print(f"\t{user.name}")
