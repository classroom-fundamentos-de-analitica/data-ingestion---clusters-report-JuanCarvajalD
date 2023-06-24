import pandas as pd
import numpy as np
import re

def ingest_data():
    df_temp = pd.read_fwf("clusters_report.txt", skiprows=4, colspecs='infer', names=['1', '2', '3', '4'])
    df = pd.DataFrame(columns=['cluster', 'cantidad_de_palabras_clave', 'porcentaje_de_palabras_clave', 'principales_palabras_clave'])

    for indice in range(len(df_temp)):
        if not np.isnan(df_temp.iloc[indice]['1']):
            df.loc[len(df.index)] = [df_temp.iloc[indice]['1'], df_temp.iloc[indice]['2'], df_temp.iloc[indice]['3'], df_temp.iloc[indice]['4']]
        else:
            df.at[len(df.index)-1, 'principales_palabras_clave'] += " " + df_temp.iloc[indice]['4']

    df['principales_palabras_clave'] = df['principales_palabras_clave'].apply(lambda x: re.sub('\s+', ' ', x))
    df['principales_palabras_clave'] = df['principales_palabras_clave'].apply(lambda x: re.sub(',\s*', ', ', x))
    df['principales_palabras_clave'] = df['principales_palabras_clave'].apply(lambda x: x.rstrip('.'))

    df['cluster'] = df['cluster'].apply(int)
    df['cantidad_de_palabras_clave'] = df['cantidad_de_palabras_clave'].apply(int)

    df['porcentaje_de_palabras_clave'] = df['porcentaje_de_palabras_clave'].apply(lambda x: float(re.sub(',', '.', re.findall('\d+,\d+', x)[0])))

    return df

