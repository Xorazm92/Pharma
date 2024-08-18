import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon

from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QListWidget,
    QListWidgetItem,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QLineEdit,
    QStackedWidget,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,                       
    QPushButton,
    QTableWidget,
    QTableWidgetItem,   
    QHeaderView,
    QLineEdit,
    QFrame
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mehnat-1")
        self.setGeometry(100, 100, 800, 600)

        main_widget = QWidget()
        main_layout = QHBoxLayout()

        self.sidebar_layout = QVBoxLayout()
        sidebar_items = [
            "Mijoz",
            "Ta'minotchi",
            "Xarid va tolov",  
            "Sotuv va Tolov",
            "Adminlar",
            "Kategoriya", 
            "Maxsulot"
        ]

        self.sidebar_buttons = []
        for i, item in enumerate(sidebar_items):
            button = QPushButton(item)
            button.setStyleSheet("""
                QPushButton {
                    border: 1px solid #ccc;
                    border-radius: 5px;
                    padding: 10px;
                    background-color: #f0f0f0;
                    text-align: left;
                }
                QPushButton:hover {
                    background-color: #e0e0e0;
                }
                QPushButton:checked {
                    background-color: #d0d0d0;
                }
            """)
            button.setCheckable(True)
            button.clicked.connect(lambda _, idx=i: self.display_content(idx))
            self.sidebar_buttons.append(button)
            self.sidebar_layout.addWidget(button)

        self.stacked_widget = QStackedWidget()

        self.stacked_widget.addWidget(self.create_customer_page())
        self.stacked_widget.addWidget(self.create_supplier_page())
        self.stacked_widget.addWidget(self.create_purchase_payment_page())
        self.stacked_widget.addWidget(self.create_sale_payment_page())
        self.stacked_widget.addWidget(self.create_users_page())
        self.stacked_widget.addWidget(self.create_category_page())
        self.stacked_widget.addWidget(self.create_product_page())

        main_layout.addLayout(self.sidebar_layout, 1)
        main_layout.addWidget(self.stacked_widget, 3)

        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

    def display_content(self, index):
        self.stacked_widget.setCurrentIndex(index)

    def create_customer_page(self):
        widget = QWidget()
        layout = QVBoxLayout()

        employee_frame = QFrame()
        employee_frame.setFrameShape(QFrame.Shape.Box)
        employee_frame.setFrameShadow(QFrame.Shadow.Raised)
        employee_frame.setLineWidth(2)
        employee_layout = QVBoxLayout(employee_frame)

        employee_title = QLabel("Registered Employees")
        employee_title.setStyleSheet("font-weight: bold; font-size: 16px;")
        employee_layout.addWidget(employee_title)

        self.employee_list = QListWidget()
        self.populate_employee_list()
        employee_layout.addWidget(self.employee_list)

        button_layout = QHBoxLayout()
        delete_button = QPushButton("Delete Selected")
        delete_button.clicked.connect(self.delete_selected_employee)
        view_button = QPushButton("View Details")
        view_button.clicked.connect(self.view_employee_details)
        button_layout.addWidget(delete_button)
        button_layout.addWidget(view_button)
        
        employee_layout.addLayout(button_layout)

        layout.addWidget(employee_frame)
        widget.setLayout(layout)
        
        return widget

    def populate_employee_list(self):
        employees = [
            ("John Doe", "Employee ID: 1234", "Sales"),
            ("Jane Smith", "Employee ID: 5678", "Marketing"),
            ("Emily Davis", "Employee ID: 9101", "HR"),
            ("Michael Brown", "Employee ID: 1121", "IT")
        ]
        self.employee_list.clear()
        for name, id_info, department in employees:
            item_text = f"{name}\n{id_info}\nDepartment: {department}"
            self.employee_list.addItem(item_text)

    def delete_selected_employee(self):
        selected_items = self.employee_list.selectedItems()
        if selected_items:
            for item in selected_items:
                self.employee_list.takeItem(self.employee_list.row(item))

    def view_employee_details(self):
        selected_items = self.employee_list.selectedItems()
        if selected_items:
            selected_item = selected_items[0]
            employee_info = selected_item.text()
            self.show_employee_details(employee_info)

    def show_employee_details(self, info):
        from PyQt6.QtWidgets import QMessageBox
        details_dialog = QMessageBox(self)
        details_dialog.setWindowTitle("Employee Details")
        details_dialog.setText(f"Details:\n{info}\n\nPurchase history information would be here.")
        details_dialog.exec()
        
        return self.create_page_widget("Mijozlar sahifasi")

    def create_supplier_page(self):
        widget = self.create_page_widget("Ta'minotchilar sahifasi")

        search_layout = QHBoxLayout()
        search_input = QLineEdit()
        search_input.setPlaceholderText("Search Ta'minotchi")
        search_button = QPushButton("Search")
        search_layout.addWidget(search_input)
        search_layout.addWidget(search_button)

        supplier_list = QListWidget()
        suppliers = [
            ("OOO ART TEX SERVIS", "998 976 548 526"),
            ("X.K. NASIBA-GAVHAR", "998 551 552 355"),
            ("XARBIY ANJOMLAR", "998 881 358 604"),
            ("OOO CENTRAL TEKSTIL", "998 338 995 284"),
            ("OOO Premium", "998 932 326 589")
        ]

        for name, phone in suppliers:
            item = QListWidgetItem(f"{name}\n{phone}")
            supplier_list.addItem(item)

        layout = widget.layout()
        layout.addLayout(search_layout)
        layout.addWidget(supplier_list)

        return widget
    



