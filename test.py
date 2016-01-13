#!/usr/bin/env python
# -*- coding: utf-8 -*-
import aiml
import pymorphy2

# Create the kernel and learn AIML files
kernel = aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("load aiml b")
kernel.setBotPredicate("name", "Melody")

morph = pymorphy2.MorphAnalyzer()

# Эта Собака Максима
while True:
    message = raw_input("Enter your message >> ")
    # print(morph.normal_forms(message))

    if message == "quit":
        print ("Bye")
        exit()
    else:
        # Используя шаблон "Образуй нормальную форму от *" выведет номальную форму любого слова.
        tryparse = message.decode('utf-8').lower().encode('utf-8').replace(' ', '').split("от")
        if tryparse[0] == "образуйнормальнуюформу":
            print(morph.normal_forms(tryparse[1].decode('utf-8'))[0].encode('utf-8'))
        else:
            resp = kernel.respond(message).split("~")
            start = resp[0]
            newName = morph.parse(resp[1].decode("utf-8"))[0].inflect({"datv"}).word
            qwe = start.decode("utf-8") + newName.title()
            print (qwe)
