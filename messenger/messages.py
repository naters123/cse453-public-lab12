########################################################################
# COMPONENT:
#    MESSAGES
# Author:
#    Br. Helfrich, Kyle Mueller, Nathan Ricks, Josh Thieme, Emilio Regino
# Summary: 
#    This class stores the notion of a collection of messages
########################################################################

import control, message

##################################################
# MESSAGES
# The collection of high-tech messages
##################################################
class Messages:

    ##################################################
    # MESSAGES CONSTRUCTOR
    # Read a file to fill the messages
    ##################################################
    def __init__(self, filename):
        self._messages = []
        self._read_messages(filename)

    ##################################################
    # MESSAGES :: GETMESSAGES
    # return the list of messages
    ################################################## 
    def getMessages(self):
        return self._messages

    ##################################################
    # MESSAGES :: DISPLAY
    # Display the list of messages
    ################################################## 
    def display(self, messages):
        for m in messages:
            m.display_properties()

    ##################################################
    # MESSAGES :: SHOW
    # Show a single message
    ################################################## 
    def show(self, id):
        for m in self._messages:
            if m.get_id() == id:
                m.display_text()
                return True
        return False
    
    ##################################################
    # MESSAGES :: EXISTS
    # If a message does or does not exist
    ################################################## 
    def exists(self, id):
        for m in self._messages:
            if m.get_id() == id:
                return True
        return False

    ##################################################
    # MESSAGES :: UPDATE
    # Update a single message
    ################################################## 
    def update(self, id, text):
        for m in self._messages:
            if m.get_id() == id:
                m.update_text(text)

    ##################################################
    # MESSAGES :: REMOVE
    # Remove a single message
    ################################################## 
    def remove(self, id):
        for m in self._messages:
            if m.get_id() == id:
                m.clear()

    ##################################################
    # MESSAGES :: ADD
    # Add a new message
    ################################################## 
    def add(self, text, author, date, text_control):
        m = message.Message(text, author, date, text_control)
        self._messages.append(m)

    ##################################################
    # MESSAGES :: GETASSETCONTROL
    # Get the access level for an asset by id
    ################################################## 
    def getAssetControl(self, id):
        for m in self._messages:
            if m.get_id() == id:
                return m.get_access()

    ##################################################
    # MESSAGES :: READ MESSAGES
    # Read messages from a file
    ################################################## 
    def _read_messages(self, filename):
        try:
            with open(filename, "r") as f:
                for line in f:
                    text_control, author, date, text = line.split('|')
                    self.add(text.rstrip('\r\n'), author, date, text_control)

        except FileNotFoundError:
            print(f"ERROR! Unable to open file \"{filename}\"")
            return
