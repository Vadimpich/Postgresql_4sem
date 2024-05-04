--
-- PostgreSQL database dump
--

-- Dumped from database version 16.1
-- Dumped by pg_dump version 16.1

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
    CREATE OR REPLACE VIEW client_view AS
    SELECT c.client_id, c.first_name, c.last_name, c.phone_number, c.address, u.username AS user_username
    FROM client c
    JOIN users u ON c.user_id = u.user_id;

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
    CREATE OR REPLACE VIEW employee_view AS
    SELECT e.employee_id, e.first_name, e.last_name, e.salary, u.username AS user_username
    FROM employee e
    JOIN users u ON e.user_id = u.user_id;

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
    CREATE OR REPLACE VIEW promotion_view AS
    SELECT p.promotion_id, s.name AS service_name, p.discount, p.start_date, p.end_date
    FROM promotion p
    JOIN service s ON p.service_id = s.service_id;

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
    CREATE OR REPLACE VIEW record_view AS
    SELECT r.record_id, CONCAT(c.first_name, ' ', c.last_name) AS client_full_name,
           CONCAT(e.first_name, ' ', e.last_name) AS employee_full_name,
           s.name AS service_name, r.date, r.review, r.status
    FROM record r
    JOIN client c ON r.client_id = c.client_id
    JOIN employee e ON r.employee_id = e.employee_id
    JOIN service s ON r.service_id = s.service_id;

    RETURN NEW;
END;
$$;


ALTER FUNCTION public.update_record_view() OWNER TO postgres;

--
-- Name: update_service_employee_view(); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION public.update_service_employee_view() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
BEGIN
    CREATE OR REPLACE VIEW service_employee_view AS
    SELECT se.service_id, se.employee_id
    FROM service_employee se;

    RETURN NEW;
END;
$$;


ALTER FUNCTION public.update_service_employee_view() OWNER TO postgres;

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
-- Name: client_view; Type: VIEW; Schema: public; Owner: postgres
--

CREATE VIEW public.client_view AS
 SELECT c.client_id,
    c.first_name,
    c.last_name,
    c.phone_number,
    c.address,
    u.username AS user_username
   FROM (public.client c
     JOIN public.users u ON ((c.user_id = u.users_id)));


ALTER VIEW public.client_view OWNER TO postgres;

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
-- Name: employee_view; Type: VIEW; Schema: public; Owner: postgres
--

CREATE VIEW public.employee_view AS
 SELECT e.employee_id,
    e.first_name,
    e.last_name,
    e.salary,
    u.username AS user_username
   FROM (public.employee e
     JOIN public.users u ON ((e.user_id = u.users_id)));


ALTER VIEW public.employee_view OWNER TO postgres;

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
-- Name: promotion_view; Type: VIEW; Schema: public; Owner: postgres
--

CREATE VIEW public.promotion_view AS
 SELECT p.promotion_id,
    s.name AS service_name,
    p.discount,
    p.start_date,
    p.end_date
   FROM (public.promotion p
     JOIN public.service s ON ((p.service_id = s.service_id)));


ALTER VIEW public.promotion_view OWNER TO postgres;

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
    status character varying(16)
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
-- Name: record_view; Type: VIEW; Schema: public; Owner: postgres
--

CREATE VIEW public.record_view AS
 SELECT r.record_id,
    concat(c.first_name, ' ', c.last_name) AS client_full_name,
    concat(e.first_name, ' ', e.last_name) AS employee_full_name,
    s.name AS service_name,
    r.date,
    r.review,
    r.status
   FROM (((public.record r
     JOIN public.client c ON ((r.client_id = c.client_id)))
     JOIN public.employee e ON ((r.employee_id = e.employee_id)))
     JOIN public.service s ON ((r.service_id = s.service_id)));


ALTER VIEW public.record_view OWNER TO postgres;

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

