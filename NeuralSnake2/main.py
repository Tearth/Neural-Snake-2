import sys;
sys.path.append("AI")
sys.path.append("GUI")
sys.path.append("Helpers")

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

from window import *
from core import *

def main():
    window = Window()
    core = Core(window)

    core.start()
    window.run()
    core.stop()

if __name__ == "__main__":
    main()