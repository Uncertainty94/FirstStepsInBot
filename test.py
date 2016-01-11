import aiml

# Create the kernel and learn AIML files
kernel = aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("load aiml b")
kernel._brain._botName="Melody"
print(kernel._brain._botName)

# Press CTRL-C to break this loop
while True:
    # print kernel.respond(raw_input("Enter your message >> "))
    message = raw_input("Enter your message >> ")
    if message == "quit":
        print ("Bye")
        exit()
    print (kernel.respond(message))