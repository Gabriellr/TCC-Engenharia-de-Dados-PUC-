def number_of_rows_per_key(df, key, column_name):
    data = df.groupby(key)[key].agg(['count'])
    data.columns = [column_name]
    return data


def clean_column(column_name):
    return column_name.lower().replace(' ', '_')


@transformer
def transform(df, *args, **kwargs):
   
    
    dados2 = df
    ColunasSelecionada = ['ordem', 'ano', 'cidade', 'civil','q6', 'q7', 'q8a', 'q9', 'q11', 'q42', 'q43a', 'q44', 'q45','q46', 'q69']
    df_atividadeSelecionadas = dados2.filter(items=ColunasSelecionada )
    df_atividadeSelecionadas.rename(columns={'q6':'idade','q7':'sexo','q8a':'grau_escolaridade','q9':'peso','q11':'altura','q42':'pratica_exercicio','q43a': 'tipo_exercicio','q44':'pratica_exercicio_1_vez_na_semana', 'q45':'frequencia_exercicio', 'q46':'duracao_exercicio', 'q69':'cor'}, inplace =True)
    df_atividadeSelecionadas['imc'] = df_atividadeSelecionadas.apply(
               lambda row: round(row.peso / (((row.altura * row.altura)/1000)*0.1),0), axis=1)
    df_atividadeSelecionadas['pratica_exercicio'].replace(1,'sim', inplace =True)
    df_atividadeSelecionadas['pratica_exercicio'].replace(2,'nao', inplace =True)


    df_atividadeSelecionadas['tipo_exercicio'].replace(1,'caminhada (não vale deslocamento para trabalho)', inplace =True)
    df_atividadeSelecionadas['tipo_exercicio'].replace(2,'caminhada em esteira', inplace =True)
    df_atividadeSelecionadas['tipo_exercicio'].replace(3,'corrida (cooper)', inplace =True)
    df_atividadeSelecionadas['tipo_exercicio'].replace(4,'corrida em esteira', inplace =True)
    df_atividadeSelecionadas['tipo_exercicio'].replace(5,'musculação', inplace =True)
    df_atividadeSelecionadas['tipo_exercicio'].replace(6,'ginástica aeróbica (spinning, step, jump)', inplace =True)
    df_atividadeSelecionadas['tipo_exercicio'].replace(7,'hidroginástica', inplace =True)
    df_atividadeSelecionadas['tipo_exercicio'].replace(8,'ginástica em geral (alongamento, pilates, ioga)', inplace =True)
    df_atividadeSelecionadas['tipo_exercicio'].replace(9,'natação', inplace =True)
    df_atividadeSelecionadas['tipo_exercicio'].replace(10,'artes marciais e luta (jiu-jitsu, karatê, judô, boxe, muay thai, capoeira)', inplace =True)
    df_atividadeSelecionadas['tipo_exercicio'].replace(11,'bicicleta (inclui ergométrica)', inplace =True)
    df_atividadeSelecionadas['tipo_exercicio'].replace(12,'futebol/futsal', inplace =True)
    df_atividadeSelecionadas['tipo_exercicio'].replace(13,'basquetebol', inplace =True)
    df_atividadeSelecionadas['tipo_exercicio'].replace(14,'voleibol/futevolei', inplace =True)
    df_atividadeSelecionadas['tipo_exercicio'].replace(15,'tênis', inplace =True)
    df_atividadeSelecionadas['tipo_exercicio'].replace(16,'dança (balé, dança de salão, dança do ventre)', inplace =True)
    df_atividadeSelecionadas['tipo_exercicio'].replace(17,'outros', inplace =True)
    df_atividadeSelecionadas['grau_escolaridade'].replace(1,'curso primário', inplace =True)
    df_atividadeSelecionadas['grau_escolaridade'].replace(2,'admissão', inplace =True)
    df_atividadeSelecionadas['grau_escolaridade'].replace(3,'curso ginasial ou ginásio', inplace =True)
    df_atividadeSelecionadas['grau_escolaridade'].replace(4,'1º grau ou fundamental ou supletivo de 1º grau', inplace =True)
    df_atividadeSelecionadas['grau_escolaridade'].replace(5,'2º grau ou colégio ou técnico ou normal ou científico científico ou ensino médio ou supletivo de 2º grau', inplace =True)
    df_atividadeSelecionadas['grau_escolaridade'].replace(6,'3º grau ou curso superior', inplace =True)
    df_atividadeSelecionadas['grau_escolaridade'].replace(7,'pós-graduação (especialização, mestrado, doutorado)', inplace =True)
    df_atividadeSelecionadas['grau_escolaridade'].replace(8,'nunca estudou', inplace =True)
    df_atividadeSelecionadas['grau_escolaridade'].replace(777,'não sabe', inplace =True)
    df_atividadeSelecionadas['grau_escolaridade'].replace(888,'não quis responder', inplace =True)
    df_atividadeSelecionadas['civil'].replace(1,'solteiro', inplace =True)
    df_atividadeSelecionadas['civil'].replace(2,'casado legalmente', inplace =True)
    df_atividadeSelecionadas['civil'].replace(3,'tem união estável há mais de seis meses', inplace =True)
    df_atividadeSelecionadas['civil'].replace(4,'viúvo', inplace =True)
    df_atividadeSelecionadas['civil'].replace(5,'separado ou divorciado', inplace =True)
    df_atividadeSelecionadas['civil'].replace(888,'não quis informar', inplace =True)


