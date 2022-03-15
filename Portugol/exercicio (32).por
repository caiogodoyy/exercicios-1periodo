programa
{
	
	funcao inicio()
	{
		real nota1, nota2, media
		escreva("Digite a primeira nota do aluno ")
		leia(nota1)
		escreva("Digite a segunda nota do aluno ")
		leia(nota2)

		media = (nota1 + nota2)/2
		
		se (media >= 7) {
			escreva("\nAPROVADO!\n")
		}
		senao se (media >= 4) {
			escreva ("\nFINAL.\n")
		}
		senao {
			escreva ("\nREPROVADO.\n")
		}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 213; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */