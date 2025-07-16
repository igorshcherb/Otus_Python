-- drop table query_groups;
create table query_groups(id bigserial, code varchar(20), description varchar(200));
alter table query_groups add constraint query_groups_id_pk primary key (id);
alter table query_groups add constraint query_groups_code_uk unique (code);
alter table query_groups alter column code set not null;
comment on table query_groups is 'Группы запросов';
comment on column query_groups.id is 'Идентификатор группы запросов';
comment on column query_groups.code is 'Код группы';
comment on column query_groups.description is 'Описание группы'; 
--------------------------------------------------------------------------------------------------------------------------------
-- drop table queries;
create table queries(id bigserial, code varchar(20), query_text varchar(500), description varchar(200));
alter table queries add constraint queries_id_pk primary key (id);
alter table queries add constraint queries_code_uk unique (code);
alter table queries alter column code set not null;
alter table queries alter column query_text set not null;
comment on table queries is 'Запросы';
comment on column queries.id is 'Идентификатор запроса';
comment on column queries.code is 'Код запроса';
comment on column queries.query_text is 'Текст запроса';
comment on column queries.description is 'Описание запроса';
--------------------------------------------------------------------------------------------------------------------------------
-- drop table queries_in_groups;
create table queries_in_groups(id bigserial, query_group_id bigint, query_id bigint);
alter table queries_in_groups add constraint queries_in_groups_id_pk primary key (id);
alter table queries_in_groups add constraint queries_in_groups_group_fk 
  foreign key (query_group_id) references query_groups(id) on delete cascade;
alter table queries_in_groups add constraint queries_in_groups_query_fk 
  foreign key (query_id) references queries(id) on delete cascade;
alter table queries_in_groups add constraint queries_in_groups_uk unique (query_group_id, query_id);
alter table queries_in_groups alter column query_group_id set not null;
alter table queries_in_groups alter column query_id set not null;
comment on table queries_in_groups is 'Запросы в группах';
comment on column queries_in_groups.id is 'Идентификатор запроса в группе';
comment on column queries_in_groups.query_group_id is 'Идентификатор группы';
comment on column queries_in_groups.query_id is 'Идентификатор запроса';
--------------------------------------------------------------------------------------------------------------------------------
-- drop table connection_types;
create table connection_types(id bigserial, code varchar(20), description varchar(200));
alter table connection_types add constraint connection_types_id_pk primary key (id);
alter table connection_types add constraint connection_types_code_uk unique (code);
alter table connection_types alter column code set not null;
comment on table connection_types is 'Типы соединений';
comment on column connection_types.id is 'Идентификатор типа соединений';
comment on column connection_types.code is 'Код типа соединений';
comment on column connection_types.description is 'Описание типа соединений';
--------------------------------------------------------------------------------------------------------------------------------
-- drop table connections;
create table connections(id bigserial, code varchar(20), connection_type_id bigint, description varchar(200),
  host varchar(100), port varchar(10), database varchar(100), username varchar(100), password varchar(100));
alter table connections add constraint connections_id_pk primary key (id);
alter table connections add constraint connections_code_uk unique (code);
alter table connections add constraint connections_type_fk 
  foreign key (connection_type_id) references connection_types(id);
alter table connections alter column code set not null;
alter table connections alter column connection_type_id set not null;
comment on table connections is 'Соединения';
comment on column connections.id is 'Идентификатор соединения';
comment on column connections.code is 'Код соединения';
comment on column connections.connection_type_id is 'Идентификатор типа соединения';
comment on column connections.description is 'Описание соединения';
comment on column connections.host is 'Хост (IP-адрес)';
comment on column connections.port is 'Порт';
comment on column connections.database is 'База данных';
comment on column connections.username is 'Имя пользователя';
comment on column connections.password is 'Пароль';
--------------------------------------------------------------------------------------------------------------------------------
-- drop table benchmarks;
create table benchmarks(id bigserial, name varchar(200), query_group_id bigint, connection_id bigint,
  start_datetime timestamp);
alter table benchmarks add constraint benchmarks_pk primary key (id);
alter table benchmarks add constraint benchmarks_name_uk unique (name);
alter table benchmarks add constraint benchmarks_query_group_fk 
  foreign key (query_group_id) references query_groups(id);
alter table benchmarks add constraint benchmarks_connection_fk 
  foreign key (connection_id) references connections(id);
alter table benchmarks alter column name set not null;
alter table benchmarks alter column query_group_id set not null;
alter table benchmarks alter column connection_id set not null;
alter table benchmarks alter column start_datetime set not null;
comment on table benchmarks is 'Тесты производительности';
comment on column benchmarks.id is 'Идентификатор теста производительности';
comment on column benchmarks.name is 'Наименование теста производительности';
comment on column benchmarks.query_group_id is 'Идентификатор группы запросов, по которой выполняется тест';
comment on column benchmarks.connection_id is 'Идентификатор соединения, по которому выполняется тест';
comment on column benchmarks.start_datetime is 'Дата и время начала теста производительности';
--------------------------------------------------------------------------------------------------------------------------------
-- drop table benchmark_items;
create table benchmark_items(id bigserial, benchmark_id integer, query_id bigint, start_datetime timestamp, result float);
alter table benchmark_items add constraint benchmark_items_pk primary key (id);
alter table benchmark_items add constraint benchmark_items_benchmark_fk 
  foreign key (benchmark_id) references benchmarks(id) on delete cascade;
alter table benchmark_items add constraint benchmark_items_query_fk 
  foreign key (query_id) references queries(id);
alter table benchmark_items alter column benchmark_id set not null;
alter table benchmark_items alter column query_id set not null;
alter table benchmark_items alter column start_datetime set not null;
alter table benchmark_items alter column result set not null;
comment on table benchmark_items is 'Строки результатов тестов производительности запросов';
comment on column benchmark_items.id is 'Идентификатор строки теста производительности запросов';
comment on column benchmark_items.benchmark_id is 'Идентификатор теста производительности';
comment on column benchmark_items.query_id is 'Идентификатор запроса';
comment on column benchmark_items.start_datetime is 'Дата и время начала теста производительности запроса';
comment on column benchmark_items.result is 'Результат теста';


