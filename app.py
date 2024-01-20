import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('startup_cleaned.csv')

st.set_page_config(layout='wide',page_title='Startup Analysis')
# st.dataframe(df)
def load_investor_details(investor):
    st.title(investor)
    # load the recent 5 investment of the investor
    recent_investment=df[df['investors'].str.contains(investor)].head()[['date','startup','vertical','city','round','amount']]
    st.subheader("Most Recent Investment")
    st.dataframe(recent_investment)
    col1,col2=st.columns(2)
    with col1:
        st.subheader("Biggest Investment")
        biggest_investment=df[df['investors'].str.contains(investor)].groupby('startup')['amount'].sum().sort_values(ascending=False).head()
        fig,ax=plt.subplots()
        ax.bar(biggest_investment.index,biggest_investment.values)
        st.pyplot(fig)
    with col2:
        vertical_series=df[df['investors'].str.contains('IDG Ventures')].groupby('vertical')['amount'].sum()
        st.subheader('Sectors invested in ')
        fig1,ax1=plt.subplots()
        ax1.pie(vertical_series)
        st.pyplot(fig1)



st.sidebar.title('Startup Funding Analysis')
option=st.sidebar.selectbox('Select One',['Overall Analysis','Startup','Investor'])

if option=='Overall Analysis':
    st.title('Overall Analysis')
elif option =='Startup':
    st.sidebar.selectbox('Select Startup',sorted(df['investors'].unique().tolist()))
    btn1=st.sidebar.button('Find Startup Details')
    st.title("Startup Analysis")
else:
    selected_investor=st.sidebar.selectbox("Select  Startup",sorted(set(df['investors'].str.split(",").sum())))
    btn2=st.sidebar.button('Find Investors Details')
    if btn2:
        load_investor_details(selected_investor)
 

