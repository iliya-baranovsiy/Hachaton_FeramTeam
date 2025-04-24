from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher
from handlers import router
import asyncio
from load_conf import TOKEN


async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(router)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    asyncio.run(main())
