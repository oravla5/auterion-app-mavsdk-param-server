#!/usr/bin/python

import datetime
import libmav

import asyncio
from mavsdk import System

async def main():
    skynode = System()
    print("Created mavsdk.System object")
    await skynode.connect(system_address="tcp://172.17.0.1:5790")
    print("Connected to vehicle")
    
    await skynode.param_server.provide_param_int("FANCY_PARAM_123", 45)

if __name__ == "__main__":
    print("Starting mavsdk_param_server.py")
    asyncio.run(main())