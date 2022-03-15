programa
{
	
	funcao inicio()
	{
		inteiro cargo
		escreva("Informe o tipo de usuário; 1-Professor, 2-Aluno.\n")
		leia(cargo)
		
		se(cargo==1) {
			escreva("Você tem 10 dias para retornar o livro\n")
		}
		senao se(cargo==2) {
			escreva("Você tem 3 dias para retornar o livro\n")
		}
		senao {
			escreva("Você não é usuário dessa plataforma\n")
		}
	}
}

/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 346; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */