from pymodbus.client.sync import ModbusTcpClient


class API:
    def __init__(self, ipaddress, port):
        self.ipaddress = ipaddress
        self.port = port

    def getDeviceStatus(self):
        getDeviceStatusResult = True
        try:
            client = ModbusTcpClient(self.ipaddress, port=502)
            client.connect()
            result = client.read_holding_registers(address=20,count=1,unit=1)
            response = client.execute(result)
            print(result.registers[0])
            client.close()
        except Exception as er:
            print("ERROR: Reading Modbus registers at getDeviceStatus:")
            print(er)
            getDeviceStatusResult = False


def main():
    Prolon = API(ipaddress='192.168.1.55', port='502')

    Prolon.getDeviceStatus()


if __name__ == "__main__": main()
