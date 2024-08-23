import streamlit as st
st.header('Factorial Application')
st.write('This is a application to find factorial')
x=st.number_input('enter the number',value=1)
y=st.button('calculate')
if y:
    f=1
    for i in range (1,x+1):
        f=f*i
        i=i+1
    st.subheader(f)
        
