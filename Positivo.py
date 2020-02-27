from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def Teste_Positivo(v_Perfil,v_Aplicar,v_Investir,v_Tempo,v_medida):
   
        driver = webdriver.Firefox()
        #Acessa o site
        driver.get("https://www.sicredi.com.br/html/ferramenta/simulador-investimento-poupanca/")


        print("Valor aplicado: "+v_Aplicar+ " Valor Investido: "+v_Investir+ " por "+v_Tempo +" "+v_medida )
        #Seleciona o perfil
        print(v_Perfil)
        driver.find_element_by_css_selector("input[type='radio'][value='"+v_Perfil+"']").click()

        #Encontra o campo Qual o valor que você quer aplicar?*
        elem = driver.find_element_by_name("valorAplicar")
        elem.send_keys(v_Aplicar)

        #Encontra o campo Quanto você quer poupar todo mês?         
        elem = driver.find_element_by_name("valorInvestir")
        elem.send_keys(v_Investir)

        #Encontra o campo Por quanto tempo você quer poupar?*
        elem = driver.find_element_by_name("tempo")
        elem.send_keys(v_Tempo)

        #Abre o dropdown de Meses e Anos
        driver.find_element_by_css_selector('.btn > .seta').click()
        #Seleciona se Meses ou Anos
        driver.find_element_by_link_text(v_medida).click()

        #Print a tela
        #driver.save_screenshot("Pré-Simulado.png")
        driver.find_element_by_css_selector('.btnSimular').click()
        wait = WebDriverWait(driver, 10)
        #Verifica valor guardado


        if driver.find_element_by_class_name("valor"):
                print("Em "+v_Tempo+" "+v_medida+" você terá guardado")
                wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.btnRefazer')))
                print(driver.find_element_by_class_name("valor").text)
                ##               driver.implicitly_wait(10) # seconds
                driver.find_element_by_css_selector('.btnRefazer').click()
        else:
                print("Falhou")
        print("Fim do Teste")
        driver.quit()

