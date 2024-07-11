
# Docker Ninja

## Introduction 📘

A container is a sandboxed process running on a host machine that is isolated from all other processes running on that host machine. That isolation leverages kernel namespaces and cgroups, features that have been in Linux for a long time. Docker makes these capabilities approachable and easy to use. This repository is a collection of different applications that you can use to learn containerization using docker. 




## Author

- [Siddhant Nautiyal](https://www.github.com/WatashiwaSid)


## Acknowledgements

 This repository is based on the learnings of **"Azure Zero To Hero"** YouTube playlist made by Abhishek Veeramalla.
 - Abhishek Veeramalla - [Docker Zero To Hero](https://youtube.com/playlist?list=PLdpzxOOAlwvLjb0vTD9BXLOwwLD_GWCmC&si=_TcStvoCFZwq-fb0)

 You may also find this docker tutorial by M Prashant helful in learning docker.

 - M Prashant - [Docker For Beginners](https://youtu.be/OhnTMWmfTBE?si=dhZY7AtRBJ9cVPNm)



## Install and Setup Docker (Linux)

You can install Docker on your own system, or alternatively you can deploy a virtual machine on Azure, GCP, or AWS to setup docker to follow along.

```bash
  sudo apt-get update
  sudo apt install docker.io
```

Ensure that docker daemon is up and running, you can confirm this using systemctl command.

```bash
  sudo systemctl status docker
```

If docker daemon is not already started then start the docker daemon service using systemctl.

```bash
  sudo systemctl start docker
```

Add your user account to docker group to run docker service without sudo. This is essential to ensure that your server's security is not compromised in case if the docker service is hacked by a threat actor. This could be abused to elevate an attacker's privilege on your server. This can be done using the usermod command.

```bash
  sudo usermod -aG docker debian
```

*debian* is the name of user account in this example. This requires relogin to take effect. Please make sure you logout and login again on your system to use docker service without sudo.



    

## Install and Setup (Windows)

If you wish to follow along on a Windows System, please download the latest version of docker desktop from 
[docker's official website](https://www.docker.com/)
## Build DockerImage

Each application in this repository has a dockerfile that you can use to build your docker image and run docker container on your server. Before you start working, make sure you have git installed on your system to clone this repository locally.

```bash
  git clone https://github.com/WatashiwaSid/Docker
```

Go to an application in project directory. In this example I have used the dockerfile of *Django* application.


```bash
  cd Docker
  cd Django
```


Build Dockerimage from Dokcerfile

```bash
  docker build .
```


## Documentation

- [Docker](https://docs.docker.com/)
- [Django](https://docs.djangoproject.com/en/5.0/)


## Contributions 💡

- If you have a suggestion that would make this repository better or want to add more applications on this repository, please fork this repo and create a pull request.

- You can also open an issue.
- Please make sure you have read Contribution Guideline before submitting a pull request.
