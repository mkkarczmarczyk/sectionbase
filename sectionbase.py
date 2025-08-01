import streamlit as st
import pandas as pd

st.set_page_config(page_title="Profile stalowe", page_icon="🧱")

st.title("🧱 Przegląd profili stalowych")
st.markdown("Wybierz typ i nazwę profilu, aby zobaczyć jego parametry geometryczne.")

# Wczytywanie danych z pliku CSV
df = pd.read_csv("profile_stalowe.csv")

# Wybór typu profilu
typ_wybrany = st.radio("Wybierz typ profilu:", df["Typ"].unique())

# Lista nazw profili zależna od typu
dostepne_nazwy = df[df["Typ"] == typ_wybrany]["Nazwa"].unique()
nazwa_wybrana = st.selectbox("Wybierz nazwę profilu:", dostepne_nazwy)

# Wyświetlenie danych
dane_prof = df[df["Nazwa"] == nazwa_wybrana].T
dane_prof.columns = ["Wartość"]
st.subheader("📐 Parametry geometryczne")
st.table(dane_prof)
