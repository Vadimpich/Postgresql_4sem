--
-- PostgreSQL database dump
--

-- Dumped from database version 16.2
-- Dumped by pg_dump version 16.2

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: calculate_total(); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION public.calculate_total() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
BEGIN
    NEW.total := (SELECT pr_price * NEW.quantity FROM products WHERE id_product = NEW.id_product);
    RETURN NEW;
END;
$$;


ALTER FUNCTION public.calculate_total() OWNER TO postgres;

--
-- Name: count_orders_by_city(); Type: PROCEDURE; Schema: public; Owner: postgres
--

CREATE PROCEDURE public.count_orders_by_city()
    LANGUAGE plpgsql
    AS $$
BEGIN
    SELECT
        c.city,
        COUNT(o.id_order) AS order_count
    FROM
        customers c
    LEFT JOIN
        orders o ON c.id_customer = o.id_customer
    GROUP BY
        c.city
    ORDER BY
        c.city;
END;
$$;


ALTER PROCEDURE public.count_orders_by_city() OWNER TO postgres;

--
-- Name: delete_items_before_product(); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION public.delete_items_before_product() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
BEGIN
    DELETE FROM items WHERE id_product = OLD.id_product;
    RETURN OLD;
END;
$$;


ALTER FUNCTION public.delete_items_before_product() OWNER TO postgres;

--
-- Name: get_orders_by_city_and_interval(date, date); Type: PROCEDURE; Schema: public; Owner: postgres
--

CREATE PROCEDURE public.get_orders_by_city_and_interval(IN start_date date, IN end_date date)
    LANGUAGE plpgsql
    AS $$
BEGIN
    SELECT
        o.id_order,o.order_date,o.ship_date,c.city
    FROM
        orders o
    JOIN
        customers c ON o.id_customer = c.id_customer
    WHERE
        o.ship_date BETWEEN start_date AND end_date
    GROUP BY
        o.id_order,o.order_date,o.ship_date,c.city
    ORDER BY
        o.ship_date;
END;
$$;


ALTER PROCEDURE public.get_orders_by_city_and_interval(IN start_date date, IN end_date date) OWNER TO postgres;

--
-- Name: new_customer_trigger(); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION public.new_customer_trigger() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
BEGIN
    RAISE NOTICE 'Добавлен новый клиент: % %', NEW.first_name, NEW.last_name;
    RETURN NEW;
END;
$$;


ALTER FUNCTION public.new_customer_trigger() OWNER TO postgres;

--
-- Name: prevent_ddl_operations(); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION public.prevent_ddl_operations() RETURNS event_trigger
    LANGUAGE plpgsql
    AS $$
DECLARE
    command_tag text;
BEGIN
    command_tag := tg_tag;
    IF command_tag = 'DROP TABLE' OR command_tag = 'ALTER TABLE' THEN
        RAISE EXCEPTION 'Выполнение DDL-команды "%"', command_tag;
    END IF;
END;
$$;


ALTER FUNCTION public.prevent_ddl_operations() OWNER TO postgres;

--
-- Name: update_stock(); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION public.update_stock() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
BEGIN
    UPDATE products
    SET in_stock = in_stock - OLD.quantity
    WHERE id_product = OLD.id_product;
    RETURN OLD;
END;
$$;


ALTER FUNCTION public.update_stock() OWNER TO postgres;

--
-- Name: update_total(); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION public.update_total() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
BEGIN
    NEW.total := (SELECT pr_price * NEW.quantity FROM products WHERE id_product = NEW.id_product);
    RETURN NEW;
END;
$$;


ALTER FUNCTION public.update_total() OWNER TO postgres;

--
-- Name: НовыеКлиенты(); Type: PROCEDURE; Schema: public; Owner: postgres
--

CREATE PROCEDURE public."НовыеКлиенты"()
    LANGUAGE sql
    AS $$
