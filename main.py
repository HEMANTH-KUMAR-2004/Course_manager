from fastapi import FastAPI
app=FastAPI(title="Course management system")
@app.get("/home")
def home():
    return {"message":"This is the Home Page"}
@app.get("/contact")
def contact():
    return {"message":"This is a contact page of out FastAPI application"}

l=[]
@app.get("/courses")
def avilable_courses():
    return{"message":"The Following are the avilable courses","courses":l}

@app.post("/add_course/{course_name}")
def add_course(course_name:str):
    l.append(course_name)
    return{"message":f"course added:{course_name}"}

@app.put("/update_course/{old_course}/{new_course}")
def update_course(old_course:str,new_course:str):
    if old_course in l:
        index=l.index(old_course)
        l[index]=new_course
        return {"message":f"course update from {old_course} to {new_course} successfully"}
    else:
        return {"Message":f"Course not found {old_course}"}

@app.delete("/delete_course/{course_name}")
def delete_course(course_name:str):
    if course_name in l:
        l.remove(course_name)
        return {"message":f"course delted:{course_name}"}
    else:
        return {"meaagge":f"course not found {course_name}"}     