from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup)

def categories_buttons():
    inline_markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Category1😀", callback_data="category1")],
            [InlineKeyboardButton(text="Category2🥶", callback_data="category2")],
            [InlineKeyboardButton(text="Category3🤢", callback_data="category3")],
            [InlineKeyboardButton(text="Category4🤐", callback_data="category4")],
            [InlineKeyboardButton(text="Category5🤖", callback_data="category5")],
        ],
        resize_keyboard=True
    )

    return inline_markup


def admin_buttons():
    inline_markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Add product", callback_data="add")],
            [InlineKeyboardButton(text="View products", callback_data="viewProducts")],
            [InlineKeyboardButton(text="View users", callback_data="viewUsers")],
        ],
        resize_keyboard=True
    )

    return inline_markup