def format_cpf_cnpj(cpf_cnpj: int) -> str:
    """
    A função recebe um número e formata em CPF ou CNPJ;

    Parameters:
        cpf_cnpj: sequência de números que representam um documento de pessoa física (CPF) ou de Pessoa Jurídica (CNPJ)

    Returns:
        Uma string formatada da numeração do documento recebido.
        
    Examples:
        >>> format_cpf_cnpj(12345678910)
        '123.456.789-10'

        >>> format_cpf_cnpj(123456789101)
        '00.123.456/7891-01'
    """

    doc = str(cpf_cnpj).split('.')[0]
    try:
        if len(doc) <= 11:
            numero = '{:0>11}'.format(doc)
            t1 = numero[0:3]
            t2 = numero[3:6]
            t3 = numero[6:9]
            t4 = numero[9:]
            numero = f'{t1}.{t2}.{t3}-{t4}'
            return numero
        else:
            numero = '{:0>14}'.format(doc)
            t1 = numero[0:2]
            t2 = numero[2:5]
            t3 = numero[5:8]
            t4 = numero[8:12]
            t5 = numero[12:]
            numero = f'{t1}.{t2}.{t3}/{t4}-{t5}'
            return numero
    except:
        return ''


def format_cod(codigo: any) -> str:
    """
    Formata o código de um imóvel rural no Sistema Nacional de Cadastro Rural - SNCR

    Parameters:
        codigo: um número ou uma string com o código do imóvel rural
    
    Returns:
        Uma string formatada do código recebido.

    Examples:
        >>> format_cod('nan')
        '000.000.000.000-0'

        >>> format_cod(1234567890123)
        '123.456.789.012-3'
    """
    if codigo == 'nan':
        return '000.000.000.000-0'
    else:
        codigo = '{:0>13}'.format(str(codigo).split('.')[0])
        t1 = codigo[0:3]
        t2 = codigo[3:6]
        t3 = codigo[6:9]
        t4 = codigo[9:12]
        t5 = codigo[12:]
        codigo = f'{t1}.{t2}.{t3}.{t4}-{t5}'
        return codigo


def fundi(mf: float) -> str:
    """
    Classifica um imóvel rural com base na quantidade de múdulos fiscais

    Parameters:
        mf: Quantidade de módulos fiscais de um imóvel rural
    
    Returns:
        Uma string com a classificação do imóvel quanto ao seu tamanho [Pequeno, Médio, Grande].

    Examples:
        >>> fundi(4)
        'Pequena'
        >>> fundi(6)
        'Média'
        >>> fundi(16)
        'Grande'
    """
    if mf <= 4:
        return 'Pequena'
    elif (mf > 4) & (mf <= 15):
        return 'Média'
    else:
        return 'Grande'