# ------------------------------------------------------------
    # def create_purchase_payment_page(self):
    def create_purchase_payment_page(self):
        widget = QWidget()
        layout = QHBoxLayout()

        xarid_widget = self.create_xarid_section()
        taminotchiga_tolov_widget = self.create_taminotchiga_tolov_section()
        bugungi_xaridim_widget = self.create_bugungi_xaridim_section()

        layout.addWidget(xarid_widget)
        layout.addWidget(taminotchiga_tolov_widget)
        layout.addWidget(bugungi_xaridim_widget)

        widget.setLayout(layout)
        return widget

    def create_xarid_section(self):
        frame = QFrame()
        frame.setFrameShape(QFrame.Shape.Box)
        frame.setFrameShadow(QFrame.Shadow.Raised)
        frame.setLineWidth(1)
        
        layout = QVBoxLayout()
        
        title = QLabel("Xarid")
        title.setStyleSheet("font-weight: bold; font-size: 14px;")
        layout.addWidget(title)
        
        table = QTableWidget(4, 4)
        table.setHorizontalHeaderLabels(["Ta'minotchi", "Sana", "Xarid savatim", "Tami"])
        layout.addWidget(table)
        
        add_button = QPushButton("+ Qo'shish")
        layout.addWidget(add_button)
        
        frame.setLayout(layout)
        return frame

    def create_taminotchiga_tolov_section(self):
        frame = QFrame()
        frame.setFrameShape(QFrame.Shape.Box)
        frame.setFrameShadow(QFrame.Shadow.Raised)
        frame.setLineWidth(1)
        
        layout = QVBoxLayout()
        
        title = QLabel("Taminotchiga to'lov")
        title.setStyleSheet("font-weight: bold; font-size: 14px;")
        layout.addWidget(title)
        
        table = QTableWidget(2, 2)
        table.setHorizontalHeaderLabels(["Ta'minotchi", "To'lov"])
        layout.addWidget(table)
        
        add_button = QPushButton("To'lash")
        layout.addWidget(add_button)
        
        frame.setLayout(layout)
        return frame

    def create_bugungi_xaridim_section(self):
        frame = QFrame()
        frame.setFrameShape(QFrame.Shape.Box)
        frame.setFrameShadow(QFrame.Shadow.Raised)
        frame.setLineWidth(1)
        
        layout = QVBoxLayout()
        
        title = QLabel("Bugungi xaridim")
        title.setStyleSheet("font-weight: bold; font-size: 14px;")
        layout.addWidget(title)
        
        table = QTableWidget(0, 3)  # Start with 0 rows
        table.setHorizontalHeaderLabels(["Ta'minotchi", "Sana", "Xarid"])
        layout.addWidget(table)
        
        add_button = QPushButton("+ Qo'shish")
        layout.addWidget(add_button)
        
        frame.setLayout(layout)
        return frame
    
    
        # return self.create_page_widget("Xarid va tolov sahifasi")

