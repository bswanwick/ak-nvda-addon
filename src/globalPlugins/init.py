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

    def terminate(self):
        nodeIPC.letZamokKnow("false")

    __gestures = {
        "kb:NVDA+S": "doStuff",
        "kb:ALT+S": "doStuff",
    }
