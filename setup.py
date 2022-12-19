"""
    Owner: Hifumi1337 (https://github.com/hifumi1337)
    Project: RediSea
    License: MIT
"""

import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "redisea",
    version = "1.2.32",
    author = "Hifumi1337",
    description = "RediSea is a Redis (in-memory database) communication framework used for dumping key/value information within the Redis server, real-time Redis database analysis, and much more.",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/hifumi1337/RediSea",
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages = [
        "redisea"
    ],
    install_requires=[
        "argparse",
        "redis",
        "prettytable"
    ],
    scripts=["redisea/redisea.py"],
    entry_points={
        'console_scripts': ["redisea=redisea.redisea:RediSea.main"]
    },
    python_requires = ">=3.6"
)