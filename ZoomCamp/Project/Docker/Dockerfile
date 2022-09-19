FROM apache/airflow:2.3.4

ENV AIRFLOW_HOME=/opt/airflow

USER root

# Get JAVA
RUN apt update && \
    apt-get install -y openjdk-11-jdk && \
    apt-get install -y ant && \
    apt-get clean;

# Set JAVA_HOME
ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64/
RUN export JAVA_HOME

USER airflow

WORKDIR $AIRFLOW_HOME

COPY requirements.txt .

RUN pip install --user --upgrade pip
RUN pip install --no-cache-dir --user -r requirements.txt