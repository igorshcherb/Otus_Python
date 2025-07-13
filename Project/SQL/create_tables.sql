create sequence query_groups_seq;
create sequence queries_seq;
create sequence connections_seq;

-- drop table query_groups;
create table query_groups();

-- drop table queries;
create table queries();

-- drop table query_in_group;
create table query_in_group();

-- drop table connection_types;
create table connection_types(code varchar(20), description varchar(200));
alter table connection_types add constraint connection_types_pk PRIMARY KEY (code);

-- drop table connections;
create table connections(code varchar(20), type_code varchar(20), 
  host varchar(100), port varchar(10), database varchar(100), username varchar(100), password varchar(100));
alter table connections add constraint connections_pk PRIMARY KEY (code);
alter table connections add constraint connections_types_fk 
  foreign key (type_code) references connection_types(code);


-- drop table benchmarks;
create table benchmarks();

-- drop table benchmark_items;
create table benchmark_items();