#!/usr/bin/env python
# -*- coding: utf-8 -*-



import TabelaCampanha
from WhatsAppBot.whatsapp import WhatsApp

wa_var = WhatsApp(360,
                     "C:/Users/Machina-W10/PycharmProjects/TopWay_Campanha_Whats/session_SS.png",
                     "C:/Users/Machina-W10/PycharmProjects/TopWay_Campanha_Whats/WhatsAppBot/topway_whatsapp_session" )

wa_var.send_message("Vitor Co", "Oi Otávio!!  tudo certinho?")
wa_var.send_message("Vitor Co", "Sou executivo de seleção de alunos para a TopWay Flex, inglês rápido para profissionais. Olha este víde \U0001f4fd\uFE0F")
wa_var.send_picture("Vitor Co", "C:/Users/Machina-W10/PycharmProjects/TopWay_Campanha_Whats/documentos_enviar/video_topway_1.mp4")
wa_var.send_message("Vitor Co", u"Estamos selecionando aguns contatos para terem acesso a um benefício e desenvolver o inglês rápido. Estudando em casa com nossa plataforma registada e 100% ao vivo. (também temos programas presenciais). \n\n \u2728É um acesso bem exclusivo\u2728 ")

wa_var.send_picture("Vitor Co", "C:/Users/Machina-W10/PycharmProjects/TopWay_Campanha_Whats/documentos_enviar/video_topway_1.mp4",  "quais mudanças vão acontecer na sua vida quando você adquirir a fluência no inglês?")

wa_var.quit()
wa_var.send_message("Vitor Co", "	")

caption_xpath = "/html/body/div[1]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div[1]/span/div/div[2]/div/div[3]/div[1]"

caption_xpath = "/html/body/div[1]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div[1]/span/div/div[2]/div/div[3]/div[1]/div[2]"
send_caption = wa_var.browser.find_element_by_xpath(caption_xpath)
send_caption.send_keys("teste")