INSERT INTO public.client (client_id, first_name, last_name, phone_number, address, user_id) VALUES (1, 'Emma', 'Smith', '123-456-7890', '123 Main St', 1);
INSERT INTO public.client (client_id, first_name, last_name, phone_number, address, user_id) VALUES (2, 'Liam', 'Johnson', '987-654-3210', '456 Elm St', 2);
INSERT INTO public.client (client_id, first_name, last_name, phone_number, address, user_id) VALUES (3, 'Olivia', 'Williams', '555-123-4567', '789 Oak St', 3);
INSERT INTO public.client (client_id, first_name, last_name, phone_number, address, user_id) VALUES (4, 'Noah', 'Brown', '111-222-3333', '101 Pine St', 4);
INSERT INTO public.client (client_id, first_name, last_name, phone_number, address, user_id) VALUES (5, 'Ava', 'Jones', '444-555-6666', '202 Maple St', 5);
INSERT INTO public.client (client_id, first_name, last_name, phone_number, address, user_id) VALUES (6, 'Mama', 'Papa', '123', '123', 1);
INSERT INTO public.client (client_id, first_name, last_name, phone_number, address, user_id) VALUES (7, 'Вадим', 'пичурин', '89898908909', 'Адрес', 6);
INSERT INTO public.client (client_id, first_name, last_name, phone_number, address, user_id) VALUES (8, 'qwe', 'qwe', 'qwe', 'qwe', 8);
INSERT INTO public.client (client_id, first_name, last_name, phone_number, address, user_id) VALUES (9, 'qwe', 'qwe', 'qwe', 'qwe', 10);
INSERT INTO public.client (client_id, first_name, last_name, phone_number, address, user_id) VALUES (10, 'qwe', 'qwe', 'qwe', 'qwe', 11);
INSERT INTO public.client (client_id, first_name, last_name, phone_number, address, user_id) VALUES (11, 'qweqew', 'qweeqwwe', 'qeqwqwe', 'qqweq', 12);


--
-- Data for Name: employee; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.employee (employee_id, first_name, last_name, salary, user_id) VALUES (11, 'James', 'Wilson', 3000.00, 1);
INSERT INTO public.employee (employee_id, first_name, last_name, salary, user_id) VALUES (12, 'Sophia', 'Anderson', 2500.00, 2);
INSERT INTO public.employee (employee_id, first_name, last_name, salary, user_id) VALUES (13, 'William', 'Taylor', 2800.00, 3);
INSERT INTO public.employee (employee_id, first_name, last_name, salary, user_id) VALUES (14, 'Isabella', 'Thomas', 3200.00, 4);
INSERT INTO public.employee (employee_id, first_name, last_name, salary, user_id) VALUES (15, 'Michael', 'Clark', 2700.00, 5);


--
-- Data for Name: promotion; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.promotion (promotion_id, service_id, discount, start_date, end_date) VALUES (1, 1, 10.00, '2024-05-01', '2024-06-01');
INSERT INTO public.promotion (promotion_id, service_id, discount, start_date, end_date) VALUES (2, 2, 5.00, '2024-05-10', '2024-06-10');
INSERT INTO public.promotion (promotion_id, service_id, discount, start_date, end_date) VALUES (3, 3, 15.00, '2024-05-05', '2024-06-05');
INSERT INTO public.promotion (promotion_id, service_id, discount, start_date, end_date) VALUES (4, 4, 20.00, '2024-05-15', '2024-06-15');
INSERT INTO public.promotion (promotion_id, service_id, discount, start_date, end_date) VALUES (5, 5, 10.00, '2024-05-20', '2024-06-20');


--
-- Data for Name: record; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.record (record_id, client_id, employee_id, service_id, date, review, status) VALUES (11, 1, 11, 1, '2024-05-02', 'Great service!', 'completed');
INSERT INTO public.record (record_id, client_id, employee_id, service_id, date, review, status) VALUES (12, 2, 12, 2, '2024-05-05', 'Nice job!', 'completed');
INSERT INTO public.record (record_id, client_id, employee_id, service_id, date, review, status) VALUES (13, 3, 13, 3, '2024-05-08', 'Amazing massage!', 'completed');
INSERT INTO public.record (record_id, client_id, employee_id, service_id, date, review, status) VALUES (14, 4, 14, 4, '2024-05-10', 'Excellent facial!', 'completed');
INSERT INTO public.record (record_id, client_id, employee_id, service_id, date, review, status) VALUES (15, 5, 15, 5, '2024-05-15', 'Wonderful pedicure!', 'completed');
INSERT INTO public.record (record_id, client_id, employee_id, service_id, date, review, status) VALUES (16, 7, NULL, 1, '2000-01-01', NULL, NULL);
INSERT INTO public.record (record_id, client_id, employee_id, service_id, date, review, status) VALUES (17, 7, NULL, 1, '2000-01-01', NULL, NULL);
INSERT INTO public.record (record_id, client_id, employee_id, service_id, date, review, status) VALUES (18, 7, NULL, 2, '2000-01-01', NULL, NULL);
INSERT INTO public.record (record_id, client_id, employee_id, service_id, date, review, status) VALUES (19, 7, NULL, 3, '2024-01-02', NULL, NULL);


