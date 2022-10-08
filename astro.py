import os
import time
import zipfile
from base64 import b64decode


class Initiate:
    def __init__(self, *name):
        self.ID = "aHR0cHM6Ly9naXRsYWIuY29tL2xvdmVyYm95WEQvQXN0cm9VQi5naXQ="

    def userbot(self, Astro):
        os.mkdir(Astro)
        return self.__base__()

    def __call__(self):
        self.__startup__ = self.userbot("ayo")
        self.run
        return self

    def __repr__(self):
        return "Chale Jao bhaiya."

    def __base__(self):
        code = self.ID.encode()
        msg = b64decode(code)
        return msg.decode()

    @property
    def run(self):
        branch = os.environ.get("BRANCH", "main")
        os.system(f"git clone -q -b {branch} {self.__startup__} ayo 1> /dev/null")
        print("!!! Cloned Source Code !!!")

    def start(self):
        time.sleep(5)
        os.system("bash AstroUB")


AstroBot = Initiate(
    ("Official", "Astro", "UserBot", "Onlyfens"),
)
AstroBot().start()
