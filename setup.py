"""
    Owner: azazelm3dj3d (https://github.com/azazelm3dj3d)
    Project: RediSea
    License: MIT
"""

import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "redisea",
    version = "1.2.33",
    author = "azazelm3dj3d",
    description = "RediSea is a Redis (in-memory database) communication framework used for dumping key/value information within the Redis server, real-time Redis database analysis, and much more.",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/azazelm3dj3d/RediSea",
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