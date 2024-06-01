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
-- Name: update_client_view(); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION public.update_client_view() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
BEGIN
    REFRESH MATERIALIZED VIEW client_view;
    RETURN NEW;
END;
$$;


ALTER FUNCTION public.update_client_view() OWNER TO postgres;

--
-- Name: update_employee_view(); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION public.update_employee_view() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
BEGIN
    REFRESH MATERIALIZED VIEW employee_view;
    RETURN NEW;
END;
$$;


ALTER FUNCTION public.update_employee_view() OWNER TO postgres;

--
-- Name: update_promotion_view(); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION public.update_promotion_view() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
BEGIN
    REFRESH MATERIALIZED VIEW promotion_view;
    RETURN NEW;
END;
$$;


ALTER FUNCTION public.update_promotion_view() OWNER TO postgres;

--
-- Name: update_record_view(); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION public.update_record_view() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
BEGIN
    REFRESH MATERIALIZED VIEW record_view;
    RETURN NEW;
END;
$$;


ALTER FUNCTION public.update_record_view() OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: client; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.client (
    client_id integer NOT NULL,
    first_name character varying(50) NOT NULL,
    last_name character varying(50) NOT NULL,
    phone_number character varying(20) NOT NULL,
    address text,
    user_id integer
);


ALTER TABLE public.client OWNER TO postgres;

--
-- Name: client_client_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.client_client_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.client_client_id_seq OWNER TO postgres;

--
-- Name: client_client_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.client_client_id_seq OWNED BY public.client.client_id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    users_id integer NOT NULL,
    username character varying(32),
    password character varying(64),
    role character varying(16)
);


ALTER TABLE public.users OWNER TO postgres;

--
-- Name: client_view; Type: MATERIALIZED VIEW; Schema: public; Owner: postgres
--

CREATE MATERIALIZED VIEW public.client_view AS
 SELECT c.client_id,
    c.first_name,
    c.last_name,
    c.phone_number,
    c.address,
    u.username AS user_username
   FROM (public.client c
     LEFT JOIN public.users u ON ((c.user_id = u.users_id)))
  WITH NO DATA;


ALTER MATERIALIZED VIEW public.client_view OWNER TO postgres;

--
-- Name: employee; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.employee (
    employee_id integer NOT NULL,
    first_name character varying(50) NOT NULL,
    last_name character varying(50) NOT NULL,
    salary numeric(10,2) NOT NULL,
    user_id integer
);


ALTER TABLE public.employee OWNER TO postgres;

--
-- Name: employee_employee_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.employee_employee_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.employee_employee_id_seq OWNER TO postgres;

--
-- Name: employee_employee_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.employee_employee_id_seq OWNED BY public.employee.employee_id;


--
-- Name: employee_view; Type: MATERIALIZED VIEW; Schema: public; Owner: postgres
--

CREATE MATERIALIZED VIEW public.employee_view AS
 SELECT e.employee_id,
    e.first_name,
    e.last_name,
    e.salary,
    u.username AS user_username
   FROM (public.employee e
     LEFT JOIN public.users u ON ((e.user_id = u.users_id)))
  WITH NO DATA;


ALTER MATERIALIZED VIEW public.employee_view OWNER TO postgres;

--
-- Name: promotion; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.promotion (
    promotion_id integer NOT NULL,
    service_id integer,
    discount numeric(5,2) NOT NULL,
    start_date date NOT NULL,
    end_date date
);


ALTER TABLE public.promotion OWNER TO postgres;

--
-- Name: promotion_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.promotion_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.promotion_id_seq OWNER TO postgres;

--
-- Name: promotion_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.promotion_id_seq OWNED BY public.promotion.promotion_id;


--
-- Name: service; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.service (
    service_id integer NOT NULL,
    name character varying(255) NOT NULL,
    cost numeric(10,2) NOT NULL,
    description text
);


ALTER TABLE public.service OWNER TO postgres;

--
-- Name: promotion_view; Type: MATERIALIZED VIEW; Schema: public; Owner: postgres
--

CREATE MATERIALIZED VIEW public.promotion_view AS
 SELECT p.promotion_id,
    s.name AS service_name,
    p.discount,
    p.start_date,
    p.end_date
   FROM (public.promotion p
     LEFT JOIN public.service s ON ((p.service_id = s.service_id)))
  WITH NO DATA;


ALTER MATERIALIZED VIEW public.promotion_view OWNER TO postgres;

--
-- Name: record; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.record (
    record_id integer NOT NULL,
    client_id integer,
    employee_id integer,
    service_id integer,
    date date,
    review text,
    status character varying(16) DEFAULT 'pending'::character varying,
    CONSTRAINT check_status CHECK (((status)::text = ANY ((ARRAY['pending'::character varying, 'accepted'::character varying, 'completed'::character varying])::text[])))
);


ALTER TABLE public.record OWNER TO postgres;

--
-- Name: record_record_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.record_record_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.record_record_id_seq OWNER TO postgres;

--
-- Name: record_record_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.record_record_id_seq OWNED BY public.record.record_id;


--
-- Name: record_view; Type: MATERIALIZED VIEW; Schema: public; Owner: postgres
--

CREATE MATERIALIZED VIEW public.record_view AS
 SELECT r.record_id,
    concat(c.first_name, ' ', c.last_name) AS client_full_name,
    concat(e.first_name, ' ', e.last_name) AS employee_full_name,
    s.name AS service_name,
    r.date,
    r.review,
    r.status
   FROM (((public.record r
     LEFT JOIN public.client c ON ((r.client_id = c.client_id)))
     LEFT JOIN public.employee e ON ((r.employee_id = e.employee_id)))
     LEFT JOIN public.service s ON ((r.service_id = s.service_id)))
  WITH NO DATA;


ALTER MATERIALIZED VIEW public.record_view OWNER TO postgres;

--
-- Name: service_employee; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.service_employee (
    service_id integer NOT NULL,
    employee_id integer NOT NULL
);


ALTER TABLE public.service_employee OWNER TO postgres;

--
-- Name: service_service_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.service_service_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.service_service_id_seq OWNER TO postgres;

--
-- Name: service_service_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.service_service_id_seq OWNED BY public.service.service_id;


--
-- Name: users_user_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.users_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.users_user_id_seq OWNER TO postgres;

--
-- Name: users_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.users_user_id_seq OWNED BY public.users.users_id;


--
-- Name: client client_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.client ALTER COLUMN client_id SET DEFAULT nextval('public.client_client_id_seq'::regclass);


--
-- Name: employee employee_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.employee ALTER COLUMN employee_id SET DEFAULT nextval('public.employee_employee_id_seq'::regclass);


--
-- Name: promotion promotion_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.promotion ALTER COLUMN promotion_id SET DEFAULT nextval('public.promotion_id_seq'::regclass);


--
-- Name: record record_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.record ALTER COLUMN record_id SET DEFAULT nextval('public.record_record_id_seq'::regclass);


--
-- Name: service service_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.service ALTER COLUMN service_id SET DEFAULT nextval('public.service_service_id_seq'::regclass);


--
-- Name: users users_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users ALTER COLUMN users_id SET DEFAULT nextval('public.users_user_id_seq'::regclass);


--
-- Data for Name: client; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.client (client_id, first_name, last_name, phone_number, address, user_id) VALUES (14, 'Коля', 'Колян', '89523652265', 'папа', 14);
INSERT INTO public.client (client_id, first_name, last_name, phone_number, address, user_id) VALUES (13, 'Вадим', 'Пичурин', '+79520000000', 'Москва', 6);


--
-- Data for Name: employee; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.employee (employee_id, first_name, last_name, salary, user_id) VALUES (16, 'Никита', 'Иванов', 20000.00, 13);


--
-- Data for Name: promotion; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.promotion (promotion_id, service_id, discount, start_date, end_date) VALUES (6, 19, 10.00, '2024-05-04', '2024-06-03');
INSERT INTO public.promotion (promotion_id, service_id, discount, start_date, end_date) VALUES (10, 17, 10.00, '2024-05-04', '2024-06-03');
INSERT INTO public.promotion (promotion_id, service_id, discount, start_date, end_date) VALUES (7, 11, 15.00, '2024-05-04', '2024-06-23');
INSERT INTO public.promotion (promotion_id, service_id, discount, start_date, end_date) VALUES (8, 18, 10.00, '2024-05-04', '2024-07-03');
INSERT INTO public.promotion (promotion_id, service_id, discount, start_date, end_date) VALUES (9, 10, 20.00, '2024-05-04', '2024-07-03');