INSERT INTO customers (company_name, last_name, first_name, address, city, index_code, phone, email, country)
VALUES
    ('Техно Прогресс Лтд.', 'Иванов', 'Петр', 'Адрес 1', 'Новый Городск', 12345, '123456789', 'ivanov@example.com', 'Россия'),
    ('Инновационные решения', 'Петров', 'Иван', 'Адрес 2', 'Стартаповый', 54321, '987654321', 'petrov@example.com', 'Россия'),
    ('Глобальные Индустрии', 'Сидоров', 'Алексей', 'Адрес 3', 'Мегаполис', 67890, '456789123', 'sidorov@example.com', 'Россия');
$$;


ALTER PROCEDURE public."НовыеКлиенты"() OWNER TO postgres;

--
-- Name: Поиск_Заказов_ПоДатам(date, date, date); Type: PROCEDURE; Schema: public; Owner: postgres
--

CREATE PROCEDURE public."Поиск_Заказов_ПоДатам"(IN p_order_date date, IN p_delivery_start date, IN p_delivery_end date)
    LANGUAGE plpgsql
    AS $$
BEGIN
    SELECT *
    FROM orders
    WHERE order_date = p_order_date
    AND ship_date BETWEEN p_delivery_start AND p_delivery_end;
END;
$$;


ALTER PROCEDURE public."Поиск_Заказов_ПоДатам"(IN p_order_date date, IN p_delivery_start date, IN p_delivery_end date) OWNER TO postgres;

--
-- Name: Поиск_ПоДиапазонуЦен(numeric, numeric); Type: PROCEDURE; Schema: public; Owner: postgres
--

CREATE PROCEDURE public."Поиск_ПоДиапазонуЦен"(IN p_min_price numeric, IN p_max_price numeric)
    LANGUAGE plpgsql
    AS $$
BEGIN
    SELECT *
    FROM products
    WHERE pr_price BETWEEN p_min_price AND p_max_price;
END;
$$;


ALTER PROCEDURE public."Поиск_ПоДиапазонуЦен"(IN p_min_price numeric, IN p_max_price numeric) OWNER TO postgres;

--
-- Name: Поиск_ПоКомпании(character varying); Type: PROCEDURE; Schema: public; Owner: postgres
--

CREATE PROCEDURE public."Поиск_ПоКомпании"(IN p_company_name character varying)
    LANGUAGE plpgsql
    AS $$
BEGIN
    SELECT *
    FROM customers
    WHERE company_name = p_company_name;
END;
$$;


ALTER PROCEDURE public."Поиск_ПоКомпании"(IN p_company_name character varying) OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: customers; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.customers (
    id_customer integer NOT NULL,
    company_name character varying(255),
    last_name character varying(255) NOT NULL,
    first_name character varying(255) NOT NULL,
    address character varying(255),
    city character varying(255),
    index_code integer,
    phone character varying(255),
    email character varying(255),
    country character varying(255) DEFAULT 'Россия'::character varying
);


ALTER TABLE public.customers OWNER TO postgres;

--
-- Name: customers_id_customer_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.customers_id_customer_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.customers_id_customer_seq OWNER TO postgres;

--
-- Name: customers_id_customer_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.customers_id_customer_seq OWNED BY public.customers.id_customer;


--
-- Name: items; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.items (
    id_item integer NOT NULL,
    id_order integer,
    id_product integer NOT NULL,
    quantity integer NOT NULL,
    total numeric,
    CONSTRAINT positive_quantity CHECK ((quantity >= 0))
);


ALTER TABLE public.items OWNER TO postgres;

--
-- Name: items_id_item_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.items_id_item_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.items_id_item_seq OWNER TO postgres;

--
-- Name: items_id_item_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.items_id_item_seq OWNED BY public.items.id_item;


