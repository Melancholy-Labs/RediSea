# RediSea

<img src="assets/redisea_bannerv2.png">

RediSea is a Redis (in-memory database) communication framework used for viewing Redis keys, dumping Redis keys, dumping key information about the Redis server, real-time Redis database analysis, and much more!

Please note, this framework does work even if a Redis instance is not present. There is also an option for remotely connecting to a Redis instance, if you prefer to not have the framework on the target system.

There is now have a Linux binary available! You can use the provided executable by running the following command (after downloading from our releases):
```bash
./redisea
```

## Installation (only required if installing from source)
You can run this command to install all the required tools for this framework:
```bash
pip3 install -r requirements.txt
```

## Usage (only required if installing from source)
```bash
python3 redisea/main.py
```