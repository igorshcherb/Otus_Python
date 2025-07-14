-- drop table query_groups;
create table query_groups(code varchar(20), description varchar(200));
alter table query_groups add constraint query_groups_pk primary key (code);
comment on table query_groups is 'Группы запросов';
comment on column query_groups.code is 'Код группы';
comment on column query_groups.description is 'Описание группы'; 
--------------------------------------------------------------------------------------------------------------------------------
-- drop table queries;
create table queries(code varchar(20), query_text varchar(500), description varchar(200));
alter table queries add constraint queries_pk primary key (code);
alter table queries add constraint queries_text_not_null (code);
alter table queries alter column query_text set not null;
comment on table queries is 'Запросы';
comment on column queries.code is 'Код запроса';
comment on column queries.query_text is 'Текст запроса';
comment on column queries.description is 'Описание запроса';
--------------------------------------------------------------------------------------------------------------------------------
-- drop table queries_in_groups;
create table queries_in_groups(group_code varchar(20), query_code varchar(20));
alter table queries_in_groups add constraint queries_in_groups_group_fk 
  foreign key (group_code) references query_groups(code);
alter table queries_in_groups add constraint queries_in_groups_query_fk 
  foreign key (query_code) references queries(code);
alter table queries_in_groups add constraint queries_in_groups_uk unique (group_code, query_code);
alter table queries_in_groups alter column group_code set not null;
alter table queries_in_groups alter column query_code set not null;
comment on table queries_in_groups is 'Запросы в группах';
comment on column queries_in_groups.group_code is 'Код группы';
comment on column queries_in_groups.query_code is 'Код запроса';
--------------------------------------------------------------------------------------------------------------------------------
-- drop table connection_types;
create table connection_types(code varchar(20), description varchar(200));
alter table connection_types add constraint connection_types_pk primary key (code);
comment on table connection_types is 'Типы соединений';
comment on column connection_types.code is 'Код типа соединений';
comment on column connection_types.description is 'Описание типа соединений';
--------------------------------------------------------------------------------------------------------------------------------
-- drop table connections;
create table connections(code varchar(20), type_code varchar(20), description varchar(200),
  host varchar(100), port varchar(10), database varchar(100), username varchar(100), password varchar(100));
alter table connections add constraint connections_pk PRIMARY KEY (code);
alter table connections add constraint connections_types_fk 
  foreign key (type_code) references connection_types(code);
alter table connections alter column type_code set not null;
comment on table connections is 'Соединения';
comment on column connections.code is 'Код соединения';
comment on column connections.type_code is 'Код типа соединения';
comment on column connections.description is 'Описание соединения';
comment on column connections.host is 'Хост (IP-адрес)';
comment on column connections.port is 'Порт';
comment on column connections.database is 'База данных';
comment on column connections.username is 'Имя пользователя';
comment on column connections.password is 'Пароль';
--------------------------------------------------------------------------------------------------------------------------------
-- drop table benchmarks;
create table benchmarks(id serial, name varchar(200), query_group_code varchar(20), start_datetime timestamp);
alter table benchmarks add constraint benchmarks_pk PRIMARY KEY (id);
alter table benchmarks add constraint benchmarks_query_group_fk 
  foreign key (query_group_code) references query_groups(code);
alter table benchmarks add constraint benchmarks_name_uk unique (name);
alter table benchmarks alter column name set not null;
alter table benchmarks alter column query_group_code set not null;
alter table benchmarks alter column start_datetime set not null;
comment on table benchmarks is 'Тесты производительности';
comment on column benchmarks.id is 'Идентификатор теста производительности';
comment on column benchmarks.name is 'Наименование теста производительности';
comment on column benchmarks.query_group_code is 'Код группы запросов, по которой выполняет тест';
comment on column benchmarks.start_datetime is 'Дата и время начала теста производительности';
--------------------------------------------------------------------------------------------------------------------------------
-- drop table benchmark_items;
create table benchmark_items(id bigserial, benchmark_id integer, query_code varchar(20), start_datetime timestamp, result float);
alter table benchmark_items add constraint benchmark_items_pk PRIMARY KEY (id);
alter table benchmark_items add constraint benchmark_items_fk 
  foreign key (benchmark_id) references benchmarks(id) on delete cascade;
alter table benchmark_items alter column benchmark_id set not null;
alter table benchmark_items alter column query_code set not null;
alter table benchmark_items alter column start_datetime set not null;
alter table benchmark_items alter column result set not null;
comment on table benchmark_items is 'Строки результатов тестов производительности запросов';
comment on column benchmark_items.id is 'Идентификатор строки теста производительности запросов';
comment on column benchmark_items.benchmark_id is 'Идентификатор теста производительности';
comment on column benchmark_items.query_code is 'Код запроса';
comment on column benchmark_items.start_datetime is 'Дата и время начала теста производительности запроса';
comment on column benchmark_items.result is 'Результат теста';


