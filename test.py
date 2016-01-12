import aiml
import pymorphy2

# Create the kernel and learn AIML files
kernel = aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("load aiml b")
kernel.setBotPredicate("name", "Melody")

morph = pymorphy2.MorphAnalyzer()

print(morph.normal_forms("ежи"))


# while True:
#     message = raw_input("Enter your message >> ")
#     if message == "quit":
#         print ("Bye")
#         exit()
#     print (kernel.respond(message))