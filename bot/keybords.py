from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

menu = [
    [InlineKeyboardButton(text='Меню 📊', callback_data='menu')],
]
menu_buttons = [
    [InlineKeyboardButton(text='Общая статистика 🧐', callback_data='common_stat')],
    [InlineKeyboardButton(text='Применить фильтры 🤓', callback_data='filters')]
]

common_stat_but = [
    [InlineKeyboardButton(text='Статистика по опыту 📈', callback_data='exp')],
    [InlineKeyboardButton(text='Статистика по формату работы 📉', callback_data='format')],
    [InlineKeyboardButton(text='Анализ от ИИ 🤖', callback_data='AI')],
    [InlineKeyboardButton(text='Меню 📊', callback_data='menu')]
]

filters_kb = [
    [InlineKeyboardButton(text='Актуальность языков 📊', callback_data='actual')],
    [InlineKeyboardButton(text='Требуемый стек в ЯП 📉', callback_data='req_prog')],
    [InlineKeyboardButton(text='Детальный разбор опыта 📈', callback_data='detail')],
    [InlineKeyboardButton(text='Подбор вакансий', callback_data='search')],
    [InlineKeyboardButton(text='Меню 📊', callback_data='menu')]
]

search_list = [
    [InlineKeyboardButton(text='1-3 года', callback_data='exp_one-three')]
]

req_lang = [
    [InlineKeyboardButton(text='Python', callback_data='python')],
    [InlineKeyboardButton(text='Java', callback_data='jav')],
    [InlineKeyboardButton(text='JS', callback_data='js')],
    [InlineKeyboardButton(text='C#', callback_data='cs')],
    [InlineKeyboardButton(text='Меню 📊', callback_data='menu')]
]

inc_button = [
    [InlineKeyboardButton(text='Следующая вакансия', callback_data='next')],
    [InlineKeyboardButton(text='Меню 📊', callback_data='menu')],
]
