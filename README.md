# Hadoop Server with Docker Compose

This project provides a simple way to run a Hadoop server locally using Docker Compose. It is ideal for learning, development, and testing purposes without the need for manual Hadoop installation.

## Project Description

The repository contains a `docker-compose.yml` file that sets up a single-node Hadoop cluster. It includes all necessary services such as NameNode, DataNode, ResourceManager, and NodeManager. This setup allows you to experiment with Hadoop's distributed storage and processing capabilities in a contained environment.

## Getting Started

### Prerequisites

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/)

### Running the Hadoop Server

1. Clone this repository:
    ```bash
    git clone https://github.com/andrewgun95/hadoop-cluster
    cd hadoop-cluster
    ```
2. Start the Hadoop cluster:
    ```bash
    cd hadoop-server
    docker-compose up -d
    ```
3. Access Hadoop services via the exposed ports (see `docker-compose.yml` for details).
    - [localhost:8042](http://localhost:8042) : Node Manager UI
    - [localhost:8088](http://localhost:8088) : Resource Manager UI
    - [localhost:9870](http://localhost:9870) : Name Node UI

4. Place your Spark job application in the `/devl` directory, then submit the job from within the Spark job container:
    ```bash
    docker exec -it hadoop-server-spark-job /bin/bash
    spark-submit --master yarn --deploy-mode cluster ./example1/src/main/python/bin/basic.py
    ```

### Stopping the Cluster

```bash
docker-compose down
```

## Useful Links

- [Hadoop Documentation](https://hadoop.apache.org/docs/)
- [Docker Compose Documentation](https://docs.docker.com/compose/)

---

Feel free to customize the configuration for your specific use case.