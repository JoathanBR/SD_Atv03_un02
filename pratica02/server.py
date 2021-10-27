import Pyro4

class Server(object):
    @Pyro4.expose
    def welcomeMessage(self, name):
        certo = 0
        errado = 0
        questao = name.split(";")
        alternativa = questao[2]

        for x in alternativa:
            if(x == "V"):
                certo = certo + 1
            else:
                errado = errado + 1    
                
        return ("Questão ",questao[0], " com ", questao[1], " alternativas. Possui ", certo, " certas e ", errado, " erradas!")

def startServer():
    server = Server()
    daemon = Pyro4.Daemon()             
    ns = Pyro4.locateNS()
    uri = daemon.register(server)  
    ns.register("server", uri)   
    print("Ready. Object uri =", uri)
    daemon.requestLoop()                   

if __name__ == "__main__":
    startServer()