# ---------------------------------------------------



    # def create_sale_payment_page(self):
        # return self.create_page_widget("Sotuv va tolov sahifasi")
    def create_sale_payment_page(self):
        widget = QWidget()
        layout = QHBoxLayout()

        sotuv_widget = self.create_sotuv_section()
        bugungi_sotuv_widget = self.create_bugungi_sotuv_section()
        tolov_widget = self.create_tolov_section()

        layout.addWidget(sotuv_widget)
        layout.addWidget(bugungi_sotuv_widget)
        layout.addWidget(tolov_widget)

        widget.setLayout(layout)
        return widget

    def create_sotuv_section(self):
        frame = QFrame()
        frame.setFrameShape(QFrame.Shape.Box)
        frame.setFrameShadow(QFrame.Shadow.Raised)
        frame.setLineWidth(1)
        
        layout = QVBoxLayout()
        
        title = QLabel("Sotuv")
        title.setStyleSheet("font-weight: bold; font-size: 14px;")
        layout.addWidget(title)
        
        table = QTableWidget(5, 3)
        table.setHorizontalHeaderLabels(["Mijoz", "Sana", "Summa"])
        table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        
        data = [
            ("Buxoro MTU", "3.2.2023", "45000"),
            ("Termiz MTU", "4.2.2023", "155000"),
            ("Qo'qon MTU", "4.2.2023", "345000"),
            ("Qongirot MTU", "4.2.2023", "385000"),
            ("Qarshi MTU", "4.2.2023", "545000")
        ]

        for row, (customer, date, amount) in enumerate(data):
            table.setItem(row, 0, QTableWidgetItem(customer))
            table.setItem(row, 1, QTableWidgetItem(date))
            table.setItem(row, 2, QTableWidgetItem(amount))
        
        layout.addWidget(table)
        
        add_button = QPushButton("+ Qo'shish")
        layout.addWidget(add_button)
        
        frame.setLayout(layout)
        return frame

    def create_bugungi_sotuv_section(self):
        frame = QFrame()
        frame.setFrameShape(QFrame.Shape.Box)
        frame.setFrameShadow(QFrame.Shadow.Raised)
        frame.setLineWidth(1)
        
        layout = QVBoxLayout()
        
        title = QLabel("Bugungi sotuv")
        title.setStyleSheet("font-weight: bold; font-size: 14px;")
        layout.addWidget(title)
        
        table = QTableWidget(0, 3)
        table.setHorizontalHeaderLabels(["Mijoz", "Sana", "Summa"])
        table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        layout.addWidget(table)

        add_button = QPushButton("+ Qo'shish")
        layout.addWidget(add_button)
        
        frame.setLayout(layout)
        return frame

    def create_tolov_section(self):
        frame = QFrame()
        frame.setFrameShape(QFrame.Shape.Box)
        frame.setFrameShadow(QFrame.Shadow.Raised)
        frame.setLineWidth(1)
        
        layout = QVBoxLayout()
        
        title = QLabel("To'lov")
        title.setStyleSheet("font-weight: bold; font-size: 14px;")
        layout.addWidget(title)
        
        table = QTableWidget(5, 3)
        table.setHorizontalHeaderLabels(["Mijoz", "Summa", "Sana"])
        table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        
        data = [
            ("Qo'qon MTU", "284 000", "4.2.2023"),
            ("Buxoro MTU", "45 000", "3.2.2023"),
            ("Qo'qon MTU", "345 000", "4.2.2023"),
            ("Qo'qon MTU", "424 000", "6.2.2023"),
            ("Qarshi MTU", "545 000", "4.2.2023")
        ]

        for row, (customer, amount, date) in enumerate(data):
            table.setItem(row, 0, QTableWidgetItem(customer))
            table.setItem(row, 1, QTableWidgetItem(amount))
            table.setItem(row, 2, QTableWidgetItem(date))
            
            action_widget = QWidget()
            action_layout = QHBoxLayout(action_widget)
            action_layout.setContentsMargins(0, 0, 0, 0)
            
            for icon_name in ["trash", "edit", "undo", "redo", "print"]:
                button = QPushButton()
                button.setIcon(QIcon(f"path/to/{icon_name}_icon.png"))
                action_layout.addWidget(button)

            table.setCellWidget(row, 3, action_widget)

        layout.addWidget(table)

        add_button = QPushButton("+ To'lash")
        layout.addWidget(add_button)

        frame.setLayout(layout)
        return frame

