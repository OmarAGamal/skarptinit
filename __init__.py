from influxdb import InfluxDBClient
from datetime import datetime

client = InfluxDBClient('192.168.100.144',8086,'skarpt','skarpt','skarpt')
client.create_database('test')
#client.get_list_database()

json_payload = []
data={
       "measurement":"Tzone",
       "tags":{
               "sensor":"88880000"
       },
       "time": datetime.now(),
       "fields":{
            'value':252
       }
}

json_payload.append(data)

client.write_points(json_payload)
result= client.query('select * from Tzone;')
print("res=",result)
