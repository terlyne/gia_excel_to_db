from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

start_router = Router()


@start_router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("Привет! Пришлите нам документ в формате .xlsx для дальнейшей обработки.")