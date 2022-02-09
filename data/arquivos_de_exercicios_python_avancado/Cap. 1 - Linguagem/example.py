from string import Template


def doc():
	#
	texto = Template("""

		ASSUNTO  :  AUTO DE INFRAÇÃO
		AUTUADO  :  ${autuado}
		PROCESSO :  ${processo}


	DESPACHO :  ${num} / ${ano} 	Retornem-se os autos à Diretoria de Cobrança da Dívida Ativa, tendo\n
	em vista que as demandas e soluções possíveis na esfera administrativa pertinentes à jurisdição desta\n
	Gerência do Contencioso Fiscal (órgão julgador de primeira instância) foram finalizadas.

		Considerando a célebre atribuição pertinente à esta Secretaria Municipal de Finanças para\n
	acompanhamento de parcelamentos e ou liquidação dos tributos ora pendentes.

	 	Considerando o princípio de eficiência e eficácia na administração pública, avaliamos a necessária\n
	permanência dos autos neste órgão até que os débitos sejam liquidados para maior celeridade dos\n
	procedimentos relativos à cobrança. 

		Na oportunidade solicitamos que, os autos cujo débito ora existente tenha sido liquidado, sejam\n
	encaminhados à Diretoria de Vigilância Sanitária (sigla DPVSA) para fins de procedimentos pertinentes à\n
	Fiscalização Sanitária e posterior arquivamento dos mesmos. 


		Gerência do Contencioso Fiscal da Secretaria Municipal de Saúde.
		Goiânia, ${dia} de ${mes} de ${ano}.





							  ${nome}
							Gerente do Contencioso Fiscal
							  Decreto nº ${dec}/${ano}""")
	#
	#
	dados = {
		'autuado': 'Nome da pessoa autuada',
		'processo': 12345678,
		'num': 1234,
		'nome': 'Nome do gerente',
		'dec': 12345,
		'ano': 2022,
		'dia': 28,
		'mes': 'janeiro'
	}
	#
	#
	context = texto.substitute(dados)
	#
	print(context)


if __name__ == '__main__':
	doc()