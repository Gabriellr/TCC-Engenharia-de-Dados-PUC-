CREATE TABLE IF NOT EXISTS puc_tcc_atividade_fisica.atividade_fisica
(
ano smallint,
cidade smallint,
civil text COLLATE pg_catalog."default",
idade smallint,
sexo text COLLATE pg_catalog."default",
grau_escolaridade text COLLATE pg_catalog."default",
peso smallint,
altura smallint,
pratica_exercicio text COLLATE pg_catalog."default",
tipo_exercicio text COLLATE pg_catalog."default",
pratica_exercicio_1_vez_na_semana double precision,
frequencia_exercicio text COLLATE pg_catalog."default",
duracao_exercicio text COLLATE pg_catalog."default",
cor text COLLATE pg_catalog."default",
imc double precision
)


CREATE TABLE IF NOT EXISTS puc_tcc_atividade_fisica.cidade
(
cidade smallint,
uf text COLLATE pg_catalog."default",
nome_capital text COLLATE pg_catalog."default",
pib_per_capita text COLLATE pg_catalog."default",
regiao text COLLATE pg_catalog."default",
ano smallint,
salario_medio_mensal text COLLATE pg_catalog."default")
