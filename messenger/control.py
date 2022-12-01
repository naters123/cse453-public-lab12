########################################################################
# COMPONENT:
#    CONTROL
# Author:
#    Br. Helfrich, Kyle Mueller, Nathan Ricks
# Summary: 
#    This class stores the notion of Bell-LaPadula
########################################################################

class Control():
   
    ##################################################
    # Control CONSTRUCTOR
    # Authenticate the user and get him/her all set up
    ##################################################
    def __init__(self, username):
        self._controlLevels = {"SECRET" : 3, "PRIVILEGED" : 2, "CONFIDENTIAL" : 1, "PUBLIC" : 0}
        self._controlValue = { 3 : "SECRET", 2 : "PRIVILEGED", 1 : "CONFIDENTIAL", 0 : "PUBLIC"}
        self.subjectControl = self.authenticate(username)

    def getAuthenticateKey(self, value):
        return self._controlValue[value]
        

    def authenticate(self, username):
        if username in ["AdmiralAbe"]:
            return self._controlLevels["SECRET"]
        elif username in  ["CaptainCharlie"]:
            return self._controlLevels["PRIVILEGED"]
        elif username in  ["SeamanSam", "SeamanSue", "SeamanSly"]:
            return self._controlLevels["CONFIDENTIAL"]
        else:
            return self._controlLevels["PUBLIC"]

    def securityConditionRead(self, assetControl, subjectControl):
        return subjectControl >= self._controlLevels[assetControl]

    def securityConditionWrite(self, assetControl, subjectControl):
        return self._controlLevels[assetControl] >= subjectControl
