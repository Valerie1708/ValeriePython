import asyncio
import logging
import json
import os
from datetime import datetime
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, FSInputFile
from aiogram.enums import ParseMode

# ================== КОНФИГУРАЦИЯ ==================
TOKEN = "8819100517:AAF_XspXD-2TgWx47wj3ha4c_kMD2bAtwdI"  # Замените на ваш токен
ADMIN_ID = 925270750 # Замените на ваш Telegram ID (узнайте у @userinfobot)

# Файл для хранения подписчиков
SUBSCRIBERS_FILE = "subscribers.json"

# ================== ДАННЫЕ ОБ УЧРЕЖДЕНИИ ==================
ORG_INFO = {
    "name": "Центр цифрового образования детей «IT-куб»",
    "address": "г. Ростов-на-Дону, ул. Большая Садовая, 53",
    "phone": "+7 (988) 570-98-98",
    "email": "it-cube61@it-cube61.ru",
    "schedule": "Пн–пт: 09:00 – 18:00, Сб: 09:00 – 15:00",
    "director": "Софьянопуло Андрей Александрович",
    "about": (
        "🏛 *Центр цифрового образования «IT-куб»*\n\n"
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
        "name": "🐍 Программирование на Python",
        "age": "12–17 лет",
        "description": "Изучение основ алгоритмизации, работа с библиотеками, создание игр и веб-приложений. Подготовка к олимпиадам по программированию."
    },
    {
        "name": "📱 Мобильная разработка",
        "age": "13–18 лет",
        "description": "Разработка приложений для Android и iOS. Изучение языков Kotlin и Swift, создание полноценных мобильных продуктов."
    },
    {
        "name": "🥽 Разработка VR/AR-приложений",
        "age": "12–17 лет",
        "description": "Создание виртуальной и дополненной реальности. Работа с Unity, Blender, создание 3D-миров и интерактивных приложений."
    },
    {
        "name": "🤖 Программирование роботов",
        "age": "10–16 лет",
        "description": "Сборка и программирование роботов на Arduino и LEGO Mindstorms. Участие в соревнованиях по робототехнике."
    },
    {
        "name": "☕ Программирование на Java",
        "age": "13–18 лет",
        "description": "Изучение объектно-ориентированного программирования, создание серверных приложений, работа с базами данных."
    },
    {
        "name": "📊 Кибергигиена и большие данные",
        "age": "12–17 лет",
        "description": "Основы информационной безопасности, обработка больших данных, анализ информации, защита от киберугроз."
    }
]

# ================== ПЕДАГОГИ ==================
TEACHERS = [
    {
        "name": "Иванов Иван Иванович",
        "role": "Руководитель направления «Программирование»",
        "experience": "Опыт работы 10 лет. Кандидат технических наук. Победитель международных олимпиад.",
        "photo": None
    },
    {
        "name": "Петрова Мария Сергеевна",
        "role": "Преподаватель робототехники",
        "experience": "Инженер-робототехник. 5 лет работы с детьми. Победитель конкурса «Сердце отдаю детям».",
        "photo": None
    },
    {
        "name": "Сидоров Алексей Петрович",
        "role": "Преподаватель VR/AR-разработки",
        "experience": "Разработчик игр с 8-летним стажем. Эксперт по Unity и Unreal Engine.",
        "photo": None
    }
]

# ================== РАСПИСАНИЕ ==================
SCHEDULE = {
    "monday": "15:00 – Python (1 группа)\n16:00 – Робототехника",
    "tuesday": "15:00 – Java (1 группа)\n16:00 – VR/AR разработка",
    "wednesday": "15:00 – Python (2 группа)\n16:00 – Мобильная разработка",
    "thursday": "15:00 – Java (2 группа)\n16:00 – Кибергигиена",
    "friday": "15:00 – Робототехника\n16:00 – Python (1 группа)",
    "saturday": "10:00 – VR/AR разработка\n11:00 – Мобильная разработка",
    "sunday": "Выходной"
}

