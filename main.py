from pprint import pp
import threading
import time
import os
import logging
import ports.tcp_sensor
import adaptors.sensor_adaptor



def startSensor(PORT: int):
    os.system(f"./../sensor.fish | nc localhost {PORT}")    


if __name__ == "__main__": 
    logging.basicConfig(format="%(levelname)s:%(name)s:%(message)s", level=logging.INFO)
    logger = logging.getLogger(__name__)
    logger.warning("Application started")

    sensor1 = threading.Thread(target=startSensor, args=[9999], daemon=True) 

    x = threading.Thread(target=ports.tcp_sensor.startTCPServerThread, args=(adaptors.sensor_adaptor.print_adaptor, "localhost", 9999), daemon=True)

    x.start()
    sensor1.start()
    while True: 
        time.sleep(1)
else: 
    import pytest

    def test_create_single_temperatur(): 
        import adaptors.data_storage_adaptor as dba
        import pprint
        test_data = {
            "timestamp": "2323-2323-2323",
            "temperature": 10.5
        }

        dba.create_temperature(test_data)
        result_data = dba.read_one_temperature(test_data["timestamp"])
        if result_data == None: 
            assert False
        pprint.pprint(result_data)
        delete_result = dba.delete_one_temperature(test_data["timestamp"])
        pprint.pprint(delete_result)

        


