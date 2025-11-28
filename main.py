from aiogram import Bot, Dispatcher, F
from aiogram.types import Message,InlineKeyboardMarkup,InlineKeyboardButton,CallbackQuery
from aiogram.filters import CommandStart
import asyncio
from handler.valutahandler import v_router


bot = Bot("7658436594:AAH5xtn5fQvh02V8Fb9EtTe6oFjmZzGBQ4Q")
dp = Dispatcher()


@dp.message(CommandStart())
async def start_handle(message: Message):
    key_board=InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🇺🇸USD", callback_data="kurs_usd"),InlineKeyboardButton(text="🇦🇿AZN", callback_data="kurs_azn")],
        [InlineKeyboardButton(text="🇷🇺RUB", callback_data="kurs_rub"),InlineKeyboardButton(text="🇧🇩BDT", callback_data="_kurs_bdt")],
        [InlineKeyboardButton(text="🇪🇺EUR", callback_data="kurs_eur"),InlineKeyboardButton(text="🇧🇬BGN", callback_data="kurs_bgn")],
        [InlineKeyboardButton(text="🇬🇧GBP", callback_data="kurs_gbp"),InlineKeyboardButton(text="🇧🇭BHD", callback_data="kurs_bhd")],
        [InlineKeyboardButton(text="🇯🇵JPY", callback_data="kurs_jpy"),InlineKeyboardButton(text="🇧🇳BND", callback_data="kurs_bnd")]
    ]
    
    )
    await message.answer("Assalomu alaykum , Botimizga Xush kelibsiz.\nValuyta tanlang",reply_markup=key_board)




async def main():
 print("bot ishga tushdi")
 dp.include_router(v_router)
 await dp.start_polling(bot)

asyncio.run(main())