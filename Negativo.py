from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def Teste_Negativo_Mes_Emp():
   
        driver = webdriver.Firefox()
        #Acessa o site
        driver.get("https://www.sicredi.com.br/html/ferramenta/simulador-investimento-poupanca/")

        n_list=[["","100000","100000"],["30000","","30000"],["6","2",""],["Meses","Meses","Meses"]]
        for x in range(3):
            v_Aplicar = n_list[0][x]
            v_Investir = n_list[1][x]
            v_Tempo = n_list[2][x]
            v_medida = n_list [3][x]
            print("Valor aplicado: "+v_Aplicar+ " Valor Investido: "+v_Investir+ " por "+v_Tempo +" "+v_medida )
            #Seleciona o perfil
            driver.find_element_by_css_selector("input[type='radio'][value='paraEmpresa']").click()
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
                print("Qual o valor que você quer aplicar? = Vazio")
                print("Mensagem de erro: "+str(erro.text))
            elif v_Investir == "":
                erro = driver.find_element_by_id('valorInvestir-error')
                print("Quanto você quer poupar todo mês? = Vazio")
                print("Mensagem de erro: "+str(erro.text))
            elif v_Tempo == "":
                error = driver.find_element_by_id('tempo-error')
                print("Por quanto tempo você quer poupar? Vazio ")
                print("Mensagem de erro: "+str(erro.text))
            else:
                if driver.find_element_by_css_selector('.valor'):
                    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.btnRefazer')))
                    driver.implicitly_wait(10) # seconds
                    driver.find_element_by_css_selector('.btnRefazer').click()
                else:
                    print("Falhou")
            print("Fim do IF")

        #Encerra o teste
        driver.quit()
            


def Teste_Negativo_Anos_Emp():
   
        driver = webdriver.Firefox()
        #Acessa o site
        driver.get("https://www.sicredi.com.br/html/ferramenta/simulador-investimento-poupanca/")
        #Valida se é site esta correto
        #driver.assertIn("Simulador", driver.title)
        

        n_list=[["","100000","100000"],["30000","","30000"],["6","2",""],["Anos","Anos","Anos"]]
        for x in range(3):
            i=0
            v_Aplicar = n_list[0][x]
            v_Investir = n_list[1][x]
            v_Tempo = n_list[2][x]
            v_medida = n_list [3][x]
            print("Valor aplicado: "+v_Aplicar+ " Valor Investido: "+v_Investir+ " por "+v_Tempo +" "+v_medida )
            #Seleciona o perfil
            driver.find_element_by_css_selector("input[type='radio'][value='paraEmpresa']").click()
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
                print("Qual o valor que você quer aplicar? = Vazio")
                print("Mensagem de erro: "+str(erro.text))
            elif v_Investir == "":
                erro = driver.find_element_by_id('valorInvestir-error')
                print("Quanto você quer poupar todo mês? = Vazio")
                print("Mensagem de erro: "+str(erro.text))
            elif v_Tempo == "":
                error = driver.find_element_by_id('tempo-error')
                print("Por quanto tempo você quer poupar? Vazio ")
                print("Mensagem de erro: "+str(erro.text))
            else:
                if driver.find_element_by_css_selector('.valor'):
                    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.btnRefazer')))
                    driver.implicitly_wait(10) # seconds
                    driver.find_element_by_css_selector('.btnRefazer').click()
                else:
                    print("Falhou")
            print("Fim do IF")

        #Encerra o teste
        driver.quit()


def Teste_Negativo_Mes_VC():
   
        driver = webdriver.Firefox()
        #Acessa o site
        driver.get("https://www.sicredi.com.br/html/ferramenta/simulador-investimento-poupanca/")
        #Valida se é site esta correto
        #driver.assertIn("Simulador", driver.title)
        

        n_list=[["","100000","100000"],["30000","","30000"],["6","2",""],["Meses","Meses","Meses"]]
        for x in range(3):
            v_Aplicar = n_list[0][x]
            v_Investir = n_list[1][x]
            v_Tempo = n_list[2][x]
            v_medida = n_list [3][x]
            print("Valor aplicado: "+v_Aplicar+ " Valor Investido: "+v_Investir+ " por "+v_Tempo +" "+v_medida )
            #Seleciona o perfil
            driver.find_element_by_css_selector("input[type='radio'][value='paraVoce']").click()
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
                print("Qual o valor que você quer aplicar? = Vazio")
                print("Mensagem de erro: "+str(erro.text))
            elif v_Investir == "":
                erro = driver.find_element_by_id('valorInvestir-error')
                print("Quanto você quer poupar todo mês? = Vazio")
                print("Mensagem de erro: "+str(erro.text))
            elif v_Tempo == "":
                error = driver.find_element_by_id('tempo-error')
                print("Por quanto tempo você quer poupar? Vazio ")
                print("Mensagem de erro: "+str(erro.text))
            else:
                if driver.find_element_by_css_selector('.valor'):
                    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.btnRefazer')))
                    driver.implicitly_wait(10) # seconds
                    driver.find_element_by_css_selector('.btnRefazer').click()
                else:
                    print("Falhou")
            print("Fim do IF")

        #Encerra o teste
        driver.quit()
            


def Teste_Negativo_Anos_VC():
   
        driver = webdriver.Firefox()
        #Acessa o site
        driver.get("https://www.sicredi.com.br/html/ferramenta/simulador-investimento-poupanca/")
        #Valida se é site esta correto
        #driver.assertIn("Simulador", driver.title)
        

        n_list=[["","100000","100000"],["30000","","30000"],["6","2",""],["Anos","Anos","Anos"]]
        for x in range(3):
            i=0
            v_Aplicar = n_list[0][x]
            v_Investir = n_list[1][x]
            v_Tempo = n_list[2][x]
            v_medida = n_list [3][x]
            print("Valor aplicado: "+v_Aplicar+ " Valor Investido: "+v_Investir+ " por "+v_Tempo +" "+v_medida )
            #Seleciona o perfil
            driver.find_element_by_css_selector("input[type='radio'][value='paraVoce']").click()

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
                print("Qual o valor que você quer aplicar? = Vazio")
                print("Mensagem de erro: "+str(erro.text))
            elif v_Investir == "":
                erro = driver.find_element_by_id('valorInvestir-error')
                print("Quanto você quer poupar todo mês? = Vazio")
                print("Mensagem de erro: "+str(erro.text))
            elif v_Tempo == "":
                error = driver.find_element_by_id('tempo-error')
                print("Por quanto tempo você quer poupar? Vazio ")
                print("Mensagem de erro: "+str(erro.text))
            else:
                if driver.find_element_by_css_selector('.valor'):
                    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.btnRefazer')))
                    driver.implicitly_wait(10) # seconds
                    driver.find_element_by_css_selector('.btnRefazer').click()
                else:
                    print("Falhou")
            print("Fim do IF")

        #Encerra o teste
        driver.quit()
   

