from .kursapi import get_valuta
from aiogram import Router
from aiogram.types import Message,InlineKeyboardButton,InlineKeyboardMarkup,CallbackQuery
from aiogram import F
from aiogram.filters import Command




v_router=Router()

@v_router.callback_query(F.data.startswith("kurs_"))
async def kurs(callback_quary:CallbackQuery):
    valuta=callback_quary.data.split("_")[1]
    data= await get_valuta(valuta)
    text=f"\n🇺🇿 O'zbekiston Respublikasida\n{data[0]["CcyNm_UZ"]} kursi Quydagicha\n\n💱Valuta : {data[0]["Ccy"]} / {data[0]["CcyNm_UZ"]}\n🇺🇿Uzbek Kursi : {data[0]["Rate"]}\n📅Sana : {data[0]["Date"]}\n"
    
    buttn=InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Orqaga",callback_data="back")]
    ]
    )
    await callback_quary.message.answer(text,reply_markup=buttn)
    
    
    

@v_router.callback_query(F.data=="back")
async def back_handler(callback_quary:CallbackQuery):
     key_board=InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🇺🇸USD", callback_data="kurs_usd"),InlineKeyboardButton(text="🇦🇿AZN", callback_data="kurs_azn")],
        [InlineKeyboardButton(text="🇷🇺RUB", callback_data="kurs_rub"),InlineKeyboardButton(text="🇧🇩BDT", callback_data="_kurs_bdt")],
        [InlineKeyboardButton(text="🇪🇺EUR", callback_data="kurs_eur"),InlineKeyboardButton(text="🇧🇬BGN", callback_data="kurs_bgn")],
        [InlineKeyboardButton(text="🇬🇧GBP", callback_data="kurs_gbp"),InlineKeyboardButton(text="🇧🇭BHD", callback_data="kurs_bhd")],
        [InlineKeyboardButton(text="🇯🇵JPY", callback_data="kurs_jpy"),InlineKeyboardButton(text="🇧🇳BND", callback_data="kurs_bnd")]
    ]
    
    )
    
     
     await callback_quary.message.answer(" Qayta Valuyta Tanlang : ",reply_markup=key_board)

    



