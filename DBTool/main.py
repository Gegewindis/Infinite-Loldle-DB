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
        self.title("Infinite Loldle DB tool")
        self.selected_widget = None

        # Fonts
        self.big_text_font = customtkinter.CTkFont(family="Segoe UI", size=20, weight="normal")
        self.default_text_font = customtkinter.CTkFont(family="Segoe UI", size=14, weight="normal")
        self.default_title_font = customtkinter.CTkFont(family="Segoe UI", size=34, weight="normal")

        # Frames
        self.login_screen = customtkinter.CTkFrame(self, fg_color="transparent")
        self.main_screen = customtkinter.CTkFrame(self, fg_color="transparent")
        self.tables_frame = customtkinter.CTkScrollableFrame(self.main_screen, fg_color="#2f2f2f")
        self.buttons_frame = customtkinter.CTkFrame(self.main_screen, width=300, )
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
            self.main_remove_button.pack(pady=(30, 0), padx=20)
            self.main_modify_button.pack(pady=(30, 0), padx=20)

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
        self.insert_popup_window = customtkinter.CTkToplevel(self)
        self.insert_popup_window.title("Modify")
        self.insert_popup_window.geometry("300x500")
        self.insert_popup_window.transient(self)

        frame = customtkinter.CTkScrollableFrame(self.insert_popup_window)
        frame.pack(fill="both", expand=True)

        self.insert_entries = []
        for i in range(len(self.selected_table_header)):
            label = customtkinter.CTkLabel(frame, text=self.selected_table_header[i][0])
            entry = customtkinter.CTkEntry(frame, placeholder_text="input...")
            self.insert_entries.append(entry)
            space_frame = customtkinter.CTkFrame(frame, height=30)
            frame.grid_columnconfigure(0, weight=1)
            frame.grid_rowconfigure(0, weight=1)
            label.grid(row=i * 3, sticky="nsew", pady=10)
            entry.grid(row=1 + i * 3, sticky="nsew", padx=60)
            space_frame.grid(row=2 + i * 3, sticky="nsew")

        self.insert_submit = customtkinter.CTkButton(frame, text="Submit", command=self.insert, width=80)
        self.insert_submit.grid(row= i * 3 + 2, pady=20)
                                                     
                                                  
    def insert(self):
        new_data = []
        for entry in self.insert_entries:
            new_data.append((entry.get()))

        attributes = []
        for attr in self.selected_table_header:
            attributes.append(attr[0])

        self.cursor.execute("INSERT INTO " + self.selected_table.get() + " (" + ", ".join(attributes) + ") VALUES (" + ", ".join(new_data) + ")")
        self.selected_table_data.append(tuple(new_data))

        # CREATES ONE AT THE BOTTOM INSTEAD OF RELOADING
        # for i in range(len(self.selected_table_data[0])):
        #         label = Label(self.tables_frame, width=self.selected_table_header[i][1], text=self.selected_table_data[len(self.selected_table_data) - 1][i], relief="solid")
        #         label.grid(row=len(self.selected_table_data), column=i)
        #         label.bind("<Button-1>", self.on_label_click)

        self.mydb.commit()
        self.insert_popup_window.destroy()

        self.main_dropdown_callback(self.selected_table.get())

        
    def main_modify_button_callback(self):
        self.modify_popup_window = customtkinter.CTkToplevel(self)
        self.modify_popup_window.title("Modify")
        self.modify_popup_window.geometry("300x100")
        self.modify_popup_window.transient(self)

        label = customtkinter.CTkLabel(self.modify_popup_window, text="Change it to")
        label.pack(pady=10)

        self.modify_input_entry = customtkinter.CTkEntry(self.modify_popup_window, placeholder_text="input...", width=172)
        self.modify_input_entry.bind("<Return>", self.modify)
        self.modify_input_entry.pack()

    def modify(self, event):
        self.cursor.execute("UPDATE " + self.selected_table.get() + " SET " + self.selected_table_header[self.selected_widget['column']][0] + " = '" + self.modify_input_entry.get() + "' WHERE " + self.selected_table_header[0][0] + " = '" + self.selected_table_data[self.selected_widget['row']][0] + "'")
        self.selected_widget["widget"].config(text=self.modify_input_entry.get())
        self.mydb.commit()
        self.modify_popup_window.destroy()


    def main_remove_button_callback(self):
        self.remove_popup_window = customtkinter.CTkToplevel(self)
        self.remove_popup_window.title("Modify")
        self.remove_popup_window.geometry("400x100")
        self.remove_popup_window.transient(self)

        label = customtkinter.CTkLabel(self.remove_popup_window, text="Whats the primary key? If composite, seperate with a comma")
        label.pack(pady=10)

        self.remove_input_entry = customtkinter.CTkEntry(self.remove_popup_window, placeholder_text="key1,key2...", width=172)
        self.remove_input_entry.bind("<Return>", self.remove)
        self.remove_input_entry.pack()


    def remove(self, event):
        keys = []
        for i in range(len(self.selected_table_header)):
            if self.selected_table_header[i][2] == "#25709E": #PRIMARY KEY COLOR, might change
                keys.append(self.selected_table_header[i][0])

        keys_input = self.remove_input_entry.get().split(",")

        condition = " WHERE " + keys[0] + " = '" + keys_input[0] + "'"
        if len(keys) > 1:
            for i in range(1, len(keys)):
                condition += " AND " + keys[i] + " = '" + keys_input[i] + "'"

        self.cursor.execute("DELETE FROM " + self.selected_table.get() + condition)

        # COLORS THE REMOVED ONE INSTEAD OF RELOADING
        # for j in range(len(self.selected_table_data)):
        #     print(self.selected_table_data[j][i])
        #     if self.selected_table_data[j][i] == self.remove_input_entry.get():
        #        for widget in self.tables_frame.grid_slaves(row=j + 1):
        #            widget.config(bg="#471323")

        self.mydb.commit()
        self.remove_popup_window.destroy()

        self.main_dropdown_callback(self.selected_table.get())



    def main_dropdown_callback(self, choice):
        for widget in self.tables_frame.winfo_children():
            widget.destroy()
            self.selected_widget = {}

        if choice == "None":
            return

        self.selected_table_header = []

        self.cursor.execute("DESCRIBE " + self.selected_table.get())
        columnData = self.cursor.fetchall()

        for column in columnData:
            self.cursor.execute("SELECT MAX(CHAR_LENGTH(" + column[0] + ")) FROM " + self.selected_table.get() + ";")
            length = self.cursor.fetchall()[0][0]
            if len(column[0]) > length:
                length = len(column[0])


            if column[3] == "PRI":
                color = "#25709E"
            elif column[3] == '':
                color = "#FFFFFF"
            else:
                color = "#86213F"

            self.selected_table_header.append((column[0], length, color))

        self.cursor.execute("SELECT * FROM " + choice)
        self.selected_table_data = self.cursor.fetchall()

        current_col_amount = len(self.selected_table_data[0])
        current_row_amount = len(self.selected_table_data)

        for i in range(current_col_amount):
            label = Label(self.tables_frame, width=self.selected_table_header[i][1], text=self.selected_table_header[i][0], relief="solid", bg=self.selected_table_header[i][2])
            label.grid(row=0, column=i)

            for j in range(current_row_amount):
                label = Label(self.tables_frame, width=self.selected_table_header[i][1], text=self.selected_table_data[j][i], relief="solid")
                label.grid(row=j + 1, column=i)
                label.bind("<Button-1>", self.on_label_click)


    def on_label_click(self, event):
        if self.selected_widget:
            self.selected_widget["widget"].config(bg="#FFFFFF")
        else:
            self.selected_widget = {}

        self.selected_widget["widget"] = event.widget
        info = self.selected_widget["widget"].grid_info()
        self.selected_widget["row"] = info["row"] - 1
        self.selected_widget["column"] = info["column"]
        self.selected_widget["widget"].config(bg="lightblue")


app = App()
app.mainloop()