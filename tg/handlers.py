from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.enums import ParseMode

from tg.database.models import async_session
from tg.database.models import User
from sqlalchemy import select
from dotenv import load_dotenv

from tg.keyboards import main



class Registration(StatesGroup):
    password = State()

class Reset(StatesGroup):
    password = State()


load_dotenv()
router = Router()

@router.message(CommandStart())
async def start(message: Message):
    await message.reply("HI, this test reg bot", reply_markup=main)


#     __registration__
@router.message(F.text.lower() == 'reg')
async def start(message: Message, state: FSMContext):
    tg_id = message.from_user.id
    async with async_session() as session:
        id = await session.scalar(select(User).where(User.tg_id == tg_id))
        if not id:
            await message.answer('Send me the password:')
            await state.set_state(Registration.password)
        else:
            await message.answer(f'you are already registered!', reply_markup=main)
            await state.clear()

@router.message(Registration.password)
async def register2(message: Message, state: FSMContext):
    password = message.text
    tg_id = message.from_user.id
    async with async_session() as session:
        id = await session.scalar(select(User).where(User.tg_id == tg_id))
        if not id:
            session.add(User(tg_id=tg_id, password=password))
            await session.commit()
            await message.answer('you are successfully registered ! 🎉', reply_markup=main)
            await state.clear()
        if id:
            await message.answer("you are already registered !", reply_markup=main)
            await state.clear()


@router.message()
async def echo(messange: Message):
    await messange.answer('I dont understand you', reply_markup=main)
