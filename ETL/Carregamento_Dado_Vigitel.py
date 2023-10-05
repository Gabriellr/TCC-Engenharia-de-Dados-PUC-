import io
import pandas as pd
import requests


@data_loader
def load_data_from_api(*args, **kwargs):
    url = 'https://raw.githubusercontent.com/Gabriellr/TCC-Engenharia-de-Dados-PUC-/main/Vigitel-2019-peso-rake.csv'
    url1 = 'https://raw.githubusercontent.com/Gabriellr/TCC-Engenharia-de-Dados-PUC-/main/Vigitel-2020-peso-rake.csv'
    url2 = 'https://raw.githubusercontent.com/Gabriellr/TCC-Engenharia-de-Dados-PUC-/main/Vigitel-2021-peso-rake.csv'      
    url3 = 'https://raw.githubusercontent.com/Gabriellr/TCC-Engenharia-de-Dados-PUC-/main/Vigitel-2018-peso-rake.csv'
    response = requests.get(url)
    urlteste = pd.read_csv(io.StringIO(response.text), sep=';')

    response1 = requests.get(url1)
    urlteste1 = pd.read_csv(io.StringIO(response1.text), sep=';')

    response2 = requests.get(url2)
    urlteste2 = pd.read_csv(io.StringIO(response2.text), sep=';')

    response3 = requests.get(url3)
    urlteste3 = pd.read_csv(io.StringIO(response3.text), sep=';')
    
    df_atividade_junt1 = pd.merge(urlteste,urlteste1, how = 'outer')
    df_atividade_junt2 = pd.merge(urlteste2,urlteste3, how = 'outer')

    df_atividade_junt3 = pd.merge(df_atividade_junt1,df_atividade_junt2 , how = 'outer')
    
    return  df_atividade_junt3





@test
def test_row_count(df, *args) -> None:
    assert len(df.index) >= 1, 'Verificar se os dados possuem linhas suficientes'
