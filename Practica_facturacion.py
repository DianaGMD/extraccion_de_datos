import pandas as pd

df = pd.read_excel("datos_facturacion.xlsx")
print(df.head())

filtro1=df[(df["CVE_CLPV"] >= 1000) & (df["CVE_CLPV"]<=2000)]
print(filtro1)
filtro1.to_csv("Practica_facturacion1.csv")

filtro2 = df[~(df["CVE_VEND"] == 5.0 ) & ~(df["CVE_VEND"] == 4.0)]
print(filtro2)
filtro2.to_csv("Practica_facturacion2.csv")

filtro3=df[df["FECHA_ENT"] == '2022-28-2']
print(filtro3)
filtro3.to_csv("Practica_facturacion3.csv")


