programa
{
	
	funcao inicio()
	{
		inteiro codigo
		cadeia cargo
		real salario,novoSalario
		escreva("Escreva o código de seu cargo\n")
		leia(codigo)
		escreva("Qual seu salário atual?\n")
		leia(salario)

		escolha(codigo) {
			caso 1:
				cargo="secretário"
				novoSalario=salario*1.45
				pare
			caso 2:
				cargo="tesoureiro"
				novoSalario=salario*1.35
				pare
			caso 3:
				cargo="professor"
				novoSalario=salario*1.25
				pare
			caso 4:
				cargo="coordenador"
				novoSalario=salario*1.15
				pare
			caso 5:
				cargo="diretor"
				novoSalario=salario
				pare
			caso contrario:
				cargo="desempregado"
				novoSalario=0
		}

		escreva("Sendo você um ",cargo,", seu novo salário será: R$",novoSalario)
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 256; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */