!pip install transformers sentencepiece

from transformers import pipeline

translator = pipeline("translation_ru_to_fr", "Helsinki-NLP/opus-mt-ru-fr")

translator("Меня зовут Анастасия, я живу в Москве")

