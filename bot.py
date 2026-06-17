import asyncio
import logging
import json
import os
from datetime import datetime
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.enums import ParseMode
from aiohttp import web

# ================== КОНФИГУРАЦИЯ ==================
TOKEN = "8819100517:AAF_XspXD-2TgWx47wj3ha4c_kMD2bAtwdI"
ADMIN_ID = 925270750

# Файл для хранения подписчиков
SUBSCRIBERS_FILE = "subscribers.json"

# ================== ДАННЫЕ ОБ УЧРЕЖДЕНИИ ==================
ORG_INFO = {
    "name": "Центр цифрового образования детей «IT-куб»",
    "address": "г. Ростов-на-Дону, ул. Большая Садовая, 53",
    "email": "it-cube61@it-cube61.ru",
    "schedule": "Пн–пт: 09:00 – 18:00, Сб: 09:00 – 15:00",
    "director": "Буланов Дмитрий Павлович",
    "about": (
        "🏛 *Центр цифрового образования детей «IT-куб»*\n\n"
        "Создан в 2020 году в рамках национального проекта «Образование».\n"
        "👶 Возраст учеников: 8–18 лет\n\n"
        "📌 *Наши преимущества:*\n"
        "✅ Бесплатное обучение\n"
        "✅ Современное оборудование\n"
        "✅ Педагоги-практики\n"
        "✅ Участие в хакатонах и олимпиадах\n"
        "✅ Сертификаты государственного образца"
    )
}

