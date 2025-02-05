import smtplib
import tkinter as tk
from tkinter import messagebox

def send_mail():
    sender_email = entry_yourmail.get()  
    sender_password = entry_password.get()  
    receiver_email = entry_to.get()
    subject = entry_subject.get()
    message = text_message.get("1.0", tk.END)
    
    email_text = f"Subject: {subject}\n\n{message}"
    
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, email_text)
        server.quit()
        messagebox.showinfo("Email sent")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to send email\n{e}")


root = tk.Tk()
root.title("Email sending program")

tk.Label(root, text="Your Mail: ").pack()
entry_yourmail = tk.Entry(root)
entry_yourmail.pack()

tk.Label(root, text="Password: ").pack()
entry_password = tk.Entry(root)
entry_password.pack()

tk.Label(root, text="Receiver email:").pack()
entry_to = tk.Entry(root)
entry_to.pack()

tk.Label(root, text="Subject:").pack()
entry_subject = tk.Entry(root)
entry_subject.pack()

tk.Label(root, text="Message:").pack()
text_message = tk.Text(root, height=5)
text_message.pack()

tk.Button(root, text="Send", command=send_mail).pack()

root.mainloop()