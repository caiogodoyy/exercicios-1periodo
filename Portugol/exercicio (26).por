programa
{
	
	funcao inicio()
	{
		real salario
		escreva("Digite o salário a ser calculado\n")
		leia(salario)

		se (salario <= 1500) {
			escreva("Imposto de renda é isento")
		}
		se (salario > 1500 e salario <= 2500) {
			escreva("Imposto de renda é: R$",salario*0.15)
		}
		se (salario > 2500 e salario <= 4000) {
			escreva("Imposto de renda é: R$",salario*0.275)
		}
		se (salario > 4000) {
			escreva("Imposto de renda é: R$",salario*0.35)
		}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 263; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */