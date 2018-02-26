#! /usr/bin/env python

import sys
sys.path.append("./gen-py")

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TCompactProtocol
from RTB.RtbService import Client
from RTB.RtbService import Request
from RTB.RtbService import ScanData
from RTB.RtbService import RequestException

__HOST = '192.168.2.198'
__PORT = 9999

if __name__ == '__main__':

    try:

        tsocket = TSocket.TSocket(__HOST, __PORT)
        tsocket.setTimeout(ms=12000)
        transport = TTransport.TBufferedTransport(tsocket)
        protocol = TCompactProtocol.TCompactProtocol(transport)
        client = Client(protocol)

        allScanData = []
        count = 0
        while (count < 5):
            count = count + 1
            scanData = ScanData(macAddress='00:e0:70:25:18:5f', rssi='-30')
            allScanData.append(scanData)

        req = Request(deviceId=999, allScanData=allScanData)
        transport.open()
        resp = client.getRtbByDeviceIdAndScanData(request=req)
        print "Response:" + str(resp)

        transport.close()

    except RequestException as re:
        print "RequestException:" + re.message

    except Exception as e:
        print "Exception:" + e