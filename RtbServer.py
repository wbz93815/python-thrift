#! /usr/bin/env python

import sys
sys.path.append("./gen-py")

from RTB import RtbService
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TCompactProtocol
from thrift.server import TServer

import time

__HOST = '192.168.2.198'
__PORT = 9999

class RtbServiceHandler(object):
    def getRtbByDeviceIdAndScanData(self, request):
        print "deviceId:" + str(request.deviceId)
        ticks = time.time()
        print "time:" + str(ticks)
        time.sleep(5)
        return str(request.deviceId + 1)


if __name__ == '__main__':
    try:
        handler = RtbServiceHandler()
        processor = RtbService.Processor(handler)
        transport = TSocket.TServerSocket(__HOST, __PORT)
        tfactory = TTransport.TBufferedTransportFactory()
        pfactory = TCompactProtocol.TCompactProtocolFactory()
        # rpcServer = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
        rpcServer = TServer.TThreadedServer(processor, transport, tfactory, pfactory)
        # rpcServer = TServer.TThreadPoolServer(processor, transport, tfactory, pfactory)

        print('Starting the rpc server at', __HOST, ':', str(__PORT))
        rpcServer.serve()

    except Exception as e:
        print e