--
-- Name: orders; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.orders (
    id_order integer NOT NULL,
    id_customer integer NOT NULL,
    order_date date DEFAULT CURRENT_DATE NOT NULL,
    ship_date date,
    paid_date date,
    status character(1),
    CONSTRAINT ship_date_check CHECK ((ship_date >= order_date)),
    CONSTRAINT status_check CHECK ((status = ANY (ARRAY['C'::bpchar, 'P'::bpchar, 'A'::bpchar])))
);


ALTER TABLE public.orders OWNER TO postgres;

--
-- Name: orders_id_order_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.orders_id_order_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.orders_id_order_seq OWNER TO postgres;

--
-- Name: orders_id_order_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.orders_id_order_seq OWNED BY public.orders.id_order;


--
-- Name: products; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.products (
    id_product integer NOT NULL,
    pr_name character varying(255) NOT NULL,
    pr_price numeric,
    in_stock integer,
    re_order boolean,
    description character varying(255),
    CONSTRAINT in_stock_positive CHECK ((in_stock > 0)),
    CONSTRAINT positive_price CHECK ((pr_price >= (0)::numeric))
);


ALTER TABLE public.products OWNER TO postgres;

--
-- Name: products_id_product_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.products_id_product_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.products_id_product_seq OWNER TO postgres;

--
-- Name: products_id_product_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.products_id_product_seq OWNED BY public.products.id_product;


--
-- Name: test; Type: TABLE; Schema: public; Owner: test_user
--

CREATE TABLE public.test (
);


ALTER TABLE public.test OWNER TO test_user;

--
-- Name: customers id_customer; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.customers ALTER COLUMN id_customer SET DEFAULT nextval('public.customers_id_customer_seq'::regclass);


--
-- Name: items id_item; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.items ALTER COLUMN id_item SET DEFAULT nextval('public.items_id_item_seq'::regclass);


--
-- Name: orders id_order; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.orders ALTER COLUMN id_order SET DEFAULT nextval('public.orders_id_order_seq'::regclass);


--
-- Name: products id_product; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.products ALTER COLUMN id_product SET DEFAULT nextval('public.products_id_product_seq'::regclass);


--
-- Data for Name: customers; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.customers (id_customer, company_name, last_name, first_name, address, city, index_code, phone, email, country) VALUES (1, 'ООО Пример', 'Иванов', 'Петр', 'ул. Примерная, 1', 'Город', 12345, '+7 (123) 456-7890', 'ivanov@example.com', 'Россия');
INSERT INTO public.customers (id_customer, company_name, last_name, first_name, address, city, index_code, phone, email, country) VALUES (2, 'ИП Разработка', 'Смирнова', 'Анна', 'ул. Разработчиков, 10', 'Городское', 54321, '+7 (987) 654-3210', 'smirnova@example.com', 'Россия');
INSERT INTO public.customers (id_customer, company_name, last_name, first_name, address, city, index_code, phone, email, country) VALUES (3, 'ООО Тестовые технологии', 'Петров', 'Игорь', 'пр. Тестовый, 5', 'Городок', 67890, '+7 (234) 567-8901', 'petrov@example.com', 'Россия');
INSERT INTO public.customers (id_customer, company_name, last_name, first_name, address, city, index_code, phone, email, country) VALUES (4, 'ИП Ремонтник', 'Козлов', 'Михаил', 'ул. Ремонтная, 20', 'Городище', 34567, '+7 (876) 543-2109', 'kozlov@example.com', 'Россия');
INSERT INTO public.customers (id_customer, company_name, last_name, first_name, address, city, index_code, phone, email, country) VALUES (5, 'ООО Инновации', 'Сидорова', 'Елена', 'пр. Инновационный, 15', 'Новый Город', 78901, '+7 (321) 098-7654', 'sidorova@example.com', 'Россия');
INSERT INTO public.customers (id_customer, company_name, last_name, first_name, address, city, index_code, phone, email, country) VALUES (6, 'ИП Креатив', 'Андреев', 'Наталья', 'ул. Креативная, 8', 'Творческий', 21098, '+7 (654) 321-0987', 'andreeva@example.com', 'Россия');
INSERT INTO public.customers (id_customer, company_name, last_name, first_name, address, city, index_code, phone, email, country) VALUES (7, 'ООО СервисГарант', 'Морозов', 'Александр', 'пр. Сервисный, 12', 'Обслуживаемый', 87654, '+7 (789) 012-3456', 'morozov@example.com', 'Россия');
INSERT INTO public.customers (id_customer, company_name, last_name, first_name, address, city, index_code, phone, email, country) VALUES (8, 'ИП ТехноМастер', 'Николаева', 'Ольга', 'ул. Техническая, 25', 'Ремонтопригодный', 10987, '+7 (210) 987-6543', 'nikolaeva@example.com', 'Россия');
INSERT INTO public.customers (id_customer, company_name, last_name, first_name, address, city, index_code, phone, email, country) VALUES (9, 'ООО ПродажиИТ', 'Григорьев', 'Дмитрий', 'пр. Продажный, 18', 'Технополис', 54320, '+7 (543) 210-9876', 'grigoriev@example.com', 'Россия');
INSERT INTO public.customers (id_customer, company_name, last_name, first_name, address, city, index_code, phone, email, country) VALUES (10, 'ИП ЭлектроТех', 'Кузнецова', 'Мария', 'ул. Электрическая, 22', 'Техноград', 87653, '+7 (876) 543-2109', 'kuznetsova@example.com', 'Россия');


