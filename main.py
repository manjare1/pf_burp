import csv, asyncio, os

from tasks.pumpfun import Pumpfun
from tasks.burp_ai import burp_detect
from tasks.test_burp import test_burp_detect


async def main():
    pumpfun = Pumpfun()

  
    # mp3_file_path = r'audio\burp.mp3'          # Burp
    # test_burp_detect(mp3_file_path)

    burp_detect()
    await pumpfun.create_token()


if __name__ == '__main__':
    # if platform.system() == "Windows":
    #     asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
