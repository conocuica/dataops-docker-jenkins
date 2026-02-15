import pandas as pd

data = {
    "Empleado": ["Ana", "Luis", "Carlos"],
    "Ventas": [1000, 1500, 2000]
}

df = pd.DataFrame(data)
df["Comision"] = df["Ventas"] * 0.10

df.to_excel("comisiones.xlsx", index=False)

print("Archivo generado correctamente")
