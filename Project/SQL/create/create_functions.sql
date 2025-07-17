-- drop function insert_benchmark
create or replace function insert_benchmark(p_name varchar, p_query_group_code varchar, p_connection_code varchar,
  p_start_datetime timestamp) returns int
language plpgsql  
as $$
declare
  v_id int;
begin
  insert into benchmarks(name, query_group_id, connection_id, start_datetime) 
    values(p_name, (select id from query_groups where code = p_query_group_code), 
      (select id from connections where code = p_connection_code), p_start_datetime) 
    returning id into v_id;
  return v_id;
end;
$$;
------------------------------------------------------------------------------------------------------------------
-- drop procedure insert_benchmark_item
create or replace procedure insert_benchmark_item(p_benchmark_id integer, p_query_code varchar, 
  p_start_datetime timestamp, p_result float)
language plpgsql  
as $$
begin
  insert into benchmark_items(benchmark_id, query_id, start_datetime, result) 
    values(p_benchmark_id, 
      (select id from queries where code = p_query_code), p_start_datetime, p_result);
end;
$$;



