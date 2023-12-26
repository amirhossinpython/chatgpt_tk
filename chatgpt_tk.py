import tkinter as tk
from tkinter import ttk
import requests

def get_response():
    inp = entry.get()
    wait_label.config(text="در حال پردازش...")
    window.update_idletasks()  # بروزرسانی پنجره
    req = requests.get(f"https://pyrubi.b80.xyz/chat.php/?text={inp}").json()
    res = req[0]["text"]
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, res + "\n")
    wait_label.config(text="")  # حذف پیام "در حال پردازش..."

window = tk.Tk()
window.title("ChatGPT-TURBO-3.5")
icon = tk.PhotoImage(file="ico_ai_11zon.png")
window.iconphoto(True, icon)

style = ttk.Style()
style.configure('TButton', font=('Tahoma', 12), foreground='black', background='light green', padding=10)
style.configure('TEntry', font=('Tahoma', 14), padding=10)
style.configure('TText', font=('Tahoma', 12), background='light blue', padding=10)

input_frame = ttk.Frame(window)
input_frame.pack(pady=10)

entry = ttk.Entry(input_frame, font=('Tahoma', 14),width=30)
entry.pack(side=tk.LEFT)

submit_button = ttk.Button(input_frame, text="ارسال", command=get_response,style='TButton')
submit_button.pack(side=tk.LEFT, padx=10)

result_text = tk.Text(window, font=('Tahoma', 12), background='light blue', width=100, height=30)
result_text.pack(pady=10)

wait_label = tk.Label(window, text="", font=('Tahoma', 12))
wait_label.pack()

window.mainloop()
