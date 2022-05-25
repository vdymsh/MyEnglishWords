"""
Reformat file exported into text from .djvu file(s), and having a special format such as
d:\English\Books\Английский клуб\0. Beginner\Andersen H.C.- The Snow Queen.djvu
into readable text file.
1) Format into 72-symbol line
2) Exclude comments and exsercises
3) Format into paragraphs if possible

Old file: AndersenTheSnowQueenDjvu.txt
New file: AndersenTheSnowQueen.txt
Directory: .\data
"""

# Исходный текст содержит ненужные части - словари, упражнения, а также состоит из коротеньких строк.
# Программа выделяет из исходного текста только содержательную часть, разбитую по главам,
# находящимся между номером главы, начинающимся со слова STORY и окончанием главы, за которым
# следуте слово "Helpful". Весь текст заканчивается там, где встречается слово "Vocabulary"
#
# Далее для каждой главы исходный текст считывается построчно, и далее формируются параграфы
# нового текста. Длина строки нового текста не превышает MAX_LEN. Параграф формируется до
# тех пор, пока в конце строки не встретится знак .?! и при этом количество слов во вновь
# формируемом параграфе должно быть не менее MIN_PARAGRAPH.


def main():
    try:
        fin = open(r"data\AndersenTheSnowQueenDjvu.txt", 'r', encoding="utf-8")
        fout = open(r"data\AndersenTheSnowQueen.txt", 'w', encoding="utf-8")
        good_line = False
        lines = fin.readlines()

        MAX_LEN = 72        # максимальная длина строки
        MIN_PARAGRAPH = 33  # минимальное количество слов в параграфе

        chunk = []          # набор строк исходного текста (paragraph) до .!? в конце строки
        to_write = []       # новый набор строк (paragraph) длиной до MAX_LEN для записи
        for line in lines:
            s = line.strip()
            if s.startswith("STORY"):   # начало собственно, фрагмента текста (главы)
                s1 = '=' * len(s)
                good_line = True        # индикатор того, что эта строка - полезный текст
                fout.write(s + '\n' + s1 + '\n\n')
                continue
            if s.startswith("Helpful"): # окончание собственно, фрагмента текста (главы)
                good_line = False
                fout.write('\n')
                continue
            if s.startswith("Vocabulary"):  # окончание всего текста
                break
            if good_line:
                s.replace('\n', ' ')
                chunk.extend(s.split(' '))  # формируем список слов для данного параграфа

                sign = True if s[-1] in ".!?" and len(chunk) > MIN_PARAGRAPH else False
                # индикатор того, что строка s - последняя для формируемого параграфа
                if sign:
                    # Формируем из строк в chunk новые строки для записи в списке строк to_write
                    s = ""
                    for ndx in range(len(chunk)):
                        next_chunk = chunk[ndx]
                        if next_chunk.isdigit():    # это, скорее всего, номер страницы исходного djvu текста
                            continue
                        if len(s) + len(next_chunk) <= MAX_LEN - 1:
                            # следующее слово не приведет к строке размера больше максимального
                            if s == '':
                                s = next_chunk  # первое слово в новой строке
                            else:
                                s = s + ' ' + next_chunk    # продолжение строки
                        else:   # макссимальная длина строки достигнута, следующее слово приведет к превышению MAX_LEN
                            s += '\n'
                            to_write.append(s)  # добавляем строку в список для записи параграфа
                            s = next_chunk      # начинаем формировать следующую строку
                        if ndx == len(chunk) - 1:   # последнее слово параграфа
                            s += '\n\n'             # параграфы разделяем пустой строкой
                            to_write.append(s)      # окончательно формируем список для записи параграфа
                            s = ""
                            for w in to_write:      # записываем параграф в файл
                                fout.write(w)

                            # инициализируем следующий параграф
                            chunk = []
                            to_write = []

    finally:
        if fin:
            fin.close()
        if fout:
            fout.close()


if __name__ == "__main__":
    main()
    print("All Done!")