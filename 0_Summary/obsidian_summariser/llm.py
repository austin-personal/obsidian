from tenacity import retry, wait_exponential, stop_after_attempt
import openai, logging, os

openai.api_key = os.getenv("OPENAI_API_KEY")


@retry(wait=wait_exponential(1, 2, 60), stop=stop_after_attempt(5), reraise=True)
def chat(messages, model="gpt-4o-mini", max_tokens=800, temperature=0.3):
    res = openai.ChatCompletion.create(
        model=model, messages=messages, max_tokens=max_tokens, temperature=temperature
    )
    u = res.usage
    logging.info(
        "tokens prompt=%d, completion=%d (~$%.4f)",
        u.prompt_tokens,
        u.completion_tokens,
        u.total_tokens * 0.00001,
    )  # 단가는 필요 시 조정
    return res.choices[0].message.content.strip()
