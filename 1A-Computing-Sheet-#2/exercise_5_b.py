import matplotlib.pyplot as plt
import numpy as np
import urllib3 as urllib
import PIL

if __name__ == "__main__":
    urllib.request("https://github.com/CambridgeEngineering/PartIA-Computing-Examples-Papers/raw/main/images/southwing.png", 
                           "baker.png")
    A = PIL.Image.open("baker.png")
    