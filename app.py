


# %%

def tarief(dagkwh, nachtkwh):
    dag_ppkwh = 0.33
    nacht_ppkwh = 0.22
    subtotaal = dag_ppkwh * dagkwh + nacht_ppkwh * nachtkwh
    btw = 0.21*subtotaal
    totaal = btw + subtotaal
    
    return totaal

dag_input = float(input("Geef je elektriciteitsverbruik (kWh) overdag:"))
nacht_input = float(input("Geef je elektriciteitsverbruik (kWh) overnacht:"))

kost = tarief(dag_input, nacht_input)

print("Je energiekost is ", round(kost,2), "euro")

import matplotlib.pyplot as plt

dagen = ["Ma", "Di", "Wo", "Do", "Vr", "Za", "Zo"]
verbruik = [3.2, 4.0, 2.5, 3.8, 4.1, 2.2, 2.9]  # kWh per dag

plt.plot(dagen, verbruik, marker='o')
plt.title("Elektriciteitsverbruik per dag")
plt.xlabel("Dag")
plt.ylabel("Verbruik (kWh)")
plt.grid(True)
plt.show()

import streamlit as st

st.title("🔌 Elektriciteitskost Berekenen")

verbruik = st.number_input("Geef je verbruik in kWh:", min_value=0.0, step=0.1)

prijs_per_kwh = 0.29
btw_percentage = 0.21

if verbruik > 0:
    prijs = prijs_per_kwh * verbruik
    btw = prijs * btw_percentage
    totaal = prijs + btw

    st.write(f"💰 Prijs zonder BTW: €{prijs:.2f}")
    st.write(f"🧾 BTW (21%): €{btw:.2f}")
    st.write(f"✅ Totale kost: **€{totaal:.2f}**")

