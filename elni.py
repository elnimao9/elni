from seleniumbase import SB
import time
import requests
import sys
import requests
import os
import random
import subprocess
from dataclasses import dataclass
from typing import List, Optional
import requests
import base64

name = "YnJ1dGFsbGVz"

name_d = base64.b64decode(name)
fulln = name_d.decode("utf-8")
urlt = f"https://www.twitch.tv/{fulln}"
urly = f"https://www.youtube.com/@{fulln}/live"
while True:
    with SB(uc=True, test=True,locale="en") as elny:
        rnd = random.randint(450,900)
        elny.uc_open_with_reconnect(urlt, 5)
        elny.sleep(10)
        if elny.is_element_present("#live-channel-stream-information"):
        
            if elny.is_element_present('button:contains("Accept")'):
                elny.uc_click('button:contains("Accept")', reconnect_time=4)
            if True:
                elny2 = elny.get_new_driver(undetectable=True)
                elny2.uc_open_with_reconnect(urlt, 5)
                elny2.sleep(10)
                if elny2.is_element_present('button:contains("Accept")'):
                    elny2.uc_click('button:contains("Accept")', reconnect_time=4)
                elny.sleep(10)
                elny3 = elny.get_new_driver(undetectable=True)
                elny3.uc_open_with_reconnect(urly, 5)
                elny3.sleep(10)
                if elny3.is_element_present('button:contains("Accept")'):
                    elny3.uc_click('button:contains("Accept")', reconnect_time=4)
                    elny3.sleep(10)
                else:
                    elny3.sleep(10)
                    elny3.uc_gui_press_key('K')
                elny.sleep(rnd)
                elny.quit_extra_driver()
        else:
            break
