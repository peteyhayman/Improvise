
# class MethodModule():

#     # def __init__(self, services, events, textToSpeech):
#     self.services = services
#     self.TextToSpeech = textToSpeech

# def HandleRequest(self, params):
#     self.DoMethod(params)
#     return {'status': 'all good'}

# def DoMethod(self, params):
#     if not 'async' in params:
#         params['async'] = True
#     meth = getattr(self, params['methodName'])
#     # print 'METHOD CALLED', params
#     meth(params)

# def Say(self, params):
#     self.TextToSpeech.Say(params)

# def SetAutoState(self, params):
#     self.services.autonomousLife.setState(params['state'], _async=True)

# def PlayAudio(self, params):
#     self.services.audioPlayer.playFile(params['path'], _async=True)
#     # id = self.services.audioPlayer.loadFile(params[0])

# def SetLeds(self, params):
#     if not 'async' in params:
#         params['async'] = True
#     if not 'duration' in params:
#         params['duration'] = 1
#     if not 'name' in params:
#         params['name'] = "FaceLeds"
#     self.services.leds.fadeRGB(
#         params['name'], params['colorName'], params['duration'], _async=params['async'])
#     # white, red, green, blue, yellow, magenta, cyan

# def RunBasicAction(self, params):
#     params['path'] = 'extra-nao-behaviors-93b077/' + params['action']
#     self.RunBehavior(params)
# extra-nao-behaviors-93b077/breathe
# extra-nao-behaviors-93b077/rest
# extra-nao-behaviors-93b077/sit_down
# extra-nao-behaviors-93b077/stand_up
# extra-nao-behaviors-93b077/wake_up
# extra-nao-behaviors-93b077/recognize_speech
