# Load Balancing
It shows how to use nginx to load balancing between two applications with split traffic.

![alt text](architecture.png "Split Traffic")

## Stack
* Python 3
* Flask
* Docker
* Nginx


## Run it!

```bash
$ docker-compose up --build
```

The command above will spin up two flask apps and one instance of nginx acting as the load balancing. The traffic is splitted as bellow:
* 60% - App V1
* 30% - App V2

In order to test, you can run the `smoke-test.sh` script typing the comand bellow:

```bash
$ smoke-test.sh
```