# ================== НАПРАВЛЕНИЯ ОБУЧЕНИЯ ==================
DIRECTIONS = [
    {
        "name": "Пиктомир",
        "age": "для детей 6-7 лет",
        "description": "Бестекстовая цифровая образовательная среда «ПиктоМир», разработанная для погружения дошкольников и младших школьников в современное программирование"
    },
    {
        "name": "Разработка игр Kodu Game Lab",
        "age": "для детей 6-8 лет",
        "description": "Этот курс знакомит учащихся с основами создания 3D-игр в визуальной среде Kodu Game Lab — простом и удобном инструменте для начинающих гейм-дизайнеров."
    },
    {
        "name": "Основы конструирования",
        "age": "для детей 6-8 лет",
        "description": "Этот курс знакомит учащихся с базовыми принципами инженерного проектирования, механики и робототехники, развивая логическое мышление и техническую креативность."
    },
    {
        "name": "Основы компьютерной грамотности и безопасности",
        "age": "для детей 7-8 лет",
        "description": "Формирование базовых знаний при работе на компьютере и интернет-безопасности"
    },
    {
        "name": "Робототехника, Робоспорт, Спортивная робототехника",
        "age": "для детей 8-11 лет",
        "description": "Курс развивает логику и техническое мышление через сборку и программирование робототехнических моделей."
    },
    {
        "name": "Введение в программирование",
        "age": "для детей 10-12 лет",
        "description": "Базовые навыки программирования на Scratch подобных языках"
    },
    {
        "name": "Программирование на Scratch",
        "age": "для детей 11-13 лет",
        "description": "Курс предназначен для начинающих и детей, которые хотят освоить основы программирования в увлекательной визуальной среде."
    },
    {
        "name": "Компьютерная графика",
        "age": "для детей 11-13 лет",
        "description": "Программа рассчитана на детей, проявляющих интерес к современным компьютерным технологиям. Курс знакомит с основами создания и обработки цифровых изображений."
    },
    {
        "name": "3D - моделирование",
        "age": "для детей 11-13 лет",
        "description": "3D – моделирование одно из самых востребованных направлений IT – сферы. Метод трехмерного моделирования широко распространен в игровой индустрии, кино и анимации."
    },
    {
        "name": "Кибербезопасность",
        "age": "для детей 12-15 лет",
        "description": "Безопасность пользователей в цифровом пространстве"
    },
    {
        "name": "Введение в программирование на Python (базовый уровень)",
        "age": "для детей 13-16 лет",
        "description": "Изучение основ программирования на языке Python, развитие алгоритмического мышления учащихся и творческих способностей."
    },
    {
        "name": "Разработка VR/AR приложений",
        "age": "",
        "description": "Этот курс идеально подходит для тех, кто хочет погрузиться в увлекательный мир виртуальной и дополненной реальности."
    },
    {
        "name": "Основы программирования на Python",
        "age": "для детей 14-18 лет",
        "description": "По окончании полного курса обучения школьники будут иметь навыки, достаточные для работы младшим разработчиком или стажёром."
    },
    {
        "name": "Мобильная разработка Android приложений на языке Kotlin",
        "age": "для детей 14-18 лет",
        "description": "Разработка на языке Kotlin для платформы Android"
    },
    {
        "name": "C++, базовый курс",
        "age": "для детей 15-17 лет",
        "description": "Изучение основ программирования на C++ и работы с библиотекой SFML."
    },
    {
        "name": "Нейросети",
        "age": "для детей 13-17 лет",
        "description": "Основы применения искусственного интеллекта в повседневной жизни. Генерация текста, графики, иллюстраций, видео и аудио."
    },
    {
        "name": "Медиа-менеджмент (SMM)",
        "age": "для детей 13-17 лет",
        "description": "Создание текстового, визуального и видеоконтента для разных соцсетей. Основы работы с графическими редакторами."
    },
    {
        "name": "Web разработка (С кодом)",
        "age": "для детей 14-17 лет",
        "description": "Основы программирования на JavaScript и основы веб-верстки с помощью HTML и CSS."
    },
    {
        "name": "Web разработка (Без кода)",
        "age": "для детей 14-17 лет",
        "description": "Создание собственного сайта или лендинг страницы без необходимости знания программирования. Работа с конструктором Tilda."
    },
    {
        "name": "Работа с базами данных",
        "age": "для детей 14-17 лет",
        "description": "Изучение основ проектирования баз данных, построения ERD-диаграмм и работы с MySQL, освоение языка SQL."
    },
    {
        "name": "Азбука программирования",
        "age": "для детей 12-15 лет",
        "description": "Изучение основ цифрового проектирования в Figma и программирования на языках Python, C++ и Java."
    },
    {
        "name": "Основы программирования Java",
        "age": "для детей 14-17 лет",
        "description": "Изучение основ программирования на языке Java, освоение базовых алгоритмических конструкций и принципов объектно-ориентированного программирования."
    },
]

