import asyncio
import websockets
import json
import time
import helper
from QuizWebsocket import QuizWebsocket
from price import Price
from prices import prices

config = helper.read_config()

async def main():
    async with QuizWebsocket() as echo:
        await echo.send()
        return await echo.receive()


if __name__ == '__main__':

    list_size = int(config['APPSettings']['list_size'])
    number_of_samples = int(config['APPSettings']['number_of_samples'])
    wait_between_samples_seconds = int(config['APPSettings']['wait_between_samples_seconds'])
    
    market = config['APPSettings']['Market']
    
    info = prices(list_size)

    for i in range(number_of_samples):
        time.sleep(wait_between_samples_seconds)

        response = asyncio.run(main())
        response_dict = json.loads(response)
        new_price = Price(i + 1, response_dict["prices"][market]["bid"], response_dict["prices"][market]["ask"])

        info.add_price(new_price)
