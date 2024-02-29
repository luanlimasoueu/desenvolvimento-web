import streamlit as st
import pandas as pd

a = 1
b = 2
c =  a + b
st.markdown("As informações necessárias")
st.markdown(a)
st.markdown(c)

def contar( e, f):
    if e > f:
        return f
    else:
        return e

d = contar(a, b)
st.markdown(d)



j = [
   {
     'titulo': 'JSON x XML',
     'resumo': 'o duelo de dois modelos de representação de informações',
     'ano': 2012,
     'genero': ['aventura', 'ação', 'ficção']
    },
   {
     'titulo': 'JSON James',
     'resumo': 'a história de uma lenda do velho oeste',
     'ano': 2012,
     'genero': ['western']
    }
]

st.markdown(j[0]['titulo'])

df = pd.DataFrame({'calorias':[200, 350, 550], 'gordura (%)':[0, 6, 15]})
st.markdown(df['calorias'][0])