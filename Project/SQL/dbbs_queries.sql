select q.query_text
from queries_in_groups qin
     left join queries q on q.code = qin.query_code
where qin.group_code = 'gr1'

delete from benchmarks

select * from benchmarks

delete from benchmark_items

select * from benchmark_items

select count(*) from benchmark_items


