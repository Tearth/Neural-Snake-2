import sys;
sys.path.append("AI")
sys.path.append("GUI")
sys.path.append("Helpers")

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