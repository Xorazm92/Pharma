from PyQt6.QtWidgets import(
        QApplication,
        QWidget,
        QHBoxLayout,
        QVBoxLayout,
        QPushButton,
        QLabel,
        QFormLayout,
        QScrollArea,
        QLineEdit,
        QMenu,
        QMenuBar,
        QTableWidgetItem,
    )
from PyQt6 import QtWidgets, QtCore
from PyQt6.QtGui import QAction, QIcon, QPixmap, QFont
from PyQt6.QtCore import Qt


class AboutPage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Login Page")
        self.showMaximized()
        self.setStyleSheet("""
            background-color: #fff;
            font-size: 30px;
        """)
        # 
        self.v_box = QVBoxLayout()

        form_layout = QVBoxLayout()
        form_layout.setContentsMargins(50, 10, 50, 10)
        form_layout.setSpacing(20)
        form_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # logo bolimi
        self.logo_lebel = QLabel(self)
        self.logo_lebel.setStyleSheet("""
            QLabel{
                background-color: #424c59
            }
        """)
        pixmap = QPixmap("logo.png")
        self.logo_lebel.setPixmap(pixmap)
        self.logo_lebel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        form_layout.addWidget(self.logo_lebel)

        self.title = QLabel("""
            <div style="text-align: center;line-height:0.8;">
                <p style="font-size: 28px; font-weight:bold; color: #00838f;">Dorixona dasturlari boshqaruvchilari va foydalanuvchilari uchun ro'yxatdan o'tish</p>
                <p style="font-size: 26px; font-weight:bold; color: #00838f;"> va da'vo qilish uchun mo'ljallangan portalga xush kelibsiz!</p>
            </div>
        """)
        self.title.setStyleSheet("color: #00838f;")
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        form_layout.addWidget(self.title)
        

        
        self.line_lebel = QLabel(self)
        pixline = QPixmap("line.png")
        self.line_lebel.setPixmap(pixline)
        self.line_lebel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        form_layout.addWidget(self.line_lebel)
        


        self.enter_button = QPushButton("Kirish")
        self.enter_button.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border: 4px ridge #f1f2f3;
                border-radius: 12px;
                padding: 10px 25px;
                width: 150px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }

        """)
        form_layout.addWidget( self.enter_button, alignment=Qt.AlignmentFlag.AlignCenter)
        self.enter_button.clicked.connect(self.def_login)

        
        self.info_title = QLabel("""
            <div style="text-align: left; width: 100%; line-height:0;">
                <h3>Dori-Darmonlar Bo'yicha Imtiyozlar:</h3>
                <hr>
                <ul>
                    <li><b>Bepul Dori-Darmonlar:</b> Ehtiyojmand keksa odamlar va nogironlar uchun davlat tomonidan belgilangan ro'yxatdagi ayrim dori-darmonlar bepul taqdim etiladi.</li>
                    <li>Pensiya va ijtimoiy nafaqa oluvchilar uchun ayrim dori-darmonlar bepul yoki subsidiyalangan narxda taqdim etiladi.</li>
                </ul>
            </div>
            <div style="text-align: left; width: 100%; line-height:0;">
                <h3 >Bepul Davolanish Bo'yicha Imtiyozlar:</h3>
                <hr>
                <ul>
                    <li><b>Davlat Tibbiy Xizmatlari:</b> Davlat tomonidan moliyalashtiriladigan poliklinikalar va gospitalarda keksa odamlar va nogironlar uchun bepul tibbiy xizmatlar ko'rsatiladi.</li>
                    <li>Keksalar va nogironlar uchun umumiy terapevtik xizmatlar, diagnostika tahlillari va laboratoriya tekshiruvlari bepul taqdim etiladi.</li>
                    <li><b>Maxsus Tibbiy Xizmatlar:</b> Keksalar va nogironlar uchun reabilitatsiya markazlarida bepul davolanish va fizioterapiya xizmatlari ko'rsatiladi.</li>
                </ul>
            </div>
        """)
        self.info_title.setStyleSheet("font-size: 18px; color: #333333;")
        self.info_title.setAlignment(Qt.AlignmentFlag.AlignLeft)
        form_layout.addWidget(self.info_title)
       
        self.v_box.addLayout(form_layout)
        self.setLayout(self.v_box)


        # scroll_area = QScrollArea()
        # scroll_area.setWidgetResizable(True)
        # scroll_content = QWidget()
        # scroll_content.setLayout(self.v_box)
        # scroll_area.setWidget(scroll_content)

        # main_layout = QVBoxLayout(self)
        # main_layout.addWidget(scroll_area)

        # self.setLayout(main_layout)

    def def_login(self):
        self.close()
        self.login = LoginPage()

class LoginPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login Page")
        self.showMaximized()
        self.setStyleSheet("""
            background-color: #fff;
            font-size: 30px;
        """)

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(20)
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
      # Logo va title uchun layout
        form_layout = QVBoxLayout()
        form_layout.setContentsMargins(0, 0, 0, 0)
        form_layout.setSpacing(20)
        form_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.login_logo_label = QLabel(self)
        self.login_logo_label.setStyleSheet("""
            QLabel{
                background-color: #424c59
            }
        """)
        pixmapl = QPixmap("login_logo.png")
        self.login_logo_label.setPixmap(pixmapl)
        self.login_logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        form_layout.addWidget(self.login_logo_label)

        self.login_title = QLabel("Platformaga kirish")
        self.login_title.setStyleSheet("""
            QLabel{
                background-color: #14808d;
            }
        """)
        # self.login_title.setFont(QFont("Poppins", 32, QFont.Weight.Medium))
        self.login_title.setStyleSheet("color: #F9E400;")
        self.login_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        form_layout.addWidget(self.login_title)
 # Login va parol uchun form layout
        form_layout1 = QVBoxLayout()
        form_layout1.setContentsMargins(0, 0, 0, 0)
        form_layout1.setSpacing(20)
        form_layout1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        login_layout = QHBoxLayout()
        self.login_label = QLabel("Login:")
        self.login_label.setMinimumWidth(100)
        self.login_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.login_input = QLineEdit()
        self.login_input.setStyleSheet("""
            background-color: #2d3137;
            color: white;
            font-size: 25px;
            padding: 10px 25px 10px 25px;
            border: 4px ridge #f1f2f3;
            border-radius: 12px;
        """)
        self.login_input.setPlaceholderText("👤 Loginni kiriting...")
        self.login_input.setMinimumWidth(200)

        login_layout.addWidget(self.login_label)
        login_layout.addWidget(self.login_input)

        login_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)        
        form_layout1.addLayout(login_layout)

        
       
        password_layout = QHBoxLayout()
        self.password_label = QLabel("Parol:")
        self.password_label.setMinimumWidth(100)
        self.password_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.password_input = QLineEdit()
        self.password_input.setStyleSheet("""
            background-color: #2d3137;
            color: white;
            font-size: 25px;
            padding: 10px 25px 10px 25px;
            border: 4px ridge #f1f2f3;
            border-radius: 12px;
        """)
        self.password_input.setPlaceholderText("🔒 Parolni kiriting...")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setMinimumWidth(200)

        password_layout.addWidget(self.password_label)
        password_layout.addWidget(self.password_input)
        password_layout.setAlignment(Qt.AlignmentFlag.AlignCenter) 
        form_layout1.addLayout(password_layout)
              


        self.info_label = QLabel()
# Login tugmasi
        self.login_button = QPushButton("Login")
        self.login_button.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border: 4px ridge #f1f2f3;
                border-radius: 12px;
                padding: 10px 25px;
                width: 150px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }

        """)
        form_layout1.addWidget(self.login_button)

        # form_layout1.addWidget(self.login_button)
        # self.login_button.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.login_button.clicked.connect(self.handle_login)

        social_layout = QHBoxLayout()
        social_layout.setContentsMargins(0, 30, 0, 0)
        social_layout.setSpacing(25)

        self.forget_button = QPushButton("Parolni tiklash")
        self.forget_button.setStyleSheet("""
            background-color: rgba(255,255,255,0.27);
            color: #eaf0fb;
            padding: 10px;
            border-radius: 3px;
            font-size: 14px;
        """)
        social_layout.addWidget(self.forget_button)

        self.registration_button = QPushButton("Ro'yxatdan o'tish")
        self.registration_button.clicked.connect(self.registr)
        self.registration_button.setStyleSheet("""
            background-color: rgba(255,255,255,0.27);
            color: #eaf0fb;
            padding: 10px;
            border-radius: 3px;
            font-size: 14px;
        """)
        social_layout.addWidget(self.registration_button)

        form_layout1.addLayout(social_layout)
        # Form Layout va form_layout1ni qo'shamiz
        form_layout.addLayout(form_layout1)
        main_layout.addLayout(form_layout)

        # Asosiy layoutni o'rnatamiz
        self.setLayout(main_layout)


    def handle_login(self):
        login = self.login_input.text()
        password = self.password_input.text()

        if not login:
            self.login_input.setPlaceholderText("To'ldirilmagan")
        if not password:
            self.password_input.setPlaceholderText("To'ldirilmagan")

        if login and password:
            user = {
                'login': login,
                'password': password
            }
            
            _id = self.core.get_id(user)
            if _id[5]=='admin':
                self.close()
                self.admin = AdminPage(_id, self.core)  
                self.admin.show()
            elif _id[5]=='user':
                self.close()
                self.user = UserPage(_id, self.core)
                self.user.show()

            else:
                print("Invalid login credentials")

    def registr(self):
        self.close()
        self.registration = RegistrationPage()

