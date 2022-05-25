import db_engine
import utilites


def main():
    dbe = db_engine.DbEngine("all_english_words.db")

    utilites.create_table_word_keys(dbe)
    utilites.create_table_word_forms(dbe)
    utilites.create_table_word_meanings(dbe)
    utilites.create_table_word_examples(dbe)
    # utilites.create_table_dictionary_keys(dbe)
    # utilites.create_table_dictionary_meanings(dbe)

    utilites.fill_dictionary_tables(dbe, r"data\5000.txt")
    utilites.fill_frequent_dictionary_table(dbe, r"data\5000_Frequent.csv")


if __name__ == "__main__":
    main()
