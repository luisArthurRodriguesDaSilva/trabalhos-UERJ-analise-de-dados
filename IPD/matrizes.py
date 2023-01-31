def identidade (ordem):
  '''gera uma matriz identidade da ordem definida como parâmetro'''
  matriz = []
  for i in range(ordem):
    internMatriz = []
    for k in range(ordem):
      internMatriz.append(1 if k == i else 0)
    matriz.append(internMatriz)
  return matriz

def criar_matriz_nula(linhas,colunas):
  '''gera uma matriz nula com as  devidas dimensões'''
  matriz = []
  for i in range(linhas):
    internMatriz = []
    for k in range(colunas):
      internMatriz.append(0)
    matriz.append(internMatriz)
  return matriz

def densidade(matriz):
  '''análiza a densidadde da matriz (quantidade de zeros)/não zeros'''
  nonZeros = 0
  size = len(matriz)*len(matriz[0])
  for linha in matriz:
    for elemento in linha:
      if elemento != 0:
        nonZeros +=1
  return nonZeros/size

def mult_escalar(matriz,escalar):
  '''faz a multiplicação da matriz por um escalar'''
  novaMatriz = []
  for linha in matriz:
    internMatriz = []
    for elemento in linha:
      z = elemento*escalar
      internMatriz.append(z)
    novaMatriz.append(internMatriz)
  return novaMatriz

def verificar_igualdade_proporcional(m1,m2):

  hm1,hm2 = len(m1), len(m2)
  lm1,lm2 = len(m1[0]), len(m2[0])
  if hm1 == hm2 and lm1 == lm2:
    return True
  return False

def soma_matrizes (m1,m2):
  '''retorn a soma das matrizes'''
  if not verificar_igualdade_proporcional(m1,m2):
    return -1
  novaMatriz=[]
  for indexL,LineM1 in enumerate(m1):
    internMatriz = []
    for indexE,elementM1 in enumerate(LineM1):
      internMatriz.append(elementM1+m2[indexL][indexE])
    novaMatriz.append(internMatriz)
  return novaMatriz

def isQuadrada (matriz):
  '''verifica se a matriz é quadrada'''
  if len(matriz) == len(matriz[0]):
    return True
  return False

def isTriangularSuperior(matriz):
  '''verifica se a matriz é triangular superior (zeros apenas em baixo)'''
  if not isQuadrada(matriz):
    return -1
  for lIndex,linha in enumerate(matriz):
    for cIndex , elemento in enumerate(linha):
      if lIndex > cIndex and elemento != 0: #verifica apenas a parte inferior
        return False
  return True

def isTriangularInferior(matriz):
  '''verifica se a matriz é triangular superior (zeros apenas em cima)'''
  if not isQuadrada(matriz):
    return -1
  for lIndex,linha in enumerate(matriz):
    for cIndex , elemento in enumerate(linha):
      if lIndex < cIndex and elemento != 0: #verifica apenas a parte superior
        return False
  return True

def multiplica_matrizes(m1,m2):
  '''realiza a operação de multiplicar as matrizes'''
  if len(m1) != len(m2[0]):
    return -1
  resultado = criar_matriz_nula(len(m1),len(m2[0]))
  for x in range(len(m1)):
    for y in range(len(m2[0])):
       for c in range(len(m2)):
           resultado[x][y] += m1[x][c] * m2[c][y]
  return resultado

def redefinir_elemento(matriz,novo_elemento,coordenadaLinha,coordenadaColuna):
  '''nomes autoexplicativos ja bastam ~ cleanCode'''
  if coordenadaLinha > len(matriz) or coordenadaColuna > len(matriz[0]):
    return print('coodernadas invalidas')
  matriz[coordenadaLinha][coordenadaColuna] = novo_elemento
  return matriz

def show_matriz(matriz):
  '''mostra a matriz na tela de maneira agradável'''
  print('\n\n')
  for i,l in enumerate(matriz):
    for e in l:
      print(e,end='  ')
    print('\n\n')

