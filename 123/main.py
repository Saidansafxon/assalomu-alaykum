# import asyncio
# from aiogram import Bot, Dispatcher, Router, F
# from aiogram.types import Message, CallbackQuery
# from aiogram.filters import Command,CommandStart
# from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
# from aiogram.fsm.state import State,StatesGroup
# from aiogram.fsm.context import FSMContext
# from aiogram.fsm.storage.memory import MemoryStorage

# TOKEN="8286493693:AAE6P4YjQZvHLiQB9FGArZXsYWp848sGSAo"
# bot=Bot(token=TOKEN)
# dp=Dispatcher(storage=MemoryStorage())

# inlinne_button=InlineKeyboardMarkup(
#     inline_keyboard=[
#         [InlineKeyboardButton(text="Ro'yxatdan o'tish",callback_data="sa")]
#     ]
# )

# class RegisterState(StatesGroup):
#     name=State()
#     surename=State()
#     age=State()

# @dp.message(CommandStart())
# async def start_handler(msg:Message):
#     await msg.answer("Assalomu Alaykum, o'yin o'ynash uchun ro'yxatdan o'tishingiz kerak.",reply_markup=inlinne_button)

# @dp.callback_query(F.data=="sa")
# async def register(call:CallbackQuery,state:FSMContext):
#     await call.message.answer("Ismingiz kiriting:")
#     await state.set_state(RegisterState.name)
#     await call.answer()

# @dp.message(RegisterState.name)
# async def register(msg:Message,state:FSMContext):
#     await state.update_data(name=msg.text)
#     await msg.answer("Familyangizni kiriting:")
#     await state.set_state(RegisterState.surename)

# @dp.message(RegisterState.surename)
# async def register(msg:Message,state:FSMContext):
#     await state.update_data(surename=msg.text)
#     await msg.answer("Yoshingizni kiriting:")
#     await state.set_state(RegisterState.age)

# @dp.message(RegisterState.age)
# async def register(msg:Message,state:FSMContext):
#     await state.update_data(age=msg.text)
#     data=await state.get_data()
#     await msg.answer(f"ro'yxatdan otdingiz  ↓ \nIsmingiz: {data["name"]} \nFamilyangiz: {data["surename"]} \nYoshingiz: {data["age"]}")
#     await state.clear()

# async def main():
#     print("Bot is start...")
#     await dp.start_polling(bot)

# if __name__=="__main__":
#     asyncio.run(main())




# import asyncio
# from aiogram import Bot, Dispatcher, Router, F
# from aiogram.types import Message, CallbackQuery
# from aiogram.filters import Command,CommandStart
# from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
# from aiogram.fsm.state import State,StatesGroup
# from aiogram.fsm.context import FSMContext
# from aiogram.fsm.storage.memory import MemoryStorage

# TOKEN="8286493693:AAE6P4YjQZvHLiQB9FGArZXsYWp848sGSAo"
# bot=Bot(token=TOKEN)
# dp=Dispatcher(storage=MemoryStorage())

# inlinne_button=InlineKeyboardMarkup(
#     inline_keyboard=[
#         [InlineKeyboardButton(text="Ro'yxatdan o'tish",callback_data="sa1")]
#     ]
# )

# class RegisterState(StatesGroup):
#     name=State()
#     tugilgan_kuningiz=State()
#     number=State()
#     email=State()
#     familiya=State()
#     parol=State()
#     rasm=State()

# @dp.message(CommandStart())
# async def start_handler(msg:Message):
#     await msg.answer("Assalomu Alaykum, ro'yxatdan o'ting!",reply_markup=inlinne_button)


# @dp.callback_query(F.data=="sa1")
# async def register(call:CallbackQuery,state:FSMContext):
#     await call.message.answer("Ismingiz kiriting:")
#     await state.set_state(RegisterState.name)
#     await call.answer()

# @dp.message(RegisterState.name)
# async def register(msg:Message,state:FSMContext):
#     await state.update_data(name=msg.text)
#     await msg.answer("Tugilgan kuningizni kiriting:")
#     await state.set_state(RegisterState.tugilgan_kuningiz)

# @dp.message(RegisterState.tugilgan_kuningiz)
# async def register(msg:Message,state:FSMContext):
#     await state.update_data(tugilgan_kuningiz=msg.text)
#     await msg.answer("Telefon raqamingizni kiriting:")
#     await state.set_state(RegisterState.number)

# @dp.message(RegisterState.number)
# async def register(msg:Message,state:FSMContext):
#     await state.update_data(number=msg.text)
#     await msg.answer("Email ingizni kiriting:")
#     await state.set_state(RegisterState.email)

# @dp.message(RegisterState.email)
# async def register(msg:Message,state:FSMContext):
#     await state.update_data(email=msg.text)
#     await msg.answer("Familiyangizni kiriting:")
#     await state.set_state(RegisterState.familiya)

# @dp.message(RegisterState.familiya)
# async def register(msg:Message,state:FSMContext):
#     await state.update_data(familiya=msg.text)
#     await msg.answer("Parolingizni kiriting:")
#     await state.set_state(RegisterState.parol)
#     data=await state.get_data()
#     await msg.answer(f"ro'yxatdan otdingiz  ↓ \nIsmingiz: {data["name"]} \nTugilgan kuningiz: {data["tugilgan_kuningiz"]} \nRaqamingiz: {data["number"]} \nEmail ingiz: {data("email")} \nFamiliyangiz: {data("familiya")} \nParolingiz: {data("parol")}")
#     await state.clear()

# async def main():
#     print("Bot is start...")
#     await dp.start_polling(bot)

# if __name__=="__main__":
#     asyncio.run(main())



import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

sa = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Ish joyi kerak")],
        [KeyboardButton(text="Hodim kerak")]
    ],
    resize_keyboard=True
)

TOKEN="8286493693:AAE6P4YjQZvHLiQB9FGArZXsYWp848sGSAo"
bot=Bot(token=TOKEN)
dp=Dispatcher()

@dp.message(CommandStart())
async def start_handler(msg:Message):
    await msg.answer("Assalomu Alaykum", reply_markup=sa)

@dp.message(F.text=="Ish joyi kerak")
async def answer(msg:Message):
    await msg.answer("Ish joyi kerak bo'lsa meni saytimga kiring: saidansaf_ish_joylari.com")

@dp.message(F.text=="Hodim kerak")
async def answer(msg:Message):
    await msg.answer("Hodim kerak bo'lsa meni saytimga kiring: saidansaf_hodim_kerak.com")

async def main():
    print("Bot is start...")
    await dp.start_polling(bot)

if __name__=="__main__":
    asyncio.run(main())
