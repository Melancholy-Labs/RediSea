# -*- coding: utf-8 -*-

import redis, time, sys, os

from subprocess import getoutput

r = redis.Redis()
version = '0.1.25'
author = 'Hifumi1337'

class RediSea:

    def banner(self):
        print("""
            ██████╗ ███████╗██████╗ ██╗███████╗███████╗ █████╗ 
            ██╔══██╗██╔════╝██╔══██╗██║██╔════╝██╔════╝██╔══██╗
            ██████╔╝█████╗  ██║  ██║██║███████╗█████╗  ███████║
            ██╔══██╗██╔══╝  ██║  ██║██║╚════██║██╔══╝  ██╔══██║
            ██║  ██║███████╗██████╔╝██║███████║███████╗██║  ██║
            ╚═╝  ╚═╝╚══════╝╚═════╝ ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝
                            
                            {0} | v{1}

    Traverse the Redis-cli in a much simpler way by using our open prompt!

                    Start by typing "h" in the prompt below
        
        """.format(author, version))

    def redis_comms(self):

        rsb = RediSea()

        whoami = getoutput("whoami")

        print("Connecting...")
        time.sleep(1)

        while True:
            
            command = input(f"{whoami}@RediSea:~$ ")

            if command == "h" or command == "help":
                print("q, quit      Quit program")
                print("h, help      Displays help menu")
                print("k, key       Search for a specific Redis key")
                print("v, version   Check version of Redis & RediSea")
                print("c, clear     Clears all data in the terminal")
                print("d, dump      Dump entire Redis database (keys)")
                print("df, dumpf    Dump entire Redis database (keys) into a file")
                print("b, banner    Displays our cool banner!")
                print("i, info      Return general information about the Redis instance")
            elif command == "q" or command == "quit":
                print("Disconnecting...")
                time.sleep(0.5)
                sys.exit(0)
            elif command == "v" or command == "version":
                print("RediSea Version:", version)
                print("Redis Version:", r.execute_command('INFO')['redis_version'])
            elif command == "k" or command == "key":
                key = input("Key: ")
                key_output = r.mget(key)
                
                print(f"Key: {key} \n Value: {key_output}")
            elif command == "c" or command == "clear":
                os.system("clear")
            elif command == "dump" or command == "d":
                for key in r.scan_iter("*"):
                    print(key)
            elif command == "df" or command == "dumpf":
                with open('redis_dump.log', 'w') as f:
                    for key in r.scan_iter("*"):
                        f.write(str(key) + "\n")
                
                print("Data successfully dumped!")
            elif command == "b" or command == "banner":
                rsb.banner()
            elif command == "i" or command == "info":
               redis_data = r.execute_command('CLIENT LIST')
               redis_data_str = str(redis_data)
               
               print(redis_data_str)
            else:
                print("? Unrecognized Command ?")

if __name__ == '__main__':
    rs = RediSea()
    rs.banner()
    rs.redis_comms()