import streamlit as st
#import mysql.connector

# Connect to MySQL
def get_connection():
    return mysql.connector.connect(
        host="127.0.0.1",    # or your cloud DB host
        user="Swati",         # your MySQL username
        password="Swati1007", # your MySQL password
        database="teksdb"      # your database name
    )

st.title("USA Housing")

# Input fields
Avg_Area_Income = st.number_input("Enter income")
Avg_Area_house_age= st.number_input("Enter house age", min_value=1, max_value=100)
Avg_Area_Number_of_Rooms = st.number_input("Enter number of rooms")
Avg_Area_number_of_bedrooms=st.number_input("Enter Bedrooms",min_value=1,max_value=100)
Avg_Area_population=st.number_input("Enter Population",min_value=1,max_value=1000000)
Price=st.number_input("Enter Price",min_value=1,max_value=10000000)


if st.button("Submit"):
    conn = get_connection()
    cursor = conn.cursor()
    #cursor.execute("INSERT INTO Usa_Housing ( 'Avg. Area Income','Avg. Area House Age','Avg. Area Number of Rooms','Avg. Area Number of Bedrooms','Area Population',Price) VALUES (%s, %s, %s,%s,%s,%s)", 
    #               (Avg_Area_Income, Avg_Area_house_age,Avg_Area_Number_of_Rooms,Avg_Area_number_of_bedrooms,Avg_Area_population,Price))
    
    cursor.execute("INSERT INTO Usa_Housing  VALUES (%s, %s, %s,%s,%s,%s)", 
                   (Avg_Area_Income, Avg_Area_house_age,Avg_Area_Number_of_Rooms,Avg_Area_number_of_bedrooms,Avg_Area_population,Price))
    
   
    conn.commit()
    conn.close()
    st.success("Data inserted successfully!")

if st.button("Show Records"):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM USA_Housing")
    rows = cursor.fetchall()
    conn.close()
    
    for row in rows:

        st.write(row)
