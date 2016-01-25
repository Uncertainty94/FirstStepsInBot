#!/usr/bin/env python
# -*- coding: utf-8 -*-
import aiml
import pymorphy2
import lexem

# Create the kernel and learn AIML files
kernel = aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("load aiml b")
kernel.setBotPredicate("name", "Melody")

morph = pymorphy2.MorphAnalyzer()

while True:
    message = raw_input("Enter your message >> ")

    if message.lower() == "пока":
        print ("Пока")
        exit()
    else:
        # Используя шаблон "Образуй нормальную форму от *" выведет номальную форму любого слова.
        tryparse = message.decode('utf-8').lower().encode('utf-8').replace(' ', '').split("от")
        if tryparse[0] == "образуйнормальнуюформу":
            print(morph.normal_forms(tryparse[1].decode('utf-8'))[0].encode('utf-8'))

        elif "собака" in message:       # Эта собака Максима
            resp = kernel.respond(message).split("~")
            start = resp[0]
            newName = morph.parse(resp[1].decode("utf-8"))[0].inflect({lexem.Lexem.Case.datv}).word
            answer = start.decode("utf-8") + newName.title()
            print (answer)

        else:
            # Все остальные ответы из aiml
            print(kernel.respond(message))