--
-- Data for Name: items; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.items (id_item, id_order, id_product, quantity, total) VALUES (1, 1, 1, 2, 2000);
INSERT INTO public.items (id_item, id_order, id_product, quantity, total) VALUES (2, 1, 2, 1, 500);
INSERT INTO public.items (id_item, id_order, id_product, quantity, total) VALUES (3, 2, 3, 3, 4500);
INSERT INTO public.items (id_item, id_order, id_product, quantity, total) VALUES (5, 1, 1, 2, 2000);
INSERT INTO public.items (id_item, id_order, id_product, quantity, total) VALUES (6, 1, 2, 1, 500);
INSERT INTO public.items (id_item, id_order, id_product, quantity, total) VALUES (7, 2, 3, 3, 4500);
INSERT INTO public.items (id_item, id_order, id_product, quantity, total) VALUES (8, 5, 4, 2, 3000);
INSERT INTO public.items (id_item, id_order, id_product, quantity, total) VALUES (9, 4, 5, 1, 700);
INSERT INTO public.items (id_item, id_order, id_product, quantity, total) VALUES (10, 4, 6, 4, 8000);
INSERT INTO public.items (id_item, id_order, id_product, quantity, total) VALUES (11, 5, 7, 2, 1500);
INSERT INTO public.items (id_item, id_order, id_product, quantity, total) VALUES (12, 6, 8, 1, 900);
INSERT INTO public.items (id_item, id_order, id_product, quantity, total) VALUES (13, 6, 9, 3, 2700);
INSERT INTO public.items (id_item, id_order, id_product, quantity, total) VALUES (14, 7, 10, 2, 1200);
INSERT INTO public.items (id_item, id_order, id_product, quantity, total) VALUES (15, NULL, 8, 6, 222);


