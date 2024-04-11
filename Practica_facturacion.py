import pandas as pd

df = pd.read_excel("datos_facturacion.xlsx")
print(df.head())

#CVE_CLPV      (valores: 1000 a 2000)
filtro1=df[(df["CVE_CLPV"] >= 1000) & (df["CVE_CLPV"]<=2000)]
#print(filtro1)
filtro1.to_csv("Practica_facturacion1.csv")

#CVE_VEND     (Todas las claves excepto “5” y “4”)
filtro2 = df[~(df["CVE_VEND"] == 5.0 ) & ~(df["CVE_VEND"] == 4.0)]
#print(filtro2)
filtro2.to_csv("Practica_facturacion2.csv")

#FECHA_ENT   (Fechas de “28/02/2022”)
filtro3=df[df["FECHA_ENT"] == '2022-28-2']
#print(filtro3)
filtro3.to_csv("Practica_facturacion3.csv")

#CAN_TOT       (Cantidades menores a 5951.7)   o  STATUS (“E”)
filtro4=df[(df["CAN_TOT"] < 5951.7)| (df["STATUS"] == "E")]
print(filtro4)
filtro4.to_csv("Practica_facturacion4.csv")





