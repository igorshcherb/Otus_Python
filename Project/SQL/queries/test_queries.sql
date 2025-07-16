set schema 'bookings'

create index on bookings(book_date);
create index on bookings(total_amount);

-- select tablename from pg_tables where schemaname='bookings' order by tablename;

select * from aircrafts;
select * from airports;
select * from boarding_passes;
select * from bookings;
select * from flights;
select * from seats;
select * from ticket_flights;
select * from tickets;
--