# ================== КЛАВИАТУРЫ ==================
def get_main_keyboard():
    """Главное меню"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🏛 Об учреждении", callback_data="about_org")],
        [InlineKeyboardButton(text="📚 Направления", callback_data="directions_list")],
        [InlineKeyboardButton(text="👨‍🏫 Педагоги", callback_data="teachers_list")],
        [InlineKeyboardButton(text="📅 Расписание", callback_data="schedule_today")],
        [InlineKeyboardButton(text="📞 Контакты", callback_data="contacts")],
        [InlineKeyboardButton(text="🔔 Уведомления", callback_data="toggle_subscribe")]
    ])

def get_directions_keyboard():
    """Клавиатура для списка направлений"""
    kb = []
    for i, d in enumerate(DIRECTIONS):
        kb.append([InlineKeyboardButton(text=d["name"], callback_data=f"direction_{i}")])
    kb.append([InlineKeyboardButton(text="🔙 Назад", callback_data="back_main")])
    return InlineKeyboardMarkup(inline_keyboard=kb)

def get_teachers_keyboard():
    """Клавиатура для списка педагогов"""
    kb = []
    for i, t in enumerate(TEACHERS):
        kb.append([InlineKeyboardButton(text=t["name"], callback_data=f"teacher_{i}")])
    kb.append([InlineKeyboardButton(text="🔙 Назад", callback_data="back_main")])
    return InlineKeyboardMarkup(inline_keyboard=kb)

def get_schedule_keyboard():
    """Клавиатура для расписания"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📅 Сегодня", callback_data="schedule_today")],
        [InlineKeyboardButton(text="📆 По дням недели", callback_data="schedule_week")],
        [InlineKeyboardButton(text="🔙 Назад", callback_data="back_main")]
    ])

def get_week_schedule_keyboard():
    """Клавиатура для выбора дня недели"""
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
    text = (
        f"🚀 *Добро пожаловать в {ORG_INFO['name']}*\n\n"
        f"📍 {ORG_INFO['address']}\n\n"
        f"Я виртуальный помощник. Выберите раздел:"
    )
    await message.answer(text, parse_mode=ParseMode.MARKDOWN, reply_markup=get_main_keyboard())

# ================== ОБ УЧРЕЖДЕНИИ ==================
@dp.callback_query(F.data == "about_org")
async def about_org(callback: types.CallbackQuery):
    text = ORG_INFO["about"]
    await callback.message.edit_text(text, parse_mode=ParseMode.MARKDOWN, reply_markup=get_main_keyboard())
    await callback.answer()

# ================== КОНТАКТЫ ==================
@dp.callback_query(F.data == "contacts")
async def contacts(callback: types.CallbackQuery):
    text = (
        f"📞 *Контакты*\n\n"
        f"📍 *Адрес:* {ORG_INFO['address']}\n"
        f"📅 *Режим работы:* {ORG_INFO['schedule']}\n"
        f"📧 *Email:* `{ORG_INFO['email']}`\n"
        f"📱 *Телефон:* `{ORG_INFO['phone']}`\n\n"
        f"👨‍🏫 *Руководитель:* {ORG_INFO['director']}\n\n"
        f"🔗 *Сайт:* it-cube61.ru"
    )
    await callback.message.edit_text(text, parse_mode=ParseMode.MARKDOWN, reply_markup=get_main_keyboard())
    await callback.answer()

# ================== НАПРАВЛЕНИЯ ==================
@dp.callback_query(F.data == "directions_list")
async def directions_list(callback: types.CallbackQuery):
    text = "📚 *Направления обучения:*\n\nВыберите направление для подробной информации:"
    await callback.message.edit_text(text, parse_mode=ParseMode.MARKDOWN, reply_markup=get_directions_keyboard())
    await callback.answer()

@dp.callback_query(F.data.startswith("direction_"))
async def direction_detail(callback: types.CallbackQuery):
    index = int(callback.data.split("_")[1])
    d = DIRECTIONS[index]
    text = (
        f"*{d['name']}*\n\n"
        f"👶 *Возраст:* {d['age']}\n\n"
        f"📖 *Описание:*\n{d['description']}"
    )
    await callback.message.edit_text(text, parse_mode=ParseMode.MARKDOWN, reply_markup=get_directions_keyboard())
    await callback.answer()

