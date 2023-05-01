# prompt-engineering
Prompt Engineering For Different Tasks using Large Language Models

## References
- https://github.com/MantisAI/prompt_engineering
- [Deep Learning AI for Prompt Engineering](https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/)

## I. Prompt Structure
General Structure of prompts:
`SYSTEM_PROMPT` -> `USER_PROMPT` -> `OUTPUT`
- `SYSTEM_PROMPT`: Defines the overall context for the model to perform. For example, select the domain of which the Large Language Model is restricted to generate its outputs.
- `USER_PROMPT`: Task Specific Instructions

## II. Techniques:
### 1. **Zero-shot Prompting**: Only the question is provided. No sample answer is provided to the LLM.

Example: 

```
text = <text input>

prompt = f"""
Do some instructions on the text delimited by triple backticks.
``` {text} ```
"""
```

### 2. **N-shot Prompting**: At least one example of question-answer pair is given.
```
prompt = f"""
Do a task following a consistent format provided.

Text: Input Text
Label: Output Label

Text: Input Text
Label: Output Label

Text: Input Text
"""
```

### 3. **Chain-Of-Thought Prompting**: Prompting LLMs to generate series of intermediate steps that lead to the final results of a multi-step problem. Especially useful in comprehension and arithmetic operations.
```
text = <text input>

prompt = f"""
Execute the following sequence of actions on text delimited by backticks.

Step 1: <Instructions 1>
Step 2: <Instructions 2>
...
Step n: <Instructions n>

``` {text} ```
"""
```

### 4. Tips
#### 1. Use delimiters

- Quotes: ` """ `
- Backticks: ` ``` `
- Dashses: ` --- `
- Angle brackets: ` <> `
- XML tags: ` <tag></tag> `

#### 2. Control Output template
```
prompt = f"""
Perform tasks etc.

Use the following format for outputs:
Text: <text>
Summary: <summary>
Output JSON: <json with summary>
"""
```

#### 3. Additional Instructions:
- Limit output length
- 

## III. Hyperparameters:
- `temperature`: 
- `top-k`:
- `top-p`:
- `top-n`:

## IV. Task-specific Prompt
### 1. Name Entity Recognition (NER)
- [QaNER: Prompting Question Answering Models for Few-shot NER](https://arxiv.org/pdf/2203.01543.pdf)

### 2. Text Summarization  
```
input_text = <input_text>

prompt = f"""
Your task is to generate a short summary of ... # System Prompt

Summarize the text below, delimited by triple backticks, in at most <n> words

Text: ``` {input_text} ```
"""
```

## 