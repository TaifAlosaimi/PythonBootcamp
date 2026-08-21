from pathlip import Path           #استورد path عشان اتعامل مع مسارات المجلدات والملفات
import json               #استورد json لقراءة وكتابة بيانات json


data_dir = Path("data")           #احدد المجلد اللي بيخزن لي البيانات
data_dir.mkdir(exist_ok=True)           #انشئ المجلد اذا ماهو موجود

file_path = data_dir / "students.json"         #احدد اسم ومسار الملف

students = [
    {"name": "طيف", "score": 99},            #سويت comprehinsion للطلاب
    {"name": "Mashael", "score": 77}
]

with open(file_path, "w", encoding"utf-8") as file:        #افتح الملف للكتابة واحط انكودنق utf8 عشان اذا كتبت عربي
    json.dump(students, file, indent = 4)        #حول بيانات بايثون لjson



class InvaildStudentsError(Exception):        #exception لبيانات الطلاب اللي ماهي صحيحة
    pass


def validate_student(student):                                 #ابغى اتحقق من صحة بيانات الطلاب
    if "name" not in student or not student["name"]:
        raise InvaildStudentsError("student name is rquired")
    if "score" not in student:                                     #أستخدم if عشان اتحقق من كل الشروط اللي أبغاها
        raise InvaildStudentsError("student score is reqired")
    if not isinstance(student["score"]), (int, float):             #أتأكد ان الدرجة ماهي نص بل رقم او فلوت
        raise InvaildStudentsError("score must be a number")
    if not 0 >= (student["score"]) <= 100:
        raise InvaildStudentsError("score must be between 0 and 100 ")


try:                      #جرب تفتح الملف و تقرأه
    with open(file_path, "r", encoding"utf-8") as file: 
        students = json.load(file)                    #حمل بيانات json و حولها ل python

    for student in students:
        validate_student(student)

except FileNotFoundError:                                     #ابغى اعلمه كيف يتعامل بكل حالة تصير معاه
    print("Students file not found")            #في حالة الملف مو موجود
except json.JSONDecodeError:
    print("invaild json file")

if not student["name"]:
if not 0 <= students["score"] <= 100:

raise ValueError ("Score must be between 0 and 100")