import streamlit as st
import requests
BASE_URL="https://course-manager-kif6.onrender.com"
st.markdown(
    """
    <style>
    /* Main background */
    .stApp {
        background: linear-gradient(135deg, #667eea, #764ba2);
    }

    /* Title styling */
    h1 {
        color: white;
        text-align: center;
        font-size: 45px;
        font-weight: bold;
    }

    /* Subheader styling */
    h2, h3 {
        color: #ffffff;
        font-weight: bold;
    }

    /* Sidebar styling */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #141E30, #243B55);
    }

    section[data-testid="stSidebar"] * {
        color: white;
    }

    /* Text styling */
    p {
        color: white;
        font-size: 18px;
    }

    /* Input boxes */
    input {
        background-color: white !important;
        color: black !important;
        border-radius: 10px;
    }

    /* Buttons */
    div.stButton > button {
        background: linear-gradient(90deg, #ff9966, #ff5e62);
        color: white;
        font-size: 18px;
        font-weight: bold;
        border-radius: 12px;
        padding: 10px 25px;
        border: none;
    }

    div.stButton > button:hover {
        background: linear-gradient(90deg, #00c6ff, #0072ff);
        color: white;
    }

    /* JSON box */
    div[data-testid="stJson"] {
        background-color: rgba(255,255,255,0.9);
        border-radius: 15px;
        padding: 15px;
    }

    </style>
    """,
    unsafe_allow_html=True
)

st.title("Course management system")
menu=st.sidebar.selectbox(
    "choose an operation",
    ["view course","Add Course","update Course","Delete Course"]
)
if menu=="view course":
    st.header("Available Courses")
    response=requests.get(f"{BASE_URL}/courses")
    if response.status_code==200:
        data=response.json()
        st.write(data["courses"])
    else:
        st.error("Unable to fetch the courses")
elif menu=="Add Course":
    st.header("Add a course")
    course=st.text_input("Course Name")
    if st.button("Add"):
        response=requests.post(f"{BASE_URL}/add_course/{course}")
        if response.status_code==200:
            st.success(response.json()["message"])
        else:
            st.error("Failed to add course.")

elif menu=="update Course":
    st.header("Update a Course")
    old_course=st.text_input("Old Course Name")
    new_course=st.text_input("New Course Name")
    if st.button("Update"):
        response=requests.put(
            f"{BASE_URL}/update_course/{old_course}/{new_course}"
        )
        if response.status_code==200:
            st.success(response.json()["message"])
        else:
            st.error("Failed to update a course.")
elif menu=="Delete Course":
    st.header("Delete a course")
    course=st.text_input("Course_Name")
    if st.button("Delete"):
        response=requests.delete(
            f"{BASE_URL}/delete_course/{course}"
        )
        if response.status_code==200:
            st.success(response.json()["message"])
        else:
            st.error("Failed to delete code.")
