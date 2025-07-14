-- select * from queries order by code;
-- delete from queries;
--
insert into queries(code, description, query_text)
  values('q01', 'Последовательное сканирование', 
         'select * from flights;');
insert into queries(code, description, query_text)
  values('q02', 'Сканирование индекса',
         'select * from bookings where book_ref = ''CDE08B'';');

insert into queries(code, description, query_text)
  values('q03', 'Поиск по диапазону',
         'select * from bookings where book_ref > ''000900'' and book_ref < ''000939'';');

insert into queries(code, description, query_text)
  values('q04', 'Поиск отдельных значений',
         'select * from bookings where book_ref in (''000906'',''000909'',''000917'',''000930'',''000938'');');

insert into queries(code, description, query_text)
  values('q05', 'Сканирование по битовой карте',
         'select * from bookings where total_amount < 5000;');

insert into queries(code, description, query_text)
  values('q06', 'Объединение битовых карт',
         'select * from bookings where total_amount < 5000 or total_amount > 500000;');

insert into queries(code, description, query_text)
  values('q07', 'Объединение битовых карт по разным индексам',
         'select * from bookings where total_amount < 5000 OR book_date = bookings.now() - INTERVAL ''1 day'';');

insert into queries(code, description, query_text)
  values('q08', 'Объединение битовых карт с перепроверкой (Recheck Cond)',
         'select count(*) from bookings where total_amount < 5000 and book_date > ''2017-07-15 18:00:00+03''::timestamp;');

insert into queries(code, description, query_text)
  values('q09', 'Сканирование только индекса',
         'select total_amount from bookings where total_amount > 200000;');

insert into queries(code, description, query_text)
  values('q10', 'Сканирование многоколоночного индекса',
         'select * from ticket_flights where ticket_no = ''0005432000284'' and flight_id = 187662;');

insert into queries(code, description, query_text)
  values('q11', 'Параллельное последовательное сканирование',
         'select count(*) from bookings;');

insert into queries(code, description, query_text)
  values('q12', 'Параллельное сканирование индекса',
         'select sum(total_amount) from bookings where book_ref < ''400000'';');

insert into queries(code, description, query_text)
  values('q13', 'Параллельное сканирование только индекса',
         'select count(book_ref) from bookings where book_ref <= ''400000'';');

insert into queries(code, description, query_text)
  values('q14', 'Параллельное сканирование по битовой карте',
         'select count(*) from bookings where total_amount < 20000 and book_date > ''2017-07-15 18:00:00+03''::timestamp;');

insert into queries(code, description, query_text)
  values('q15', 'Сортировка в оконных функциях',
         'select *, sum(total_amount) over (order by book_date) from bookings;');

insert into queries(code, description, query_text)
  values('q16', 'Оконные функции, требующие разного порядка строк',
         'select *, sum(total_amount) over (order by book_date), count(*) over (order by book_ref) from bookings;');

insert into queries(code, description, query_text)
  values('q17', 'Применение группировки',
         'select fare_conditions from seats group by fare_conditions;');

insert into queries(code, description, query_text)
  values('q18', 'Группировка сортировкой',
         'select ticket_no, count(ticket_no) from ticket_flights group by ticket_no;');

insert into queries(code, description, query_text)
  values('q19', 'Комбинированная группировка',
         'select fare_conditions, ticket_no, amount, count(*) from ticket_flights
          group by grouping sets (fare_conditions, ticket_no, amount);');

insert into queries(code, description, query_text)
  values('q20', 'Группировка в параллельных планах',
         'select flight_id, count(*) from ticket_flights group by flight_id;');

insert into queries(code, description, query_text)
  values('q21', 'Соединение вложенным циклом',
         'select * from tickets t join ticket_flights tf on tf.ticket_no = t.ticket_no where t.ticket_no in (''0005432312163'',''0005432312164''');

insert into queries(code, description, query_text)
  values('q22', 'Вложенный цикл для левого соединения',
         'select * from aircrafts a left join seats s on (a.aircraft_code = s.aircraft_code) where a.model like ''аэробус%'';');

insert into queries(code, description, query_text)
  values('q23', 'Вложенный цикл для антисоединения',
         'select * from aircrafts a where a.model like ''аэробус%''
          and not exists (select * from seats s where s.aircraft_code = a.aircraft_code);');

insert into queries(code, description, query_text)
  values('q24', 'Вложенный цикл для полусоединения',
         'select * from aircrafts a where a.model like ''аэробус%''
          and exists (select * from seats s where s.aircraft_code = a.aircraft_code);');

insert into queries(code, description, query_text)
  values('q25', 'Мемоизация - кеширование повторяющихся данных внутреннего набора',
         'select * from flights f join aircrafts_data a on f.aircraft_code = a.aircraft_code where f.flight_no = ''PG0003'';');

insert into queries(code, description, query_text)
  values('q26', 'Вложенный цикл в параллельных планах',
         'select t.passenger_name from tickets t join ticket_flights tf on tf.ticket_no = t.ticket_no
          join flights f on f.flight_id = tf.flight_id where f.flight_id = 12345;');

insert into queries(code, description, query_text)
  values('q27', 'Функциональные зависимости предикатов (dependencies)',
         'select * from flights where flight_no = ''PG0007'' and departure_airport = ''VKO'';');

insert into queries(code, description, query_text)
  values('q28', 'Наиболее частые комбинации значений (mcv)',
         'select * from flights where departure_airport = ''LED'' and aircraft_code = ''321'';');

insert into queries(code, description, query_text)
  values('q29', 'Уникальные комбинации',
         'select distinct departure_airport, arrival_airport from flights;');

insert into queries(code, description, query_text)
  values('q30', 'Статистика по выражению',
         'select * from flights where extract(month from scheduled_departure at time zone ''Europe/Moscow'') = 1;');

insert into queries(code, description, query_text)
  values('q31', 'Узел Materialize',
         'select a1.city, a2.city from airports a1, airports a2 where a1.timezone = ''Europe/Moscow''
          and abs(a2.coordinates[1]) > 66.652;');

insert into queries(code, description, query_text)
  values('q32', 'Материализация CTE',
         'with q as materialized (select f.flight_id, a.aircraft_code from flights f join aircrafts a on a.aircraft_code = f.aircraft_code) 
          select * from q join seats s on s.aircraft_code = q.aircraft_code where s.seat_no = ''1A'';');

insert into queries(code, description, query_text)
  values('q33', 'Рекурсивные запросы',
         'with recursive r(n, airport_code) as (
          select 1, a.airport_code
          from airports a
          union all
          select r.n+1, f.arrival_airport
          from r
          join flights f on f.departure_airport = r.airport_code
          where r.n < 2
          )
          select * from r;');

