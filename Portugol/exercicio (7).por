programa
{
	
	funcao inicio()
	{
		real altura,maiorAltura,menorAltura,alturaM,alturaF,mediaAlturaM,mediaAlturaF
		caracter sexo
		inteiro pessoas,homens,mulheres
		pessoas=5
		maiorAltura=0
		menorAltura=1000
		alturaM=0
		alturaF=0
		mulheres=0
		homens=0
		mediaAlturaM=0
		mediaAlturaF=0

		enquanto(pessoas>0) {
			escreva("Digite a altura, em metros:\n")
			leia(altura)
			escreva("Digite o sexo: M=Masculino F=Feminino\n")
			leia(sexo)
			se(altura>maiorAltura) {
				maiorAltura=altura
			}
			se(altura<menorAltura) {
				menorAltura=altura
			}
			se(sexo=='M') {
				alturaM=alturaM+altura
			}
			se(sexo=='F') {
				alturaF=alturaF+altura
			}
			se(sexo=='M') {
				homens=homens+1
			}
			se(sexo=='F') {
				mulheres=mulheres+1
			}
			pessoas=pessoas-1
			limpa()
		}

		mediaAlturaM=alturaM/homens
		mediaAlturaF=alturaF/mulheres
		escreva("A maior altura do grupo é ",maiorAltura,"m e a menor é ",menorAltura,"m.\n")

		se(homens==0) {
			escreva("A média de altura das mulheres é ",mediaAlturaF,".\n")
		}
		se(mulheres==0) {
			escreva("A média de altura dos homens é ",mediaAlturaM,".\n")
		}
		senao {
			escreva("A média das alturas das mulheres é ",mediaAlturaF," e a média dos homens é ",mediaAlturaM,".\n")
		}
		escreva("O número de homens é ",homens," e o de mulheres é ",mulheres,".\n")
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 1082; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */