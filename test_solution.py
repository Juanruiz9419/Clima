from solution import ej_1_cargar_datos_demograficos, ej_2_cargar_calidad_aire


def test_sol_1():
    df = ej_1_cargar_datos_demograficos()
    idxs = [1995, 1360, 982, 2264, 2096, 1733, 1804, 2025, 2070, 507]

    
    selected_rows = df.iloc[idxs].values

    assert len(selected_rows) == len(idxs), f"Expected {len(idxs)} rows, got {len(selected_rows)}"


def test_sol_2():
    df = ej_1_cargar_datos_demograficos()
    
    
    api_key = 'PNASBBFw1H12S3TIP6UUcw==Dg7XGrxKKKAh94O5'
    
    
    ej_2_cargar_calidad_aire(set(df["City"].tolist()), api_key)