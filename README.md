<h1 align="center">
  <br>
  <img src="readme_assets/logo.png" alt="Remote Python Logo" width="200">
  <br>
  Remote Python
  <br>
</h1>

<h4 align="center">A remote code execution solution for python scripts.</h4>

<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#how-to-set-up-remote-python-server">Set up server</a> •
  <a href="#how-to-set-up-nodes">How To Set Up Nodes</a> •
  <a href="#license">License</a>
</p>

## Key Features

* Remote Code Execution

## How to set up remote python server

In order to run remote scripts on your server you will need [OpenSSH-server](https://ubuntu.com/server/docs/service-openssh) installed in addition to [Python](https://www.python.org/downloads/) and [pip](https://www.python.org/).

```bash
$ sudo apt install openssh-server
$ sudo apt install python3
$ sudo apt install python3-pip
```

That's it... your server is set up to run python scripts!


## Run any Python script with no external requirements

To add to Python scrips with no external requirements, you'll need [Python](https://www.python.org/downloads/) installed on your computer. And the following environment variables set...

```python
PYTHON_SERVER_IP        # The ip of the remote server you wish to run your scripts on.
PYTHON_SERVER_USER      # The username that you use to remotely connect to the server.
PYTHON_SERVER_PASS      # The password that you use to remotely connect to the server.
```


Add the following to the top of the python script you wish to run remotely:
```python
try:
    from RemotePython import RemotePython
    RemotePython.run_no_requirements()
except Exception:
    pass
    
# The rest of the script you wish to run remotely below
```

## Next steps in development
- Add ability to run scripts with external requirements

- Add gui
  - List running scrips
  - Upload script
  - Run an uploaded script
  - Stop an uploaded script
  - Delete an uploaded script



## License

MIT

---
> [zlincoln.dev](https://www.zlincoln.dev) &nbsp;&middot;&nbsp;
> GitHub [@ZacharyLincoln](https://github.com/ZacharyLincoln)

