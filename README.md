# kafka-playground
Playground for Kafka

# Running Kafka
This assumes docker & docker-compose are already installed
```bash
docker-compose up
```

# Build the scripts runner image
```bash
docker build --pull -t kafka-scripts:latest .
```

# Run the various scripts
Assumes you're running the cluster with the above command
```bash
# Run the container linked into the cluster
docker run -it --network kafka-playground_cluster --rm -v $(pwd):/scripts -w '/scripts' kafka-scripts:latest /bin/bash

# Create the default topics
./create-topics.py
```
