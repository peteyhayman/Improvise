import sys
from pkg.modules.nao.nao import Nao
# from pkg.modules.message_client.client import MessageClient
from pkg.modules.behavior_planner.behavior_planner import BehaviorPlanner
from pkg.modules.server import Server
import time
# pow


class AutoImprovise():
    def __init__(self, ipAddress, port, deployed):
        self.nao = Nao(ipAddress)
        serverIP = '127.0.0.1' if not deployed else self.nao.properties.properties['ipAddress']['get']()
        self.server = Server(port, serverIP)
        self.server.RequestCallback = self.OnModuleRequest
        self.behaviorPlanner = BehaviorPlanner(self.nao)

    def OnModuleRequest(self, moduleName, reqBody):
        attr = getattr(self, moduleName)
        resBody = attr.OnRequest(reqBody)
        return resBody


if __name__ == "__main__":
    NAOIP = sys.argv[1]
    PORT = 5000
    deployed = True if '-d' in sys.argv else False
    print 'starting up...'
    print 'deployed:', deployed
    autoImprovise = AutoImprovise(NAOIP, PORT, deployed)
    autoImprovise.behaviorPlanner.Begin()
    autoImprovise.server.Run()
    try:
        while autoImprovise.behaviorPlanner.rootMind.travelMind.room != None:
            time.sleep(0.01)
    except KeyboardInterrupt:
        print 'exiting..'
    autoImprovise.behaviorPlanner.End()
    autoImprovise.nao.ExitProgram()
    autoImprovise.server.Stop()
    print 'program terminated'
