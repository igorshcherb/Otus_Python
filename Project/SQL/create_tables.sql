-- drop table query_groups;
create table query_groups(code varchar(20), description varchar(200));
alter table query_groups add constraint query_groups_pk primary key (code);

-- drop table queries;
create table queries(code varchar(20), query_text varchar(500), description varchar(200));
alter table queries add constraint queries_pk primary key (code);

-- drop table queries_in_groups;
create table queries_in_groups(group_code varchar(20), query_code varchar(20));
alter table queries_in_groups add constraint queries_in_groups_group_fk 
  foreign key (group_code) references query_groups(code);
alter table queries_in_groups add constraint queries_in_groups_query_fk 
  foreign key (query_code) references queries(code);
alter table queries_in_groups add constraint queries_in_groups_uk unique (group_code, query_code);

-- drop table connection_types;
create table connection_types(code varchar(20), description varchar(200));
alter table connection_types add constraint connection_types_pk primary key (code);

-- drop table connections;
create table connections(code varchar(20), type_code varchar(20), description varchar(200),
  host varchar(100), port varchar(10), database varchar(100), username varchar(100), password varchar(100));
alter table connections add constraint connections_pk PRIMARY KEY (code);
alter table connections add constraint connections_types_fk 
  foreign key (type_code) references connection_types(code);

-- drop table benchmarks;
create table benchmarks(id serial, name varchar(200), start_datetime timestamp);
alter table benchmarks add constraint benchmarks_pk PRIMARY KEY (id);

-- drop table benchmark_items;
create table benchmark_items(id bigserial, benchmark_id integer, query_code varchar(20), start_datetime timestamp, result float);
alter table benchmark_items add constraint benchmark_items_pk PRIMARY KEY (id);
alter table benchmark_items add constraint benchmark_items_fk 
  foreign key (benchmark_id) references benchmarks(id) on delete cascade;