--
-- Data for Name: record; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.record (record_id, client_id, employee_id, service_id, date, review, status) VALUES (27, 13, NULL, 13, '2024-05-04', NULL, 'pending');
INSERT INTO public.record (record_id, client_id, employee_id, service_id, date, review, status) VALUES (28, 14, NULL, 18, '2024-06-02', NULL, 'pending');
INSERT INTO public.record (record_id, client_id, employee_id, service_id, date, review, status) VALUES (29, 13, NULL, 11, '2024-05-04', NULL, 'pending');
INSERT INTO public.record (record_id, client_id, employee_id, service_id, date, review, status) VALUES (30, 13, NULL, 10, '2025-05-04', NULL, 'pending');
INSERT INTO public.record (record_id, client_id, employee_id, service_id, date, review, status) VALUES (31, 13, NULL, 16, '2024-05-23', NULL, 'pending');
INSERT INTO public.record (record_id, client_id, employee_id, service_id, date, review, status) VALUES (26, 13, 16, 10, '2025-05-04', 'None', 'accepted');


--
-- Data for Name: service; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.service (service_id, name, cost, description) VALUES (10, 'Установка ОС', 50.00, 'Установка и настройка операционной системы');
INSERT INTO public.service (service_id, name, cost, description) VALUES (11, 'Антивирусная проверка', 30.00, 'Проверка на вирусы и удаление вредоносных программ');
INSERT INTO public.service (service_id, name, cost, description) VALUES (14, 'Настройка сети', 40.00, 'Настройка локальной сети и интернета');
INSERT INTO public.service (service_id, name, cost, description) VALUES (15, 'Восстановление данных', 60.00, 'Восстановление удаленных или поврежденных данных');
INSERT INTO public.service (service_id, name, cost, description) VALUES (16, 'Обслуживание ПК', 25.00, 'Техническое обслуживание и чистка компьютера');
INSERT INTO public.service (service_id, name, cost, description) VALUES (17, 'Установка антивируса', 15.00, 'Установка и настройка антивирусной программы');
INSERT INTO public.service (service_id, name, cost, description) VALUES (18, 'Обучение', 35.00, 'Обучение основам работы с компьютером');
INSERT INTO public.service (service_id, name, cost, description) VALUES (19, 'Консультация', 20.00, 'Консультация по вопросам компьютерной безопасности');
INSERT INTO public.service (service_id, name, cost, description) VALUES (12, 'Обновление ПО1', 20.00, 'Обновление операционной системы и программного обеспечения');
INSERT INTO public.service (service_id, name, cost, description) VALUES (13, 'Обновление ПО', 20.00, 'Обновление операционной системы и программного обеспечения');


--
-- Data for Name: service_employee; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.users (users_id, username, password, role) VALUES (1, 'admin', '8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918', 'admin');
INSERT INTO public.users (users_id, username, password, role) VALUES (13, 'nikita', '8458b1d651d9faf2691730497b34526730947b758078610ec3a56ebe844fd1a3', 'employee');
INSERT INTO public.users (users_id, username, password, role) VALUES (6, 'vadim', '90e61fd0c8a40f52cba6a0a010314537c8b59f25d9356ebd838cf49be5f3168f', 'user');
INSERT INTO public.users (users_id, username, password, role) VALUES (14, 'kolya', '6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b', 'user');


--
-- Name: client_client_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.client_client_id_seq', 14, true);


--
-- Name: employee_employee_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.employee_employee_id_seq', 16, true);


--
-- Name: promotion_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.promotion_id_seq', 10, true);


--
-- Name: record_record_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.record_record_id_seq', 31, true);


--
-- Name: service_service_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.service_service_id_seq', 19, true);


--
-- Name: users_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.users_user_id_seq', 14, true);


