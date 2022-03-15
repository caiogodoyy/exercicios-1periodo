programa
{
	
	funcao inicio()
	{
		inteiro codigo
		real salario
		escreva("Digite o código do respectivo cargo:\n")
		leia(codigo)
		escreva("Digite o salário atual:\n")
		leia(salario)
		limpa()
		escolha(codigo) {
			caso 1:
			salario=salario*1.45
			pare
			caso 2:
			salario=salario*1.35
			pare
			caso 3:
			salario=salario*1.25
			pare
			caso 4:
			salario=salario*1.15
			pare
			caso 5:
			salario=salario
			pare
			caso contrario:
			escreva("Código não existente.") 
		}
		se(codigo>0 e codigo<6)
		escreva("Com a mudança, o novo salário é R$",salario,"\n")
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 201; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */