import json
import os

FILENAME = "contacts.json"

# اگر فایل وجود نداشته باشه، یه لیست خالی ایجاد می‌کنیم
if os.path.exists(FILENAME):
    with open(FILENAME, "r", encoding="utf-8") as f:
        contacts = json.load(f)
else:
    contacts = []

# ذخیره کردن مخاطبین در فایل
def save_contacts():
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(contacts, f, ensure_ascii=False, indent=4)

# اضافه کردن مخاطب جدید
def add_contact():
    name = input("نام: ")
    phone = input("شماره تلفن: ")
    city = input("شهر: ")
    contact = {"name": name, "phone": phone, "city": city}
    contacts.append(contact)   #  اضافه کردن به لیست
    save_contacts()
    print(" مخاطب اضافه شد.")

# نمایش همه مخاطبین
def show_contacts():
    if not contacts:
        print(" هیچ مخاطبی وجود ندارد.")
        return
    for i, c in enumerate(contacts, start=1):
        print(f"{i}. {c['name']} | {c['phone']} | {c['city']}")

# جستجو در مخاطبین
def search_contact():
    keyword = input(" جستجو (نام/شهر/شماره): ")
    results = [c for c in contacts if keyword in c['name'] or keyword in c['phone'] or keyword in c['city']]
    if results:
        for c in results:
            print(f"{c['name']} | {c['phone']} | {c['city']}")
    else:
        print(" مخاطبی یافت نشد.")

# منوی اصلی
while True:
    print("\n--- دفترچه تلفن ---")
    print("1. افزودن مخاطب")
    print("2. نمایش همه مخاطبین")
    print("3. جستجو")
    print("4. خروج")

    choice = input("انتخاب: ")
    if choice == "1":
        add_contact()
    elif choice == "2":
        show_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        print(" خداحافظ!")
        break
    else:
        print("گزینه نامعتبر!")
