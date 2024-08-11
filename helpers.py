import json
import time
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

class WebDriverUtils:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, by, value, timeout=10):
        """Espera hasta que un elemento esté presente en el DOM."""
        return WebDriverWait(self.driver, timeout).until(ec.presence_of_element_located((by, value)))

    def wait_for_element_to_be_clickable(self, by, value, timeout=10):
        """Espera hasta que un elemento sea clickable."""
        return WebDriverWait(self.driver, timeout).until(ec.element_to_be_clickable((by, value)))

    def wait_for_element_to_be_clickable_2(self, by, value, timeout=10):
        """Espera hasta que un elemento sea clickable (duplicado de la anterior)."""
        return WebDriverWait(self.driver, timeout).until(ec.element_to_be_clickable((by, value)))

    def wait_for_element_to_be_visible(self, by, value, timeout=40):
        """Espera hasta que un elemento sea visible en el DOM."""
        return WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located((by, value)))

    def wait_for_element_to_be_visible_2(self, by, value, timeout=40):
        """Espera hasta que un elemento sea visible en el DOM (duplicado de la anterior)."""
        return WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located((by, value)))


def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber" 
                            "solicitado el código en tu aplicación.")
        return code

    # Las siguientes son funciones que permiten realizar esperas en las pruebas
