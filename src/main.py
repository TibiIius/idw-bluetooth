import pydbus
import time
import atexit

# This is the RSSI value at 1 meter distance
MEASURED_POWER = -48


def get_distance(rssi):
    # Calculate distance from RSSI value
    return 10 ** ((MEASURED_POWER - rssi) / (10 * 2))


if __name__ == "__main__":
    bus = pydbus.SystemBus()
    host = bus.get("org.bluez", "/org/bluez/hci0")
    # dev = bus.get("org.bluez", "/org/bluez/hci0/dev_20_9B_A5_9A_B5_0D")
    dev = bus.get("org.bluez", "/org/bluez/hci0/dev_F0_79_60_4A_D6_85")

    # We connect a hook on exit here so we can reconnect the device before shutdown
    atexit.register(lambda: dev.Connect())

    # Start discorvering so we can get RSSI values of devices
    host.StartDiscovery()

    # For some reason, blueZ apparently can't get RSSI values of connected devices, or the DBUS API of blueZ at least
    if dev.Get("org.bluez.Device1", "Connected"):
        dev.Disconnect()

    # Wait a bit because `RSSI` property doesn't get accessible immediately
    time.sleep(1)

    while True:
        print(dev.Get("org.bluez.Device1", "RSSI"))
        print(get_distance(dev.Get("org.bluez.Device1", "RSSI")))
        time.sleep(1)
