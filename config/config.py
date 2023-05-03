import os

MAIN_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(MAIN_DIR, "data")
PROMPT_DIR = os.path.join(MAIN_DIR, "prompt")

TEMPERATURE = 0.0
TOP_K = 50
TOP_P = 0.9

CLASS_LIST = [
    
]