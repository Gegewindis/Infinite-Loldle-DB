import customtkinter
import mysql.connector
from tkinter import Label

# TEST VAR
USER = "root"
PASSWORD = "georgeadrian2005@"

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
        self.tables_frame = customtkinter.CTkFrame(self.main_screen, fg_color="#008DD5")
        self.buttons_frame = customtkinter.CTkFrame(self.main_screen, width=300)
        self.buttons_frame.pack(anchor="w", side='left', fill="both")
        self.tables_frame.pack(anchor="e", side='right', expand=True, fill="both")

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

        # Main Screen Button Widgets
        self.tables = ["None"]
        self.selected_table = customtkinter.StringVar(value=self.tables[0])
        
        self.main_logout_button = customtkinter.CTkButton(self.buttons_frame, text="Log out", font=self.default_text_font, command=self.main_logout_button_callback, width=50)
        self.main_logout_button.pack(anchor="w", padx=10, pady=10)

        self.main_select_text = customtkinter.CTkLabel(self.buttons_frame, text="Select table:", fg_color="transparent", font=self.default_text_font)

        self.main_insert_button = customtkinter.CTkButton(self.buttons_frame, text="Insert", font=self.default_text_font, command=self.main_insert_button_callback)

        self.main_modify_button = customtkinter.CTkButton(self.buttons_frame, text="modify", font=self.default_text_font, command=self.main_modify_button_callback)

        self.main_remove_button = customtkinter.CTkButton(self.buttons_frame, text="remove", font=self.default_text_font, command=self.main_remove_button_callback)

        
    def login_button_callbck(self):
        try:
            self.mydb = mysql.connector.connect(
                host="localhost",
                user= USER, #self.login_entry_user.get(),
                passwd= PASSWORD #self.login_entry_pass.get()
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
            self.main_dropdown = customtkinter.CTkOptionMenu(self.buttons_frame, values=self.tables, variable=self.selected_table, command=self.main_dropdown_callback)
            self.main_select_text.pack(pady=(50, 0), padx=20)
            self.main_dropdown.pack(pady=(10, 0), padx=20)
            self.main_insert_button.pack(pady=(100, 0), padx=20)
            self.main_modify_button.pack(pady=(30, 0), padx=20)
            self.main_remove_button.pack(pady=(30, 0), padx=20)

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

    def main_dropdown_callback(self, choice):
        if choice == "None":
            return
        
        header = []
        self.cursor.execute("DESCRIBE " + self.selected_table.get())


        # Gets the column names and their correct lenght
        columnData = self.cursor.fetchall()
        for column in columnData:
            self.cursor.execute("SELECT MAX(CHAR_LENGTH(" + column[0] + ")) FROM " + self.selected_table.get() + ";")
            length = self.cursor.fetchall()[0][0]
            header.append((column[0], length))

        print(header)

        self.cursor.execute('SELECT * FROM ' + choice)
        data = self.cursor.fetchall()
        current_col_amount = len(data[0])
        current_row_amount = len(data)

        for i in range(current_col_amount):

            for j in range(current_row_amount):
                label = Label(self.tables_frame, width=header[i][1], text=data[j][i], relief="solid")
                label.grid(row=j, column=i)


        print(current_col_amount, current_row_amount)

app = App()
app.mainloop()