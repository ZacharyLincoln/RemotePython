import inspect
import os
import socket

import paramiko
from scp import SCPClient


class RemotePython:

    @staticmethod
    def run_no_requirements(server_hostname="python-runner", filename=""):
        if filename == "":
            frame = inspect.stack()[1]
            module = inspect.getmodule(frame[0])
            filename = module.__file__

        username = os.getenv('PYTHON_SERVER_USER')
        password = os.getenv('PYTHON_SERVER_PASS')

        ip = os.getenv('PYTHON_SERVER_IP')

        hostname = socket.gethostname()

        if hostname == server_hostname:
            return


        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, username=username, password=password)

        ssh.exec_command("mkdir serv")
        ssh.exec_command("mkdir serv/python-remote")
        ssh.exec_command("touch serv/python-remote/" + filename.split("\\")[len(filename.split("\\"))-1])

        scp = SCPClient(ssh.get_transport())
        scp.put(filename, "~/serv/python-remote/" + filename.split("\\")[len(filename.split("\\"))-1])

        stdin, stdout, stderr = ssh.exec_command("python3 " + "~/serv/python-remote/" + filename.split("\\")[len(filename.split("\\"))-1], get_pty=True)

        print("Running " + filename.split("\\")[len(filename.split("\\"))-1] + " on " + ip)

        for line in iter(lambda: stdout.readline(2048), ""):
            print(line, end="")


        print("Script ended on " + ip)


        exit()

