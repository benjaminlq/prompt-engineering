from typing import List, Dict

def ner_tagging_prompt(
    input: str,
    class_list: List,
    examples: Dict
):
    example_text = "\n."
    prompt = f"""
    Your task is to perform name entity recognition (NER) for each word \
    inside the text delimited by triple backticks into following {len(class_list)} labels: {[", ".join(class_list)]}.

    Output requirements:
    - The answer should return the sentence and the tags next to its corresponding words inside <>. 
    - Follow the format of the example provided.

    Example:
    Text: Maria is living in New York.
    Maria <person> is living in New <city> York <city>.
    """
    
    return prompt