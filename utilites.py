def create_table_word_keys(dbe):
    dbe.execute_query("""create table if not exists word_keys
    (
        word varchar(50) not null unique primary key,
        main_word varchar(50),
        form_to_main int
    )
    """)


def create_table_word_forms(dbe):
    dbe.execute_query("""create table if not exists word_forms
    (
        form_id integer primary key autoincrement,
        form_description varchar(255)
    )
    """)


def create_table_word_meanings(dbe):
    dbe.execute_query("""create table if not exists word_meanings
    (
        meaning_id integer primary key autoincrement,
        word varchar(50) not null,
        meaning varchar(255), 
        form_id int
    )
    """)


def create_table_word_examples(dbe):
    dbe.execute_query("""create table if not exists word_examples
    (
        meaning_id integer,
        example varchar(50)
    )
    """)


def create_table_dictionary_keys(dbe):
    dbe.execute_query("""create table if not exists dictionary_keys
    (
        word varchar(50) not null unique primary key
    )
    """)


def create_table_dictionary_meanings(dbe):
    dbe.execute_query("""create table if not exists dictionary_meanings
    (
        word varchar(50) not null,
        meaning varchar(255)
    )
    """)


def create_table_frequent_dictionary(dbe):
    dbe.execute_query("""create table if not exists frequent_dictionary
    (
        position integer not null unique primary key, 
        word varchar(50) not null,
        part_of_speach char(1)
    )
    """)

    dbe.execute_query(r"CREATE UNIQUE INDEX idx_word_part ON frequent_dictionary (word, part_of_speach)")


def fill_dictionary_tables(dbe, file_name, encoding_string="utf-8"):
    dbe.execute_query(r"drop table if exists dictionary_meanings")
    dbe.execute_query(r"drop table if exists dictionary_keys")
    create_table_dictionary_keys(dbe)
    create_table_dictionary_meanings(dbe)
    dbe.execute_query("BEGIN;")
    try:
        with open(file_name, 'r', encoding=encoding_string) as f:
            for r in f:
                r = r.replace(',', '-')
                r = r.replace(r'/', '-')
                rl = r.split('-')
                x = rl[0].strip().lower()

                dbe.execute_query(r"insert or ignore into dictionary_keys (word) values(?)", (x,))
                for i in range(1, len(rl)):
                    y = rl[i].strip().lower()
                    dbe.execute_query(r"insert into dictionary_meanings (word, meaning) values(?, ?)", (x, y))
        dbe.commit()
    except Exception as e:
        print(e)
        dbe.rollback()


def fill_frequent_dictionary_table(dbe, file_name, encoding_string="utf-8"):
#    dbe.execute_query(r"drop table if exists frequency_wordlist")
    dbe.execute_query(r"drop table if exists frequent_dictionary")
    create_table_frequent_dictionary(dbe)
    dbe.execute_query("BEGIN;")
    try:
        with open(file_name, 'r', encoding=encoding_string) as f:
            f.readline()
            f.readline()
            for r in f:
                rl = r.split(',')
                n = int(rl[0])
                w = rl[1].strip()
                p = rl[2].strip()[0]
                dbe.execute_query(r"""insert into frequent_dictionary (position, word, part_of_speach) 
                    values(?, ?, ?)""", (n, w, p))
        dbe.commit()
    except Exception as e:
        print(e)
        dbe.rollback()


