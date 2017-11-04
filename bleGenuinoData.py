import json
import struct
import time
from gattlib import GATTRequester

req = GATTRequester("98:4f:ee:10:d4:90")
bufferSize = 4

class ImuPacket(): pass
class ImuPayload(): pass

while True:
	data = [0] * bufferSize
	for i in range(bufferSize):
		data[i] = req.read_by_uuid("3a19")[0]

	dataList = []
	imuPacketList = []
	for j in range(0, bufferSize):

		currentBufferMsg = '{ ax: '+ str(struct.unpack_from('f', data[j], 0)[0]) + ', ay:' + str(struct.unpack_from('f', data[j], 2)[0]) + ', az:' + str(struct.unpack_from('f', data[j], 4)[0]) + ', gx:' + str(struct.unpack_from('f', data[j], 6)[0]) + ', gy:' + str(struct.unpack_from('f', data[j], 8)[0]) + ', gz:' + str(struct.unpack_from('f', data[j], 10)[0])  + '}'
		
                currentImuPayload = ImuPayload()
                currentImuPayload.ax = round(struct.unpack_from('f', data[j], 10)[0], 2)
                currentImuPayload.ay = struct.unpack_from('f', data[j], 10)[0]




                currentImuPayload.ax = round(struct.unpack_from('f', data[j], 0)[0], 2)
                currentImuPayload.ay = round(struct.unpack_from('f', data[j], 2)[0], 2)
                currentImuPayload.az = round(struct.unpack_from('f', data[j], 4)[0], 2)
                currentImuPayload.gx = round(struct.unpack_from('f', data[j], 6)[0], 2)
                currentImuPayload.gy = round(struct.unpack_from('f', data[j], 8)[0], 2)
                currentImuPayload.gz = round(struct.unpack_from('f', data[j], 10)[0], 2)
                
		currentImuPacket = ImuPacket()
                currentImuPacket.timestamp = time.time()
                currentImuPacket.data = currentImuPayload				
				
                imuPacketList.append(currentImuPacket)

                dataList.append([0, currentBufferMsg])

	dataListStr = json.dumps(dataList) # '[1, 2, [3, 4]]'
	print dataListStr
	print ""


	class C(): pass
	class D(): pass
	c = C()
	c.what = "now?"
	c.now = "what?"
	c.d = D()
	c.d.what = "d.what"	
	classesStr = json.dumps(c, default=lambda o: o.__dict__)
	print classesStr

	#from json import encoder
	
#	json.encoder.FLOAT_REPR = lambda f: ("%.2f" % f)
#	precision = lambda x: format(x, '.2f')

#	import decimal	

	imuPacketListStr = json.dumps(imuPacketList, default=lambda o: o.__dict__)

	print imuPacketListStr

	time.sleep(1.05)
