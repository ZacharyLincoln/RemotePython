try:
    from RemotePython import RemotePython
    RemotePython.run()
except ImportError:
    pass

from time import sleep
import platform

while True:
    print("Running on", platform.system())
    sleep(10)


