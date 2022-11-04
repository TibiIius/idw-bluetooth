import pydbus
import time
import atexit

if __name__ == "__main__":
    bus = pydbus.SystemBus()
    host = bus.get("org.bluez", "/org/bluez/hci0")
    dev = bus.get("org.bluez", "/org/bluez/hci0/dev_20_9B_A5_9A_B5_0D")

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
        time.sleep(1)
