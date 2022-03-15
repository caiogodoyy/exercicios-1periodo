programa
{
	
	funcao inicio()
	{
		real salario, reajuste1, reajuste2, reajuste3
		escreva("Qual valor do seu salário\n")
		leia(salario)

		reajuste1 = salario*1.05
		reajuste2 = salario*1.10
		reajuste3 = salario*1.15
		
		se(salario>7000) {
			escreva("Seu novo salário é igual a ", reajuste1) 
		}
		senao se(salario>=5000) {
			escreva("Seu novo salário é igual a ", reajuste2)
		}
		senao se(salario<5000) {
			escreva("Seu novo salário é igual a ", reajuste3)
		}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 458; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */