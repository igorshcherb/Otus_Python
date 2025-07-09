insert into store_app_category(name, description) 
  values ('Канцтовары', 'Ручки, тетрадки...');

insert into store_app_category(name, description) 
  values ('Продукты питания', 'Еда');


insert into store_app_product(name, description, price, created_at, category_id)
  values('Ручка 1', 'Ручка синяя', 100, now(), 1);

insert into store_app_product(name, description, price, created_at, category_id)
  values('Ручка 2', 'Ручка черная', 100, now(), 1);

insert into store_app_product(name, description, price, created_at, category_id)
  values('Ручка 3', 'Ручка красная', 100, now(), 1);

insert into store_app_product(name, description, price, created_at, category_id)
  values('Тетрадь 1', 'Тетрадь 10 страниц', 30, now(), 1);

insert into store_app_product(name, description, price, created_at, category_id)
  values('Тетрадь 2', 'Тетрадь 48 страниц', 200, now(), 1);

insert into store_app_product(name, description, price, created_at, category_id)
  values('Тетрадь 3', 'Тетрадь со сменными блоками', 400, now(), 1);

insert into store_app_product(name, description, price, created_at, category_id)
  values('Макароны', 'Макароны', 200, now(), 2);

-- select * from store_app_category;
-- select * from store_app_product;