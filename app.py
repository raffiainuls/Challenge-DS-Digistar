import streamlit as st
from scipy.stats import gaussian_kde
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from challenge_ds_digistar_class_telkom import plot_count_gender, race_ethnicity_score_type, parental_type_score, lunch_type_score, preparation_course_type_score,distribution_score_prepare_test, bar_plot_parental_education
from prediction import prediction

# Set page config
st.set_page_config(page_title="Challenge DS Digistar Raffi", page_icon=":guardsman:", layout="wide")

# Add margin between components
st.markdown("""<style>div.Widget.row-widget.stRadio > div{flex-direction:row;}</style>""",unsafe_allow_html=True)
st.markdown("""<style>div.row-widget.stRadio > div{margin-left:20px;margin-right:20px;}</style><br>""",unsafe_allow_html=True)



def main():
    # Buat dua halaman menggunakan st.sidebar
    st.sidebar.title("Navigation")
    pages = ["Analysist Data", "App Prediction"]
    selection = st.sidebar.radio("Go to", pages)

    # Halaman Home
    if selection == "Analysist Data":
        
        header_image = Image.open("image.jpg")
        header_image = header_image.resize((1010, 400))
        st.image(header_image,  use_column_width=True)
        st.markdown("<h1 style = 'text-align : center; font_size : 40 px; font-family : Arial'><b>Challenge DS Digistar Class<b></h1>", unsafe_allow_html= True)
        st.markdown("------")
        st.markdown("Created by [Raffi Ainul Afif](linkedin.com/in/raffi-ainul-afif-9811a411b/)")
        
        #analysist gender
        st.markdown("<h1 style = 'text-align : left;  font-size : 25px; font-family : Arial'> <b>Analysist Gender<b></h1>", unsafe_allow_html= True)
        st.plotly_chart(plot_count_gender, use_container_width=True, height=500)
        paragraf_gender = ''' <p style = 'font-size : 14px; font-family : Arial; color : white;'> Jika dilihat dari column plot diatas ternyata jumlah student female
        pada data lebih banyak jika dibandingkan dengan jumlah student male.</p>'''
        st.markdown(paragraf_gender, unsafe_allow_html= True)
        

        #analysist race_ethnicity
        st.markdown("<h1 style = 'text-align : left; color : white; font-size : 25px; font-family : Arial'> <b>Analysist Race/Ethinicity<b></h1>", unsafe_allow_html= True)
        paragraf_ethinicity = ''' <p style = 'font-size : 14px; font-family : Arial; color : white;'> Race/Ethinicity 
        Student dengan category group A,B,C untuk math score, dan reading score lebih banyak yang dibawah rata-rata, sedangkan untuk group D,dan E sebaliknya. Uniknya untuk reading score
        berbeda group A,dan B tetap lebih banyak yang dibawah rata-rata tetapi untuk group C mengikuti grup D dan E yaitu lebih banyak student yang nilainya diatas rata-rata. </p>'''

        option_ethinicity = st.selectbox('Choose Category',
                                  ('Math Score', 'Writing Score', 'Reading Score', 'Total Score'), key ='option_ethinicity')
        if option_ethinicity == 'Math Score':
            st.plotly_chart(race_ethnicity_score_type('type_math_score'), use_container_width=True, height=500)
        
        elif option_ethinicity == 'Writing Score':
            st.plotly_chart(race_ethnicity_score_type('type_writing_score'), use_container_width=True, height=500)
        
        elif option_ethinicity == 'Reading Score':
            st.plotly_chart(race_ethnicity_score_type('type_reading_score'), use_container_width=True, height=500)
        
        elif option_ethinicity == 'Total Score':
            st.plotly_chart(race_ethnicity_score_type('type_total_score'), use_container_width=True, height=500)
        st.markdown(paragraf_ethinicity, unsafe_allow_html= True)
        
        #analysist Parental_education

        st.markdown("<h1 style = 'text-align : left; font-size : 25px; font-family : Arial'> <b>Analysist Parental Education<b></h1>", unsafe_allow_html= True)
        paragraf_parental_education = ''' <p style = 'font-size : 14px; font-family : Arial; color : white;'> Grafik Pie Chart diatas menampilkan presentase 
        komposisi Parental Education untuk nilai diatas rata-rata. Untuk Math Score sebanyak 23.6% student yang nilainya diatas ratarata parental 
        educationnya some college, untuk writing dan reading score kategori parental education tertinggi diduduki oleh associate's degree. Hal ini tidak
          bisa dicadikan acuan bahwa parental students education berpengaruh terhadap nilai, karena proporsi jumlah dari setiap kategori education parentnya pun juga 
          berbeda-beda dapat dilihat dibawah untuk jumlah tiap kategori parental education level </p>'''
        option_parental_education = st.selectbox('Choose Category',
                                  ('Math Score', 'Writing Score', 'Reading Score', 'Total Score'),key = 'option_parental_education')
        if option_parental_education == 'Math Score':
            st.plotly_chart(parental_type_score('type_math_score'), use_container_width=True, height=500)
        
        elif option_parental_education == 'Writing Score':
            st.plotly_chart(parental_type_score('type_writing_score'), use_container_width=True, height=500)
        
        elif option_parental_education == 'Reading Score':
            st.plotly_chart(parental_type_score('type_reading_score'), use_container_width=True, height=500)
        
        elif option_parental_education == 'Total Score':
            st.plotly_chart(parental_type_score('type_total_score'), use_container_width=True, height=500)
        st.markdown(paragraf_parental_education, unsafe_allow_html= True)
        st.plotly_chart(bar_plot_parental_education, use_container_width=True, height=500)
        
        #analysist lunch
        st.markdown("<h1 style = 'text-align : left; font-size : 25px; font-family : Arial'> <b>Analysist Type Lunch Student<b></h1>", unsafe_allow_html= True)
        paragraf_lunch = ''' <p style = 'font-size : 14px; font-family : Arial; color : white;'>Grafik Stacked Chart dibawah menampilakn jumlah student  
        dengan nilai dibawah rata-rata dan diatas rata rata untuk masing masing nilai yang dilihat dari type lunch. Dari grafik tersebut dapat disimpulkan 
        kemungkinan type lunch sedikit berpengaruh terhadap nilai karena untuk tipe lunch standart nilai diatas rata rata lebih banyak dibandingkan dibawah, 
        dan sebaliknya untuk tipe lunch free/reduced nilai diatas rata-rata lebih sedikit dibandingkan dibawah rata-rata, dan hal tersebut terjadi untuk setiap 
        kategori score yaitu math score, reading score, dan writing score. </p>'''
        st.markdown(paragraf_lunch, unsafe_allow_html= True)
        option_lunch = st.selectbox('Choose Category',
                                  ('Math Score', 'Writing Score', 'Reading Score', 'Total Score'), key = 'option_lunch')
        if option_lunch == 'Math Score':
            st.plotly_chart(lunch_type_score('type_math_score'), use_container_width=True, height=500)
        
        elif option_lunch == 'Writing Score':
            st.plotly_chart(lunch_type_score('type_writing_score'), use_container_width=True, height=500)
        
        elif option_lunch == 'Reading Score':
            st.plotly_chart(lunch_type_score('type_reading_score'), use_container_width=True, height=500)
        
        elif option_lunch == 'Total Score':
            st.plotly_chart(lunch_type_score('type_total_score'), use_container_width=True, height=500)
        
        #analysist preperation course
        st.markdown("<h1 style = 'text-align : left;  font-size : 25px; font-family : Arial'> <b>Analysist preparation course<b></h1>", unsafe_allow_html= True)
        paragraf_preparation_course = ''' <p style = 'font-size : 14px; font-family : Arial; color : white;'> Grafik diatas menampilkan presentase proporsi nilai 
        student yang diatas rata-rata berdasarkan preparation course. Uniknya justru jika kita langsung melihat pada grafik pie chart diatas justru presentase student dengan preparation completed kalah oleh none, mengapa bisa dimikian ya? 
        secara logika seharusnya jika kita menyiapkan sebuah test dengan baik tentunya akan berpengaruh dengan nilai yang lebih baik pula. </p>'''
    
        option_preparation_course = st.selectbox('Choose Category',
                                  ('Math Score', 'Writing Score', 'Reading Score', 'Total Score'), key = 'option_preparation_course')
        if option_preparation_course == 'Math Score':
            st.plotly_chart(preparation_course_type_score('type_math_score'), use_container_width=True, height=500)
        
        elif option_preparation_course == 'Writing Score':
            st.plotly_chart(preparation_course_type_score('type_writing_score'), use_container_width=True, height=500)
        
        elif option_preparation_course == 'Reading Score':
            st.plotly_chart(preparation_course_type_score('type_reading_score'), use_container_width=True, height=500)
        
        elif option_preparation_course == 'Total Score':
            st.plotly_chart(preparation_course_type_score('type_total_score'), use_container_width=True, height=500)
        st.markdown(paragraf_preparation_course, unsafe_allow_html= True)

        
    
        if option_preparation_course == 'Math Score':
            st.plotly_chart(distribution_score_prepare_test('math score'), use_container_width=True, height=500)
        
        elif option_preparation_course == 'Writing Score':
            st.plotly_chart(distribution_score_prepare_test('writing score'), use_container_width=True, height=500)
        
        elif option_preparation_course == 'Reading Score':
            st.plotly_chart(distribution_score_prepare_test('reading score'), use_container_width=True, height=500)
        
        elif option_preparation_course == 'Total Score':
            st.plotly_chart(distribution_score_prepare_test('total score'), use_container_width=True, height=500)

        paragraf_preparation_course2 = ''' <p style = 'font-size : 14px; font-family : Arial; color : white;'>Mungkin jawabannya dapat kita lihat dari boxplot diatas, 
        kelompok student dengan none preparatin course presentasenya lebih banyak, dikarenakan memang banyak student yang tipe preparationnya none, berbeda cukup 
        jauh jumlahnya dengan student yang menyiapkan testnya dengan mengikuti course. Posisi boxplot untuk tipe preparation complated berada sedikit lebih diatas 
        dari none, dari situ dapat disimpulkan bahwa nilai untuk kelompok students yang menyiapkan testnya juga sebenarnya diatas dibandingkan dengan kelompok students 
        yang tipe preparationnya none. Kesimpulannya preparation course bisa dikatakan berpengaruh untuk nilai students </p>'''
        st.markdown(paragraf_preparation_course2, unsafe_allow_html= True)
    
    elif selection == "App Prediction":
        st.header('Input Data')
        gender = st.selectbox('Gender', ['Male', 'Female'])
        ethinicity = st.selectbox('Race/Ethnicity', ['group A', 'group B', 'group C', 'group D', 'group E'])
        parental_education = st.selectbox('Parental Education Level', ["bachelor's degree", "some college", "master's degree", "associate's degree", "high school", "some high school"])
        lunch = st.selectbox('Lunch', ['standard', 'free/reduced'])
        test_preparation = st.selectbox('Preparation Test', ['none', 'completed'])
        math_score = st.number_input('Math Score', min_value = 0, key = 'math_score')
        writing_score = st.number_input('Writing Score', min_value = 0, key = 'writing_score')
        reading_score = st.number_input('Reading Score', min_value = 0, key = 'reading_score')
        

        if st.button('Prediksi'):

            result,prediction_score = prediction(gender, ethinicity, parental_education, lunch, test_preparation, math_score,writing_score, reading_score)
            st.subheader('Hasil Prediksi')
            st.write(f'Data yang dimasukan masuk pada clustering {result} dengan akurasi prediksi {prediction_score}')

if __name__ == '__main__':
    main()








        