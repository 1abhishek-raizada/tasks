from langchain.prompts import FewShotPromptTemplate, PromptTemplate

examples = [
    {"word": "happy", "antonym": "sad"},
    {"word": "fast", "antonym": "slow"}
]

example_prompt = PromptTemplate.from_template("Word: {word}\nAntonym: {antonym}")

prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    suffix="Word: {input}\nAntonym:",
    input_variables=["input"]
)

formatted = prompt.format(input="hot")
print(formatted)
