from llmlingua import PromptCompressor
from fastapi import FastAPI

app = FastAPI()
llm_lingua = PromptCompressor()

@app.get("/compress")

async def compress_prompt(input_prompt: str):
    """
    Calls LLMLingua PromptCompressor and returns the compressed prompt
    """
    
    compressed_prompt = llm_lingua.compress_prompt(context, instruction="", question=question, target_token=200)

    return compressed_prompt['compressed_prompt']