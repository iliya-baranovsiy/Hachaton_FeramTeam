import asyncio

from openai import OpenAI
from servesies.file_work import str_read


async def AiAnalyse():
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key="",
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
