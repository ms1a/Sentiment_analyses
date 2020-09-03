# Модуль для диалогового окна
from tkinter import filedialog as fd
# Модуль os предоставляет множество функций для работы с операционной системой
import os


# send_words функция для того чтобы разделить строку на слова
def send_words(dict,list_text):
  # список перебирается по словам
  for word in list_text:
    sentiment(dict,word)
# separation_text - Функция для приведения проверяемого текста к виду без лишних символов и разделенному на элементы списка
def separation_text(file_text):
  # Функция replace() возвращает копию строки, в которой вхождение старой подстроки old
  # будет заменено новой подстрокой new. эта функция применена к нашему тексту
  text = file_text.read()
  # заменяем лишние символы на пробел
  text = text.replace(',', ' ')
  text = text.replace('.', ' ')
  text = text.replace(':', ' ')
  # split
  list_text = text.split()
  # Возвращает наш list_text
  return list_text
# ищет слово в словаре и изменяет общую оценку проверяемого текста
def sentiment(dictionary,word):
  # объявляем senti и counter глобальными переменными
  global senti,counter
  # ограничиваем слово ';'
  word = word + ';'
  # словарь перебирается по строкам
  for line in dictionary:
    # запускается условие
    # слово начинается нулевого значения, поиск первого вхождения
    if line.find(word) == 0:
      # counter + 1, прибавляет одно значение
      counter +=1
      # split разделяет наш список знаком ;
      list = line.split(';')
      # в словаре ищет 3 индекс
      senti_word = int(list[3])
      # условие если слово равно 1
      if senti_word == 1:
        # то senti записывает senti + 1
        senti += 1
        # условие если сенти равно -1
      elif senti_word == -1:
        # то senti записывает senti - 1
        senti -= 1
        # остановка
      break
# просто возвращает текстовый результат.
def status():
  # объявление глобальной senti
  global senti
  # создается условие
  # если senti положительная то позитивный
  if senti > 0:
    resault = "Positive"
    # если senti равен 0 то нейтральный
  elif senti == 0:
    resault = "Neutral"
    # если senti отрицательный то негативный
  else:
    resault = "Negative"
    # возвращение результата
  return resault
# Функция для того чтобы выбрать фаил в диалоговом окне в ручную.
def open_file():
  # диалоговое окно для открытия файла
  file_name = fd.askopenfilename()
  # открытие самого файла, чтение, кодировка utf-8
  file_text = open(file_name, 'r', encoding='utf-8')
  # возращает file_text
  return file_text

# переменная file_text открывает функцию open.file()
file_text = open_file()
# переменная file_list открывает функцию separation_text(file_text), нарезка текста
list_text = separation_text(file_text)
print('the text contains: ',len(list_text),'words')
# считываем список файлов в папке lib,формируется список имен фаилов
dict_list = os.listdir(path="lib")
# Цикл перебирает словари из списка словарей, и запускает проверку текста. формирует результат по конкретному словарю
for dict_name in dict_list:
  #обявляем
  senti = 0
  counter = 0
  # dict_fail
  dict_fail = open("lib\\" + dict_name, 'r', encoding='utf-8')
  try:
    # формируется список построчно из фаила
    dict = dict_fail.readlines()
  except:
    dict_fail = open("lib\\" + dict_name)
    dict = dict_fail.readlines()
  send_words(dict, list_text)
  my_other_dict = {'newemo.txt': 1, 'rusentilex_2017.txt': 2, 'words_all_full_rating.csv': 3
  }
  print('In the dictionary: ',dict_name,'Words found: ',counter)
  print('sentimental your text:',status())