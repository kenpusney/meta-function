
#dispatcher builder
def dispatch():
    status = 0
    #some other shared variables
    while True:
        command = yield status
        print "I got command " + command
        if command == "exit ":
            status = -1
        else:
            #dispatch the command and return status
            status = 1

disp = dispatch();

#launch the dispatcher
next(disp)

cmds = ["hello",'world','hahhaha','oho','exit'];

for cmd in cmds:
    status = disp.send(cmd)
    if status < 0:
        try:
            #terminate the dispatcher
            disp.throw(Exception)
        except:
            #end the loop
            break
