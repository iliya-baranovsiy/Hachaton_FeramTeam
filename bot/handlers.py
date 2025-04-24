from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from keybords import *
from aiogram.types.input_file import FSInputFile
from servesies.ai import *
import asyncio
from servesies.db import db
from form_vac import form

router = Router()
user_dict = {}


@router.message(CommandStart())
async def start_mes(mes: Message):
    count = 0
    id = mes.chat.id
    user_dict[id] = []
    user_dict[id].append(count)
    buttons = InlineKeyboardMarkup(inline_keyboard=menu)
    await mes.answer(
        'Привет, я бот-аналитик 👋\n\nЯ помогаю анализировать данные об IT вакансиях и выдвать статистику по ним📊\nС моей помощью ты сможешь быстро и просто ознакомиться с обстановкой на текущем рынке IT труда 🖥️\n\nМои возможности:\n\n1)Предоставлять актуальные данные с помощью гистограмм и куруговых диаграмм 📈\n\n2)Предоставлять актуальные данные и вакансии по твоим собственным фильтрам 📉\n\n3)Анализировать рынок труда с помощью ИИ 🤖\n\nРад знакомству с тобой, теперь приступим к действию 👨‍🚀')
    await asyncio.sleep(3)
    await mes.answer('Выбери один из пунктов меню 👇', reply_markup=buttons)


@router.callback_query(F.data == 'menu')
async def menu_disp(callback: CallbackQuery):
    buttons = InlineKeyboardMarkup(inline_keyboard=menu_buttons)
    await callback.message.edit_text("Выбери один из пунктов меню 👇", reply_markup=buttons)


@router.callback_query(F.data == "common_stat")
async def common_display(call: CallbackQuery):
    buttons = InlineKeyboardMarkup(inline_keyboard=common_stat_but)
    await call.message.edit_text('Выбери один из пунктов 👇', reply_markup=buttons)


@router.callback_query(F.data == 'exp')
async def send_exp(call: CallbackQuery):
    buttons = InlineKeyboardMarkup(inline_keyboard=menu_buttons)
    await call.message.answer_photo(photo=types.FSInputFile("experience_distribution.png"),
                                    caption='Круговая диагармма анализа опыта работы 🤓')
    await call.message.answer('Выбери один из пунктов 👇', reply_markup=buttons)
    await call.message.delete()


@router.callback_query(F.data == 'format')
async def send_type(call: CallbackQuery):
    buttons = InlineKeyboardMarkup(inline_keyboard=menu_buttons)
    await call.message.answer_photo(photo=FSInputFile('work_formats_distribution.png'),
                                    caption='Гистограмма форматов работы 🧐')
    await call.message.answer('Выбери один из пунктов 👇', reply_markup=buttons)
    await call.message.delete()


@router.callback_query(F.data == 'AI')
async def ai_answer(call: CallbackQuery):
    buttons = InlineKeyboardMarkup(inline_keyboard=menu_buttons)
    try:
        await call.message.edit_text('Генерируем ответ... 🤖')
        ans = await AiAnalyse()
        await call.message.answer(ans)
        await call.message.answer('Для продолжения выбери один из пунктов 👇', reply_markup=buttons)
    except:
        await call.message.answer('Что-то пошло не так, попробуй заново 🔄', reply_markup=buttons)


@router.callback_query(F.data == 'filters')
async def get_filters(call: CallbackQuery):
    buttons = InlineKeyboardMarkup(inline_keyboard=filters_kb)
    await call.message.edit_text('Выбери один из пунктов 👇', reply_markup=buttons)


@router.callback_query(F.data == 'actual')
async def actual(call: CallbackQuery):
    buttons = InlineKeyboardMarkup(inline_keyboard=menu_buttons)
    await call.message.answer_photo(photo=FSInputFile('pic/gisto_count.png'),
                                    caption='Гистограмма с данными об актуальности ЯП')
    await asyncio.sleep(2)
    await call.message.answer('Для продолжения выбери один из пунктов 👇', reply_markup=buttons)
    await call.message.delete()


