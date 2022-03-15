programa
{
	
	funcao inicio()
	{
		inteiro x,y,z
		escreva("Digite o primeiro valor\n")
		leia(x)
		escreva("Digite o segundo valor\n")
		leia(y)
		escreva("\nAgora digite um terceiro valor\n")
		leia(z)

		se(x==y) {
			se(x==z e y==z) {
					escreva("\n",z," está no intervalo entre ",x," e ",y)
				}
				senao {
					escreva("\n",z," não está no intervalo entre ",x," e ",y)
				}
		}
		
		se(x>y) {
			se(x>=z e y<=z) {
					escreva("\n",z," está no intervalo entre ",x," e ",y)
				}
				senao {
					escreva("\n",z," não está no intervalo entre ",x," e ",y)
				}
		}
		
		se(y>x) {
			se(y>=z e x<=z) {
					escreva("\n",z," está no intervalo entre ",y," e ",x)
				}
				senao {
					escreva("\n",z," não está no intervalo entre ",y," e ",x)
				}
		}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 489; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */