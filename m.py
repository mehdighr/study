import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

all_data = {}

# ---------------- Functions ----------------
def add_num():
    name = simpledialog.askstring("افزودن مخاطب", "نام را وارد کنید:")
    tel = simpledialog.askstring("افزودن مخاطب", "شماره تلفن را وارد کنید:")
    if name and tel:
        all_data[name] = tel
        messagebox.showinfo("ثبت شد", f"{name} با موفقیت اضافه شد.")
        update_tree()

def show_num():
    if not all_data:
        messagebox.showinfo("لیست خالی", "دفترچه خالی است.")
    else:
        contacts = "\n".join([f"{k}: {v}" for k, v in all_data.items()])
        messagebox.showinfo("مخاطبین", contacts)

def del_num():
    name = simpledialog.askstring("حذف مخاطب", "نام مخاطب را وارد کنید:")
    if name in all_data:
        del all_data[name]
        messagebox.showinfo("حذف شد", f"{name} با موفقیت حذف شد.")
        update_tree()
    else:
        messagebox.showwarning("خطا", "مخاطب پیدا نشد.")

def find_num():
    num = simpledialog.askstring("جستجو", "شماره‌ای را برای جستجو وارد کنید:")
    for name, tel in all_data.items():
        if tel == num:
            messagebox.showinfo("یافت شد", f"این شماره متعلق به {name} است.")
            return
    messagebox.showinfo("یافت نشد", "این شماره در دفترچه نیست.")

def update_tree():
    for i in tree.get_children():
        tree.delete(i)
    for name, tel in all_data.items():
        tree.insert("", tk.END, values=(name, tel))

# ---------------- GUI Setup ----------------
root = tk.Tk()
root.title("📱 دفترچه تلفن پیشرفته")
root.geometry("500x550")
root.configure(bg="#f7f9fc")

# فونت‌ها و استایل‌ها
style = ttk.Style()
style.configure("Treeview.Heading", font=("Tahoma", 11, "bold"), foreground="#444")
style.configure("Treeview", font=("Tahoma", 10), rowheight=28)

# ---------------- Title ----------------
title = tk.Label(root, text="📒 دفترچه تلفن", font=("Tahoma", 20, "bold"), bg="#f7f9fc", fg="#2b2d42")
title.pack(pady=15)

# ---------------- Buttons ----------------
btn_frame = tk.Frame(root, bg="#f7f9fc")
btn_frame.pack(pady=10)

def create_button(text, command, color="#3a86ff"):
    return tk.Button(
        btn_frame, text=text, command=command, font=("Tahoma", 11),
        bg=color, fg="white", activebackground="#2b5db6",
        width=20, relief=tk.FLAT, pady=6
    )

create_button("➕ افزودن مخاطب", add_num).grid(row=0, column=0, padx=10, pady=5)
create_button("📋 نمایش همه", show_num).grid(row=1, column=0, padx=10, pady=5)
create_button("🔍 جستجوی شماره", find_num).grid(row=2, column=0, padx=10, pady=5)
create_button("❌ حذف مخاطب", del_num, color="#ef233c").grid(row=3, column=0, padx=10, pady=5)
create_button("🚪 خروج", root.quit, color="#6c757d").grid(row=4, column=0, padx=10, pady=10)

# ---------------- Contact List ----------------
list_frame = tk.Frame(root, bg="#f7f9fc")
list_frame.pack(pady=10, fill=tk.BOTH, expand=True)

tree = ttk.Treeview(list_frame, columns=("Name", "Phone"), show="headings", height=8)
tree.heading("Name", text="نام")
tree.heading("Phone", text="شماره تلفن")
tree.column("Name", anchor=tk.CENTER, width=200)
tree.column("Phone", anchor=tk.CENTER, width=200)
tree.pack(padx=15, pady=5, fill=tk.BOTH, expand=True)

# ---------------- Footer ----------------
footer = tk.Label(root, text="ساخته شده با ❤️ توسط شما", font=("Tahoma", 9), bg="#f7f9fc", fg="#888")
footer.pack(pady=10)

# ---------------- Run ----------------
root.mainloop()

