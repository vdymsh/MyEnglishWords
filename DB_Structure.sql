create table word_keys
(
	word varchar(50) not null unique primary key,
	main_word varchar(50),
	form_to_main int
)

create table word_forms
(
	form_id integer primary key autoincrement,
	form_description varchar(255)
)

create table word_meanings
(
	meaning_id integer primary key autoincrement,
	word varchar(50) not null,
	meaning varchar(255), 
	form_id int
)

create table word_examples
(
	meaning_id int,
	example varchar(50)
)

create table dictionary_keys
(
	word varchar(50) not null unique primary key
)

create table dictionary_meanings
(
	word varchar(50) not null,
	meaning varchar(255) 
)


