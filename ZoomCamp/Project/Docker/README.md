# Airflow on Docker

To run Airflow on docker, all you have to do is pull the docker-compose file from their [website](https://airflow.apache.org/docs/apache-airflow/stable/start/docker.html) which shows step by step instructions on how to do so, but it is as simple as shown below.

```bash
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.3.4/docker-compose.yaml'
```
This pulls the docker-compose file to your working directory. The next step is to make a directory for the dags, logs and plugins.

```bash
mkdir -p ./dags ./logs ./plugins
```

Also, create an environment file as follows:

```bash
echo -e "AIRFLOW_UID=$(id -u)" > .env
```

In this .env file, you can put the rest of your environments.
