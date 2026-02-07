import customtkinter
import mysql.connector

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1280x720")
        self.title("Infinite Loldle WBMS")

        # Fonts
        self.big_text_font = customtkinter.CTkFont(family="Segoe UI", size=20, weight="normal")
        self.default_text_font = customtkinter.CTkFont(family="Segoe UI", size=14, weight="normal")
        self.default_title_font = customtkinter.CTkFont(family="Segoe UI", size=34, weight="normal")

        # Frames
        self.login_screen = customtkinter.CTkFrame(self, fg_color="transparent")
        self.main_screen = customtkinter.CTkFrame(self, fg_color="transparent")

        # Pack login frame
        self.login_screen.pack(fill="both", expand=True)

        # Login Screen Widgets
        self.login_title = customtkinter.CTkLabel(self.login_screen, text="Welcome!", fg_color="transparent", font=self.default_title_font)
        self.login_title.pack(pady=50)

        self.login_entry_user = customtkinter.CTkEntry(self.login_screen, placeholder_text="user", width=172)
        self.login_entry_user.pack(pady=10)

        self.login_entry_pass = customtkinter.CTkEntry(self.login_screen, placeholder_text="password", width=172, show="*")
        self.login_entry_pass.pack(pady=10)
        
        self.login_button = customtkinter.CTkButton(self.login_screen, text="Login", font=self.big_text_font, command=self.login_button_callbck, width=70, height=40)
        self.login_button.pack(padx=20, pady=20)

        # Main Screen Widgets
        self.tables = ["None"]
        self.selected_option = customtkinter.StringVar(value=self.tables[0])
        
        self.main_logout_button = customtkinter.CTkButton(self.main_screen, text="Log out", font=self.default_text_font, command=self.main_logout_button_callback, width=50)
        self.main_logout_button.pack(anchor="w", padx=10, pady=10)

        self.main_selected_text = customtkinter.CTkLabel(self.main_screen, text="Select table:", fg_color="transparent", font=self.default_text_font)

        self.main_insert_button = customtkinter.CTkButton(self.main_screen, text="Insert", font=self.default_text_font, command=self.main_insert_button_callback)

        self.main_modify_button = customtkinter.CTkButton(self.main_screen, text="modify", font=self.default_text_font, command=self.main_modify_button_callback)

        self.main_remove_button = customtkinter.CTkButton(self.main_screen, text="remove", font=self.default_text_font, command=self.main_remove_button_callback)

        
    def login_button_callbck(self):
        try:
            self.mydb = mysql.connector.connect(
                host="localhost",
                user=self.login_entry_user.get(),
                passwd=self.login_entry_pass.get()
            )

            self.login_entry_user.delete(0, "end")
            self.login_entry_pass.delete(0, "end")
            print("Connection made!")

            # Setup for main screen
            self.cursor = self.mydb.cursor()

            self.cursor.execute("USE infloldle")
            self.cursor.execute("SHOW TABLES")

            for element in self.cursor.fetchall():
                self.tables.append(element[0])

            # Initilazing some widgets
            self.main_dropdown = customtkinter.CTkOptionMenu(self.main_screen, values=self.tables, variable=self.selected_option)
            self.main_selected_text.pack(pady=(50, 0), padx=20, anchor="w")
            self.main_dropdown.pack(pady=(10, 0), padx=20, anchor="w")
            self.main_insert_button.pack(pady=(100, 0), padx=20, anchor="w")
            self.main_modify_button.pack(pady=(30, 0), padx=20, anchor="w")
            self.main_remove_button.pack(pady=(30, 0), padx=20, anchor="w")

            # Switch screen
            self.login_screen.pack_forget()
            self.main_screen.pack(fill="both", expand=True)

        except mysql.connector.Error as err:
            print("Error:", err)
    
    def main_logout_button_callback(self):
            # Switch screen
            self.main_screen.pack_forget()
            self.login_screen.pack(fill="both", expand=True)

    def main_insert_button_callback(self):
        print("insert")

    def main_modify_button_callback(self):
        print("modify")

    def main_remove_button_callback(self):
        print("remove")

app = App()
app.mainloop()