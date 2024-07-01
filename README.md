# Prompt Engineering on Large Language Models using LangChain framework
Prompt Engineering For Different Tasks using Large Language Models

## References
- https://github.com/MantisAI/prompt_engineering
- [Deep Learning AI for Prompt Engineering](https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/)
- [How to generate text using different decoding methods](https://huggingface.co/blog/how-to-generate)


## I. Prompt Structure
General Structure of prompts:
`SYSTEM/CONTEXT PROMPT` -> `USER PROMPT` -> `OUTPUT`
- `SYSTEM/CONTEXT PROMPT`: Defines the overall context for the model to perform. Set behaviour of the Assistant without User awareness.
- `USER PROMPT`: Task Specific Instructions, Questions from Users, etc
- `ASSISTANT PROMPT`: Assistant (LLM Model) answer output. Use as previous response in sequential interactions (e.g. Chatbot)

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
- Limit output length: `in at most <n> words`
- Limit output label: `Give your answer in a single word, either "label1", "label2" or "label3".`

## III. Hyperparameters:
- `temperature`: Control the degree of randomness of the generative model during decoding. If the output tokens are generated by sampling from the temperatured Softmax probability distribution defined by the equation:

$$ p_i = \frac{e^{z_i/temperature}}{\sum_j{e^{z_j/temperature}}} $$

High temperature results in more random behaviour while low temperature results in less random behaviour. <br>
At t = 0, **softmax == argmax**

- `top-k`: Basically choose the top k words based on highest probability before applying probability distribution for sampling.
- `top-p`: Nucleus sampling. Choose the smallest possible sets of words which gives cumulative probability > `top-p`. When p = 1 -> Choose all vocabulary.
- `n`: Number of sequence outputs to be returned by the model.
