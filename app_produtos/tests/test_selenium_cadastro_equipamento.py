from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()  
    driver.maximize_window()
    yield driver
    driver.quit()

def test_cadastrar_equipamento(driver):
    
    driver.get("http://127.0.0.1:8000/cadastrarEquipamento/")

    
    campo_cod = driver.find_element(By.NAME, "cod_equipamento")
    campo_cod.send_keys("2005")

    campo_nome = driver.find_element(By.NAME, "nome_equipamento")
    campo_nome.send_keys("Protetor auricular")

    
    botao_salvar = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    botao_salvar.click()

    
    WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "notificationModal"))
)


    modal_title = driver.find_element(By.ID, "notificationLabel").text
    modal_message = driver.find_element(By.ID, "notificationMessage").text

    assert modal_title == "Sucesso!"  
    assert modal_message == "Equipamento cadastrado com sucesso!"


    
    print(modal_title)
    print(modal_message)
