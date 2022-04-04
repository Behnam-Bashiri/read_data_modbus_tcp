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
            f = open("res.txt", "a")
            # for i in range(40069, 40090):
            result = client.read_holding_registers(address=40069, count=100, unit=1)
            response = client.execute(result)
            for i in range(0,100):
                f.write('{}\n'.format(result.registers[i]))
            client.close()
            f.close()
        except Exception as er:
            print("ERROR: Reading Modbus registers at getDeviceStatus:")
            print(er)
            getDeviceStatusResult = False


def main():
    Prolon = API(ipaddress='192.168.100.114', port='502')

    Prolon.getDeviceStatus()


if __name__ == "__main__": main()