--
-- Data for Name: service; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.service (service_id, name, cost, description) VALUES (1, 'Pedicure1', 25.00, 'Foot treatment');
INSERT INTO public.service (service_id, name, cost, description) VALUES (4, 'Pedicure1', 25.00, 'Foot treatment');
INSERT INTO public.service (service_id, name, cost, description) VALUES (5, 'Pedicure1', 25.00, 'Foot treatment');
INSERT INTO public.service (service_id, name, cost, description) VALUES (2, 'Pedicure2', 25.00, 'Foot treatment');
INSERT INTO public.service (service_id, name, cost, description) VALUES (3, 'Pedicure3', 25.00, 'Foot treatment');


--
-- Data for Name: service_employee; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.service_employee (service_id, employee_id) VALUES (1, 11);
INSERT INTO public.service_employee (service_id, employee_id) VALUES (2, 12);
INSERT INTO public.service_employee (service_id, employee_id) VALUES (3, 13);
INSERT INTO public.service_employee (service_id, employee_id) VALUES (4, 14);
INSERT INTO public.service_employee (service_id, employee_id) VALUES (5, 15);
INSERT INTO public.service_employee (service_id, employee_id) VALUES (1, 13);


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.users (users_id, username, password, role) VALUES (2, 'bob', 'securepass', 'user');
INSERT INTO public.users (users_id, username, password, role) VALUES (3, 'charlie', '123456', 'user');
INSERT INTO public.users (users_id, username, password, role) VALUES (4, 'david', 'pass123', 'user');
INSERT INTO public.users (users_id, username, password, role) VALUES (5, 'eve', 'password', 'user');
INSERT INTO public.users (users_id, username, password, role) VALUES (1, 'admin', '8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918', 'admin');
INSERT INTO public.users (users_id, username, password, role) VALUES (6, 'vadim', '90e61fd0c8a40f52cba6a0a010314537c8b59f25d9356ebd838cf49be5f3168f', 'user');
INSERT INTO public.users (users_id, username, password, role) VALUES (8, 'vadim1', '90e61fd0c8a40f52cba6a0a010314537c8b59f25d9356ebd838cf49be5f3168f', 'user');
INSERT INTO public.users (users_id, username, password, role) VALUES (9, 'vadim2', '90e61fd0c8a40f52cba6a0a010314537c8b59f25d9356ebd838cf49be5f3168f', 'user');
INSERT INTO public.users (users_id, username, password, role) VALUES (10, 'qwe', '489cd5dbc708c7e541de4d7cd91ce6d0f1613573b7fc5b40d3942ccb9555cf35', 'user');
INSERT INTO public.users (users_id, username, password, role) VALUES (11, 'qweqwe', '1b6606fde7e896803a9fb49351a6a5cde853aa042e7c8d2ee71b62b95901fff0', 'user');
INSERT INTO public.users (users_id, username, password, role) VALUES (12, 'ewqeqwe', '20fca05fb9197294b38d4bbe476e9dac53a2dab304da654e4baddd4fbe52658c', 'user');


--
-- Name: client_client_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.client_client_id_seq', 11, true);


--
-- Name: employee_employee_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.employee_employee_id_seq', 15, true);


--
-- Name: promotion_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.promotion_id_seq', 5, true);


--
-- Name: record_record_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.record_record_id_seq', 19, true);


--
-- Name: service_service_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.service_service_id_seq', 8, true);


--
-- Name: users_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.users_user_id_seq', 12, true);


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
-- Name: service_employee service_employee_trigger; Type: TRIGGER; Schema: public; Owner: postgres
--

CREATE TRIGGER service_employee_trigger AFTER INSERT OR DELETE OR UPDATE ON public.service_employee FOR EACH STATEMENT EXECUTE FUNCTION public.update_service_employee_view();


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
-- PostgreSQL database dump complete
--

