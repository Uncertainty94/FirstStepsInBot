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


while True:
    message = raw_input("Enter your message >> ")
    # print(morph.normal_forms(message))

    if message == "quit":
        print ("Bye")
        exit()
    else:
        tryparse = message.decode('utf-8').lower().encode('utf-8').replace(' ', '').split("от")
        if tryparse[0] == "образуйнормальнуюформу":
            print(morph.normal_forms(tryparse[1].decode('utf-8'))[0].encode('utf-8'))
        else:
            print (kernel.respond(message))