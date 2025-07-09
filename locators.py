from selenium.webdriver.common.by import By
name_field = (By.NAME, "name") # поле Имя
email_field = (By.NAME, "email") # поле Email
password_field = (By.NAME, "password") # поле Пароль
registration_button = (By.XPATH, "//button[text()='Зарегистрироваться']") #кнопка зарегистрироваться
login_button_after_reg = (By.TAG_NAME, "h2") #кнопка Войти, доступная после регистрации
password_error_text = (By.CLASS_NAME, "input__error text_type_main-default") # Надпись Некорректный пароль
login_button = (By.XPATH, "//button[text()='Войти']") #кнопка Войти
login_link = (By.CLASS_NAME, "Auth_link__1fOlj") #ссылка на форму входа
constructor_button = (By.XPATH, "//button[text()='Конструктор']") #кнопка Конструктор
logout_button = (By.XPATH, "//button[text()='Выход']") #кнопка Выход
account_button = (By.CLASS_NAME, "Account_link__2ETsJ text text_type_main-medium text_color_inactive Account_link_active__2opc9" ) # кнопка Профиль
log_in_account_button = (By.XPATH, "//button[text()='Войти в аккаунт']")   # кнопка Войти в аккаунт
profile_button = (By.XPATH, "//button[text()='Личный кабинет']")  #кнопка Личный кабинет
logo = (By.CSS_SELECTOR, "[xmlns='http://www.w3.org/2000/svg']") # логотип сайта
bread_button = (By.XPATH, "//span[text()='Булки']")  # Кнопка "Булки"
souses_button = (By.XPATH, "//span[text()='Соусы']")  # Кнопка "Соусы"
toppings_button = (By.XPATH, "//span[text()='Начинки']")  # Кнопка "Начинки"