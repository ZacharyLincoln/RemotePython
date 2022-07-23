from pathlib import Path

try:
    from RemotePython import RemotePython

    #RemotePython.run(required_files=["C:\\Users\\Zach\\Documents\\Development\\Python\\RemotePython\\beep.py", "C:\\Users\\Zach\\Documents\\Development\\Python\\RemotePython\\README.md"])
    #RemotePython.run(required_files=["C:\\Users\\Zach\\Documents\\Development\\Python\\RemotePython\\beep.py",
                                     #"C:\\Users\\Zach\\Documents\\Development\\Python\\RemotePython\\README.md"], output=True)
    RemotePython.run()
except ImportError:
    pass

from time import sleep
import platform

while True:
    print("Running on", platform.system())
    sleep(10)


