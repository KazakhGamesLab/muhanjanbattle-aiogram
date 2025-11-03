from aiogram.fsm.context import FSMContext
from states.states import UserRegistration
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from api.api_client import post_user
from muhanjanbattle_models.user import UserCreate
from aiogram import Router
router = Router()

@router.message(UserRegistration.waiting_for_twitch_nickname)
async def handle_twitch_nick(message: Message, state: FSMContext) -> None:

    user_data = UserCreate(
        telegram_id=message.from_user.id,
        twitch_nickname=message.text.strip(),
        first_name=message.from_user.first_name,
        telegram_username=message.from_user.username or 'Неизвестный'
    )
    print(await post_user(user_data))

    await state.clear()
    await message.answer("Регистрация завершена!")