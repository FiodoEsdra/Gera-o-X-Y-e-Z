


nome= input("Qual seu nome? ")
print ("Obrigado")
seg_nome= input("Qual seu segundo nome? ")
print ("Obrigado")
sob_nome= input("Qual seu sobrenome? ")
print ("Obrigado")
ano_nasc= int(input("Digite o ano que voce Nasceu?"))
ano_atual = 2022
idade = ano_atual - ano_nasc
if (ano_nasc >= 1965) and (ano_nasc <= 1980):
  print ("Voce é da Geração X")
if (ano_nasc >= 1981) and (ano_nasc <= 1999):
  print ("Voce é da Geração Y")
if (ano_nasc >= 2000) and (ano_nasc <= 2010):
  print ("Voce é da Geração Z")
print("Sua idade é de "  ,idade, "anos ")
print ("Seu nome completo é:" ,nome + " " + seg_nome + " " + sob_nome, )
res_ger= input("Quer Saber mais da sua Geração? ")

if res_ger == "sim":
  print ("Pesquisa no Google então, não vou formatar texto no Python só porque voce " ,nome, "quer" )
if res_ger == "não":
  print("Então vá a merda")
if res_ger != "sim" or "não":
  print("Não entendi sua resposta, escreva direito, não igual uma mula")