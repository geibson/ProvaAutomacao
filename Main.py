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

print("Teste_Positivo_Perfil_Empresa_Meses")
p.Teste_Positivo(n_list_p[0][0] ,n_list_p[1][0],n_list_p[2][0],n_list_p [3][0],n_list_p[4][0])
print("-------------------------------------------------")
print("-------------------------------------------------")
print("Teste_Positivo_Perfil_Empresa_Anos")
p.Teste_Positivo(n_list_p[0][0] ,n_list_p[1][0],n_list_p[2][0],n_list_p [3][0],n_list_p[4][1])
print("-------------------------------------------------")
print("-------------------------------------------------")

print("Teste_Positivo_Perfil_Você_Meses")
p.Teste_Positivo(n_list_p[0][1] ,n_list_p[1][1],n_list_p[2][1],n_list_p [3][1],n_list_p[4][0])
print("-------------------------------------------------")
print("-------------------------------------------------")

print("Teste_Positivo_Perfil_Você_Anos")
p.Teste_Positivo(n_list_p[0][1] ,n_list_p[1][1],n_list_p[2][1],n_list_p [3][1],n_list_p[4][1])




##Testes Negativos


print("Teste_Negativo_Mes_Perfil_Empresa")
n.Teste_Negativo(n_list_n[0][0] ,n_list_n[1][0],n_list_n[2][0],n_list_n [3][0],n_list_n[4][0])
print("-------------------------------------------------")
print("-------------------------------------------------")

print("Teste_Negativo_Mes_Perfil_Empresa")
n.Teste_Negativo(n_list_n[0][0] ,n_list_n[1][1],n_list_n[2][1],n_list_n [3][2],n_list_n[4][0])
print("-------------------------------------------------")
print("-------------------------------------------------")

print("Teste_Negativo_Mes_Perfil_Empresa")
n.Teste_Negativo(n_list_n[0][0] ,n_list_n[1][2],n_list_n[2][2],n_list_n [3][1],n_list_n[4][0])
print("-------------------------------------------------")
print("-------------------------------------------------")

print("Teste_Negativo_Mes_Perfil_Empresa")
n.Teste_Negativo(n_list_n[0][0] ,n_list_n[1][0],n_list_n[2][1],n_list_n [3][0],n_list_n[4][0])
print("-------------------------------------------------")
print("-------------------------------------------------")

print("Teste_Negativo_Mes_Perfil_Empresa")
n.Teste_Negativo(n_list_n[0][0] ,n_list_n[1][0],n_list_n[2][0],n_list_n [3][1],n_list_n[4][0])
print("-------------------------------------------------")
print("-------------------------------------------------")

print("Teste_Negativo_Mes_Perfil_Empresa")
n.Teste_Negativo(n_list_n[0][0] ,n_list_n[1][1],n_list_n[2][1],n_list_n [3][1],n_list_n[4][0])
print("-------------------------------------------------")
print("-------------------------------------------------")

print("Teste_Negativo_Mes_Perfil_Empresa")
n.Teste_Negativo(n_list_n[0][0] ,n_list_n[1][0],n_list_n[2][0],n_list_n [3][0],n_list_n[4][1])
print("-------------------------------------------------")
print("-------------------------------------------------")

print("Teste_Negativo_Mes_Perfil_Empresa")
n.Teste_Negativo(n_list_n[0][0] ,n_list_n[1][1],n_list_n[2][1],n_list_n [3][2],n_list_n[4][1])
print("-------------------------------------------------")
print("-------------------------------------------------")

print("Teste_Negativo_Mes_Perfil_Empresa")
n.Teste_Negativo(n_list_n[0][0] ,n_list_n[1][2],n_list_n[2][2],n_list_n [3][1],n_list_n[4][1])
print("-------------------------------------------------")
print("-------------------------------------------------")

print("Teste_Negativo_Mes_Perfil_Empresa")
n.Teste_Negativo(n_list_n[0][0] ,n_list_n[1][0],n_list_n[2][1],n_list_n [3][0],n_list_n[4][1])
print("-------------------------------------------------")
print("-------------------------------------------------")

