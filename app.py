from llmlingua import PromptCompressor
import runpod

llm_lingua = PromptCompressor()

def transform_prompt(job):   

    job_input = job["input"]
    input_prompt = job_input["input_prompt"]

    lines = input_prompt.splitlines()

    context = "\n".join(lines[:-1])

    question = lines[-1]
    
    compressed_prompt = llm_lingua.compress_prompt(context, instruction="", question=question, target_token=500)

    return compressed_prompt

runpod.serverless.start({"handler": transform_prompt})