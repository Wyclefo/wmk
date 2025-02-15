import streamlit as st
st.set_option('deprecation.showPyplotGlobalUse', False)

st.title('Password Strength Calculator')

import streamlit as st
#function to compute Shannon entropy score
import re
import string
import collections as ct
def entropy(password):
    #count number of numerals 
    num_chars = string.digits
    nums = sum(v for k, v in ct.Counter(password).items() if k in num_chars)
    #count number of special characters
    special_chars = string.punctuation
    chars = sum(v for k, v in ct.Counter(password).items() if k in special_chars)
    #count number of lower case letters
    lowers = len(re.sub("[^a-z]", "", password))
    #count number of capital letters
    caps = len(re.sub("[^A-Z]", "", password))
    #'''Compute entropy'''
    import math
    #Constants

    log_2 = math.log(2)
    capN = 26
    smallN = 26
    numN = 10
    SymbolCountN = 62
    special = 32
    CountN = SymbolCountN + special

    length_of_password = len(password)
    no_of_pos_chars = 26

    entropy = round(length_of_password*(math.log(CountN))/math.log(2), 1)
    return entropy
password = st.text_input('Enter your password', type = "password")
        # Display text
#with st.expander("See password"):
    #st.write(password)
    
if st.button('Compute'):
    result = entropy(password)
    if result < 50:
        st.write('Terribly weak password. Password strength: %s' % result)
    elif result < 60:
        st.write('You can do a tinsy better. Password strength: %s' % result)
        
    elif result < 70:
        st.write("Almost there, add a few more characters, 2 maybe?. Password strength: %s" % result)
    elif result < 80:
        st.write('Great choice!. Password strength: %s' % result)
    elif result < 100:
         st.write('Very strong password!. Password strength: %s' % result)
    else:
        st.write('That was an overkill :). Password strength: %s' % result)
