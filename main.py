import asyncio
import logging
from aiogram import Bot
from aiogram import Dispatcher
from aiogram import Router

from config import settings
from handlers.document import document_router
from handlers.start import start_router


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


bot = Bot(settings.BOT_TOKEN)
dp = Dispatcher()

async def main():
    router = Router()
    
    router.include_router(start_router)
    router.include_router(document_router)

    dp.include_router(router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
