import requests


class test_Api():
    file=open("D:\\Python\\Sicredi\\RelatorioExecução.txt",mode="a+",encoding="utf-8")
    url = 'http://5b847b30db24a100142dce1b.mockapi.io/api/v1/simulador'    
    resp = requests.get(url)           
    
    file.write(resp.text[0:1])
    file.write("\n")
    
    file.write("    " +resp.text[1:8])
    file.write("\n")
    
    file.write("    "+resp.text[8:42])
    file.write("\n")
    
    file.write("    "+resp.text[42:83])
    file.write("\n")
    
    file.write(resp.text[83:])
    file.write("\n")

    file.close()