print("Teste_Negativo_Mes_Perfil_Empresa")
n.Teste_Negativo(n_list_n[0][0] ,n_list_n[1][0],n_list_n[2][0],n_list_n [3][1],n_list_n[4][1])
print("-------------------------------------------------")
print("-------------------------------------------------")

print("Teste_Negativo_Mes_Perfil_Empresa")
n.Teste_Negativo(n_list_n[0][0] ,n_list_n[1][1],n_list_n[2][1],n_list_n [3][1],n_list_n[4][1])
print("-------------------------------------------------")
print("-------------------------------------------------")





print("Teste_Negativo_Mes_Perfil_Você")
n.Teste_Negativo(n_list_n[0][1] ,n_list_n[1][0],n_list_n[2][0],n_list_n [3][0],n_list_n[4][0])
print("-------------------------------------------------")
print("-------------------------------------------------")

print("Teste_Negativo_Mes_Perfil_Você")
n.Teste_Negativo(n_list_n[0][1] ,n_list_n[1][1],n_list_n[2][1],n_list_n [3][2],n_list_n[4][0])
print("-------------------------------------------------")
print("-------------------------------------------------")

print("Teste_Negativo_Mes_Perfil_Você")
n.Teste_Negativo(n_list_n[0][1] ,n_list_n[1][2],n_list_n[2][2],n_list_n [3][1],n_list_n[4][0])
print("-------------------------------------------------")
print("-------------------------------------------------")

print("Teste_Negativo_Mes_Perfil_Você")
n.Teste_Negativo(n_list_n[0][1] ,n_list_n[1][0],n_list_n[2][1],n_list_n [3][0],n_list_n[4][0])
print("-------------------------------------------------")
print("-------------------------------------------------")

print("Teste_Negativo_Mes_Perfil_Você")
n.Teste_Negativo(n_list_n[0][1] ,n_list_n[1][0],n_list_n[2][0],n_list_n [3][1],n_list_n[4][0])
print("-------------------------------------------------")
print("-------------------------------------------------")

print("Teste_Negativo_Mes_Perfil_Você")
n.Teste_Negativo(n_list_n[0][1] ,n_list_n[1][1],n_list_n[2][1],n_list_n [3][1],n_list_n[4][0])
print("-------------------------------------------------")
print("-------------------------------------------------")

print("Teste_Negativo_Mes_Perfil_Você")
n.Teste_Negativo(n_list_n[0][1] ,n_list_n[1][0],n_list_n[2][0],n_list_n [3][0],n_list_n[4][1])
print("-------------------------------------------------")
print("-------------------------------------------------")

print("Teste_Negativo_Mes_Perfil_Você")
n.Teste_Negativo(n_list_n[0][1] ,n_list_n[1][1],n_list_n[2][1],n_list_n [3][2],n_list_n[4][1])
print("-------------------------------------------------")
print("-------------------------------------------------")

print("Teste_Negativo_Mes_Perfil_Você")
n.Teste_Negativo(n_list_n[0][1] ,n_list_n[1][2],n_list_n[2][2],n_list_n [3][1],n_list_n[4][1])
print("-------------------------------------------------")
print("-------------------------------------------------")

print("Teste_Negativo_Mes_Perfil_Você")
n.Teste_Negativo(n_list_n[0][1] ,n_list_n[1][0],n_list_n[2][1],n_list_n [3][0],n_list_n[4][1])
print("-------------------------------------------------")
print("-------------------------------------------------")

print("Teste_Negativo_Mes_Perfil_Você")
n.Teste_Negativo(n_list_n[0][1] ,n_list_n[1][0],n_list_n[2][0],n_list_n [3][1],n_list_n[4][1])
print("-------------------------------------------------")
print("-------------------------------------------------")

print("Teste_Negativo_Mes_Perfil_Você")
n.Teste_Negativo(n_list_n[0][1] ,n_list_n[1][1],n_list_n[2][1],n_list_n [3][1],n_list_n[4][1])
