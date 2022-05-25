drop table if exists word_frequent_list;
create table if not exists word_frequent_list
(
	word_position integer primary key,
	word varchar(50) not null
);

drop table if exists word_meanings;
create table  if not exists word_meanings
(
	word_meaning_id integer primary key autoincrement,
	word_position integer,
	meaning varchar(50)
);

drop table if exists word_examples;
create table if not exists word_examples
(
	word_example_id integer primary key autoincrement,
	word_meaning_id int,
	example varchar(254)
);