# ================== ПЕДАГОГИ (без опыта) ==================
TEACHERS = [
    {"name": "Дмитрий Буланов", "role": "педагог направлений «Основы программирования на Java», «Мобильная разработка на языке Kotlin», «Основы программирования на языке Python»", "photo": None},
    {"name": "Сергей Гергель", "role": "педагог направления «Киберспорт»", "photo": None},
    {"name": "Яна Горшколепова", "role": "педагог направлений «Основы компьютерной грамотности и безопасности», «Разработка игр Kodu Game Lab»", "photo": None},
    {"name": "Саидбек Давранбеков", "role": "педагог направления «Web-разработка с кодом»", "photo": None},
    {"name": "Максим Домрин", "role": "педагог направления «Кибербезопасность»", "photo": None},
    {"name": "Кирилл Засыпкин", "role": "педагог студии детского телевидения «ТелеРовесник»", "photo": None},
    {"name": "Владислав Каламбет", "role": "педагог направления «Web-разработка с кодом»", "photo": None},
    {"name": "Евгений Ковальцов", "role": "педагог направлений «Робототехника», «Робоспорт» и «Спортивная робототехника»", "photo": None},
    {"name": "Марина Крамаренко", "role": "педагог направлений «Введение в программирование», «Основы конструирования»", "photo": None},
    {"name": "Ксения Криводанова", "role": "педагог направлений «Основы программирования на Scratch», «Введение в программирование», «Основы программирования»", "photo": None},
    {"name": "Оксана Лагутина", "role": "педагог направления «Основы компьютерной грамотности и безопасности»", "photo": None},
    {"name": "Инна Ливанцова", "role": "педагог студии детского телевидения «ТелеРовесник»", "photo": None},
    {"name": "Егор Литвинов", "role": "педагог направлений «Введение в программирование», «Введение в программирование на Python»", "photo": None},
    {"name": "Илья Лошкарёв", "role": "педагог направления «Основы программирования на языке Python»", "photo": None},
    {"name": "Александр Меркулов", "role": "педагог направлений «Робототехника», «Основы компьютерной графики»", "photo": None},
    {"name": "Анна Носкова", "role": "педагог направления «C++»", "photo": None},
    {"name": "Владимир Обухов", "role": "педагог направления «Разработка VR/AR приложений»", "photo": None},
    {"name": "Мария Покровина", "role": "педагог направлений «Основы программирования Python», «Основы компьютерной графики»", "photo": None},
    {"name": "Роман Пошибайло", "role": "педагог направления «3-Д моделирование»", "photo": None},
    {"name": "Ольга Пусева", "role": "педагог направления «Основы промышленного программирования»", "photo": None},
    {"name": "Алия Уразгильдеева", "role": "педагог направления «Пиктомир»", "photo": None},
    {"name": "Камилла Уразгильдеева", "role": "педагог направлений «Медиа-менеджмент(SMM)», «Нейросети»", "photo": None},
    {"name": "Дарья Харина", "role": "педагог направления «Web-разработка без кода»", "photo": None},
]

# ================== РАСПИСАНИЕ ==================
SCHEDULE = {
    "monday": "09:00-11:00 - Спортивная робототехника\n16:00-18:00 – Спортивная робототехника\n18:00-20:00 - Спортивная робототехника\n14:00-16:00 - Основы программирования Scratch\n16:00-18:00 - Основы программирования Scratch\n18:00-20:00 - Мобильная разработка Android-приложений на Kotlin\n14:00-16:00 – Основы программирования Python\n16:00-18:00 – Основы программирования Python\n16:00-18:00 – Основы программирования на Java\n14:00-16:00 – Робототехника",
    "tuesday": "14:00-16:00 - Основы программирования Scratch\n14:00-16:00 – Основы программирования Python\n16:00-18:00 – Основы программирования Python",
    "wednesday": "09:00-11:00 - Разработка игр Kodu game lab\n14:00-16:00 - Разработка игр Kodu game lab\n16:00-18:00 - Разработка игр Kodu game lab\n09:00-11:00 – Спортивная робототехника\n15:00-17:00 – Нейросети\n17:00-19:00 – Нейросети\n15:00-17:00 - Основы программирования Scratch\n16:00-18:00 – Робототехника\n18:00-20:00 – Робототехника",
    "thursday": "16:00-18:00 - Кибербезопасность\n18:00-20:00 - Кибербезопасность\n09:00-11:00 - Разработка игр Kodu game lab\n14:00-16:00 – Основы конструирования\n16:00-18:00 – Основы конструирования\n15:00-17:00 – Медиа-менеджмент\n17:00-19:00 – Медиа-менеджмент\n18:00-20:00 - Мобильная разработка Android-приложений на Kotlin",
    "friday": "09:00-11:00 – Основы конструирования\n14:00-16:00 – Основы конструирования\n16:00-18:00 – Основы конструирования\n09:00-11:00 – Спортивная робототехника\n16:00-18:00 – Основы программирования Python\n18:00-20:00 – Основы программирования Python\n14:00-16:00 – Робототехника\n16:00-18:00 – Робототехника\n18:00-20:00 – Робототехника\n16:00-18:00 – Азбука программирования\n18:00-20:00 – Азбука программирования",
    "saturday": "10:00-12:00 – Основы программирования Python\n12:00-14:00 – Основы программирования Python\n12:00-14:00 – С++\n12:00-14:00 – С++\n16:00-18:00 – Основы компьютерной графики\n18:00-20:00 – Основы программирования Python\n10:00-12:00 – Основы компьютерной грамотности и безопасности\n12:00-14:00 – Основы компьютерной грамотности и безопасности\n14:00-16:00 – Основы компьютерной грамотности и безопасности\n16:00-18:00 – Основы компьютерной грамотности и безопасности\n10:00-12:00 – WEB-разработка (без кода)\n12:00-14:00 – WEB-разработка (без кода)\n10:00-12:00 – WEB-разработка (с кода)\n12:00-14:00 – WEB-разработка (с кода)",
    "sunday": "14:00-16:00 - Разработка игр Kodu game lab\n16:00-18:00 - Разработка игр Kodu game lab\n12:00-14:00 – С++\n12:00-14:00 – С++\n16:00-18:00 – Основы компьютерной графики\n18:00-20:00 – Основы программирования Python\n11:00-13:00 – Практика программирования Python\n13:00-15:00 – Практика программирования Python\n12:00-14:00 – Основы компьютерной грамотности и безопасности\n10:00-12:00 – WEB-разработка (без кода)\n12:00-14:00 – WEB-разработка (без кода)\n10:00-12:00 – WEB-разработка (с кода)\n12:00-14:00 – WEB-разработка (с кода)\n10:00-12:00 – Азбука программирования\n10:00-12:00 – Азбука программирования\n12:00-14:00 – Азбука программирования\n15:00-17:00 – База данных",
}

