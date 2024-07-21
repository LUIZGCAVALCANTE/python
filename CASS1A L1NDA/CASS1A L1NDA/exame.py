import csv
#primeiro modulo recebe o gabarito e o nome do curso
def receber_gabarito(qtd_questoes):
    gabarito = []
    print("Digite o gabarito da prova:")
    for i in range(qtd_questoes):
        resposta_valida = False
        while not resposta_valida:
            resposta = input(f"Questão {i+1}: ").lower().strip()
            if resposta in ['a', 'b', 'c', 'd']:
                gabarito.append(resposta)
                resposta_valida = True
            else:
                print("Resposta não aceita nesse concurso. Digite apenas conforme esse exemplo: a, b, c ou d.")
    return gabarito
#aqui é recebido as respostas e o nome dos candidatos.
def receber_respostas_candidatos(qtd_questoes):
    with open('respostas_candidatos.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Nome"] + [f"Questão {i+1}" for i in range(qtd_questoes)])
        nome = ""
        while nome.lower() != 'sair':
            nome = input("Nome do candidato (ou 'sair' para encerrarmos): ").strip()
            if nome.lower() == 'sair':
                continue
            respostas = []
            for i in range(qtd_questoes):
                resposta_valida = False
                while not resposta_valida:
                    resposta = input(f"Questão {i+1}: ").lower().strip()
                    if resposta in ['a', 'b', 'c', 'd']:
                        respostas.append(resposta)
                        resposta_valida = True
                    else:
                        print("Resposta não aceita nesse concurso. Digite apenas conforme esse exemplo: a, b, c ou d.")
            writer.writerow([nome] + respostas)
#aqui ocorre professora a correção e inserção das respostas no csv
def corrigir_provas(gabarito):
    resultados = []
    with open('respostas_candidatos.csv', mode='r') as file:
        reader = csv.reader(file)
        next(reader) 
        for row in reader:
            nome = row[0]
            respostas = row[1:]
            pontuacao = sum(1 for i in range(len(gabarito)) if respostas[i] == gabarito[i])
            resultados.append((nome, pontuacao))
    
    with open('pontuacoes_candidatos.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Nome", "Pontuação"])
        writer.writerows(resultados)
    
    return resultados
#aqui é print das respostas 
def exibir_pontuacoes(titulo_concurso):
    print("\n" + titulo_concurso)
    print(f"{'Nome do Candidato':<30}{'Pontuação':<10}")
    print("="*40)
    with open('pontuacoes_candidatos.csv', mode='r') as file:
        reader = csv.reader(file)
        next(reader) 
        for row in reader:
            nome, pontuacao = row
            print(f"{nome:<30}{pontuacao:<10}")
#calculo da aritimética geral 
def calcular_media():
    total_pontos = 0
    num_candidatos = 0
    with open('pontuacoes_candidatos.csv', mode='r') as file:
        reader = csv.reader(file)
        next(reader)  
        for row in reader:
            total_pontos += int(row[1])
            num_candidatos += 1
    media = total_pontos / num_candidatos if num_candidatos > 0 else 0
    return media
#inserção do nome do concurso e algumas orientações básicas
def main():
    titulo_concurso = input(" Por favor digite o título do concurso: ").strip()
    
    qtd_questoes_valida = False
    while not qtd_questoes_valida:
        try:
            qtd_questoes = int(input("Digite a quantidade de questões que essa  prova irá ter: ").strip())
            if qtd_questoes > 0:
                qtd_questoes_valida = True
            else:
                print("O número de questões deve ser um inteiro positivo, numeros decimais, negativos não serão aceitos ok?.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

    gabarito = receber_gabarito(qtd_questoes)
    
    receber_respostas_candidatos(qtd_questoes)
    
    resultados = corrigir_provas(gabarito)
    
    exibir_pontuacoes(titulo_concurso)
    
    media = calcular_media()
    print(f"\nMédia de acertos: {media:.2f}")

if __name__ == "__main__":
    main()

#não coloquei break pois sei que você não gosta 