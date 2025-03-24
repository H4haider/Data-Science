import streamlit as st
import pandas as pd
st.sidebar.title("Navigation")
screen=st.sidebar.radio("Go to", ["Create", "Read", "Update", "Delete"])

if "data" not in st.session_state:
    st.session_state.data = []

if screen=="Create":
    st.title("Create Entry")
    with st.form("form"):
        name=st.text_input("Enter Name")
        age=st.number_input("Input Age", min_value=1, max_value=100)
        city=st.text_input("Enter City")
        submit=st.form_submit_button("Add Entry")
        if(submit):
            st.session_state.data.append({"Name":name, "Age":age, "City":city})
            st.success("Entry Added!")

elif screen=="Read":
    st.title("Read Entries")
    df=pd.DataFrame(st.session_state.data)
    st.table(df)

elif screen=="Update":
    st.title("Update Entries")
    df=pd.DataFrame(st.session_state.data)
    val=st.number_input("Enter updated Age: ", min_value=1, max_value=100)
    index=st.selectbox("Enter Entry no. to update: ", range(len(df)))
    if df.empty:
        st.warning("Data is empty")
    else:
        if st.button("Update Age"):
            st.session_state.data[index]["Age"]=val
            st.success("Age Updated!")
        


elif screen=="Delete":
    st.title("Delete Entries")
    df=pd.DataFrame(st.session_state.data)
    index=st.selectbox("Enter Enter no. to update: ", range(len(df)))
    if df.empty:
        st.warning("Data is Empty")
    else:
        if st.button("Delete Entry"):
            st.session_state.data.pop(index)
            st.success("Entry Deleted!")





