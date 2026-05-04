import os

def menu():
    print("\n--- اجهزة ذكية للمستقبل ---")
    print("1. ثغرة حقن SQL")
    print("2. كشف التسريبات")
    print("3. البحث عن أرقام (شيرلوك)")
    
    choice = os.getenv('CHOICE', '1')

    if choice == "1":
        target = "https://example.com"
        os.system(f"python3 sqlmap/sqlmap.py -u {target} --batch")
    elif choice == "2":
        target = "email@example.com"
        os.system(f"h8mail -t {target}")

menu()

