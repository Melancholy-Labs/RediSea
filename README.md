<img src="https://raw.githubusercontent.com/azazelm3dj3d/RediSea/main/assets/redisea_banner_v3.png">

RediSea is a Redis (in-memory database) communication framework used for viewing Redis keys, dumping Redis keys, dumping key information about the Redis server, real-time Redis database analysis, and much more!

Please note, this framework does work even if a Redis instance is not present. There is also an option for remotely connecting to a Redis instance.

RediSea is available through pip:
```bash
pip install redisea
```

Once RediSea is installed, you can run it like any other executable:
```bash
redisea
```

After running RediSea, it'll boot up the application in an open prompt.

## Usage (only required if installing from source)
You can run this command to install all the required tools for this framework:
```bash
pip3 install -r requirements.txt
```
```bash
python3 redisea/main.py
```