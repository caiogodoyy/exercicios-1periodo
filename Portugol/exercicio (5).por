programa
{
	
	funcao inicio()
	{
		cadeia nome,alunoPior,alunoMelhor
		inteiro idade,alunos,menorIdade,maiorIdade
		real nota,idadeMedia,notaMedia,maiorNota,menorNota

		alunos=0
		maiorIdade=0
		menorIdade=150
		idadeMedia=0
		maiorNota=0
		menorNota=10
		notaMedia=0
		alunoPior="x"
		alunoMelhor="x"
		escreva("Digite -1 na idade para sair.\n")
		faca {
			escreva("\nQual idade do aluno?\n")
			leia(idade)
			se (idade<=-1) {
				pare
			}
			escreva("Qual nome do aluno?\n")
			leia(nome)
			escreva("Qual a nota do aluno?\n")
			leia(nota)
			limpa()

			se (idade>0 e idade<150) {
			alunos=alunos+1
			idadeMedia=idadeMedia+idade
			notaMedia=notaMedia+nota

			se (idade>maiorIdade) {
				maiorIdade=idade
			}
			se (idade<menorIdade) {
				menorIdade=idade
			}
			se (nota>maiorNota) {
				maiorNota=nota
				alunoMelhor=nome
			}
			se (nota<menorNota) {
				menorNota=nota
				alunoPior=nome
			}
			}
		} enquanto (idade!=-1)

		idadeMedia=idadeMedia/alunos
		notaMedia=notaMedia/alunos
		se (alunos==0) {
			escreva("Alunos não informados")
		}
		senao {
		escreva("A quantidade total de alunos é ",alunos,".\n")
		escreva("A maior idade é ",maiorIdade," anos, a menor idade é ",menorIdade," anos e a média das idades é ",idadeMedia," anos.\n")
		escreva("A maior nota é ",maiorNota,", de ",alunoMelhor,", a menor nota é ",menorNota,", de ",alunoPior,", e a média das notas é ",notaMedia,".\n")
		}	
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 946; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */