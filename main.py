from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import data
from helpers import retrieve_phone_code, WebDriverUtils
from urban_routes_page import UrbanRoutesPage  # Importa la clase de la página


class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):
        options = Options()
        options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})

        cls.driver = webdriver.Chrome(options=options)
        cls.webdriver_times = WebDriverUtils(cls.driver)

    def test_start_navigator(self):
        self.driver.get(data.urban_routes_url)

    def test_set_route(self):
        self.test_start_navigator()
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_from(address_from)
        routes_page.set_to(address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_comfort_fee(self):
        self.test_set_route()
        routes_page = UrbanRoutesPage(self.driver)
        self.webdriver_times.wait_for_element_to_be_clickable(*routes_page.flash_mode).click()
        self.webdriver_times.wait_for_element_to_be_clickable(*routes_page.ask_for_a_taxi_button).click()
        self.webdriver_times.wait_for_element_to_be_clickable(*routes_page.comfort_fee_button).click()
        active_comfort_container = self.webdriver_times.wait_for_element_to_be_clickable(
            *routes_page.active_comfort_fee_button)
        comfort_title_text = active_comfort_container.text  # Obtén el texto directamente del WebElement
        assert comfort_title_text == "Comfort"  # Compara el texto

    def test_fill_phone_number(self):
        self.test_comfort_fee()
        routes_page = UrbanRoutesPage(self.driver)
        self.webdriver_times.wait_for_element_to_be_clickable(*routes_page.telephone_number_button).click()
        phone_number = data.phone_number
        routes_page.set_a_telephone_number(phone_number)
        self.webdriver_times.wait_for_element_to_be_clickable(*routes_page.next_button_telephone_menu).click()
        phone_code = retrieve_phone_code(self.driver)
        routes_page.set_a_telephone_code(phone_code)
        assert routes_page.get_telephone_code() == phone_code
        self.webdriver_times.wait_for_element_to_be_clickable(*routes_page.confirm_telephone_code_button).click()
        telephone_added = self.webdriver_times.wait_for_element_to_be_clickable(*routes_page.telephone_number_reserved)
        telephone_text = telephone_added.text
        assert telephone_text == data.phone_number

    def test_add_credit_card(self):
        self.test_fill_phone_number()
        routes_page = UrbanRoutesPage(self.driver)
        self.webdriver_times.wait_for_element_to_be_clickable(*routes_page.payment_method_button).click()
        self.webdriver_times.wait_for_element_to_be_clickable(*routes_page.add_payment_card).click()
        new_card_number = data.card_number
        routes_page.set_a_card_number(new_card_number)
        new_code_number = data.card_code
        routes_page.set_a_card_code_number(new_code_number)
        assert routes_page.get_card_code_number() == new_code_number
        self.webdriver_times.wait_for_element_to_be_clickable(*routes_page.any_part_payment_method_zone).click()
        self.webdriver_times.wait_for_element_to_be_clickable(*routes_page.payment_method_confirmation).click()
        self.webdriver_times.wait_for_element_to_be_clickable(*routes_page.close_payment_method_window).click()
        card_number_added = self.webdriver_times.wait_for_element_to_be_clickable(*routes_page.card_label_confirmation)
        card_menu_text = card_number_added.text
        assert card_menu_text == 'Tarjeta'

    def test_write_a_message_to_driver(self):
        self.test_add_credit_card()
        routes_page = UrbanRoutesPage(self.driver)
        self.webdriver_times.wait_for_element_to_be_clickable(*routes_page.message_for_driver).click()
        new_message = data.message_for_driver
        label_for_driver = self.webdriver_times.wait_for_element(*routes_page.label_for_driver)
        label_for_driver.send_keys(new_message)
        assert routes_page.get_message_for_driver() == new_message

    def test_ask_for_a_blanket(self):
        self.test_write_a_message_to_driver()
        routes_page = UrbanRoutesPage(self.driver)
        switch_element = routes_page.get_switch_element()
        initial_position = switch_element.location
        self.webdriver_times.wait_for_element_to_be_clickable(*routes_page.ask_for_a_blanket_and_a_handkerchief).click()
        self.webdriver_times.wait_for_element_to_be_visible(*routes_page.ask_for_a_blanket_and_a_handkerchief)
        updated_switch_element = routes_page.get_switch_element()
        new_position = updated_switch_element.location
        assert initial_position != new_position

    def test_ask_for_two_icecreams(self):
        self.test_ask_for_a_blanket()
        routes_page = UrbanRoutesPage(self.driver)

        # Hacemos clic en el botón para pedir dos helados.
        ask_for_icecreams_button = self.webdriver_times.wait_for_element_to_be_clickable(*routes_page.ask_for_2_icecreams)
        ask_for_icecreams_button.click()
        ask_for_icecreams_button.click()  # Hacemos clic dos veces para pedir dos helados

        # Obtenemos el contador de helados y verificamos que muestra '2'.
        quantity_displayed = self.webdriver_times.wait_for_element_to_be_clickable(*routes_page.ice_cream_counter)
        quantity_text = quantity_displayed.text
        assert quantity_text == '2'

    def test_taxi_modal_appearing(self):
        self.test_ask_for_two_icecreams()
        routes_page = UrbanRoutesPage(self.driver)
        self.webdriver_times.wait_for_element_to_be_clickable(*routes_page.reserve_order).click()
        assert self.webdriver_times.wait_for_element_to_be_visible(*routes_page.order_modal) is not None

    def test_driver_information_appearing(self):
        self.test_taxi_modal_appearing()
        routes_page = UrbanRoutesPage(self.driver)
        assert self.webdriver_times.wait_for_element_to_be_visible_2(*routes_page.order_modal_confirmation) is not None

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