# ================== КЛАВИАТУРЫ ==================
def get_main_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🏛 Об учреждении", callback_data="about_org")],
        [InlineKeyboardButton(text="📚 Направления", callback_data="directions_list")],
        [InlineKeyboardButton(text="👨‍🏫 Педагоги", callback_data="teachers_list")],
        [InlineKeyboardButton(text="📅 Расписание", callback_data="schedule_today")],
        [InlineKeyboardButton(text="📞 Контакты", callback_data="contacts")],
        [InlineKeyboardButton(text="🔔 Уведомления", callback_data="toggle_subscribe")]
    ])

def get_directions_keyboard():
    kb = []
    for i, d in enumerate(DIRECTIONS):
        kb.append([InlineKeyboardButton(text=d["name"], callback_data=f"direction_{i}")])
    kb.append([InlineKeyboardButton(text="🔙 Назад", callback_data="back_main")])
    return InlineKeyboardMarkup(inline_keyboard=kb)

def get_teachers_keyboard():
    kb = []
    for i, t in enumerate(TEACHERS):
        kb.append([InlineKeyboardButton(text=t["name"], callback_data=f"teacher_{i}")])
    kb.append([InlineKeyboardButton(text="🔙 Назад", callback_data="back_main")])
    return InlineKeyboardMarkup(inline_keyboard=kb)

def get_schedule_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📅 Сегодня", callback_data="schedule_today")],
        [InlineKeyboardButton(text="📆 По дням недели", callback_data="schedule_week")],
        [InlineKeyboardButton(text="🔙 Назад", callback_data="back_main")]
    ])

def get_week_schedule_keyboard():
    days = {
        "monday": "Понедельник",
        "tuesday": "Вторник",
        "wednesday": "Среда",
        "thursday": "Четверг",
        "friday": "Пятница",
        "saturday": "Суббота",
        "sunday": "Воскресенье"
    }
    kb = []
    for key, name in days.items():
        kb.append([InlineKeyboardButton(text=name, callback_data=f"schedule_day_{key}")])
    kb.append([InlineKeyboardButton(text="🔙 Назад", callback_data="schedule_back")])
    return InlineKeyboardMarkup(inline_keyboard=kb)

