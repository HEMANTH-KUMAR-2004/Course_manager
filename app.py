import streamlit as st
import requests
BASE_URL="https://course-manager-kif6.onrender.com"
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