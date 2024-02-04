import tkinter as tk

class login:
    def __init__(self):
        self.window_ask = tk.Tk()
        self.window_ask.title("ask")

        label = tk.Label(self.window_ask, text="Choose User Type:")
        label.pack(pady=10)

        option1_button = tk.Button(self.window_ask, text="Student", command=self.login_kill_client)
        option1_button.pack(pady=5)

        option2_button = tk.Button(self.window_ask, text="Admin", command=self.login_kill_admin)
        option2_button.pack(pady=5)

        self.window_ask.mainloop()

    def login_admin(self):
        window_admin = tk.Tk()
        window_admin.title("Admin")

        username_label = tk.Label(text="Username:")
        username_label.grid(row=0, column=0, sticky="e", pady=5)
        username_entry = tk.Entry()
        username_entry.grid(row=0, column=1, pady=5)

        password_label = tk.Label(text="Password:")
        password_label.grid(row=1, column=0, sticky="e", pady=5)
        password_entry = tk.Entry(show="*")
        password_entry.grid(row=1, column=1, pady=5)

        login_button = tk.Button(text="Login")
        login_button.grid(row=2, column=0, columnspan=2, pady=10)

        window_admin.mainloop()
    
    def login_client(self):
        window_client = tk.Tk()
        window_client.title("Client")
        
        username_label = tk.Label(window_client, text="Username:")
        username_label.grid(row=0, column=0, sticky="e", pady=5)
        username_entry = tk.Entry(window_client)
        username_entry.grid(row=0, column=1, pady=5)

        password_label = tk.Label(window_client, text="Password:")
        password_label.grid(row=1, column=0, sticky="e", pady=5)
        password_entry = tk.Entry(window_client, show="*")
        password_entry.grid(row=1, column=1, pady=5)

        login_button = tk.Button(window_client, text="Login")
        login_button.grid(row=2, column=0, columnspan=2, pady=10)

        window_client.mainloop()
    
    def login_kill_admin(self):
        self.window_ask.destroy()
        self.login_admin()

    def login_kill_client(self):
        self.window_ask.destroy()
        self.login_client()
    
login_instance = login()