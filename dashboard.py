import streamlit as st
from streamlit_gsheets import GSheetsConnection

# import ydata_profiling
import pandas as pd
from ydata_profiling import ProfileReport

# report utk streamlit
from streamlit_pandas_profiling import st_profile_report

st.set_page_config(
    page_title="Data Profiler Dashboard",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ..............judul dashboard.......

st.title("Data Profiler")
st.markdown("<h1 style='text-align: center;'> Data Profiler App </h1>",
            unsafe_allow_html=True)
            

st.markdown("---")

#.....sidebar....

with st.sidebar:
    st.subheader("Promotion Data")
    st.markdown("---")

##------------Buat button

if st.sidebar.button("Start Profiling Data") :
    ## Read Data
    conn = st.connection("gsheet", type=GSheetsConnection)

    
    df = conn.read(
        spreadsheet = st.secrets.gsheet_promotion["spreadsheet"],
        worksheet = st.secrets.gsheet_promotion["worksheet"]
    )


    ## Generate Report dari ydata_profiling nya
    pr = ProfileReport(df)

    st_profile_report(pr)

else:
    st.info("Click button in the left sidebar to generate data report")