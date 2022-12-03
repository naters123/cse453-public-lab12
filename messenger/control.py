########################################################################
# COMPONENT:
#    CONTROL
# Author:
#    Br. Helfrich, Kyle Mueller, Nathan Ricks, Josh Thieme, Emilio Regino
# Summary: 
#    This class stores the notion of Bell-LaPadula
########################################################################

class Control():
   
    ##################################################
    # Control CONSTRUCTOR
    # Authenticate the user and get him/her all set up
    # and establish control levels
    ##################################################
    def __init__(self):
        self._controlLevels = {"SECRET" : 3, "PRIVILEGED" : 2, "CONFIDENTIAL" : 1, "PUBLIC" : 0}
        self._controlValue = { 3 : "SECRET", 2 : "PRIVILEGED", 1 : "CONFIDENTIAL", 0 : "PUBLIC"}        

    ##################################################
    # Control GET AUTHENTICATION KEY
    # Get the authentication name based on value 
    # (for adding new messages)
    ##################################################
    def getAuthenticateKey(self, value):
        return self._controlValue[value]

    ##################################################
    # Control AUTHENTICATE
    # Get the authentication value based on name
    # If the user enters a wrong password, then their
    # access level become PUBLIC
    ##################################################
    def authenticate(self, username, password):
        if username in ["AdmiralAbe"]:
            if password == "password":
                self.subjectControl = self._controlLevels["SECRET"]
                return self.subjectControl
            else:
                self.subjectControl = self._controlLevels["PUBLIC"]
                return self.subjectControl
        
        elif username in  ["CaptainCharlie"]:
            if password == "password":
                self.subjectControl = self._controlLevels["PRIVILEGED"]
                return self.subjectControl
            else:
                self.subjectControl = self._controlLevels["PUBLIC"]
                return self.subjectControl
            
        elif username in  ["SeamanSam", "SeamanSue", "SeamanSly"]:
            if password == "password":
                self.subjectControl = self._controlLevels["CONFIDENTIAL"]
                return self.subjectControl
            else:
                self.subjectControl = self._controlLevels["PUBLIC"]
                return self.subjectControl
            
        else:
            self.subjectControl = self._controlLevels["PUBLIC"]
            return self.subjectControl

    ##################################################
    # Control SECURITY CONDITION READ
    # If the current user may read the requested message
    ##################################################
    def securityConditionRead(self, assetControl, subjectControl):
        return subjectControl >= self._controlLevels[assetControl]

    ##################################################
    # Control SECURITY CONDITION WRITE
    # If the current user may modify the requested message
    ##################################################
    def securityConditionWrite(self, assetControl, subjectControl):
        return subjectControl <= self._controlLevels[assetControl]
