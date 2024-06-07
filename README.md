# asgi-test

## Background
This repo tests how we can use dd-trace-py (Datadog Python Tracer) for a vanilla set up with the Quart Framework (Python). 

## Useful Links
- https://ddtrace.readthedocs.io/en/stable/integrations.html?highlight=asgi
- https://github.com/pallets/quart

### Clone the repo
```
git clone https://github.com/jon94/asgi-test.git

cd asgi-test
```
### Add Datadog API Key
- Add your Datadog API Key into the docker-compose.yaml file

### Bring up the services
```
docker compose up -d --force-recreate --no-deps --build
```

### Generate Traffic
```
docker ps -a

CONTAINER ID   IMAGE                  COMMAND                  CREATED          STATUS                             PORTS                                            NAMES
7335bbfb3d86   admin-quart            "ddtrace-run hyperco…"   25 seconds ago   Up 23 seconds                      0.0.0.0:8000->8000/tcp                           admin-quart-1

0e073671afd5   datadog/agent:7.54.0   "/bin/entrypoint.sh"     25 seconds ago   Up 24 seconds (health: starting)   0.0.0.0:8125->8125/udp, 0.0.0.0:8126->8126/tcp   admin-datadog-agent-1

```

```
docker exec -it 7335bbfb3d86 /bin/bash

root@7335bbfb3d86:/app# curl localhost:8000/api
hello

```

### View it in Datadog
![asgi datadog](https://github.com/jon94/asgi-test/assets/40360784/b9915894-6688-43f0-8624-47f843dc9ec4)
