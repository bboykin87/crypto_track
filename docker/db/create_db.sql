CREATE SCHEMA crypto;

ALTER SCHEMA crypto
    OWNER TO cwatch;

-- SEQUENCE: crypto.coins_id_seq

-- DROP SEQUENCE crypto.coins_id_seq;

CREATE SEQUENCE crypto.coins_id_seq
    INCREMENT 1
    START 2000
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

ALTER SEQUENCE crypto.coins_id_seq
    OWNER TO cwatch;

-- Table: crypto.coins

-- DROP TABLE crypto.coins;

CREATE TABLE crypto.coins
(
    id integer NOT NULL DEFAULT nextval('crypto.coins_id_seq'::regclass),
    coin character varying(10) COLLATE pg_catalog."default" NOT NULL,
    symbol character varying(10) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT coins_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE crypto.coins
    OWNER to cwatch;

GRANT SELECT ON crypto.coins TO cwatch_ronly;

-- SEQUENCE: crypto.exchange_id_seq

-- DROP SEQUENCE crypto.exchange_id_seq;

CREATE SEQUENCE crypto.exchange_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

ALTER SEQUENCE crypto.exchange_id_seq
    OWNER TO cwatch;

-- Table: crypto.exchange

-- DROP TABLE crypto.exchange;

CREATE TABLE crypto.exchange
(
    id integer NOT NULL DEFAULT nextval('crypto.exchange_id_seq'::regclass),
    exchange character varying(25) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT exchange_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE crypto.exchange
    OWNER to cwatch;

GRANT SELECT ON crypto.exchange TO cwatch_ronly;

-- SEQUENCE: crypto.holdings_id_seq

-- DROP SEQUENCE crypto.holdings_id_seq;

CREATE SEQUENCE crypto.holdings_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

ALTER SEQUENCE crypto.holdings_id_seq
    OWNER TO cwatch;

-- Table: crypto.holdings

-- DROP TABLE crypto.holdings;

CREATE TABLE crypto.holdings
(
    id integer NOT NULL DEFAULT nextval('crypto.holdings_id_seq'::regclass),
    wallet_id integer NOT NULL,
    coin_id integer NOT NULL,
    amount numeric(9,2) NOT NULL,
    CONSTRAINT holdings_pkey PRIMARY KEY (id),
    CONSTRAINT fk_holdings_coin_id FOREIGN KEY (coin_id)
        REFERENCES crypto.coins (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT fk_holdings_wallet_id FOREIGN KEY (wallet_id)
        REFERENCES crypto.wallet (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE crypto.holdings
    OWNER to cwatch;

GRANT SELECT ON crypto.holdings TO cwatch_ronly;


-- Table: crypto.prices

-- DROP TABLE crypto.prices;

CREATE TABLE crypto.prices
(
    asset character varying(30) COLLATE pg_catalog."default" NOT NULL,
    symbol character varying(10) COLLATE pg_catalog."default" NOT NULL,
    price numeric(14,8) NOT NULL,
    lst_update time without time zone,
    exchange_id integer NOT NULL,
    CONSTRAINT prices_pkey PRIMARY KEY (symbol),
    CONSTRAINT fk_exchange FOREIGN KEY (exchange_id)
        REFERENCES crypto.exchange (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE crypto.prices
    OWNER to cwatch;

GRANT SELECT ON crypto.prices TO cwatch_ronly;

-- SEQUENCE: crypto.wallet_id_seq

-- DROP SEQUENCE crypto.wallet_id_seq;

CREATE SEQUENCE crypto.wallet_id_seq
    INCREMENT 1
    START 4000
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

ALTER SEQUENCE crypto.wallet_id_seq
    OWNER TO cwatch;

-- Table: crypto.wallet

-- DROP TABLE crypto.wallet;

CREATE TABLE crypto.wallet
(
    id integer NOT NULL DEFAULT nextval('crypto.wallet_id_seq'::regclass),
    type character varying(25) COLLATE pg_catalog."default" NOT NULL,
    exchange_id integer NOT NULL,
    coin_id integer NOT NULL,
    address text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT wallet_pkey PRIMARY KEY (id),
    CONSTRAINT fk_wallet_coin_id FOREIGN KEY (coin_id)
        REFERENCES crypto.coins (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT fk_wallet_exchange_id FOREIGN KEY (exchange_id)
        REFERENCES crypto.exchange (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE crypto.wallet
    OWNER to cwatch;

create table crypto.test
(
	test text not null,
	test_number integer not null,
	test_date date DEFAULT CURRENT_DATE,
	test_time time with time zone DEFAULT CURRENT_TIME
)

TABLESPACE pg_default;

ALTER TABLE crypto.test
	OWNER TO cwatch;

GRANT SELECT ON crypto.wallet TO cwatch_ronly;

CREATE ROLE cwatch LOGIN;
ALTER ROLE cwatch WITH PASSWORD 'cbet@$@$$3$';
CREATE ROLE cwatch_ronly LOGIN;
ALTER ROLE cwatch_ronly WITH PASSWORD 'cbet@$@$$3$';
