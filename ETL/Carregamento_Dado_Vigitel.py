import io
import pandas as pd
import requests


@data_loader
def load_data_from_api(*args, **kwargs):
    url = 'https://raw.githubusercontent.com/Gabriellr/TCC-Engenharia-de-Dados-PUC-/main/Vigitel-2019-peso-rake.csv'
    url1 = 'https://raw.githubusercontent.com/Gabriellr/TCC-Engenharia-de-Dados-PUC-/main/Vigitel-2020-peso-rake.csv'
    url2 = 'https://raw.githubusercontent.com/Gabriellr/TCC-Engenharia-de-Dados-PUC-/main/Vigitel-2021-peso-rake.csv'      

    response = requests.get(url)
    urlteste = pd.read_csv(io.StringIO(response.text), sep=';')

    response1 = requests.get(url1)
    urlteste1 = pd.read_csv(io.StringIO(response1.text), sep=';')

    response2 = requests.get(url2)
    urlteste2 = pd.read_csv(io.StringIO(response2.text), sep=';')
    
    df_atividade_junt1 = pd.merge(urlteste,urlteste1, how = 'outer')
    df_atividade_junt2 = pd.merge(df_atividade_junt1,urlteste2 , how = 'outer')
    
    return  df_atividade_junt2





@test
def test_row_count(df, *args) -> None:
    assert len(df.index) >= 1, 'Verificar se os dados possuem linhas suficientes'