# -------------------------------------------------
    

    # def create_users_page(self):
    #     """Create the Users page widget."""
    #     return self.create_page_widget("Adminlar sahifasi")

    def create_users_page(self):
        """Create the Users/Administrators page widget."""
        widget = QWidget()
        layout = QVBoxLayout()

        title = QLabel("Foydalanuvchilar")
        title.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(title)

        search_layout = QHBoxLayout()
        search_input = QLineEdit()
        search_input.setPlaceholderText("Search Foydalanuvchilar")
        search_button = QPushButton(QIcon("path/to/search_icon.png"), "")
        search_layout.addWidget(search_input)
        search_layout.addWidget(search_button)
        layout.addLayout(search_layout)

        self.users_table = QTableWidget()
        self.users_table.setColumnCount(4)
        self.users_table.setHorizontalHeaderLabels(["Name", "Email", "Role", "Actions"])
        self.users_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.populate_users_table()
        layout.addWidget(self.users_table)

        add_user_button = QPushButton("+ Yangi foyd...")
        add_user_button.clicked.connect(self.add_new_user)
        layout.addWidget(add_user_button, alignment=Qt.AlignmentFlag.AlignRight)

        widget.setLayout(layout)
        return widget

    def populate_users_table(self):
        users_data = [
            ("Admin", "rayadunia2021@gmail.com", "Admin"),
            ("Odil nazaratchi", "NBT@gmail.com", "NBT(Tarqatuvchi)"),
            ("Laziz Qarshi TB", "Qarshi@gmail.com", "TB")
        ]
        self.users_table.setRowCount(len(users_data))

        for row, (name, email, role) in enumerate(users_data):
            self.users_table.setItem(row, 0, QTableWidgetItem(name))
            self.users_table.setItem(row, 1, QTableWidgetItem(email))
            self.users_table.setItem(row, 2, QTableWidgetItem(role))

            action_widget = QWidget()
            action_layout = QHBoxLayout(action_widget)
            action_layout.setContentsMargins(0, 0, 0, 0)

            info_button = QPushButton(QIcon("path/to/info_icon.png"), "")
            info_button.clicked.connect(lambda _, r=row: self.show_user_info(r))
            action_layout.addWidget(info_button)

            self.users_table.setCellWidget(row, 3, action_widget)

    def show_user_info(self, row):
        name = self.users_table.item(row, 0).text()
        email = self.users_table.item(row, 1).text()
        role = self.users_table.item(row, 2).text()

        print(f"User Info: {name}, {email}, {role}")

    def add_new_user(self):
        print("Adding a new user")
    

    # ----------------------------------------------------

    # def create_category_page(self):
    #     """Create the Category page widget."""
    #     return self.create_page_widget("Kategoriya sahifasi")

    def create_category_page(self):
        widget = QWidget()
        layout = QVBoxLayout()

        title = QLabel("Kategoriya")
        title.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(title)

        self.categories_table = QTableWidget()
        self.categories_table.setColumnCount(3)
        self.categories_table.setHorizontalHeaderLabels(["Icon", "Name", "Actions"])
        self.categories_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.categories_table.verticalHeader().setVisible(False)
        self.populate_categories_table()
        layout.addWidget(self.categories_table)

        add_category_button = QPushButton("Kategoriya qo'shish")
        add_category_button.clicked.connect(self.add_new_category)
        layout.addWidget(add_category_button, alignment=Qt.AlignmentFlag.AlignRight)

        widget.setLayout(layout)
        return widget

    def populate_categories_table(self):
        categories_data = [
            "Maxsus kiyim",
            "Maxsus poyabzal",
            "Shaxsiy ximoya vositalari"
        ]
        self.categories_table.setRowCount(len(categories_data))

        for row, category in enumerate(categories_data):
            icon_label = QLabel()
            icon_label.setPixmap(QIcon("path/to/warning_icon.png").pixmap(24, 24))
            icon_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.categories_table.setCellWidget(row, 0, icon_label)

            self.categories_table.setItem(row, 1, QTableWidgetItem(category))

            action_widget = QWidget()
            action_layout = QHBoxLayout(action_widget)
            action_layout.setContentsMargins(0, 0, 0, 0)

            view_button = QPushButton(QIcon("path/to/view_icon.png"), "")
            edit_button = QPushButton(QIcon("path/to/edit_icon.png"), "")
            action_layout.addWidget(view_button)
            action_layout.addWidget(edit_button)

            self.categories_table.setCellWidget(row, 2, action_widget)

    def add_new_category(self):
        print("Adding a new category")
    
