create statistics (dependencies) on flight_no, departure_airport from flights;
create statistics (mcv) on departure_airport, aircraft_code from flights;
create statistics on departure_airport, arrival_airport from flights;
create statistics on extract(month from scheduled_departure at time zone 'europe/moscow') from flights;
--
select * from pg_stats_ext;
select * from pg_stats_ext_exprs;
select * from pg_statistic_ext;
select * from pg_statistic_ext_data;
