
import commandSender

__estados = {"midiendo": False,
             "seteado": False}


def isSeteado():
    return __estados["seteado"]


def isMidiendo():
    return __estados["midiendo"]


def changeModeOnLine():
    pause()
    commandSender.setMode(1)
    __estados["seteado"] = False
    __estados["midiendo"] = False

def changeModeRegistro():
    pause()
    commandSender.setMode(2)
    __estados["seteado"] = False
    __estados["midiendo"] = False


def pause():
    __estados["midiendo"] = False
    commandSender.pause()
