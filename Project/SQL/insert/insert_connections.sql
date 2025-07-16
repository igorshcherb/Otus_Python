-- select * from connections;
-- delete from connections;
insert into connections(code, type_code, description, host, port, database, username, password) 
  values ('pg1', 'postgresql', 'PostgreSQL 16', '192.168.2.171', '5432', 'demo', 'postgres', 'postgres');
