import os
import asyncio
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from app.handlers import router  # Импорт роутера с обработчиками
from app.database.models import async_main  # Импорт функции инициализации БД


# 1. Загрузка конфигурации
async def main():
    load_dotenv()
    await async_main()
    bot = Bot(token=os.getenv('TOKEN'))
    dp = Dispatcher()
    dp.include_router(router)
    try:
        # 4. Запуск бота в режиме поллинга
        print("Бот запущен!")
        await dp.start_polling(bot)
    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        # Корректное закрытие сессии при завершении
        await bot.session.close()
        print("Бот остановлен")



if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Принудительное завершение работы")


