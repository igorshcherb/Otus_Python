-- select * from connections;
-- delete from connections;
insert into connections(code, connection_type_id, description, host, port, database, username, password) 
  values ('pg1', 
          (SELECT ct.id FROM connection_types ct WHERE ct.code = 'postgresql'), 
          'PostgreSQL 16', '192.168.2.171', '5432', 'demo', 'postgres', 'postgres');
insert into connections(code, connection_type_id, description, host, port, database, username, password) 
  values ('adb', 
          (SELECT ct.id FROM connection_types ct WHERE ct.code = 'postgresql'), 
          'Arenadata DB', '192.168.2.151', '5432', 'adb', 'gpadmin', 'admin');
