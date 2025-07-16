-- select * from connections;
-- delete from connections;
insert into connections(code, connection_type_id, description, host, port, database, username, password) 
  values ('pg1', 
          (SELECT ct.id FROM connection_types ct WHERE ct.code = 'postgresql'), 
          'PostgreSQL 16', '192.168.2.171', '5432', 'demo', 'postgres', 'postgres');