--
-- Data for Name: orders; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.orders (id_order, id_customer, order_date, ship_date, paid_date, status) VALUES (1, 1, '2024-02-16', '2024-02-18', '2024-02-20', 'A');
INSERT INTO public.orders (id_order, id_customer, order_date, ship_date, paid_date, status) VALUES (2, 3, '2024-02-17', '2024-02-19', NULL, 'P');
INSERT INTO public.orders (id_order, id_customer, order_date, ship_date, paid_date, status) VALUES (4, 1, '2024-02-16', '2024-02-18', '2024-02-20', 'A');
INSERT INTO public.orders (id_order, id_customer, order_date, ship_date, paid_date, status) VALUES (5, 3, '2024-02-17', '2024-02-19', NULL, 'P');
INSERT INTO public.orders (id_order, id_customer, order_date, ship_date, paid_date, status) VALUES (6, 5, '2024-02-18', NULL, NULL, 'C');
INSERT INTO public.orders (id_order, id_customer, order_date, ship_date, paid_date, status) VALUES (7, 2, '2024-02-19', '2024-02-21', '2024-02-23', 'C');
INSERT INTO public.orders (id_order, id_customer, order_date, ship_date, paid_date, status) VALUES (8, 4, '2024-02-20', '2024-02-22', NULL, 'P');
INSERT INTO public.orders (id_order, id_customer, order_date, ship_date, paid_date, status) VALUES (9, 6, '2024-02-21', NULL, NULL, 'A');
INSERT INTO public.orders (id_order, id_customer, order_date, ship_date, paid_date, status) VALUES (10, 8, '2024-02-22', '2024-02-24', NULL, 'C');
INSERT INTO public.orders (id_order, id_customer, order_date, ship_date, paid_date, status) VALUES (11, 7, '2024-02-23', '2024-02-25', '2024-02-27', 'A');
INSERT INTO public.orders (id_order, id_customer, order_date, ship_date, paid_date, status) VALUES (12, 9, '2024-02-24', '2024-02-26', NULL, 'P');
INSERT INTO public.orders (id_order, id_customer, order_date, ship_date, paid_date, status) VALUES (13, 10, '2024-02-25', NULL, NULL, 'P');
INSERT INTO public.orders (id_order, id_customer, order_date, ship_date, paid_date, status) VALUES (15, 5, '2024-02-17', NULL, NULL, 'P');
INSERT INTO public.orders (id_order, id_customer, order_date, ship_date, paid_date, status) VALUES (16, 7, '2024-02-17', '2024-02-18', '2024-02-17', NULL);


--
-- Data for Name: products; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.products (id_product, pr_name, pr_price, in_stock, re_order, description) VALUES (2, 'Смартфон', 699.99, 100, true, 'Современный смартфон с высоким разрешением камеры');
INSERT INTO public.products (id_product, pr_name, pr_price, in_stock, re_order, description) VALUES (3, 'Планшет', 499.00, 30, true, 'Легкий и компактный планшет для развлечений и работы');
INSERT INTO public.products (id_product, pr_name, pr_price, in_stock, re_order, description) VALUES (4, 'Фотокамера', 899.99, 20, true, 'Профессиональная цифровая фотокамера');
INSERT INTO public.products (id_product, pr_name, pr_price, in_stock, re_order, description) VALUES (5, 'Телевизор', 1299.00, 15, true, 'Широкоформатный телевизор с высоким разрешением');
INSERT INTO public.products (id_product, pr_name, pr_price, in_stock, re_order, description) VALUES (6, 'Наушники', 129.99, 200, true, 'Беспроводные наушники с отличным качеством звука');
INSERT INTO public.products (id_product, pr_name, pr_price, in_stock, re_order, description) VALUES (7, 'Монитор', 399.50, 25, true, 'Широкоформатный монитор для компьютера');
INSERT INTO public.products (id_product, pr_name, pr_price, in_stock, re_order, description) VALUES (8, 'Клавиатура', 49.99, 150, true, 'Эргономичная клавиатура для комфортной работы');
INSERT INTO public.products (id_product, pr_name, pr_price, in_stock, re_order, description) VALUES (9, 'Мышь', 29.99, 300, true, 'Оптическая мышь с высокой чувствительностью');
INSERT INTO public.products (id_product, pr_name, pr_price, in_stock, re_order, description) VALUES (10, 'Принтер', 199.00, 10, true, 'Цветной лазерный принтер для быстрой печати документов');
INSERT INTO public.products (id_product, pr_name, pr_price, in_stock, re_order, description) VALUES (1, 'Ноутбук', 5000, 50, true, 'Мощный ноутбук для профессионального использования');


--
-- Data for Name: test; Type: TABLE DATA; Schema: public; Owner: test_user
--



