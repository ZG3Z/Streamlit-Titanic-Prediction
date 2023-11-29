import streamlit as st
import joblib

sex_d = {0: 'Female', 1: 'Male'}
pclass_d = {0: 'First', 1: 'Second', 2: 'Third'}
embarked_d = {0: 'Cherbourg', 1: 'Queenstown', 2: 'Southampton'}

filename = "model"
model = model = joblib.load(filename)

def main():
    st.set_page_config(page_title='Would You Survive a Disaster?')
    overview = st.container()
    left, right = st.columns(2)
    prediction = st.container()

    st.image("https://media1.popsugar-assets.com/files/thumbor/7CwCuGAKxTrQ4wPyOBpKjSsd1JI/fit-in/2048xorig/filters:format_auto-!!-:strip_icc-!!-/2017/04/19/743/n/41542884/5429b59c8e78fbc4_MCDTITA_FE014_H_1_.JPG")
    

    with overview:
        st.title('Would You Survive a Disaster?')

    with left:
        sex_ratio = st.radio('Gender', list(sex_d.keys()), format_func= lambda x: sex_d[x])
        pclass_ratio = st.radio('Class', list(pclass_d.keys()), format_func = lambda x: pclass_d[x])
        embarked_ratio = st.radio('Port', list(embarked_d.keys()), index=2, format_func = lambda x: embarked_d[x])

    with right:
        age_slider = st.slider('Age', value=50, min_value=1, max_value=100)
        sibsp_slider = st.slider('# Siblings/Spouse', min_value=0, max_value=8)
        parch_slider = st.slider('# Parents/Children', min_value=0, max_value=6)
        fare_slider = st.slider('Ticket Fare', min_value=0, max_value=500, step=10)

    data = {
        'Pclass': pclass_ratio,
        'Age': age_slider,
        'SibSp': sibsp_slider,
        'Parch': parch_slider,
        'Fare': fare_slider,
        'Embarked': embarked_ratio,
        'male': sex_ratio,
    }

    data_for_prediction = [[data[key] for key in ['Pclass', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked', 'male']]]

    survival = model.predict(data_for_prediction)[0]
    s_confidence = model.predict_proba(data_for_prediction)[0]  

    with prediction:
        st.header('Would the Person Survive?')
        if survival == 1:
            st.success('Yes')
        else:
            st.error('No')

        st.subheader("Prediction Confidence: {0:.2f}%".format(s_confidence[survival] * 100))

if __name__ == '__main__':
    main()
