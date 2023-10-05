def number_of_rows_per_key(df, key, column_name):
    data = df.groupby(key)[key].agg(['count'])
    data.columns = [column_name]
    return data


def clean_column(column_name):
    return column_name.lower().replace(' ', '_')


@transformer
def transform(df, *args, **kwargs):
   
    
  
#criar coluna com o calculo PIB dataframe df_censoSelecionadas
    
    df_censo = df
        #Criar lista das colunas que vão ser usadas Censo
    ColunasSelecionadaCenso = ['cidade', 'uf', 'nome_capital', 'populacao estimada_pessoas', 'pib_per_capita', 'regiao', 'ano','Salario_medio_mensal']
        #Filtra para o dataframe novo somente as colunas que foram selecionadas
    df_censoSelecionadas = df_censo.filter(items=ColunasSelecionadaCenso )
  
    df = df_censoSelecionadas

    # Clean column names
    df.columns = [clean_column(col) for col in df.columns]

    return df.iloc[:1000000]
  

@test
def test_number_of_columns(df, *args) -> None:
    assert len(df.columns) >= 1, 'There needs to be at least 11 columns.'