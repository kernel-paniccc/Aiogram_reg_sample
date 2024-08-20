from tg.database.models import async_main
from tg.handlers import router

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
import asyncio, os

load_dotenv()

async def main():
    await async_main()
    bot = Bot(token=os.getenv('TOKEN'))
    dp = Dispatcher()

    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':

    #logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass