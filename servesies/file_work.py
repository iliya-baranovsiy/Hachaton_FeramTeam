import asyncio
import os
from servesies.db import db

async def main():
    data = await db.select_all_from_work()
    return data


def write_file():
    with open('Ai.txt', 'w', encoding='utf-8') as f:
        for item in asyncio.run(main()):
            line = f"{item['name']}; {item['company']}; {item['salary']}; {item['experience']}; {item['work_type']}; {item['requirements']}; {item['registration_date']}\n"
            f.write(line)


def str_read():
    res_str = ""
    with open(r'D:\my\HachatoN\servesies\Ai.txt', 'r', encoding='utf-8') as f:
        for line in f:
            clean_line = line.strip()
            res_str += clean_line + '\n'
    return res_str

