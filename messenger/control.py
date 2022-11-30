########################################################################
# COMPONENT:
#    CONTROL
# Author:
#    Br. Helfrich, Kyle Mueller, <your name here if you made a change>
# Summary: 
#    This class stores the notion of Bell-LaPadula
########################################################################

# you may need to put something here...

from enum import Enum
class Control(Enum):
    PUBLIC, CONFIDENTIAL, PRIVILEGED, SECRET = range(0,3)

    def __init__():
        self._control_level