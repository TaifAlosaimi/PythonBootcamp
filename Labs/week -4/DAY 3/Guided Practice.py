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


def validate_student(student):
    if "name" not in student or not student["name"]:
        raise InvaildStudentsError("student name is rquired")
    if "score" not in student:
        raise InvaildStudentsError("student score is reqired")




with open(file_path, "r", encoding"utf-8") as file:       #افتح الملف للقراءة
    students = json.load(file)

try:
    with open(file_path, "r", encoding"utf-8") as file:
    students = json.load(file)
except FileNotFoundError:
    print("Students file not found")
except json.JSONDecodeError:
    print("invaild json file")

if not student["name"]:
if not 0 <= students["score"] <= 100:

raise ValueError ("Score must be between 0 and 100")