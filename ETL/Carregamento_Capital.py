import io
import pandas as pd
import requests


@data_loader
def load_data_from_api(*args, **kwargs):
    url = 'https://raw.githubusercontent.com/Gabriellr/TCC-Engenharia-de-Dados-PUC-/main/Capitais_Censo.csv'
    response = requests.get(url)
    return pd.read_csv(io.StringIO(response.text), sep=',')




@test
def test_row_count(df, *args) -> None:
    assert len(df.index) >= 1, 'Verificar se os dados possuem linhas suficientes'
