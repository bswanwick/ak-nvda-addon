import addonHandler
import globalPluginHandler
import keyboardHandler
import os
import speech
from . import msg
from . import nodeIPC


class GlobalPlugin(globalPluginHandler.GlobalPlugin):
    def __init__(self):
        super(GlobalPlugin, self).__init__()
        # Assume NVDA is configured to speak on start up
        nodeIPC.letZamokKnow("true")

    def script_doStuff(self, gesture):
        curSpeechMode = speech.speechMode

        if curSpeechMode == speech.speechMode_talk:
            msg.message("Sleep mode activated.  Goodbye.")
            speech.speechMode = speech.speechMode_off
            keyboardHandler.passKeyThroughCount = 0  # turn on key passthru
            nodeIPC.letZamokKnow("false")

        elif curSpeechMode == speech.speechMode_off:
            speech.speechMode = speech.speechMode_talk
            keyboardHandler.passKeyThroughCount = -1  # turn off key passthru, set back to default (bug)
            msg.message("Hello. Advanced kiosk speech activated.")
            nodeIPC.letZamokKnow("true")

    def script_sayStuff(self, gesture): 
        curSpeechMode = speech.speechMode
        
        if curSpeechMode == speech.speechMode_talk:
            if gesture.displayName == "alt+shift+8":
                starDigit = "*"
                starMsg = starDigit + " key selected."
                msg.message(starMsg)
                print(starMsg)

            elif gesture.displayName == "alt+shift+3":
                poundDigit = "#"
                poundMsg = poundDigit + " key selected."
                msg.message(poundMsg)
                print(poundMsg)

            else:
                digit = gesture.displayName[-1]
                numMsg = "Number " + digit + " selected."
                msg.message(numMsg)
                print(numMsg)

    def script_setDefaultRate(self, gesture):
        speech.getSynth()._set_rate(50)

    def terminate(self):
        nodeIPC.letZamokKnow("false")

    __gestures = {
        "kb:NVDA+S": "doStuff",
        "kb:ALT+S": "doStuff",
        "kb:ALT+0": "sayStuff",
        "kb:ALT+1": "sayStuff",
        "kb:ALT+2": "sayStuff",
        "kb:ALT+3": "sayStuff",
        "kb:ALT+4": "sayStuff",
        "kb:ALT+5": "sayStuff",
        "kb:ALT+6": "sayStuff",
        "kb:ALT+7": "sayStuff",
        "kb:ALT+8": "sayStuff",
        "kb:ALT+9": "sayStuff",
        "kb:ALT+SHIFT+8": "sayStuff",
        "kb:ALT+SHIFT+3": "sayStuff",
        "kb:ALT+J": "setDefaultRate",
    }
