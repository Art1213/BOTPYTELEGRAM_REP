import telebot
import requests

TOKEN = '6861308381:AAElABtsDM8LIy7Pm-ZXvafP-TVCnrdU8-c'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['pizza'])
def pizza(mensagem):
    bot.send_message(mensagem.chat.id, "Saindo a pizza para sua casa. Tempo de espera: 40 mim.")

@bot.message_handler(commands=['hamburguer'])
def hamburguer(mensagem):
    bot.send_message(mensagem.chat.id, "Saindo o hambúrguer para sua casa. Tempo de espera: 40 mim.")

@bot.message_handler(commands=['salada'])
def salada(mensagem):
    bot.send_message(mensagem.chat.id, "Não tem salada. Clique aqui para iniciar: /iniciar")

@bot.message_handler(commands=['opcao1'])
def opcao1(mensagem):
    texto = """
    O que você vai querer? (Clique em uma opção)
        /pizza Pizza
        /hamburguer Hambúrguer
        /salada Salada"""
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=['opcao2'])
def opcao2(mensagem):
    bot.send_message(mensagem.chat.id, 'Para enviar uma reclamação, mande um e-mail para reclamação@balbalba.com')

@bot.message_handler(commands=['opcao3'])
def opcao3(mensagem):
    bot.send_message(mensagem.chat.id, 'Olá, fulano mandou um oi de volta')

@bot.message_handler(commands=['opcao4'])
def covid_data(mensagem):
    covid_api_url = "https://api.apify.com/v2/key-value-stores/TyToNta7jGKkpszMZ/records/LATEST?disableRedirect=true"
    response = requests.get(covid_api_url)

    if response.status_code == 200:
        data = response.json()

        infected_by_region = data.get("infectedByRegion", [])

        if infected_by_region:
            text = "COVID-19 Data by Region:\n"
            for region in infected_by_region:
                text += f"{region['state']}: {region['count']} cases\n"

            bot.send_message(mensagem.chat.id, text)
        else:
            bot.send_message(mensagem.chat.id, "No COVID-19 data available.")
    else:
        bot.send_message(mensagem.chat.id, "Failed to fetch COVID-19 data. Please try again later.")

def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def resposta(mensagem):
    texto = """
    Clique em qual ação você deseja para continuar:
        /opcao1 Fazer um pedido
        /opcao2 Reclamar de um pedido
        /opcao3 Mande um abraço.
        /opcao4 Mostre os dados da Covid.
    Responder qualquer coisa não vai funcionar. Clique em umas das opções."""
    bot.reply_to(mensagem, texto)

bot.polling()