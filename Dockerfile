FROM python:3.10.11

USER root

# Install Java OpenJDK 1.8
RUN wget https://github.com/adoptium/temurin8-binaries/releases/download/jdk8u472-b08/OpenJDK8U-jdk_x64_linux_hotspot_8u472b08.tar.gz && \
    mkdir -p /usr/lib/jvm && \
    tar -xzf OpenJDK8U-jdk_x64_linux_hotspot_8u472b08.tar.gz -C /usr/lib/jvm && \
    rm OpenJDK8U-jdk_x64_linux_hotspot_8u472b08.tar.gz

ENV JAVA_HOME=/usr/lib/jvm/jdk8u472-b08
ENV PATH="$JAVA_HOME/bin:$PATH"

# Install Spark 3.5.7
RUN wget https://archive.apache.org/dist/spark/spark-3.5.7/spark-3.5.7-bin-hadoop3.tgz && \
    tar -xzf spark-3.5.7-bin-hadoop3.tgz && \
    mv spark-3.5.7-bin-hadoop3 /opt/spark && \
    rm spark-3.5.7-bin-hadoop3.tgz

# Install PySpark 3.5.7
RUN pip3 install pyspark==3.5.7

ENV SPARK_HOME=/opt/spark
ENV PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin

WORKDIR /app