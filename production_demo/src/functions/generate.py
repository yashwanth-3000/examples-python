from restack_ai.function import function, FunctionFailure, log
from openai import OpenAI

@function.defn()
async def llm_generate(prompt: str) -> str:

    try:
        client = OpenAI(base_url="http://192.168.4.142:1234/v1/",api_key="llmstudio")
    except Exception as e:
        log.error(f"Failed to create LLM client {e}")
        raise FunctionFailure(f"Failed to create OpenAI client {e}", non_retryable=True) from e

    try:
        response = client.chat.completions.create(
            model="llama-3.2-3b-instruct",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.5,
        )
    
    except Exception as e:
        log.error(f"Failed to generate {e}")
    
    return response.choices[0].message.content
