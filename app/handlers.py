from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

import app.keyboards as kb
from app.database.requests import set_user, get_user_by_tg_id
from utils.states import Registration, AdminPassword, NewFio


router = Router()


# Команда ./start 
@router.message(CommandStart())
async def start(message: Message):
    await message.answer("Добро пожаловать в корпоративный чат-бот КРОНЫ\nПеред началом пройди регистрацию:",
                         reply_markup=kb.registr)
    

# Реализация кнопки зарегистрироваться
@router.callback_query(F.data == 'registr')
async def start_registration(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Registration.name)
    await callback.message.answer("Введите своё ФИО:")
    await callback.answer()


# Обработка введенного ФИО и сохранение в БД
@router.message(Registration.name)
async def process_name(message: Message, state: FSMContext):
    """Обработка введенного ФИО"""
    try:
        user = await set_user(
            tg_id=message.from_user.id,
            name=message.text
        )
        await state.clear()
        await message.answer(
            f"Регистрация завершена, {user.name}!",
            reply_markup=kb.menu)
    except Exception as e:
        await message.answer("Ошибка при сохранении данных. Попробуйте позже.")
        print(f"Ошибка регистрации: {e}")



# Кнопка вернуться назад в меню
@router.callback_query(F.data == 'back_menu')
async def back_menu(callback: CallbackQuery):
    await callback.message.edit_text("Вернул вас назад в главное меню, выбирайте нужную функцию:)",
                                     reply_markup=kb.menu)
    

# Реализация личного кабинета сотрудника
@router.callback_query(F.data == 'employy')
async def worker_panel(callback: CallbackQuery):
    await callback.message.edit_text("Вы вошли в панель сотрудника, выберите функции ниже",
                                     reply_markup=kb.personal_panel)
    

# Реализация входа в админ панель 
@router.callback_query(F.data == 'admin_cms')
async def adminlog(callback: CallbackQuery, state: FSMContext):
    await state.set_state(AdminPassword.password)
    await callback.message.answer("Введите пароль для входа в админ панель")
    await callback.answer()


# Обработчик ввода и проверки пароля
@router.message(AdminPassword.password)
async def check_admin_password(message: Message, state: FSMContext):
    ADMIN_PASSWORD = "12345"  # Пароль администратора
    
    if message.text == ADMIN_PASSWORD:
        await message.answer(
            "Вы успешно вошли в панель администратора.\n"
            "Вы можете посмотреть информацию о работе сотрудников, а также их контактные данные",
            reply_markup=kb.admin_cms
        )
        await state.clear()  # Очищаем состояние
    else:
        await message.answer("Неверный пароль. Попробуйте еще раз.")
        

# Реализация кнопки входа в личный кабинет
@router.callback_query(F.data == 'my_info')
async def myinfo(callback: CallbackQuery):
    user = await get_user_by_tg_id(callback.from_user.id)
    
    if not user:
        await callback.answer("Вы не зарегистрированы!", show_alert=True)
        return

    text = (
        "📌 Личный кабинет:\n"
        f"• ID: {user.tg_id}\n"
        f"• ФИО: {user.name}\n\n"
        "Для изменения данных используйте кнопки ниже"
    )
    
    await callback.message.edit_text(text, reply_markup=kb.my_info)


# Реализация кнопки информация о работе сотрудников
@router.callback_query(F.data == 'workers_data')
async def AboutWorkers(callback: CallbackQuery):
    pass


# Реализация кнопки изменить данные
@router.callback_query(F.data == "update_info")
async def UpdateInfo(callback: CallbackQuery):
    await callback.message.edit_text('Вы можете изменить своё ФИО и/или добавить свои контактные данные',
                                     reply_markup=kb.re_data)
    

# Реализация кнопки изменить фио
@router.callback_query(F.data == "change_fio")
async def change_fio(callback: CallbackQuery, state: FSMContext):
    user = await get_user_by_tg_id(callback.from_user.id)

    await state.set_state(NewFio.name)
    await callback.message.edit_text(
        f"✏️ {user.name}, введите своё изменённое ФИО:",
        reply_markup=kb.back_to_menu
    )


# Фиксация и запись в личный кабинет нового ФИО
@router.message(NewFio.name)
async def process_new_fio(message: Message, state: FSMContext):
    try:
        user = await set_user(
            tg_id=message.from_user.id,
            name=message.text
        )
        await state.clear()
        await message.answer(
            f"✅ Вы обновили своё ФИО, теперь вы: {user.name}",
            reply_markup=kb.menu
        )
    except Exception as e:
        await message.answer("❌ Ошибка при сохранении")
        print(f"Ошибка обновления ФИО: {e}")

