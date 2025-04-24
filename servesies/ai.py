import asyncio

from openai import OpenAI
from servesies.file_work import str_read


async def AiAnalyse():
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key="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",
    )
    completion = client.chat.completions.create(
        model="deepseek/deepseek-chat:free",
        messages=[
            {
                "role": "user",
                "content": f"Сделай краткий но информативный анализ {str_read()}"
            }
        ]
    )
    return completion.choices[0].message.content

#print(asyncio.run(AiAnalyse()))
