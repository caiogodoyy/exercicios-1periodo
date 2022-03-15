programa
{
	
	funcao inicio()
	{
		inteiro num1[30],num2[30],soma[30],x,i
		
		x=30
		i=0
		enquanto(x>0) {
			escreva("\nDigite um número: ")
			leia(num1[i])
			escreva("Digite outro número: ")
			leia(num2[i])
			soma[i]=num1[i]+num2[i]
			escreva("A soma dois dois é: ",soma[i],"\n")
			
			i++
			x--
		}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 89; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */