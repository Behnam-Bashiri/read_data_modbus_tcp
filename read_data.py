from pymodbus.client.sync import ModbusTcpClient


class API:
    # 1. constructor : gets call everytime when create a new class
    # requirements for instantiation1. model, 2.type, 3.api, 4. address
    def __init__(self, **kwargs):  # default color is white
        # Initialized common attributes
        self.variables = kwargs
        address_parts = self.get_variable('address').split(':')
        self.set_variable('address', address_parts[0])
        self.set_variable('slave_id', int(address_parts[1]))
        self.set_variable('offline_count', 0)
        self.set_variable('connection_renew_interval', 6000)  # nothing to renew

    def renewConnection(self):
        pass

    def set_variable(self, k, v):  # k=key, v=value
        self.variables[k] = v

    def get_variable(self, k):
        return self.variables.get(k, None)  # default of get_variable is none

    def getDeviceStatus(self):
        getDeviceStatusResult = True
        try:
            client = ModbusTcpClient(self.get_variable('address'), port=502)
            client.connect()
            result = client.read_input_registers(0, 8, unit=self.get_variable('slave_id'))
            client.close()
        except Exception as er:
            print("classAPI_vav_rtu: ERROR: Reading Modbus registers at getDeviceStatus:")
            print(er)
            getDeviceStatusResult = False

        if getDeviceStatusResult == True:
            self.set_variable('offline_count', 0)
        else:
            self.set_variable('offline_count', self.get_variable('offline_count') + 1)


def main():
    # Utilization: test methods
    # Step1: create an object with initialized data from DeviceDiscovery Agent
    # requirements for instantiation1. model, 2.type, 3.api, 4. address,
    Prolon = API(model='VC1000', type='VAV', api='API', address='192.168.10.228:7')

    # Step2: Get data from device
    Prolon.getDeviceStatus()
    print(Prolon.variables)

    # Step3: change device operating set points
    # Prolon.setDeviceStatus({'flap_override':'ON','flap_position':20})
    # Prolon.setDeviceStatus({'fan_status':'ON'})

    Prolon.getDeviceStatus()
    print(Prolon.variables)


if __name__ == "__main__": main()
