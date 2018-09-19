import qi
import sys
from modules.services import ServiceModule
from modules.events import EventModule
from modules.command import CommandModule
from modules.speechRecognition import SpeechRecognitionModule

import time


class Nao():
    # exit program callback calls nao exit program
    def __init__(self, ipAddress, ExitProgramCallback, defaultPose):
        self.app = qi.Application()
        self.session = qi.Session()
        self.properties = {}
        self.isConnected = False
        self.defaultPose = defaultPose
        self.session.connect('tcp://'+ipAddress+":9559")
        self.serviceModule = ServiceModule(self.session)
        self.eventModule = EventModule(self.serviceModule.memory)
        self.speechRecognitionModule = SpeechRecognitionModule(self.serviceModule, True, False)
        self.commandModule = CommandModule(
            self.serviceModule, self.eventModule,
            self.speechRecognitionModule, ExitProgramCallback)
        self.isConnected = True

    def OnRequest(self, requestBody):
        attr = getattr(self, requestBody['module'])
        response = attr.HandleRequest(requestBody)
        return response

    def StartProgram(self):
        self.SetDefaultPose()
        self.commandModule.StartAllListeners()

    def ExitProgram(self):
        self.commandModule.StopAllListeners()
        self.SetDefaultPose()
        # self.dialog.End()

    def SetDefaultPose(self):
        if self.defaultPose == 'stand':
            self.commandModule.Run({
                "commandName": "naoqi",
                "serviceName": "ALMotion",
                "methodName": "setStiffnesses",
                "param1": 'Body',
                "param2": 1
            })
            self.commandModule.Run({
                "commandName": "runBehavior",
                "path": "custom_animations/body/stand"
            })
        elif self.defaultPose == 'rest':
            self.commandModule.Run({
                "commandName": "naoqi",
                "serviceName": "ALAutonomousLife",
                "methodName": "setState",
                "param1": "disabled"
            })
            # self.commandModule.Run({
            #     "commandName": "naoqi",
            #     "serviceName": "ALMotion",
            #     "methodName": "setStiffnesses",
            #     "param1": 'Body',
            #     "param2": 1
            # })
            # self.commandModule.Run({
            #     "commandName": "runBehavior",
            #     "path": "custom_animations/body/crouch"
            # })
            # self.commandModule.Run({
            #     "commandName": "naoqi",
            #     "serviceName": "ALMotion",
            #     "methodName": "setStiffnesses",
            #     "param1": 'Body',
            #     "param2": 0
            # })


# if __name__ == "__main__":
    # ipAddress = sys.argv[1]
    # # nao = Nao(ipAddress, )
    # # nao.commandModule.StartAllListeners()
    # try:
    #     while True:
    #         pass
    # except KeyboardInterrupt:
    #     nao.ExitProgram()
    #     pass
