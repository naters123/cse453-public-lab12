########################################################################
# COMPONENT:
#    CONTROL
# Author:
#    Br. Helfrich, Kyle Mueller, <your name here if you made a change>
# Summary: 
#    This class stores the notion of Bell-LaPadula
########################################################################

from enum import Enum

class Control():
   
    ##################################################
    # Control CONSTRUCTOR
    # Authenticate the user and get him/her all set up
    ##################################################
    def __init__(self, username):
        self._controlLevels = {"SECRET" : 3, "PRIVILEGED" : 2, "CONFIDENTIAL" : 1, "PUBLIC" : 0}
        self.subjectControl = self.authenticate(username)

    def authenticate(self, username):
        if username in ["AdmiralAbe"]:
            return self._controlLevels["SECRET"]
        elif username in  ["CaptainCharlie"]:
            return self._controlLevels["PRIVILEGED"]
        elif username in  ["SeamanSam", "SeamanSue", "SeamanSly"]:
            return self._controlLevels["CONFIDENTIAL"]
        else:
            return self._controlLevels["PUBLIC"]
    
    def assetControlNum(self, control):
        return self._controlLevels[control]

    def securityConditionRead(self, assetControl, subjectControl):
        return subjectControl >= assetControl   