--
-- Name: client client_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.client
    ADD CONSTRAINT client_pkey PRIMARY KEY (client_id);


--
-- Name: employee employee_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.employee
    ADD CONSTRAINT employee_pkey PRIMARY KEY (employee_id);


--
-- Name: promotion promotion_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.promotion
    ADD CONSTRAINT promotion_pkey PRIMARY KEY (promotion_id);


--
-- Name: record record_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.record
    ADD CONSTRAINT record_pkey PRIMARY KEY (record_id);


--
-- Name: service_employee service_employee_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.service_employee
    ADD CONSTRAINT service_employee_pkey PRIMARY KEY (service_id, employee_id);


--
-- Name: service service_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.service
    ADD CONSTRAINT service_pkey PRIMARY KEY (service_id);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (users_id);


--
-- Name: users users_username_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_username_key UNIQUE (username);


--
-- Name: client client_trigger; Type: TRIGGER; Schema: public; Owner: postgres
--

CREATE TRIGGER client_trigger AFTER INSERT OR DELETE OR UPDATE ON public.client FOR EACH STATEMENT EXECUTE FUNCTION public.update_client_view();


--
-- Name: employee employee_trigger; Type: TRIGGER; Schema: public; Owner: postgres
--

CREATE TRIGGER employee_trigger AFTER INSERT OR DELETE OR UPDATE ON public.employee FOR EACH STATEMENT EXECUTE FUNCTION public.update_employee_view();


--
-- Name: promotion promotion_trigger; Type: TRIGGER; Schema: public; Owner: postgres
--

CREATE TRIGGER promotion_trigger AFTER INSERT OR DELETE OR UPDATE ON public.promotion FOR EACH STATEMENT EXECUTE FUNCTION public.update_promotion_view();


--
-- Name: record record_trigger; Type: TRIGGER; Schema: public; Owner: postgres
--

CREATE TRIGGER record_trigger AFTER INSERT OR DELETE OR UPDATE ON public.record FOR EACH STATEMENT EXECUTE FUNCTION public.update_record_view();


--
-- Name: client client_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.client
    ADD CONSTRAINT client_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(users_id);


--
-- Name: employee employee_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.employee
    ADD CONSTRAINT employee_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(users_id);


--
-- Name: promotion promotion_service_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.promotion
    ADD CONSTRAINT promotion_service_id_fkey FOREIGN KEY (service_id) REFERENCES public.service(service_id);


--
-- Name: record record_client_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.record
    ADD CONSTRAINT record_client_id_fkey FOREIGN KEY (client_id) REFERENCES public.client(client_id);


--
-- Name: record record_employee_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.record
    ADD CONSTRAINT record_employee_id_fkey FOREIGN KEY (employee_id) REFERENCES public.employee(employee_id);


--
-- Name: record record_service_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.record
    ADD CONSTRAINT record_service_id_fkey FOREIGN KEY (service_id) REFERENCES public.service(service_id);


--
-- Name: service_employee service_employee_employee_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.service_employee
    ADD CONSTRAINT service_employee_employee_id_fkey FOREIGN KEY (employee_id) REFERENCES public.employee(employee_id);


--
-- Name: service_employee service_employee_service_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.service_employee
    ADD CONSTRAINT service_employee_service_id_fkey FOREIGN KEY (service_id) REFERENCES public.service(service_id);


--
-- Name: client_view; Type: MATERIALIZED VIEW DATA; Schema: public; Owner: postgres
--

REFRESH MATERIALIZED VIEW public.client_view;


--
-- Name: employee_view; Type: MATERIALIZED VIEW DATA; Schema: public; Owner: postgres
--

REFRESH MATERIALIZED VIEW public.employee_view;


--
-- Name: promotion_view; Type: MATERIALIZED VIEW DATA; Schema: public; Owner: postgres
--

REFRESH MATERIALIZED VIEW public.promotion_view;


--
-- Name: record_view; Type: MATERIALIZED VIEW DATA; Schema: public; Owner: postgres
--

REFRESH MATERIALIZED VIEW public.record_view;


--
-- PostgreSQL database dump complete
--

