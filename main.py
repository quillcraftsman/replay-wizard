"""
Manual run module
"""
import time
from quickstart.capturing import capture_actions
from quickstart.replay import replay_actions
from replay_wizard.__main__ import main

if __name__ == '__main__':
    capture_actions()
    time.sleep(5)
    replay_actions()
    main()