@router.callback_query(F.data == 'req_prog')
async def choice_lang(call: CallbackQuery):
    buttons = InlineKeyboardMarkup(inline_keyboard=req_lang)
    await call.message.edit_text('Выберите один из ЯП  👇', reply_markup=buttons)


@router.callback_query(F.data == 'python')
async def python_req(call: CallbackQuery):
    buttons = InlineKeyboardMarkup(inline_keyboard=menu_buttons)
    await call.message.answer_photo(FSInputFile('pic/python_reqs.png'), caption='Технологие используемые в Python')
    await call.message.answer('Для продолжения выбери один из пунктов 👇', reply_markup=buttons)
    await call.message.delete()


@router.callback_query(F.data == 'jav')
async def python_req(call: CallbackQuery):
    buttons = InlineKeyboardMarkup(inline_keyboard=menu_buttons)
    await call.message.answer_photo(FSInputFile('pic/java_reqs.png'), caption='Технологие используемые в Java')
    await call.message.answer('Для продолжения выбери один из пунктов 👇', reply_markup=buttons)
    await call.message.delete()


@router.callback_query(F.data == 'js')
async def python_req(call: CallbackQuery):
    buttons = InlineKeyboardMarkup(inline_keyboard=menu_buttons)
    await call.message.answer_photo(FSInputFile('pic/js_reqs.png'), caption='Технологие используемые в JS')
    await call.message.answer('Для продолжения выбери один из пунктов 👇', reply_markup=buttons)
    await call.message.delete()


@router.callback_query(F.data == 'cs')
async def python_req(call: CallbackQuery):
    buttons = InlineKeyboardMarkup(inline_keyboard=menu_buttons)
    await call.message.answer_photo(FSInputFile('pic/cs_reqs.png'), caption='Технологие используемые в C#')
    await call.message.answer('Для продолжения выбери один из пунктов 👇', reply_markup=buttons)
    await call.message.delete()


@router.callback_query(F.data == 'detail')
async def python_req(call: CallbackQuery):
    buttons = InlineKeyboardMarkup(inline_keyboard=menu_buttons)
    await call.message.answer_photo(FSInputFile('pic/exp_.png'), caption='Гистограмма по соотношению опыта и ЯП')
    await call.message.answer('Для продолжения выбери один из пунктов 👇', reply_markup=buttons)
    await call.message.delete()


@router.callback_query(F.data == 'search')
async def search_func(call: CallbackQuery):
    buttons = InlineKeyboardMarkup(inline_keyboard=search_list)
    await call.message.edit_text('Выберите желаемый опыт 👇', reply_markup=buttons)


@router.callback_query(F.data == 'exp_one-three')
async def one_three_exp(call: CallbackQuery):
    buttons_menu = InlineKeyboardMarkup(inline_keyboard=menu_buttons)
    try:
        id = call.message.chat.id
        count = user_dict[id][0]
        data = await db.select_info_exp()
        mes = form(data[count][0], data[count][1], data[count][2], data[count][3], data[count][4], data[count][5])
        buttons = InlineKeyboardMarkup(inline_keyboard=inc_button)
        await call.message.answer(mes, reply_markup=buttons)
        user_dict[id][0] = count + 1
    except:
        await call.message.answer('Список анкет с данным фильтром пуст, вернитесь в меню', reply_markup=buttons_menu)


@router.callback_query(F.data == 'next')
async def next_vac(call: CallbackQuery):
    buttons_menu = InlineKeyboardMarkup(inline_keyboard=menu_buttons)
    try:
        id = call.message.chat.id
        count = user_dict[id][0]
        data = await db.select_info_exp()
        mes = form(data[count][0], data[count][1], data[count][2], data[count][3], data[count][4], data[count][5])
        buttons = InlineKeyboardMarkup(inline_keyboard=inc_button)
        await call.message.answer(mes, reply_markup=buttons)
        user_dict[id][0] = count + 1
    except:
        await call.message.answer('Список анкет с данным фильтром пуст, вернитесь в меню', reply_markup=buttons_menu)





@router.message()
async def random_mes(mes: Message):
    buttons = InlineKeyboardMarkup(inline_keyboard=menu)
    await mes.answer('Перейди в меню, чтобы продолжить 👇', reply_markup=buttons)
