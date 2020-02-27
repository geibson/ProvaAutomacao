import Negativo as n
import Positivo as p
import ApiTest as t


n_list_p=[["paraEmpresa","paraVoce"],["100000","100000"],["30000","30000"],["6","2"],["Meses","Anos"]]

n_list_n=[["paraEmpresa","paraVoce"],["","100000","100000"],["30000","","30000"],["6","2",""],["Meses","Anos"]]


print("Teste_API")
t.test_Api()
print("-------------------------------------------------")
print("-------------------------------------------------")
##Testes Positivos

print("Testes Positivos")
print("Teste_Positivo_Perfil_Empresa_Meses")
##Perfil - paraEmpresa, Valor Investido - 100000, Valor Aplicado - 30000, Tempo - 6, Periodo - Meses
p.Teste_Positivo(n_list_p[0][0] ,n_list_p[1][0],n_list_p[2][0],n_list_p [3][0],n_list_p[4][0])
print("-------------------------------------------------")
print("-------------------------------------------------")
print("Teste_Positivo_Perfil_Empresa_Anos")
##Perfil - paraEmpresa, Valor Investido - 100000, Valor Aplicado - 30000, Tempo - 2, Periodo - Anos
p.Teste_Positivo(n_list_p[0][0] ,n_list_p[1][0],n_list_p[2][0],n_list_p [3][1],n_list_p[4][1])
print("-------------------------------------------------")
print("-------------------------------------------------")

print("Teste_Positivo_Perfil_Você_Meses")
##Perfil - paraVoce, Valor Investido - 100000, Valor Aplicado - 30000, Tempo - 6, Periodo - Meses
p.Teste_Positivo(n_list_p[0][1] ,n_list_p[1][1],n_list_p[2][1],n_list_p [3][0],n_list_p[4][0])
print("-------------------------------------------------")
print("-------------------------------------------------")

print("Teste_Positivo_Perfil_Você_Anos")
##Perfil - paraVoce, Valor Investido - 100000, Valor Aplicado - 30000, Tempo - 2, Periodo - Anos
p.Teste_Positivo(n_list_p[0][1] ,n_list_p[1][1],n_list_p[2][1],n_list_p [3][1],n_list_p[4][1])

print("-------------------------------------------------")
print("-------------------------------------------------")


print("Testes Negativos")
##Testes Negativos
    

print("Teste_Negativo_Mes_Perfil_Empresa-1")
##Perfil - paraEmpresa, Valor Investido - VAZIO, Valor Aplicado - 30000, Tempo - 6, Periodo - Meses
n.Teste_Negativo(n_list_n[0][0] ,n_list_n[1][0],n_list_n[2][0],n_list_n [3][0],n_list_n[4][0])
print("-------------------------------------------------")
print("-------------------------------------------------")

print("Teste_Negativo_Mes_Perfil_Empresa-2")
##Perfil - paraEmpresa, Valor Investido - 100000, Valor Aplicado - VAZIO, Tempo - VAZIO, Periodo - Meses
n.Teste_Negativo(n_list_n[0][0] ,n_list_n[1][1],n_list_n[2][1],n_list_n [3][2],n_list_n[4][0])
print("-------------------------------------------------")
print("-------------------------------------------------")

print("Teste_Negativo_Mes_Perfil_Empresa-3")
##Perfil - paraEmpresa, Valor Investido - 100000, Valor Aplicado - 30000, Tempo - 2, Periodo - Meses
n.Teste_Negativo(n_list_n[0][0] ,n_list_n[1][2],n_list_n[2][2],n_list_n [3][1],n_list_n[4][0])
print("-------------------------------------------------")
print("-------------------------------------------------")

print("Teste_Negativo_Mes_Perfil_Empresa-4")
##Perfil - paraEmpresa, Valor Investido - VAZIO, Valor Aplicado - VAZIO, Tempo - 6, Periodo - Meses
n.Teste_Negativo(n_list_n[0][0] ,n_list_n[1][0],n_list_n[2][1],n_list_n [3][0],n_list_n[4][0])
print("-------------------------------------------------")
print("-------------------------------------------------")