# ================== РАБОТА С ПОДПИСЧИКАМИ ==================
def load_subscribers():
    if os.path.exists(SUBSCRIBERS_FILE):
        with open(SUBSCRIBERS_FILE, "r", encoding="utf-8") as f:
            return set(json.load(f))
    return set()

def save_subscribers():
    with open(SUBSCRIBERS_FILE, "w", encoding="utf-8") as f:
        json.dump(list(subscribers), f, ensure_ascii=False)

subscribers = load_subscribers()

# ================== ОБРАБОТЧИКИ ==================
bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    text = f"🚀 *Добро пожаловать в {ORG_INFO['name']}*\n\n📍 {ORG_INFO['address']}\n\nЯ виртуальный помощник. Выберите раздел:"
    await message.answer(text, parse_mode=ParseMode.MARKDOWN, reply_markup=get_main_keyboard())

@dp.callback_query(F.data == "about_org")
async def about_org(callback: types.CallbackQuery):
    text = ORG_INFO["about"]
    try:
        await callback.message.edit_text(text, parse_mode=ParseMode.MARKDOWN, reply_markup=get_main_keyboard())
    except Exception as e:
        if "message is not modified" not in str(e):
            raise e
    await callback.answer()

@dp.callback_query(F.data == "contacts")
async def contacts(callback: types.CallbackQuery):
    text = (
        f"📞 *Контакты*\n\n"
        f"📍 *Адрес:* {ORG_INFO['address']}\n"
        f"📅 *Режим работы:* {ORG_INFO['schedule']}\n"
        f"📧 *Email:* `{ORG_INFO['email']}`\n"
        f"👨‍🏫 *Руководитель:* {ORG_INFO['director']}\n\n"
        "🔗 *Сайт:* it-cube61.ru"
    )
    try:
        await callback.message.edit_text(text, parse_mode=ParseMode.MARKDOWN, reply_markup=get_main_keyboard())
    except Exception as e:
        if "message is not modified" not in str(e):
            raise e
    await callback.answer()

@dp.callback_query(F.data == "directions_list")
async def directions_list(callback: types.CallbackQuery):
    text = "📚 *Направления обучения:*\n\nВыберите направление для подробной информации:"
    try:
        await callback.message.edit_text(text, parse_mode=ParseMode.MARKDOWN, reply_markup=get_directions_keyboard())
    except Exception as e:
        if "message is not modified" not in str(e):
            raise e
    await callback.answer()

@dp.callback_query(F.data.startswith("direction_"))
async def direction_detail(callback: types.CallbackQuery):
    index = int(callback.data.split("_")[1])
    d = DIRECTIONS[index]
    text = f"*{d['name']}*\n\n👶 *Возраст:* {d['age']}\n\n📖 *Описание:*\n{d['description']}"
    try:
        await callback.message.edit_text(text, parse_mode=ParseMode.MARKDOWN, reply_markup=get_directions_keyboard())
    except Exception as e:
        if "message is not modified" not in str(e):
            raise e
    await callback.answer()

@dp.callback_query(F.data == "teachers_list")
async def teachers_list(callback: types.CallbackQuery):
    text = "👨‍🏫 *Наши педагоги:*\n\nВыберите преподавателя:"
    try:
        await callback.message.edit_text(text, parse_mode=ParseMode.MARKDOWN, reply_markup=get_teachers_keyboard())
    except Exception as e:
        if "message is not modified" not in str(e):
            raise e
    await callback.answer()

@dp.callback_query(F.data.startswith("teacher_"))
async def teacher_detail(callback: types.CallbackQuery):
    index = int(callback.data.split("_")[1])
    t = TEACHERS[index]
    text = f"👨‍🏫 *{t['name']}*\n\n📌 *Должность:* {t['role']}"
    try:
        await callback.message.edit_text(text, parse_mode=ParseMode.MARKDOWN, reply_markup=get_teachers_keyboard())
    except Exception as e:
        if "message is not modified" not in str(e):
            raise e
    await callback.answer()

