programa
{
	
	funcao inicio()
	{
		real kidsDead,vida,i,menino,menina,vidaMin
		inteiro perMenino,perMenina,perVida
		caracter sexo
		escreva("Digite o número de crianças mortas nesse período: ")
		leia(kidsDead)
		se(kidsDead<0) {
		escreva("Digite o número de crianças mortas nesse período: ")
		leia(kidsDead)
		}
		limpa()

		perVida=0
		perMenino=0
		perMenina=0
		vidaMin=0
		menino=0
		menina=0
		i=kidsDead
		enquanto(i>0) {
			escreva("Digite o sexo da criança (M=Masculino F=Feminino): ")
			leia(sexo)
			escreva("\nDigite o tempo de vida da criança (Em meses): ")
			leia(vida)
			se(vida<0) {
			escreva("\nDigite o tempo de vida da criança (Em meses): ")
			leia(vida)
			}

			se(sexo=='M' ou sexo=='m') {
				menino=menino+1
			}
			se(sexo=='F' ou sexo=='f') {
				menina=menina+1
			}
			se(vida<=24) {
				vidaMin=vidaMin+1
			}
			i--
			limpa()
		}

		perMenino=(menino/kidsDead)*100
		perMenina=(menina/kidsDead)*100
		perVida=(vidaMin/kidsDead)*100
		escreva("A percentagem de crianças do sexo feminino mortas no período: ",perMenina,"%.\n")
		escreva("A percentagem de crianças do sexo masculino mortas no período: ",perMenino,"%.\n")
		escreva("A percentagem de crianças que viveram 24 meses ou menos no período: ",perVida,"%.\n")
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 317; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */