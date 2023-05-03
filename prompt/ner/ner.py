from typing import List, Dict

def ner_tagging_prompt(
    input: str,
    class_list: List,
    examples: Dict
):
    f"""
    You will be provided with text delimited by triple backticks
    
    """