print("Teste_Negativo_Mes_Perfil_Empresa-5")
##Perfil - paraEmpresa, Valor Investido - VAZIO, Valor Aplicado - 30000, Tempo - 2, Periodo - Meses
n.Teste_Negativo(n_list_n[0][0] ,n_list_n[1][0],n_list_n[2][0],n_list_n [3][1],n_list_n[4][0])
print("-------------------------------------------------")
print("-------------------------------------------------")

print("Teste_Negativo_Mes_Perfil_Empresa-6")
##Perfil - paraEmpresa, Valor Investido - 100000, Valor Aplicado - VAZIO, Tempo - 2, Periodo - Meses
n.Teste_Negativo(n_list_n[0][0] ,n_list_n[1][1],n_list_n[2][1],n_list_n [3][1],n_list_n[4][0])
print("-------------------------------------------------")
print("-------------------------------------------------")

print("Teste_Negativo_Ano_Perfil_Empresa-7")
##Perfil - paraEmpresa, Valor Investido - VAZIO, Valor Aplicado - 30000, Tempo - 6, Periodo - Anos
n.Teste_Negativo(n_list_n[0][0] ,n_list_n[1][0],n_list_n[2][0],n_list_n [3][0],n_list_n[4][1])
print("-------------------------------------------------")
print("-------------------------------------------------")

print("Teste_Negativo_Ano_Perfil_Empresa-8")
##Perfil - paraEmpresa, Valor Investido - 100000, Valor Aplicado - VAZIO, Tempo - VAZIO, Periodo - Anos
n.Teste_Negativo(n_list_n[0][0] ,n_list_n[1][1],n_list_n[2][1],n_list_n [3][2],n_list_n[4][1])
print("-------------------------------------------------")
print("-------------------------------------------------")

print("Teste_Negativo_Ano_Perfil_Empresa-9")
##Perfil - paraEmpresa, Valor Investido - 100000, Valor Aplicado - 30000, Tempo - 2, Periodo - Anos
n.Teste_Negativo(n_list_n[0][0] ,n_list_n[1][2],n_list_n[2][2],n_list_n [3][1],n_list_n[4][1])
print("-------------------------------------------------")
print("-------------------------------------------------")

print("Teste_Negativo_Ano_Perfil_Empresa-10")
##Perfil - paraEmpresa, Valor Investido - VAZIO, Valor Aplicado - VAZIO, Tempo - 6, Periodo - Anos
n.Teste_Negativo(n_list_n[0][0] ,n_list_n[1][0],n_list_n[2][1],n_list_n [3][0],n_list_n[4][1])
print("-------------------------------------------------")
print("-------------------------------------------------")

print("Teste_Negativo_Ano_Perfil_Empresa-11")
##Perfil - paraEmpresa, Valor Investido - VAZIO, Valor Aplicado - 30000, Tempo - 2, Periodo - Anos
n.Teste_Negativo(n_list_n[0][0] ,n_list_n[1][0],n_list_n[2][0],n_list_n [3][1],n_list_n[4][1])
print("-------------------------------------------------")
print("-------------------------------------------------")

print("Teste_Negativo_Ano_Perfil_Empresa-12")
##Perfil - paraEmpresa, Valor Investido - 100000, Valor Aplicado - VAZIO, Tempo - 2, Periodo - Anos
n.Teste_Negativo(n_list_n[0][0] ,n_list_n[1][1],n_list_n[2][1],n_list_n [3][1],n_list_n[4][1])
print("-------------------------------------------------")
print("-------------------------------------------------")





print("Teste_Negativo_Mes_Perfil_Você-13")
##Perfil - paraVoce, Valor Investido - VAZIO, Valor Aplicado - 30000, Tempo - 6, Periodo - Meses
n.Teste_Negativo(n_list_n[0][1] ,n_list_n[1][0],n_list_n[2][0],n_list_n [3][0],n_list_n[4][0])
print("-------------------------------------------------")
print("-------------------------------------------------")

print("Teste_Negativo_Mes_Perfil_Você-13")
##Perfil - paraVoce, Valor Investido - 100000, Valor Aplicado - VAZIO, Tempo - VAZIO, Periodo - Mese
n.Teste_Negativo(n_list_n[0][1] ,n_list_n[1][1],n_list_n[2][1],n_list_n [3][2],n_list_n[4][0])
print("-------------------------------------------------")
print("-------------------------------------------------")

