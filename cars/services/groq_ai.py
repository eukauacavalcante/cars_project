from django.conf import settings
from groq import Groq


client = Groq(api_key=settings.GROQ_API_KEY)


def get_ai_description(model, brand, year):
    response = client.chat.completions.create(
        model=settings.AI_MODEL,
        messages=[
            {
                'role': 'system', 
                'content': '''Você é um especialista em descrições de veículos para anúncios de venda. 
                Suas descrições devem ser persuasivas, técnicas e diretas.
                NUNCA use frases introdutórias como "Aqui está", "Segue", "Veja" ou similares.
                Comece SEMPRE diretamente com a descrição do veículo.
                Se o modelo não existir ou os dados estiverem incorretos, retorne apenas: "Dados insuficientes para gerar descrição."'''
            },
            {
                'role': 'user',
                'content': f'''Crie uma descrição comercial persuasiva para: {brand} {model} {year}
                            Requisitos:
                            - Máximo 1000 caracteres
                            - Destaque 2-3 características técnicas reais e específicas deste modelo/ano
                            - Use linguagem que valorize o veículo e atraia compradores
                            - Seja objetivo e direto
                            - Foque em diferenciais competitivos (motorização, tecnologia, economia, desempenho)
                            - Não invente especificações se não tiver certeza'''
            }
        ],
    )
    return response.choices[0].message.content