@dp.callback_query(F.data == "schedule_today")
async def schedule_today(callback: types.CallbackQuery):
    today = datetime.now().strftime("%A").lower()
    today_rus = {"monday": "Понедельник", "tuesday": "Вторник", "wednesday": "Среда", "thursday": "Четверг", "friday": "Пятница", "saturday": "Суббота", "sunday": "Воскресенье"}.get(today, "Сегодня")
    schedule_text = SCHEDULE.get(today, "Расписания нет")
    text = f"📅 *{today_rus}*\n\n{schedule_text}"
    try:
        await callback.message.edit_text(text, parse_mode=ParseMode.MARKDOWN, reply_markup=get_schedule_keyboard())
    except Exception as e:
        if "message is not modified" not in str(e):
            raise e
    await callback.answer()

@dp.callback_query(F.data == "schedule_week")
async def schedule_week(callback: types.CallbackQuery):
    text = "📆 *Выберите день недели:*"
    try:
        await callback.message.edit_text(text, parse_mode=ParseMode.MARKDOWN, reply_markup=get_week_schedule_keyboard())
    except Exception as e:
        if "message is not modified" not in str(e):
            raise e
    await callback.answer()

@dp.callback_query(F.data.startswith("schedule_day_"))
async def schedule_day(callback: types.CallbackQuery):
    day_key = callback.data.split("_")[2]
    day_names = {"monday": "Понедельник", "tuesday": "Вторник", "wednesday": "Среда", "thursday": "Четверг", "friday": "Пятница", "saturday": "Суббота", "sunday": "Воскресенье"}
    day_name = day_names.get(day_key, "День")
    schedule_text = SCHEDULE.get(day_key, "Расписания нет")
    text = f"📅 *{day_name}*\n\n{schedule_text}"
    try:
        await callback.message.edit_text(text, parse_mode=ParseMode.MARKDOWN, reply_markup=get_week_schedule_keyboard())
    except Exception as e:
        if "message is not modified" not in str(e):
            raise e
    await callback.answer()

@dp.callback_query(F.data == "schedule_back")
async def schedule_back(callback: types.CallbackQuery):
    text = "📅 *Расписание занятий*\n\nВыберите действие:"
    try:
        await callback.message.edit_text(text, parse_mode=ParseMode.MARKDOWN, reply_markup=get_schedule_keyboard())
    except Exception as e:
        if "message is not modified" not in str(e):
            raise e
    await callback.answer()

@dp.callback_query(F.data == "toggle_subscribe")
async def toggle_subscribe(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    if user_id in subscribers:
        subscribers.remove(user_id)
        save_subscribers()
        status = "🔕 Вы отписались от уведомлений"
    else:
        subscribers.add(user_id)
        save_subscribers()
        status = "🔔 Вы подписались! Я буду присылать важные новости."
    await callback.answer(status, show_alert=True)

@dp.callback_query(F.data == "back_main")
async def back_main(callback: types.CallbackQuery):
    text = "🚀 *Главное меню*\n\nВыберите раздел:"
    try:
        await callback.message.edit_text(text, parse_mode=ParseMode.MARKDOWN, reply_markup=get_main_keyboard())
    except Exception as e:
        if "message is not modified" not in str(e):
            raise e
    await callback.answer()

# ================== ВЕБ-СЕРВЕР ДЛЯ RENDER ==================
async def health_check(request):
    return web.Response(text="Бот работает!")

# ================== ЗАПУСК ==================
async def main():
    logging.basicConfig(level=logging.INFO)
    
    app = web.Application()
    app.router.add_get('/', health_check)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', 10000)
    await site.start()
    print("✅ Веб-сервер запущен на порту 10000")
    
    print("✅ Бот IT-куба запущен!")
    print(f"👥 Подписчиков: {len(subscribers)}")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
