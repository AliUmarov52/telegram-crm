from aiogram.fsm.state import State, StatesGroup


# Регистрация пользователя
class Registration(StatesGroup):
    tg_id = State()
    name = State()


# Запрос пароля для входа в панель администратора
class AdminPassword(StatesGroup):
    password = State()  


# Реализация повторной записи своего ФИО
class NewFio(StatesGroup):
    name = State() 
    