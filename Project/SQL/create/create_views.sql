-- drop view queries_in_groups_v;
create view queries_in_groups_v as
select qg.code group_code, q.code query_code, q.query_text
from queries_in_groups qin
     left join queries q on q.id = qin.query_id
     left join query_groups qg on qg.id = qin.query_group_id;
------------------------------------------------------------------------------------------
-- drop view benchmark_items_v;
create view benchmark_items_v as
select bi.benchmark_id, b.name benchmark_name, q.code query_code, bi.start_datetime, bi.result 
  from benchmark_items bi
       left join benchmarks b on b.id = bi.benchmark_id
       left join queries q on q.id = bi.query_id;
------------------------------------------------------------------------------------------
-- drop view compare_benchmarks_v
create view compare_benchmarks_v as
select (select name from benchmarks b1 where b1.id = bi1.benchmark_id) benchmark_name_1, 
       (select q.code from queries q where q.id = bi1.query_id) query_code_1, bi1.result result_1,
       (select name from benchmarks b2 where b2.id = bi2.benchmark_id) benchmark_name_2, 
       (select q.code from queries q where q.id = bi2.query_id) query_code_2, bi2.result result_2,
       to_char(((bi2.result - bi1.result) / bi1.result * 100), '9999.99') diff
  from benchmark_items bi1
       full outer join benchmark_items bi2 ON bi2.query_id = bi1.query_id and bi1.benchmark_id != bi2.benchmark_id;   