def getWithoutError(text,erro = False):
  '''consegue obter uma informação numérica sem quebrar o sistema inteiro em caso de erro'''
  try:
    if erro:
      return float(input(f'{text} novamente pois o input colocado foi invalido : '))
    return float(input(f'{text}: '))
  except:
    return getWithoutError(f'{text}',True)

def obterMatriz(initialText='matriz:',linhas=0,colunas=0):
  '''função utilizada para que o usuário consiga adicionar uma matriz na execução do sistema sem precisar modificar o código'''
  print(f'\n\n{initialText}\n')
  if linhas == 0 and colunas == 0:
    linhas,colunas = int(getWithoutError('linhas ')),int(getWithoutError('colunas'))
  matrizZero = criar_matriz_nula(linhas,colunas)
  for i,linha in enumerate(matrizZero):
    for k,elemento in enumerate(linha):
      matrizZero[i][k] = getWithoutError(f'elemento de coordenadas[{i + 1}][{k + 1}]')
  return {
      "matriz" : matrizZero,
      "colunas" : colunas,
      "linhas" : linhas
  }

#------------------funções de chamada-----------------------------
def opIdentidade():
  show_matriz(getWithoutError('ordem'))

def opCriar_matriz_nula():
  linhas = getWithoutError('linhas')
  colunas = getWithoutError('colunas')
  show_matriz(criar_matriz_nula(linhas,colunas))

def opDensidade():
  m = obterMatriz()['matriz']
  print(densidade(m))

def opMult_escalar():
  escalar = getWithoutError('escalar')
  m = obterMatriz()['matriz']
  show_matriz(mult_escalar(m,escalar))

def opSoma_matrizes():
  m1Dict = obterMatriz('m1:')
  linhas, colunas = m1Dict['linhas'],m1Dict['colunas']
  m1,m2 = m1Dict['matriz'], obterMatriz('m2',linhas=linhas,colunas=colunas)['matriz']
  show_matriz(soma_matrizes(m1,m2))

def opIsQuadrada():
  m1 = obterMatriz()['matriz']
  show_matriz(m1)
  print('é quadrada' if isQuadrada(m1) else 'não é quadrada')


def opIsTriangularSuperior():
  m1 = obterMatriz()['matriz']
  show_matriz(m1)
  print('é triangular superior' if isTriangularSuperior(m1) else 'não é trinagular superior')

def opIsTriangularInferior():
  m1 = obterMatriz()['matriz']
  show_matriz(m1)
  print('é triangular inferior' if isTriangularInferior(m1) else 'não é trinagular inferior')


  


  

# ----------------------------------------------------------------
funcoesDeOperacoes = [
  opIdentidade,
  opCriar_matriz_nula,
  opDensidade,
  opMult_escalar,
  opSoma_matrizes,
  opIsQuadrada,
  opIsTriangularSuperior,
  opIsTriangularInferior,
  # opMultiplica_matrizes,
  # opRedefinir_elemento,
]

def getFuncNumber():
  print('catalogo de funções, digite o numero relativo a que você quer')
  print(1,'identidade')
  print(2,'criar_matriz_nula')
  print(3,'densidade')
  print(4,'mult_escalar')
  print(5,'soma_matrizes')
  print(6,'isQuadrada')
  print(7,'isTriangularSuperior')
  print(8,'isTriangularInferior')
  print(9,'multiplica_matrizes')
  print(10,'redefinir_elemento')
  num = int(getWithoutError('numero da função'))
  return num-1

def main():
  while(1):
    numeroDaOperacao = getFuncNumber()
    if (numeroDaOperacao+1) > len(funcoesDeOperacoes):
      print('parabens por ter feito bom uso da calculadora de matrizes')
      break
    funcoesDeOperacoes[numeroDaOperacao]()
    print('\n\n')

main()


