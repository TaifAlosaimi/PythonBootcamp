from pathlib import Path

path = Path("home") / "students" / "students.txt"         # تحديد مسار الملف

path.parent.mkdir(parents=True, exist_ok=True)         # إنشاء ال parent folder وهو students

print(path.is_dir())                                   # هل المسار Directory؟
print(path.suffix)                                     # امتداد الملف
print(path.name)                                       # اسم الملف
print(path.is_file())                                  # هل المسار File؟

path.write_text("Welcome to class ", encoding="utf-8")         # كتابة النص داخل الملف  