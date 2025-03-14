import io
from aiogram import types
from aiogram import Router
from aiogram import Bot

from excel.excel import process_excel_file

document_router = Router()


@document_router.message()
async def document_handler(message: types.Message, bot: Bot):
    if message.document.mime_type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
        file_id = message.document.file_id
        file = await bot.get_file(file_id)
        
        file_content = await bot.download_file(file.file_path)
        
        excel_file = io.BytesIO(file_content.getvalue())

        await process_excel_file(excel_file)
        await message.reply("Файл успешно обработан!")
    else:
        await message.reply("Пожалуйста, отправьте файл в формате .xlsx.")

