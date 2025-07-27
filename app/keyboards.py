from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


registr = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Зарегистрироваться', callback_data='registr')]
])


menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сотрудникам', callback_data='employy')],
    [InlineKeyboardButton(text='Кабинет администратора', callback_data='admin_cms')],
    [InlineKeyboardButton(text='Личный кабинет', callback_data='my_info')]
])


personal_panel = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Записать информации о работе', callback_data='record_info')],
    [InlineKeyboardButton(text='Мои последние записи', callback_data='my_records')],
    [InlineKeyboardButton(text='Назад в меню', callback_data='back_menu')]
])


admin_cms = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Информация о работе сотрудников', callback_data='work_info')],
    [InlineKeyboardButton(text='Информация о сотрудниках', callback_data='workers_data')],
    [InlineKeyboardButton(text='Назад в меню', callback_data='back_menu')]
])


my_info = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Изменить своё ФИО', callback_data='update_info'),
    InlineKeyboardButton(text='Последние записи', callback_data='last_records')],
    [InlineKeyboardButton(text='Назад в меню', callback_data='back_menu')]
])


re_data = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Вы измените своё ФИО', callback_data='change_fio')],
    [InlineKeyboardButton(text='Назад в меню', callback_data='back_menu')]
])


back_to_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Назад в меню', callback_data='back_menu')]
])
