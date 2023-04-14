# Step 1: Update and Upgrade Ubuntu

First, update and upgrade your Ubuntu system to ensure that all packages are up to date.

```
sudo apt update
sudo apt upgrade -y
```

# Step 2: Install Java

Apache Spark requires Java to be installed on your system. You can install Java by running the following command:

```
sudo apt install openjdk-17-jdk -y
```

# Step 3: Download and Extract Apache Spark

- Download Apache Spark from the official website using the following command:

```
wget https://downloads.apache.org/spark/spark-3.4.0/spark-3.4.0-bin-hadoop3.tgz
```

- Extract the downloaded archive using the following command:

```
tar -xvf spark-3.4.0-bin-hadoop3.tgz
mv spark-3.4.0-bin-hadoop3 /opt/spark
ln -s /opt/spark-3.4.0 /opt/spark
```

# Step 4: Set Environment Variables

- Set the environment variables for Apache Spark by adding the following lines to the end of the ~/.bashrc file:

open ~/.bashrc file using the following command:

```
nano ~/.bashrc
```

add the following lines to the end of the file:

```
export SPARK_HOME=/opt/spark
export PATH=$SPARK_HOME/bin:$PATH

```

# Step 5: Start Apache Spark

You can start Apache Spark by running the following command:

```

$SPARK_HOME/sbin/start-all.sh

```

If that error out "localhost: ssh: connect to host localhost port 22: Connection refused"

    Then run the following command:

    ```
        sudo apt-get remove openssh-client openssh-server
        sudo apt-get install openssh-client openssh-server
    ```

This will start the Spark master and worker processes.

# Step 6: Verify Installation

You can verify that Apache Spark has been installed successfully by running the following command:

```

$SPARK_HOME/bin/run-example SparkPi 10

```

This will run the SparkPi example and calculate the value of pi using 10 partitions.
