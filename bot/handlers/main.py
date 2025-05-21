from aiogram import types, Bot
from bot.buttons.inline_keyboard.foods import way_to_list_of_food, list_of_food, food_
from bot.recipes import recipes


async def start(message: types.Message):
    await message.answer('Здравствуйте.', reply_markup=way_to_list_of_food())


async def foods(query: types.CallbackQuery, bot: Bot):
    await bot.edit_message_text(
        text='Выберите блюдо', chat_id=query.message.chat.id,
        message_id=query.message.message_id, reply_markup=list_of_food()
    )


async def food(query: types.CallbackQuery, bot: Bot):
    food_name = query.data.split('_')[-1]
    photo = types.FSInputFile('media/' + food_name + '.png')
    await bot.delete_message(query.message.chat.id, query.message.message_id)
    await bot.send_photo(
        chat_id=query.message.chat.id, photo=photo,
        reply_markup=food_(food_name)
    )


async def recipe_of_food(query: types.CallbackQuery, bot: Bot):
    food_name = query.data.split('_')[-1]
    await bot.delete_message(query.message.chat.id, query.message.message_id)
    await bot.send_message(
        chat_id=query.message.chat.id, text=recipes[food_name],
        reply_markup=way_to_list_of_food()
    )



