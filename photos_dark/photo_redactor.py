#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont
import os


def text(our_list, our_number):
    """Функция которая перебирает текст и делает отступы"""
    text = ""
    count = 80
    for number, letter in enumerate(our_list[our_number]):
       text += our_list[our_number][number]
       if number == count:
           text += "\n"
           count += 80
    return text.replace("&ndash;", "").replace("&nbsp;", "")


def abs_path(name):
    """Функция формирует абсолютный путь к фотографиям"""
    abs_path = os.path.abspath(os.path.join("photos_dark/", name))
    return abs_path


def image_redactor(abs_path, file_name, data, size):
    """Функция которая накладывает текст на картинку"""
    image = Image.open(abs_path(f"{file_name}.jpeg"))
    font = ImageFont.truetype(abs_path("unutterable.ttf"), size=size)
    draw = ImageDraw.Draw(image)
    indent = 40
    for i in range(len(data)):
        draw.text((40, indent), text(data, i), font=font, fill="yellow")
        indent += ((len(data[i]) // 80) + 1) * 26
    return image.save(f"photo_with_text/{file_name}.jpeg")
