-- drop view queries_in_groups_v;
create view queries_in_groups_v as
select qin.group_code, qin.query_code, q.query_text
from queries_in_groups qin
     left join queries q on q.code = qin.query_code;
------------------------------------------------------------------------------------------
-- drop view benchmark_items_v;
create view benchmark_items_v as
select bi.benchmark_id, b.name benchmark_name, bi.query_code, bi.start_datetime, bi.result 
  from benchmark_items bi
       left join benchmarks b on b.id = bi.benchmark_id;
------------------------------------------------------------------------------------------