print("Teste_Negativo_Mes_Perfil_Você-14")
##Perfil - paraVoce, Valor Investido - 100000, Valor Aplicado - 30000, Tempo - 2, Periodo - Meses
n.Teste_Negativo(n_list_n[0][1] ,n_list_n[1][2],n_list_n[2][2],n_list_n [3][1],n_list_n[4][0])
print("-------------------------------------------------")
print("-------------------------------------------------")

print("Teste_Negativo_Mes_Perfil_Você-15")
##Perfil - paraVoce, Valor Investido - VAZIO, Valor Aplicado - VAZIO, Tempo - 6, Periodo - Meses
n.Teste_Negativo(n_list_n[0][1] ,n_list_n[1][0],n_list_n[2][1],n_list_n [3][0],n_list_n[4][0])
print("-------------------------------------------------")
print("-------------------------------------------------")

print("Teste_Negativo_Mes_Perfil_Você-16")
##Perfil - paraVoce, Valor Investido - VAZIO, Valor Aplicado - 30000, Tempo - 2, Periodo - Meses
n.Teste_Negativo(n_list_n[0][1] ,n_list_n[1][0],n_list_n[2][0],n_list_n [3][1],n_list_n[4][0])
print("-------------------------------------------------")
print("-------------------------------------------------")

print("Teste_Negativo_Mes_Perfil_Você-17")
##Perfil - paraVoce, Valor Investido - 100000, Valor Aplicado - VAZIO, Tempo - 2, Periodo - Meses
n.Teste_Negativo(n_list_n[0][1] ,n_list_n[1][1],n_list_n[2][1],n_list_n [3][1],n_list_n[4][0])
print("-------------------------------------------------")
print("-------------------------------------------------")

print("Teste_Negativo_Ano_Perfil_Você-18")
##Perfil - paraVoce, Valor Investido - VAZIO, Valor Aplicado - 30000, Tempo - 6, Periodo - Anos
n.Teste_Negativo(n_list_n[0][1] ,n_list_n[1][0],n_list_n[2][0],n_list_n [3][0],n_list_n[4][1])
print("-------------------------------------------------")
print("-------------------------------------------------")

print("Teste_Negativo_Ano_Perfil_Você-19")
##Perfil - paraVoce, Valor Investido - 100000, Valor Aplicado - VAZIO, Tempo - VAZIO, Periodo - Anos
n.Teste_Negativo(n_list_n[0][1] ,n_list_n[1][1],n_list_n[2][1],n_list_n [3][2],n_list_n[4][1])
print("-------------------------------------------------")
print("-------------------------------------------------")

print("Teste_Negativo_Ano_Perfil_Você-20")
##Perfil - paraVoce, Valor Investido - 100000, Valor Aplicado - 30000, Tempo - 2, Periodo - Anos
n.Teste_Negativo(n_list_n[0][1] ,n_list_n[1][2],n_list_n[2][2],n_list_n [3][1],n_list_n[4][1])
print("-------------------------------------------------")
print("-------------------------------------------------")

print("Teste_Negativo_Ano_Perfil_Você-21")
##Perfil - paraVoce, Valor Investido - VAZIO, Valor Aplicado - VAZIO, Tempo - 6, Periodo - Anos
n.Teste_Negativo(n_list_n[0][1] ,n_list_n[1][0],n_list_n[2][1],n_list_n [3][0],n_list_n[4][1])
print("-------------------------------------------------")
print("-------------------------------------------------")

print("Teste_Negativo_Ano_Perfil_Você-22")
##Perfil - paraVoce, Valor Investido - VAZIO, Valor Aplicado - 30000, Tempo - 2, Periodo - Anos
n.Teste_Negativo(n_list_n[0][1] ,n_list_n[1][0],n_list_n[2][0],n_list_n [3][1],n_list_n[4][1])
print("-------------------------------------------------")
print("-------------------------------------------------")

print("Teste_Negativo_Ano_Perfil_Você-23")
##Perfil - paraVoce, Valor Investido - 100000, Valor Aplicado - VAZIO, Tempo - 2, Periodo - Anos
n.Teste_Negativo(n_list_n[0][1] ,n_list_n[1][1],n_list_n[2][1],n_list_n [3][1],n_list_n[4][1])