#formate a coluna frequencia exercicio
    df_atividadeSelecionadas['frequencia_exercicio'].replace(1,'1 a 2 dias por semana', inplace =True)
    df_atividadeSelecionadas['frequencia_exercicio'].replace(2,'3 a 4 dias por semana', inplace =True)
    df_atividadeSelecionadas['frequencia_exercicio'].replace(3,'5 a 6 dias por semana', inplace =True)
    df_atividadeSelecionadas['frequencia_exercicio'].replace(4,'todos os dias ( inclusive sábado e domingo)', inplace =True)


#formate a coluna duracao exercicio
    df_atividadeSelecionadas['duracao_exercicio'].replace(1,'menos que 10 minutos', inplace =True)
    df_atividadeSelecionadas['duracao_exercicio'].replace(2,'entre 10 e 19 minutos', inplace =True)
    df_atividadeSelecionadas['duracao_exercicio'].replace(3,'entre 20 e 29 minutos', inplace =True)
    df_atividadeSelecionadas['duracao_exercicio'].replace(4,'entre 30 e 39 minutos', inplace =True)
    df_atividadeSelecionadas['duracao_exercicio'].replace(5,'entre 40 e 49 minutos', inplace =True)
    df_atividadeSelecionadas['duracao_exercicio'].replace(6,'entre 50 e 59 minutos', inplace =True)
    df_atividadeSelecionadas['duracao_exercicio'].replace(7,'60 minutos ou mais', inplace =True)


#formate a coluna cor
    df_atividadeSelecionadas['cor'].replace(1,'branca', inplace =True)
    df_atividadeSelecionadas['cor'].replace(2,'preta', inplace =True)
    df_atividadeSelecionadas['cor'].replace(3,'amarela', inplace =True)
    df_atividadeSelecionadas['cor'].replace(4,'parda', inplace =True)
    df_atividadeSelecionadas['cor'].replace(5,'indígena', inplace =True)
    df_atividadeSelecionadas['cor'].replace(80,'Morena', inplace =True)
    df_atividadeSelecionadas['cor'].replace(777,'não sabe', inplace =True)
    df_atividadeSelecionadas['cor'].replace(888,'não quis informar', inplace =True)

    df_atividadeSelecionadas['sexo'].replace(1,'masculino', inplace =True)
    df_atividadeSelecionadas['sexo'].replace(2,'feminino', inplace =True)

    df = df_atividadeSelecionadas


    #df_atividade_junt = df.drop(['chave'], axis = 1) # remove coluna 


    # Clean column names
    df.columns = [clean_column(col) for col in df.columns]

    return df.iloc[:1000000]


@test
def test_number_of_columns(df, *args) -> None:
    assert len(df.columns) >= 1, 'There needs to be at least 11 columns.'