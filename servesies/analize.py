import asyncio
from matplotlib import pyplot as plt
from collections import Counter
from db import db
import numpy as np


async def split_formats(formats):
    split_list = []
    for format in formats:
        format = format.replace('или', ',')
        split_list.extend([f.strip() for f in format.split(',')])
    return split_list


async def circle_image():
    data_set = [i[0] for i in await db.select_all_exp()]
    experience_counts = Counter(data_set)
    labels = experience_counts.keys()
    sizes = experience_counts.values()
    plt.figure(figsize=(10, 7))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.title('Распределение опыта')
    return plt.savefig('experience_distribution.png', format='png')


async def gistogram(data_list):
    format_counts = Counter(data_list)

    labels = format_counts.keys()
    sizes = format_counts.values()

    plt.figure(figsize=(8, 6))
    plt.bar(labels, sizes, color='skyblue')
    plt.xlabel('Форматы работы')
    plt.ylabel('Количество')
    plt.title('Распределение форматов работы')
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig('work_formats_distribution.png')


def gisto_counter():
    lang_data = asyncio.run(db.select_lang_num())

    languages = list(lang_data.keys())
    vacancies = list(lang_data.values())

    plt.figure(figsize=(10, 6))
    plt.bar(languages, vacancies, color='skyblue')
    plt.xlabel('Язык')
    plt.ylabel('Кол-во вакансий')
    plt.title('Кол-во вакансий по языкам')
    plt.xticks(rotation=45)
    plt.tight_layout()
    return plt.savefig('gisto_count.png')


def cs_req():
    lang_data = asyncio.run(db.reqs_cs())

    labels = lang_data.keys()
    sizes = lang_data.values()

    plt.figure(figsize=(8, 8))  # Размер фигуры
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.title('Технологии C#')
    return plt.savefig('cs_reqs.png')


def js_req():
    lang_data = asyncio.run(db.reqs_js())

    labels = lang_data.keys()
    sizes = lang_data.values()

    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.title('Технологии js')
    return plt.savefig('js_reqs.png')


def java_req():
    lang_data = asyncio.run(db.reqs_java())

    labels = lang_data.keys()
    sizes = lang_data.values()

    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.title('Технологии java')
    return plt.savefig('java_reqs.png')


def python_req():
    lang_data = asyncio.run(db.reqs_pyt())

    labels = lang_data.keys()
    sizes = lang_data.values()

    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.title('Технологии python')
    return plt.savefig('python_reqs.png')


def visual_exp():
    data = asyncio.run(db.select_exp())
    languages = list(data.keys())
    no_experience = [data[lang]['None exp'] for lang in languages]
    one_to_three_years = [data[lang]['1-3'] for lang in languages]
    three_to_six_years = [data[lang]['3-6'] for lang in languages]
    more_than_six_years = [data[lang]['>6'] for lang in languages]
    bar_width = 0.2
    x = np.arange(len(languages))
    plt.figure(figsize=(10, 6))
    plt.bar(x - bar_width * 1.5, no_experience, width=bar_width, label='Без опыта')
    plt.bar(x - bar_width / 2, one_to_three_years, width=bar_width, label='1-3 года')
    plt.bar(x + bar_width / 2, three_to_six_years, width=bar_width, label='3-6 лет')
    plt.bar(x + bar_width * 1.5, more_than_six_years, width=bar_width, label='Более 6 лет')
    plt.xlabel('Языки программирования')
    plt.ylabel('Количество вакансий')
    plt.title('Количество вакансий по языкам программирования и опыту работы')
    plt.xticks(x, languages)
    plt.legend()
    plt.tight_layout()
    return plt.savefig('exp_.png')




"""async def main():
    list_ = await db.select_work_type()
    redy_list = await split_formats(list_)
    await gistogram(redy_list)


asyncio.run(main())"""