--
-- Name: customers_id_customer_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.customers_id_customer_seq', 10, true);


--
-- Name: items_id_item_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.items_id_item_seq', 14, true);


--
-- Name: orders_id_order_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.orders_id_order_seq', 17, true);


--
-- Name: products_id_product_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.products_id_product_seq', 10, true);


--
-- Name: customers customers_last_name_first_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.customers
    ADD CONSTRAINT customers_last_name_first_name_key UNIQUE (last_name, first_name);


--
-- Name: customers customers_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.customers
    ADD CONSTRAINT customers_pkey PRIMARY KEY (id_customer);


--
-- Name: items items_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.items
    ADD CONSTRAINT items_pkey PRIMARY KEY (id_item);


--
-- Name: orders orders_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.orders
    ADD CONSTRAINT orders_pkey PRIMARY KEY (id_order);


--
-- Name: products products_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.products
    ADD CONSTRAINT products_pkey PRIMARY KEY (id_product);


--
-- Name: items calculate_total_trigger; Type: TRIGGER; Schema: public; Owner: postgres
--

CREATE TRIGGER calculate_total_trigger BEFORE INSERT ON public.items FOR EACH ROW EXECUTE FUNCTION public.calculate_total();


--
-- Name: products delete_items_trigger; Type: TRIGGER; Schema: public; Owner: postgres
--

CREATE TRIGGER delete_items_trigger BEFORE DELETE ON public.products FOR EACH ROW EXECUTE FUNCTION public.delete_items_before_product();


--
-- Name: customers new_customer; Type: TRIGGER; Schema: public; Owner: postgres
--

CREATE TRIGGER new_customer AFTER INSERT ON public.customers FOR EACH ROW EXECUTE FUNCTION public.new_customer_trigger();


--
-- Name: items update_stock_trigger; Type: TRIGGER; Schema: public; Owner: postgres
--

CREATE TRIGGER update_stock_trigger AFTER DELETE ON public.items FOR EACH ROW EXECUTE FUNCTION public.update_stock();


--
-- Name: items update_total_trigger; Type: TRIGGER; Schema: public; Owner: postgres
--

CREATE TRIGGER update_total_trigger BEFORE UPDATE OF quantity ON public.items FOR EACH ROW EXECUTE FUNCTION public.update_total();


--
-- Name: items items_id_product_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.items
    ADD CONSTRAINT items_id_product_fkey FOREIGN KEY (id_product) REFERENCES public.products(id_product);


--
-- Name: orders orders_id_customer_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.orders
    ADD CONSTRAINT orders_id_customer_fkey FOREIGN KEY (id_customer) REFERENCES public.customers(id_customer);


--
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: pg_database_owner
--

GRANT CREATE ON SCHEMA public TO read_write_role;


--
-- Name: TABLE customers; Type: ACL; Schema: public; Owner: postgres
--

GRANT SELECT ON TABLE public.customers TO read_table_role;


--
-- Name: TABLE items; Type: ACL; Schema: public; Owner: postgres
--

GRANT SELECT ON TABLE public.items TO read_table_role;


--
-- Name: TABLE orders; Type: ACL; Schema: public; Owner: postgres
--

GRANT SELECT ON TABLE public.orders TO read_table_role;


--
-- Name: TABLE products; Type: ACL; Schema: public; Owner: postgres
--

GRANT SELECT ON TABLE public.products TO read_table_role;


--
-- Name: TABLE test; Type: ACL; Schema: public; Owner: test_user
--

GRANT SELECT ON TABLE public.test TO read_table_role;


--
-- Name: safety; Type: EVENT TRIGGER; Schema: -; Owner: postgres
--

CREATE EVENT TRIGGER safety ON ddl_command_start
   EXECUTE FUNCTION public.prevent_ddl_operations();


ALTER EVENT TRIGGER safety OWNER TO postgres;

--
-- PostgreSQL database dump complete
--

