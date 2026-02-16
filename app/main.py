import pandas as pd

data = {
    "Empleado": ["Ana", "Luis", "Carlos"],
    "Ventas": [1000, 1500, 2000]
}

df = pd.DataFrame(data)
df["Comision"] = df["Ventas"] * 0.16

# Crear carpeta output si no existe
os.makedirs("/app/output", exist_ok=True)

df.to_excel("/app/output/comisiones.xlsx", index=False)

#df.to_excel("comisiones.xlsx", index=False)

print("Archivo generado correctamente")
    