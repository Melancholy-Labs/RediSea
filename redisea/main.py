# -*- coding: utf-8 -*-

import redis, time, sys, os, platform, argparse

from subprocess import getoutput
from prettytable import PrettyTable

r = redis.Redis()
version = '0.2.30'
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

Traverse a Redis database instance in a much simpler way by using our open prompt!

                    Start by typing "h" in the prompt below
        
        """.format(author, version))
    
    def real_time_render(self):

        parser = argparse.ArgumentParser()
        parser.add_argument('-s', '--start_server', help="Choose specific keys to investigate in real-time", action='store_true', default=True, required=False)
        args = parser.parse_args()

        def clear():
            if platform.system() == "Windows":
                os.system("cls")
            else:
                os.system("clear")
        
        timer = 0

        if args.start_server:

            print("Example: key1 key2 key3")
            user_keys = input("Enter Search Criteria (seperated by spaces): ")

            key_list = user_keys.split()

            while True:
                time.sleep(0.1) # 100ms
                clear()

                state_header = PrettyTable(["Keys", "Values"])
                
                for key_stuff in key_list:
                    state_value = r.mget(key_stuff)
                    state_header.add_row([key_stuff, state_value])
                
                print(state_header.get_string(title="Real Time Redis Data"))

                timer += 100

                print("\nTime Elapsed: {0}ms".format(timer))
                print("\nYou can exit out by pressing Ctrl + C")

    def redis_comms(self):

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
                print("r, remote    Remotely connect to a Redis instance")
                print("rt, realtime View Redis data update in real-time")
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
                system_info = platform.system()

                if system_info == 'Windows':
                    os.system("cls")
                else:
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
                RediSea().banner()
            elif command == "i" or command == "info":
               redis_data = r.execute_command('CLIENT LIST')
               redis_data_str = str(redis_data)
               
               print(redis_data_str)
            elif command == "r" or command == "remote":
                print("When remotely connecting to Redis, you will be removed from the RediSea shell!")
                
                ip_address = input("IP Address: ")
                port = input("Port: ")
                
                confirm_choice = input("Are you sure you would like to continue (y/n)? ")

                if confirm_choice == "y":
                    os.system(f"redis-cli -h {ip_address} -p {port}")
                elif confirm_choice == "n":
                    print("Exiting...")
                else:
                    print("Please choose y/n")
            elif command == "rt" or command == "realtime":
                RediSea().real_time_render()
            else:
                print("? Unrecognized Command ?")

if __name__ == '__main__':
    rs = RediSea()
    rs.banner()
    rs.redis_comms()