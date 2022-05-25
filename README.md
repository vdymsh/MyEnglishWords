# MyEnglishWords
Различные программки для поддержки англо-русского толкового словаря online 
и изучения английских слов.

Dict_2000_Spec.txt  - часть спецификации проекта, написанные 2 года назад 
MVP_Spec_20220522.txt - сегодняшнее видение спецификации проекта
GoogleAPI_Test.py - Тестовая утилита, работающая через API Google Translate
YandexAPI_Test.py, YandexTranslateKey.txt - Тестовая утилита, работающая через Yandex API и ключ к ней - 
											что-то в последний раз дала сделать только один или три пперевода и сказала - хватит.

JsonThesaurus.py - работа с толковым словарем английских слов из data\data.json
SQLiteThesaurusCreateTable.py, SQLiteThesaurusSelect.py - работа с тем же толковым словарем, переформатированным в Thesaurus.db (SQLite)
ReformatPostDjvu.py - утилита для приведения файла,сформированного из djvu в норм.вид. Подробное описание - в файле программы
WebsterTest.py - скачивает html страницу с нужным словом с сайта www.merriam-webster.com
CambridgeTest.py - скачивает html страницу с нужным словом с сайта dictionary.cambridge.org

Собственно, файлы проекта:
utilities.py
main.py
db_engine.py

all_english_words - база данных проекта (вне индекса)

Все данные и необработанные словари - в директории .\data
(вне git индекса)