# -----------------------------------------------------
    # def create_product_page(self):
    #     """Create the Product page widget."""
    #     return self.create_page_widget("Maxsulot sahifasi")

    def create_product_page(self):
        widget = QWidget()
        layout = QVBoxLayout()

        title_layout = QHBoxLayout()
        title = QLabel("Maxsulotlar")
        title.setStyleSheet("font-size: 18px; font-weight: bold;")
        add_product_button = QPushButton("+ Maxsulot qo'shish")
        add_product_button.clicked.connect(self.add_new_product)
        title_layout.addWidget(title)
        title_layout.addStretch()
        title_layout.addWidget(add_product_button)
        layout.addLayout(title_layout)

        search_layout = QHBoxLayout()
        search_input = QLineEdit()
        search_input.setPlaceholderText("Maxsulotlarni qidirish")
        search_button = QPushButton(QIcon("path/to/search_icon.png"), "")
        search_layout.addWidget(search_input)
        search_layout.addWidget(search_button)
        layout.addLayout(search_layout)

        self.products_table = QTableWidget()
        self.products_table.setColumnCount(6)
        self.products_table.setHorizontalHeaderLabels(["Rasm", "Nomi", "Kategoriyasi", "Miqdori", "Narxi", "Amallar"])
        self.products_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.products_table.verticalHeader().setVisible(False)
        self.populate_products_table()
        layout.addWidget(self.products_table)

        widget.setLayout(layout)
        return widget

    def populate_products_table(self):
        """Populate the products table with sample data."""
        products_data = [
            ("Etik", "Maxsus poyabzal", "100", "50000"),
            ("Qo'lqop", "Shaxsiy ximoya vositalari", "200", "15000"),
            ("Kaska", "Shaxsiy ximoya vositalari", "50", "100000")
        ]
        self.products_table.setRowCount(len(products_data))
        
        for row, (name, category, quantity, price) in enumerate(products_data):
            image_label = QLabel()
            image_label.setPixmap(QIcon("path/to/product_image_placeholder.png").pixmap(32, 32))
            image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.products_table.setCellWidget(row, 0, image_label)

            self.products_table.setItem(row, 1, QTableWidgetItem(name))
            self.products_table.setItem(row, 2, QTableWidgetItem(category))
            self.products_table.setItem(row, 3, QTableWidgetItem(quantity))
            self.products_table.setItem(row, 4, QTableWidgetItem(price))

            action_widget = QWidget()
            action_layout = QHBoxLayout(action_widget)
            action_layout.setContentsMargins(0, 0, 0, 0)

            view_button = QPushButton(QIcon("path/to/view_icon.png"), "")
            edit_button = QPushButton(QIcon("path/to/edit_icon.png"), "")
            delete_button = QPushButton(QIcon("path/to/delete_icon.png"), "")
            action_layout.addWidget(view_button)
            action_layout.addWidget(edit_button)
            action_layout.addWidget(delete_button)

            self.products_table.setCellWidget(row, 5, action_widget)

    def add_new_product(self):
        print("Adding a new product")
   
# ----------------------------------------------------



    def create_page_widget(self, title):
        widget = QWidget()
        layout = QVBoxLayout()
        frame = QFrame()
        frame.setFrameShape(QFrame.Shape.Box)
        frame.setFrameShadow(QFrame.Shadow.Raised)
        frame.setLineWidth(2)

        frame_layout = QVBoxLayout(frame)
        frame_layout.addWidget(QLabel(title))
        frame.setLayout(frame_layout)

        layout.addWidget(frame)
        widget.setLayout(layout)
        return widget

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())