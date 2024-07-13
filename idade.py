idade = int(input('Qual é a sua idade? ')) #Pergunta de qual é a sua idade
altura = float(input('Qual é a altura? ')) #Pergunta de qual é a sua altura

tickat_valido = True #Validando o tickat

if tickat_valido: # < Caso se digitar correto 
   print('\nSeu tickat é válido!')

if idade > 18 and altura > 1.5: # < Caso for verdadeiro é para printar "Entrada permitida"
  print('\nEntrada permitida!')
     
else:   # < Caso o valor digitado for falso
  print('\nEntrada não permitida!')
