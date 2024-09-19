import streamlit as st

with st.form('form 1'):
    st.write('This is the body of this form')
    check = st.checkbox('Please check this box to confirm')
    
    submitted = st.form_submit_button()
    if check and submitted:
        st.write('**Thank you**')
    else:
      st.write('You forgot to check the box.')      
    