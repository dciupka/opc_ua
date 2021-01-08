"""client to server with cerated nodes"""
from opcua import Client
import time

url = "opc.tcp://127.0.0.1:4840"

client = Client(url)

client.connect()

print("Client Connect")

while True:
    timer = client.get_node("ns=2;i=4")
    TIME = timer.get_value()
    print(TIME)

    Temp = client.get_node("ns=2;i=2")
    Temperature = Temp.get_value()
    print(Temperature)

    Press = client.get_node("ns=2;i=3")
    Pressure = Press.get_value()
    print(Pressure)

    time.sleep(2)

