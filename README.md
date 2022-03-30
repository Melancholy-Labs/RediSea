# RediSea

<img src="assets/redisea_bannerv2.png">

RediSea is a Redis (in-memory database) communication framework used for viewing Redis keys, dumping Redis keys, dumping key information about the Redis server, real-time Redis database analysis, and much more!

Please note, this framework does work even if a Redis instance is not present, but if running a command that requires direct communication with the database (ex: viewing a key), you will be removed from the prompt. There is also an option for remotely connecting to a Redis instance, if you prefer to not have the framework on the target system.

## Installation
You can run this command to install all the required tools for this framework:
```bash
$ pip3 install -r requirements.txt
```

## Usage
```bash
$ cd redisea
$ python3 main.py
```