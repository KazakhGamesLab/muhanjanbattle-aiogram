from states.states import UserRegistration
from aiogram.types import Message
from aiogram.fsm.context import FSMContext


async def register_user(message: Message, state: FSMContext) -> None:
    await message.answer("Пожалуйста, введите ваш Twitch-никнейм:")
    await state.set_state(UserRegistration.waiting_for_twitch_nickname)