class RegistrationPage(QWidget):
    def __init__(self):
        super().__init__()
        self.core = Database()
        self.setWindowTitle("Registration")
        self.showMaximized()
        self.setStyleSheet("""
            font-size: 30px;
            background-color: #bdd2e2;
        """)

        self.initUI()
    
    def initUI(self):
        self.v_box = QVBoxLayout()

        self.login_input = QLabelEdit()
        self.login_input.setPlaceholderText("Login kiriting")
        self.password_input = Edit()
        self.password_input.setPlaceholderText("Parol kiriting")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.email_input = Edit()
        self.email_input.setPlaceholderText("Email kiriting")
        self.cardnumber_input = Edit()
        self.cardnumber_input.setPlaceholderText("Card number kiriting")
        self.cardpin_input = Edit()
        self.cardpin_input.setPlaceholderText("Card pin kiriting")
        self.cardpin_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.info_label = QLabel()

        self.save_btn = Button("Saqlash")
        self.save_btn.clicked.connect(self.create_user)

        self.back_button = QPushButton("Back")
        self.back_button.setStyleSheet("""
            background-color: #f44336;
            color: #ffffff;
            padding: 10px;
            font-size: 20px;
            border-radius: 5px;
            cursor: pointer;
        """)
        self.back_button.clicked.connect(self.back)


        self.v_box.addStretch(80)
        self.v_box.addWidget(self.name_input, 0, Qt.AlignmentFlag.AlignCenter)
        self.v_box.addWidget(self.login_input, 0, Qt.AlignmentFlag.AlignCenter)
        self.v_box.addWidget(self.password_input, 0, Qt.AlignmentFlag.AlignCenter)
        self.v_box.addWidget(self.email_input, 0, Qt.AlignmentFlag.AlignCenter)
        self.v_box.addWidget(self.cardnumber_input, 0, Qt.AlignmentFlag.AlignCenter)
        self.v_box.addWidget(self.cardpin_input, 0, Qt.AlignmentFlag.AlignCenter)
        self.v_box.addWidget(self.info_label, 0, Qt.AlignmentFlag.AlignCenter)
        self.v_box.addStretch(5)
        self.v_box.addWidget(self.save_btn, 0, Qt.AlignmentFlag.AlignCenter)
        self.v_box.addStretch(40)
        self.v_box.addWidget(self.back_button, 0,Qt.AlignmentFlag.AlignCenter )

        self.setLayout(self.v_box)
        self.show()
    def create_user(self):
        self.info_label.clear()
        name = self.name_input.text()
        login = self.login_input.text()
        password = self.password_input.text()
        email = self.email_input.text()
        cardnumber = self.cardnumber_input.text()
        cardpin = self.cardpin_input.text()
        if name and login and password and email and cardnumber and cardpin:
            user = {
                'name': name,
                'login': login,
                'password': password,
                'email': email,
                'cardnumber': cardnumber,
                'cardpin': cardpin
            } 
            err = self.core.insert_user(user)
            if err:
                self.info_label.setText("Bunday login mavjud")
            else: 
                self.info_label.setText("Muvaffaqiyatli ro'yxatdan o'tdingiz")
        else:
            self.info_label.setText("Barcha bandlarni to'ldiring")

    def back(self):
        self.close()
        self.login = LoginPage()

    



        
        

if __name__ == "__main__":
    app = QApplication([])
    window = AboutPage()
    window.show()
    app.exec()



