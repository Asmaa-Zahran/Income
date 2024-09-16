import streamlit as st
# import seaborn as sns
# import matplotlib.pyplot as plt
import pandas as pd
# import plotly.express as px

adult = pd.read_csv("adult.csv")

def main_page():
    st.title('Application :')
    st.number_input(label='Age :')
    workclass = ['Private', 'Local-gov', 'Self-emp-not-inc', 'Federal-gov',
        'State-gov', 'Self-emp-inc', 'Without-pay', 'Never-worked']
    st.select_slider(label='Work Class',options=workclass)
    st.number_input(label='Fnlwgt :')
    education = ['11th', 'HS-grad', 'Assoc-acdm', 'Some-college', '10th',
        'Prof-school', '7th-8th', 'Bachelors', 'Masters', 'Doctorate',
        '5th-6th', 'Assoc-voc', '9th', '12th', '1st-4th', 'Preschool']
    st.selectbox(label='Education',options=education)
    marital_status = ['Never-married', 'Married-civ-spouse', 'Widowed', 'Divorced',
        'Separated', 'Married-spouse-absent', 'Married-AF-spouse']
    st.selectbox(label='Marital Status',options=marital_status)  
    occupation = ['Machine-op-inspct', 'Farming-fishing', 'Protective-serv', '?',
        'Other-service', 'Prof-specialty', 'Craft-repair', 'Adm-clerical',
        'Exec-managerial', 'Tech-support', 'Sales', 'Priv-house-serv',
        'Transport-moving', 'Handlers-cleaners', 'Armed-Forces']
    st.selectbox(label='Occupation',options = occupation) 
    relationship = ['Own-child', 'Husband', 'Not-in-family', 'Unmarried', 'Wife',
        'Other-relative']
    st.select_slider(label='RelationShip :',options = relationship)
    race = ['Black', 'White', 'Asian-Pac-Islander','Amer-Indian-Eskimo','Other']
    st.radio(label='Race :',options=race)
    st.radio(label='Race :',options=['Female','Male'])
    st.number_input(label='Capital gain :')
    st.number_input(label='Capital loss :')
    st.number_input(label='Hours per week :')
    country = ['United-States', 'Peru', 'Guatemala', 'Mexico',
        'Dominican-Republic', 'Ireland', 'Germany', 'Philippines',
        'Thailand', 'Haiti', 'El-Salvador', 'Puerto-Rico', 'Vietnam',
        'South', 'Columbia', 'Japan', 'India', 'Cambodia', 'Poland',
        'Laos', 'England', 'Cuba', 'Taiwan', 'Italy', 'Canada', 'Portugal',
        'China', 'Nicaragua', 'Honduras', 'Iran', 'Scotland', 'Jamaica',
        'Ecuador', 'Yugoslavia', 'Hungary', 'Hong', 'Greece',
        'Trinadad&Tobago', 'Outlying-US(Guam-USVI-etc)', 'France',
        'Holand-Netherlands']
    st.selectbox(label='Native Country',options=country)   

def first_page():
    st.title("About Adult-income dataset :")
    
    adult = pd.read_csv("adult.csv")
    st.markdown(f"<h6 style='color:gray;'>{adult.shape[0]} rows <h6>",unsafe_allow_html=True)
    st.dataframe(adult.head(10))
    st.title("Columns :")
    st.image('Dataset.png')

def second_page():
    import seaborn as sns
    import matplotlib.pyplot as plt
    import pandas as pd
    import plotly.express as px
    st.title('Uni-Variate Analysis :')    
    adult = pd.read_csv("adult.csv")

    st.markdown('#### Categorical Columns :')
    cat_cols = adult.select_dtypes(include='object')
    for cat in cat_cols:
        if adult[cat].nunique() <= 8:
            data = adult[cat].value_counts()
            fig = px.pie(data,names=data.index,title=cat,values=data.values,height=500,width=500,hole=0.3,color_discrete_sequence=px.colors.plotlyjs.Portland)
            st.plotly_chart(fig,use_container_width=True)

    # cat_cols = adult.select_dtypes(include='object').columns
    
    for cat in cat_cols:
        if adult[cat].nunique() > 8 and adult[cat].nunique() <= 15:
            fig = plt.figure(figsize=(25,7))
            sns.countplot(data=adult,x=adult[cat])
            st.pyplot(fig)
        elif adult[cat].nunique() > 15:
            fig = plt.figure(figsize=(20,7))
            top_df = adult[cat].value_counts().head(15).index
            filter_df = adult[adult[cat].isin(top_df)]
            sns.countplot(data=filter_df,y=cat)   
            st.pyplot(fig)   

    st.markdown('#### Numerical Columns :')
    num_cols = adult.select_dtypes(include='number').columns
    for col in num_cols :
        fig = plt.figure(figsize=(10,7))
        sns.histplot(adult[col],kde=True)
        st.pyplot(fig)

def third_page():
    import seaborn as sns
    import matplotlib.pyplot as plt
    import pandas as pd
    import plotly.express as px
    st.title("Bi-Variate Analysis")
    fig = plt.figure(figsize=(10,7))
    adult_df = adult.select_dtypes('number')
    sns.heatmap(adult_df.corr(),annot=True)
    st.pyplot(fig)
    num_cols = ['age', 'fnlwgt', 'educational-num', 'capital-gain', 'capital-loss',
       'hours-per-week','None']
    result = st.selectbox(label="Visualization of income with (Numerical Columns): ",options=num_cols)
    if result == 'None':
        st.markdown("<h6 style='color:red;'>*Please choose a Column : <h6>",unsafe_allow_html=True)
    else:
        fig = plt.figure(figsize=(20,7))
        sns.boxplot(y=adult[result], x=adult["income"])
        st.pyplot(fig)

    cat_cols = ['workclass', 'education', 'marital-status', 'occupation',
       'relationship', 'race', 'gender', 'native-country']
    result = st.selectbox(label="Visualization of income with (Categorical Columns): ",options=cat_cols)
    if result == 'None':
        st.markdown("<h6 style='color:red;'>*Please choose Category : <h6>",unsafe_allow_html=True)
    else:
        fig = plt.figure(figsize=(10,7))
        sns.countplot(data=adult,x=result,hue='income')
        st.pyplot(fig)


page = st.sidebar.selectbox(label="choose a page", options=["main page", "About Dataset","Uni-Variate Analysis","Bi-Variate Analysis"])
mapper_name_fn = {"main page":main_page ,'About Dataset':first_page , "Uni-Variate Analysis" : second_page ,"Bi-Variate Analysis": third_page}
mapper_name_fn[page]()
