from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def Teste_Negativo(v_Perfil,v_Aplicar,v_Investir,v_Tempo,v_medida):
        file=open("D:\\Python\\Sicredi\\RelatorioExecução.txt",mode="a+",encoding="utf-8")
        file.write("\n")
        file.write("Inicio Teste Negativo")
        file.write("\n")
        driver = webdriver.Firefox()
        #Acessa o site
        driver.get("https://www.sicredi.com.br/html/ferramenta/simulador-investimento-poupanca/")

        file.write("Valor aplicado: "+v_Aplicar+ " Valor Investido: "+v_Investir+ " por "+v_Tempo +"  "+v_medida )
        file.write("\n")
        #Seleciona o perfil
        driver.find_element_by_css_selector("input[type='radio'][value='"+v_Perfil+"']").click()
        #Encontra o campo Qual o valor que você quer aplicar?*
        elem = driver.find_element_by_name("valorAplicar")
        elem.clear()
        elem.send_keys(v_Aplicar)

        #Encontra o campo Quanto você quer poupar todo mês?         
        elem = driver.find_element_by_name("valorInvestir")
        elem.clear()
        elem.send_keys(v_Investir)

        #Encontra o campo Por quanto tempo você quer poupar?*
        elem = driver.find_element_by_name("tempo")
        elem.clear()
        elem.send_keys(v_Tempo)

        #Abre o dropdown de Meses e Anos
        driver.find_element_by_css_selector('.btn > .seta').click()

        #Seleciona se Meses ou Anos
        driver.find_element_by_link_text(v_medida).click()
        #Clica  no botão Simular
        driver.find_element_by_css_selector('.btnSimular').click()
        wait = WebDriverWait(driver, 10)

        #Verifica as mensagens de erro
        if v_Aplicar == "":
                erro = driver.find_element_by_id('valorAplicar-error')
                file.write("Qual o valor que você quer aplicar? = Vazio")
                file.write("\n")
                file.write("Mensagem de erro: "+str(erro.text))
                file.write("\n")
        elif v_Investir == "":
                erro = driver.find_element_by_id('valorInvestir-error')
                file.write("Quanto você quer poupar todo mês? = Vazio")
                file.write("\n")
                file.write("Mensagem de erro: "+str(erro.text))
                file.write("\n")
        elif v_Tempo == "":
                error = driver.find_element_by_id('tempo-error')
                file.write("Campo Obrigatorio")
                file.write("\n")
                file.write("Por quanto tempo você quer poupar? Vazio ")
                file.write("\n")
                #print("Mensagem de erro: "+str(erro.text))
        else:
                if driver.find_element_by_css_selector('.valor'):
                    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.btnRefazer')))
                    driver.implicitly_wait(10) # seconds
                    driver.find_element_by_css_selector('.btnRefazer').click()
                else:
                    file.write("\n")
                    file.write("Falhou")
        file.write("\n")
        file.write("Fim do Teste")
        file.write("\n")
        file.close()
        #Encerra o teste
        driver.quit()
            

