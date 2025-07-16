select q.query_text
from queries_in_groups qin
     left join queries q on q.code = qin.query_code
where qin.group_code = 'gr1';

select * from benchmarks;
select * from benchmark_items;
select * from queries_in_groups;
select * from queries;
select * from query_groups;
--
delete from benchmark_items;
delete from benchmarks;
delete from queries_in_groups;
delete from queries;
--
select * from compare_benchmarks_v where benchmark_name_1 = 'benchmark01' and benchmark_name_2 = 'benchmark09'



