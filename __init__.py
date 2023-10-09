from influxdb import InfluxDBClient
import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS

client = InfluxDBClient(host='localhost', port=8086)
#client.create_database('skarpt')
json_body = [
    {
        "measurement": "Tzone",
        "tags": {
            "host": "192.168.100.144",
            "region": "egpyt"
        },
        "fields": {
            "Float_value": 525.25,
            "Int_value": 525,
            "String_value": "startvalue",
            "Bool_value": True
        }
    }
]

client.write_points(json_body)
result = client.query('select * from Tzone')
print("Result: {0}".format(result))
