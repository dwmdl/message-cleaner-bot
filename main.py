import asyncio
import logging
import config
from aiogram import Bot, Dispatcher, types

bot = Bot(token=config.API_TOKEN)
dp = Dispatcher()


@dp.message()
async def delete_message(message: types.Message):
    if any([
        message.new_chat_members,
        message.new_chat_photo,
        message.new_chat_title,
        message.left_chat_member,
        message.delete_chat_photo,
        message.video_chat_ended,
        message.video_chat_started,
        message.pinned_message
    ]):
        await message.delete()


async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

# requirements
