from aiogram.utils.keyboard import InlineKeyboardBuilder


def way_to_list_of_food():
    builder = InlineKeyboardBuilder()
    builder.button(text='Еды', callback_data='foods')
    builder.adjust(1)
    return builder.as_markup()


def list_of_food():
    builder = InlineKeyboardBuilder()
    builder.button(text='Плов', callback_data='food_polov')
    builder.button(text='Манты', callback_data='food_manty')
    builder.button(text='Ханым', callback_data='food_hanym')
    builder.button(text='Самса с курицей', callback_data='food_samsa')
    builder.button(text='Машхурда', callback_data='food_mashhurda')
    builder.button(text='Шашлык', callback_data='food_shashlik')
    builder.adjust(3)
    return builder.as_markup()


def food_(food_name):
    builder = InlineKeyboardBuilder()
    builder.button(text='Рецепт', callback_data=f'recipe_of_{food_name}')
    return builder.as_markup()

