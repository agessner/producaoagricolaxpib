def indexar_lista(lista, fn_chave):
    lista_indexada = {}
    for item in lista:
        valor_chave = fn_chave(item)
        if valor_chave not in lista_indexada:
            lista_indexada[valor_chave] = []
        lista_indexada[valor_chave].append(item)
    return lista_indexada
