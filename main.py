from src.mod.session import Session
import pprint
import logging.config
import logging
import json
import os
'''
TODO: 
+ [ ] Write Tests for all the current features
+ [x] Write docstrings for all the current methods and classes
+ [ ] create logging methods using the following format:

<"severity" - "scope" : "message" - "timestamp:2022-05-14T14:16:15+00:00">

'''

def setup_logging(config_path:str):
    """Sets up logging configuration from a JSON file."""
    with open(config_path, 'r') as f:
        config = json.load(f)
    logging.config.dictConfig(config)

def play():

    logger = logging.getLogger("__main__")

    logger.info("Initiate session:")
    session_mem = Session()
    logger.info("session initiated")

    while True:
        logger.info("generate random string-note combination:")
        res = session_mem.randomize()
        print(f"current random {res}")
        single_string = res[0]
        note = res[1]
        # add to session_memory
        session_mem.insert(string_no=str(single_string), note=str(note))
        # check if session is done:
        if session_mem.done:
            print("current session:")
            pprint.pprint(session_mem.data)
            print(f"finished string: {session_mem.finished}")
            print("Thank you for playing")
            break
        # ask if you still want to play
        print("current session:")
        pprint.pprint(session_mem.data)
        print(f"finished string: {session_mem.finished}")
        print("continue (Default yes)? (Y/N)")
        ans = input()
        if ans.upper() != "N":
            continue
        else:
            break

if __name__ == "__main__":
    pwd = os.getcwd()
    config_file_path = os.path.join(pwd, "log_config.json")
    setup_logging(config_file_path)
    logger = logging.getLogger(__name__)
    logger.info("start playing")
    play()
    logger.info("session ends!")