# ================== ПЕДАГОГИ ==================
@dp.callback_query(F.data == "teachers_list")
async def teachers_list(callback: types.CallbackQuery):
    text = "👨‍🏫 *Наши педагоги:*\n\nВыберите преподавателя:"
    await callback.message.edit_text(text, parse_mode=ParseMode.MARKDOWN, reply_markup=get_teachers_keyboard())
    await callback.answer()

@dp.callback_query(F.data.startswith("teacher_"))
async def teacher_detail(callback: types.CallbackQuery):
    index = int(callback.data.split("_")[1])
    t = TEACHERS[index]
    text = (
        f"👨‍🏫 *{t['name']}*\n\n"
        f"📌 *Должность:* {t['role']}\n\n"
        f"📋 *Опыт:*\n{t['experience']}"
    )
    
    if t["photo"] and os.path.exists(t["photo"]):
        photo = FSInputFile(t["photo"])
        await callback.message.delete()
        await callback.message.answer_photo(photo, caption=text, parse_mode=ParseMode.MARKDOWN, reply_markup=get_teachers_keyboard())
    else:
        await callback.message.edit_text(text, parse_mode=ParseMode.MARKDOWN, reply_markup=get_teachers_keyboard())
    await callback.answer()

# ================== РАСПИСАНИЕ ==================
@dp.callback_query(F.data == "schedule_today")
async def schedule_today(callback: types.CallbackQuery):
    today = datetime.now().strftime("%A").lower()
    today_rus = {
        "monday": "Понедельник",
        "tuesday": "Вторник",
        "wednesday": "Среда",
        "thursday": "Четверг",
        "friday": "Пятница",
        "saturday": "Суббота",
        "sunday": "Воскресенье"
    }.get(today, "Сегодня")
    
    schedule_text = SCHEDULE.get(today, "Расписания нет")
    text = f"📅 *{today_rus}*\n\n{schedule_text}"
    
    await callback.message.edit_text(text, parse_mode=ParseMode.MARKDOWN, reply_markup=get_schedule_keyboard())
    await callback.answer()

@dp.callback_query(F.data == "schedule_week")
async def schedule_week(callback: types.CallbackQuery):
    text = "📆 *Выберите день недели:*"
    await callback.message.edit_text(text, parse_mode=ParseMode.MARKDOWN, reply_markup=get_week_schedule_keyboard())
    await callback.answer()

@dp.callback_query(F.data.startswith("schedule_day_"))
async def schedule_day(callback: types.CallbackQuery):
    day_key = callback.data.split("_")[2]
    day_names = {
        "monday": "Понедельник",
        "tuesday": "Вторник",
        "wednesday": "Среда",
        "thursday": "Четверг",
        "friday": "Пятница",
        "saturday": "Суббота",
        "sunday": "Воскресенье"
    }
    day_name = day_names.get(day_key, "День")
    schedule_text = SCHEDULE.get(day_key, "Расписания нет")
    
    text = f"📅 *{day_name}*\n\n{schedule_text}"
    await callback.message.edit_text(text, parse_mode=ParseMode.MARKDOWN, reply_markup=get_week_schedule_keyboard())
    await callback.answer()

@dp.callback_query(F.data == "schedule_back")
async def schedule_back(callback: types.CallbackQuery):
    text = "📅 *Расписание занятий*\n\nВыберите действие:"
    await callback.message.edit_text(text, parse_mode=ParseMode.MARKDOWN, reply_markup=get_schedule_keyboard())
    await callback.answer()

# ================== ПОДПИСКА ==================
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

# ================== НАЗАД ==================
@dp.callback_query(F.data == "back_main")
async def back_main(callback: types.CallbackQuery):
    text = "🚀 *Главное меню*\n\nВыберите раздел:"
    await callback.message.edit_text(text, parse_mode=ParseMode.MARKDOWN, reply_markup=get_main_keyboard())
    await callback.answer()

# ================== ЗАПУСК ==================
async def main():
    logging.basicConfig(level=logging.INFO)
    print("✅ Бот IT-куба запущен!")
    print(f"👥 Подписчиков: {len(subscribers)}")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())