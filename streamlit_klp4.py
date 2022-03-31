import pandas as pd
import datetime
import streamlit as st
def data_idn(d=0,data_all=[]):
    data_lok=data_all[(data_all['date']== d) & (data_all['location'] == 'Indonesia')]
    if(len(data_lok.index)==0):
        return 0
    data_lok=data_lok['total cases']
    return data_lok
def data_tgjum(d,data_all):
    data_lok=data_all[(data_all['date']== d) & (data_all['location'] != 'Indonesia')]
    data_lok=data_lok[['location','new cases','new deaths','new recovered','total cases']]
    return data_lok
def data_map(d=0,data_all=[]):
    if(d==0):
        return data_all[data_all['location'] != 'Indonesia']
    data_lok=data_all[(data_all['date']== d) & (data_all['location'] != 'Indonesia')]
    return data_lok
@st.cache
def load_data(nrows):
    data = pd.read_csv('covid_19_indonesia_time_series_all.csv', nrows=nrows,index_col=None)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data['date'] =pd.to_datetime(data['date'])
    return data
st.title('Data Covid Di indonesia')
data_load_state = st.text('Loading data...')
data = load_data(10000)
data_load_state.text("Data berhasil dibaca")
a_date = st.date_input("masukan tanggal :")
a_date=datetime.datetime.strftime(a_date,'%Y-%m-%d')
st.subheader(f"data persebaran kasus covid di indonesia pada {a_date} sebanyak : {data_idn(d=a_date,data_all=data)}")
st.map(data_map(d=a_date,data_all=data))
st.subheader("Total kasus")
st.table(data_tgjum(d=a_date,data_all=data))