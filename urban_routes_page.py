from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

class UrbanRoutesPage:
    # Indicadores configuración dirección
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    # Indicadores selección tarifa confort
    flash_mode = (By.XPATH, "//div[text()='Flash']")
    ask_for_a_taxi_button = (By.XPATH, "//button[text()='Pedir un taxi']")
    comfort_fee_button = (By.XPATH, "//div[@class='tcard-title' and text()='Comfort']")
    active_comfort_fee_button = (By.XPATH, "//div[text()='Comfort']")
    comfort_Fee_button_confirmation = (By.XPATH, "//div[@class='r-sw-label' and text()='Manta y pañuelos']")
    # Indicadores para agregar número de teléfono
    telephone_number_button = (By.CLASS_NAME, 'np-button')
    telephone_number_space = (By.ID, 'phone')
    telephone_number_reserved = (By.XPATH, "//div[@class='np-text' and text()='+1 123 123 12 12']")
    next_button_telephone_menu = (By.CSS_SELECTOR, "button.button.full")
    telephone_code_received = (By.ID, 'code')
    confirm_telephone_code_button = (By.XPATH, "//button[text()='Confirmar']")
    # Indicadores para agregar tarjeta de crédito
    payment_method_button = (By.XPATH, "//div[@class='pp-text' and text()='Método de pago']")
    add_payment_card = (By.CLASS_NAME, 'pp-plus-container')
    card_code_number = (By.XPATH, "//input[@placeholder='12']")
    card_number = (By.XPATH, "//input[@id='number' and @name='number']")
    payment_method_confirmation = (By.XPATH, "//button[text()='Agregar']")
    any_part_payment_method_zone = (By.CLASS_NAME, 'plc')
    close_payment_method_window = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/button')
    card_label_confirmation = (By.XPATH, "//div[@class='pp-value-text' and text()='Tarjeta']")
    # Indicadores para dejar mensaje al conductor
    message_for_driver = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[3]/div')
    label_for_driver = (By.XPATH, '/html/body/div/div/div[3]/div[3]/div[2]/div[2]/div[3]/div/input')
    # Indicadores para abrir requerimientos
    order_requirements = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[1]/div[1]')
    requirements_menu = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]')
    # Indicadores para solicitar una manta y pañuelos
    ask_for_a_blanket_and_a_handkerchief = (By.XPATH, "//span[@class='slider round']")
    # Indicadores para pedir dos helados
    ask_for_2_icecreams = (By.XPATH, "//div[@class='r-counter-label' and text()='Helado']//following::div[@class='counter-plus']")
    ice_cream_counter = (By.XPATH, "(//div[@class='counter-value'])[1]")
    # Indicador para reservar
    reserve_order = (By.CLASS_NAME, 'smart-button-secondary')
    # Indicador para comprobar el modal de la orden
    order_modal = (By.CLASS_NAME, 'order-body')
    order_modal_confirmation = (By.CLASS_NAME, 'order-btn-rating')
    order_modal_confirmation_second = (By.CLASS_NAME, 'order-numer')

    def __init__(self, driver):
        self.wait_1 = WebDriverWait(driver, 5)
        self.wait_2 = WebDriverWait(driver, 45)
        self.driver = driver

    # Primer prueba
    def set_from(self, from_address):
        from_field = self.wait_1.until(ec.presence_of_element_located(self.from_field))
        from_field.send_keys(from_address)

    def set_to(self, to_address):
        to_field = self.wait_1.until(ec.presence_of_element_located(self.to_field))
        to_field.send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_attribute('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_attribute('value')

    # Segunda prueba
    def click_flash_mode(self):
        self.driver.find_element(*self.flash_mode).click()

    def click_ask_for_a_taxi_button(self):
        self.driver.find_element(*self.ask_for_a_taxi_button).click()

    def click_comfort_fee(self):
        self.driver.find_element(*self.comfort_fee_button).click()

    def comfort_fee_active(self):
        return self.driver.find_element(*self.active_comfort_fee_button).get_attribute('value')

    # Tercera prueba
    def click_telephone_number_button(self):
        self.driver.find_element(*self.telephone_number_button).click()

    def set_a_telephone_number(self, phone_number):
        self.driver.find_element(*self.telephone_number_space).send_keys(phone_number)

    def telephone_number_active(self):
        return self.driver.find_element(*self.telephone_number_reserved).get_attribute('value')

    def get_telephone_number(self):
        return self.driver.find_element(*self.telephone_number_space).get_attribute('value')

    def click_button_next_in_phone_menu(self):
        self.driver.find_element(*self.next_button_telephone_menu).click()

    def set_a_telephone_code(self, phone_code):
        self.driver.find_element(*self.telephone_code_received).send_keys(phone_code)

    def get_telephone_code(self):
        return self.driver.find_element(*self.telephone_code_received).get_attribute('value')

    def click_confirm_telephone_code_number(self):
        self.driver.find_element(*self.confirm_telephone_code_button).click()

    # Cuarta prueba
    def click_payment_method(self):
        self.driver.find_element(*self.payment_method_button).click()

    def click_add_credit_card(self):
        self.driver.find_element(*self.add_payment_card).click()

    def set_a_card_number(self, new_card_number):
        card_number = self.wait_1.until(ec.presence_of_element_located(self.card_number))
        card_number.send_keys(new_card_number)

    def get_card_number(self):
        return self.driver.find_element(*self.card_number).get_attribute('value')

    def set_a_card_code_number(self, new_code_number):
        self.driver.find_element(*self.card_code_number).send_keys(new_code_number)

    def get_card_code_number(self):
        return self.driver.find_element(*self.card_code_number).get_attribute('value')

    def click_any_part_credit_card_window(self):
        self.driver.find_element(*self.any_part_payment_method_zone).click()

    def click_add_into_payment_window(self):
        self.driver.find_element(*self.payment_method_confirmation).click()

    def click_close_into_payment_window(self):
        self.driver.find_element(*self.close_payment_method_window).click()

    def get_card_at_menu(self):
        return self.driver.find_element(*self.card_label_confirmation).get_attribute('value')

    # Quinta prueba
    def click_in_message_for_driver_option(self):
        self.driver.find_element(*self.message_for_driver).click()

    def set_a_message_for_driver(self, new_message):
        label_for_driver = self.wait_1.until(ec.presence_of_element_located(self.label_for_driver))
        label_for_driver.send_keys(new_message)

    def get_message_for_driver(self):
        return self.driver.find_element(*self.label_for_driver).get_attribute('value')

    # Sexta prueba
    def get_switch_element(self):
        return self.driver.find_element(*self.ask_for_a_blanket_and_a_handkerchief)
    def click_order_requirements_button(self):
        self.driver.find_element(*self.requirements_menu).click()

    def click_blanket_and_a_handkerchief_button(self):
        self.driver.find_element(*self.ask_for_a_blanket_and_a_handkerchief).click()

    # Séptima prueba
    def click_icecream_button(self):
        self.driver.find_element(*self.ask_for_2_icecreams).click()

    def click_twice_icecream_button(self):
        self.driver.find_element(*self.ask_for_2_icecreams).click()

    # Octava prueba
    def click_in_reserve_button(self):
        self.driver.find_element(*self.reserve_order).click()

    def check_the_reserve_is_done(self):
        reserve_check = self.wait_1.until(ec.visibility_of_element_located(self.order_modal))
        return reserve_check

    # Novena prueba
    def check_the_driver_information_appears(self):
        driver_information = self.wait_2.until(ec.visibility_of_element_located(self.order_modal_confirmation))
        return driver_information