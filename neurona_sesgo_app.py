import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Título de la app
st.title("Visualizador de la Función Sigmoide con Sesgo")

# Slider para controlar el valor del sesgo
bias = st.slider("Selecciona el valor del sesgo (bias):", min_value=-10.0, max_value=10.0, value=0.0, step=0.1)

# Definir la función sigmoide
def logsig(x):
    return 1 / (1 + np.exp(-x))

# Crear el rango de entradas
x = np.linspace(-10, 10, 400)
y = logsig(x + bias)

# Crear el gráfico
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(x, y, label=f"Sesgo = {bias}", color='blue')
ax.axvline(0, color='gray', linestyle='--')
ax.axhline(0.5, color='gray', linestyle='--')
ax.set_title("Efecto del Sesgo en la Función Sigmoide")
ax.set_xlabel("Entrada neta (net)")
ax.set_ylabel("Salida (y)")
ax.set_ylim(-0.1, 1.1)
ax.legend()
ax.grid(True)

# Mostrar el gráfico
st.pyplot(fig)
{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "11c73810-ac3e-4ceb-a8bf-10ff34551b4c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "net_i = 1.0454\n",
      "y_i = logsig(1.0454) = 0.7399\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "# Entradas\n",
    "x = np.array([0.13, 0.78, 0.66, 0.75, 1])  # Los 4 valores + el bias\n",
    "w = np.array([0.44, 0.15, 0.82, 0.24, 0.15])  # Pesos correspondientes\n",
    "\n",
    "# Cálculo de net_i - producto escalar x*w\n",
    "net_i = np.dot(x, w)\n",
    "\n",
    "# Función de activación logística (logsig)\n",
    "def logsig(x):\n",
    "    return 1 / (1 + np.exp(-x))\n",
    "\n",
    "# Salida de la neurona\n",
    "y_i = logsig(net_i)\n",
    "\n",
    "print(f\"net_i = {net_i:.4f}\")\n",
    "print(f\"y_i = logsig({net_i:.4f}) = {y_i:.4f}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b34f3209-8ecf-45d2-904b-f6360267a4d5",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
