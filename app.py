import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf
import base64

st.title("S&P 500 Stock Price Analysis")
st.write("This app allows you to analyze the stock prices of S&P 500")
st.markdown("[Wikipedia](https://en.wikipedia.org/wiki/List_of_S%26P_500_companies)")
st.sidebar.header('User Input Features')

#scrapping de la page wikipedia
@st.cache_data
def load_data():
    url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    tables = pd.read_html(url)
    df = tables[0]
    return df
df = load_data()
sector = df.groupby('GICS Sector')
#selection de secteur d activites sur le sidebar
sorted_sector_unique = sorted(df['GICS Sector'].unique())
selected_sector = st.sidebar.multiselect('Select Sector(s)', sorted_sector_unique)

#Selection des secteurs d activites et shape
df_selected_sector = df[(df['GICS Sector'].isin(selected_sector))]
st.header('Display companies in selected sector(s)')
st.write('Data Dimension: ' + str(df_selected_sector.shape[0]) + ' rows and ' + str(df_selected_sector.shape[1]) + ' columns.')


#Bouton Download
def filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes
    href = f'<a href="data:file/csv;base64,{b64}" download="stock_list.csv">Download csv file</a>'
    return href
st.markdown(filedownload(df_selected_sector), unsafe_allow_html=True)
st.write(df_selected_sector)

#Appel Yahoo finance
try:
   data = yf.download(
    tickers = list(df_selected_sector[:10].Symbol),
    period="ytd", interval="1d",group_by="ticker",auto_adjust=True,
    prepost=True,threads=True,proxy=None)
except:
    print('No selected sector')

#Plot closing price of query symbol
def price_plot(symbol):
    df = pd.DataFrame(data[symbol].Close)
    df.Date = df.index
    fig,ax = plt.subplots()
    plt.fill_between(df.Date,df.Close,color='skyblue')
    plt.plot(df.Date,df.Close,color='skyblue')
    plt.xticks(rotation=90)
    plt.title(symbol,fontweight='bold')
    plt.xlabel('Date',fontweight='bold')
    plt.ylabel('Close Price',fontweight='bold')
    return st.pyplot(fig)

num_company = st.sidebar.slider('Number of companies', 1, 5,)
if st.button('Show Plots'):
    st.header('Stock Closing Price')
    for i in list(df_selected_sector.Symbol)[:num_company]:
        price_plot(i)
        