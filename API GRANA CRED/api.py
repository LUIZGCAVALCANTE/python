from flask import Flask, request, jsonify
import re

app = Flask(__name__)

def check_topic(query):
    allowed_topics = [
        "simulação do FGTS", "autorizar o banco", "análise da solicitação",
        "simulação ou antecipação", "quitar antecipação", "vale a pena",
        "situação do meu FGTS", "saldo do FGTS", "saque-aniversário",
        "documentos necessários", "pagamento", "bancos aceitos", "mês do aniversário",
        "contato com a Granacred"
    ]
    
    return any(topic.lower() in query.lower() for topic in allowed_topics)

def calculate_amount(saldo, birthdate):
    try:
        saldo = float(re.sub(r'[^\d.]', '', saldo))
        amount = saldo * 0.68
        return f"O valor liberado aproximado é de R${amount:.2f}."
    except ValueError:
        return "Não foi possível calcular o valor liberado. Por favor, forneça um saldo válido."

@app.route('/api', methods=['POST'])
def api():
    data = request.json
    query = data.get('query')
    
    if not check_topic(query):
        return jsonify({"response": "Não posso responder essa pergunta. Faça uma nova pergunta."})
    
    if "iniciar a simulação do FGTS" in query:
        return jsonify({"response": "Para iniciar a simulação, autorize o 'PARANA BANCO S/A' e o banco Safra no aplicativo do FGTS. Após essa autorização, nos informe para que possamos dar continuidade ao processo."})
    
    if "autorizei o banco no aplicativo" in query:
        return jsonify({"response": "Ótimo! Agora, por favor, nos forneça seu CPF para continuarmos com a simulação. Lembre-se, o CPF deve ter entre 8 e 11 dígitos."})
    
    if "dificuldades para autorizar o banco" in query:
        return jsonify({"response": "Se estiver tendo problemas para autorizar o banco, tente reiniciar seu celular ou reinstalar o aplicativo do FGTS. Se os problemas persistirem, pode ser necessário atualizar seus dados de acesso junto a uma agência da Caixa."})
    
    if "quanto tempo leva a análise" in query:
        return jsonify({"response": "Realizamos a análise de forma ágil para evitar demoras. Você receberá uma atualização sobre o status da sua solicitação em breve."})
    
    if "é possível fazer mais de uma simulação" in query:
        return jsonify({"response": "Sim, é possível realizar novas simulações ou antecipações a cada 60 dias, desde que você esteja empregado e ativo na empresa."})
    
    if "quitar minha antecipação" in query:
        return jsonify({"response": "Sim, você pode quitar sua antecipação quando desejar. Ao quitar, você poderá beneficiar-se de descontos nos juros, que podem chegar a até 70%."})
    
    if "hesitante sobre a antecipação" in query:
        return jsonify({"response": "Entendemos suas preocupações. Comparando com outras modalidades de crédito, a antecipação do FGTS pode oferecer vantagens, especialmente em termos de juros. A decisão deve ser baseada na sua situação financeira e necessidades específicas."})
    
    if "como fica a situação do meu FGTS" in query:
        return jsonify({"response": "Com a antecipação, o valor correspondente do seu FGTS será gerido pelo banco escolhido, que antecipará esse valor para você. Você pode quitar a antecipação a qualquer momento."})
    
    if "saldo do FGTS é inferior a R$200,00" in query:
        return jsonify({"response": "Para a antecipação, é necessário um saldo mínimo de R$200,00 no FGTS. Se seu saldo for inferior a esse valor, infelizmente, não será possível prosseguir com a solicitação."})
    
    if "mudar de ideia sobre o saque-aniversário" in query:
        return jsonify({"response": "Se optar pela modalidade de saque-aniversário, você deverá aguardar um período obrigatório de 24 meses antes de poder voltar para a modalidade de saque-rescisão."})
    
    if "documentos necessários" in query:
        return jsonify({"response": "Aceitamos uma variedade de documentos para verificação, como RG, CNH, carteira de trabalho, desde que estejam em bom estado e sejam legíveis."})
    
    if "quando o pagamento será efetuado" in query:
        return jsonify({"response": "Os pagamentos são processados de maneira rápida, podendo ser concluídos em minutos. Dependendo do volume de operações, pode ser necessário esperar até o próximo dia útil."})
    
    if "bancos aceitos" in query:
        return jsonify({"response": "Aceitamos uma ampla variedade de bancos, incluindo instituições digitais como Nubank, Caixa Tem, Next, além de bancos tradicionais."})
    
    if "antecipação no mês do meu aniversário" in query:
        return jsonify({"response": "Sim, se já optou pela modalidade de saque-aniversário, pode prosseguir com a antecipação. Caso contrário, será necessário aguardar até o próximo ciclo."})
    
    if "entrar em contato com a Granacred" in query:
        return jsonify({"response": "Você pode nos contatar pelos números fornecidos. Estamos aqui para ajudar com qualquer dúvida ou assistência que você possa precisar."})
    
    if "não conseguir autorizar o banco pelo aplicativo" in query:
        return jsonify({"response": "Se enfrentar dificuldades técnicas, sugerimos reiniciar o dispositivo ou tentar novamente mais tarde. Problemas persistentes podem ser resolvidos com nosso especialista no WhatsApp: wa.me/551832721351."})
    
    saldo_match = re.search(r'meu saldo é de ([0-9,.]+)', query)
    if saldo_match:
        saldo = saldo_match.group(1)
        return jsonify({"response": "Qual é a sua data de aniversário?"})
    
    birthdate_match = re.search(r'\d{2}/\d{2}/\d{4}', query)
    if birthdate_match:
        birthdate = birthdate_match.group(0)
        return jsonify({"response": calculate_amount(saldo, birthdate) + " Para o valor real, fale com nosso especialista: wa.me/551832714834."})

    return jsonify({"response": "Não sei como responder essa pergunta. Vou te encaminhar para um especialista no WhatsApp: wa.me/551832721351."})

if __name__ == '__main__':
    app.run(debug=False)