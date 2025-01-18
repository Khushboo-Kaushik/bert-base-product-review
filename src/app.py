# djangodevloper/bert-base-uncased-product-review-classification
import streamlit as st 
from transformers import pipeline

st.title("Product Review App")
classifier = pipeline('text-classification', model = 'djangodevloper/bert-base-uncased-product-review-classification')
text= st.text_area("Enter Your comments")
review_comment = st.button('Review', type='primary', use_container_width=True)

if review_comment:
    if text:
        report = classifier(text)
        print(report)
        result =''
        for r in report:
            st.write(f'{r["label"]} : {r["score"]}  ')
    else:
        st.info("Kindly enter your review")
            
