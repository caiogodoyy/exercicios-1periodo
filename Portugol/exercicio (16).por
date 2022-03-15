programa
{
	
	funcao inicio()
	{
		real precoFabrica, lucro, imposto
		escreva("Para calcular o valor do carro, é preciso dos seguintes valores")
		escreva("\nPreço de fábrica: ")
		leia(precoFabrica)
		escreva("\nPorcentagem de lucro da distribuidora: ")
		leia(lucro)
		escreva("\nPorcentagem dos impostos: ")
		leia(imposto)
		lucro=lucro/100
		imposto=imposto/100
		limpa()
		escreva("Com as informações dadas, o valor correspondente ao lucro do distribuidor é: ", precoFabrica*lucro)
		escreva("\nO valor correspondente aos impostos é: ", precoFabrica*imposto)
		escreva("\nO preço final do veículo sai por: ", precoFabrica+(precoFabrica*imposto)+(precoFabrica*lucro))
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 377; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */