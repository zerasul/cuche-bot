import sqlite3
from sys import argv

class Chiste:
    id=None
    autor=None
    chiste=None

    def __init__(self, id=None, autor=None, chiste=None):
        self.id=id
        self.autor=autor
        self.chiste=chiste
        pass
    def __str__(self):
        return "id: {}, autor: {}, chiste: {}".format(self.id,self.autor,self.chiste)
    def prettystring(self):
        return "{} dijo: {}".format(self.autor,self.chiste)
pass

class ChisteController:
    db=None
    def __init__(self):
        self.db=sqlite3.connect('chistes.db')
    def createSchema(self):
        self.db.execute('create table chistes(id integer PRIMARY KEY AUTOINCREMENT,autor text NOT NULL,chiste text NOT NULL)')
    def getChistes(self):
        c= self.db.execute('select * from chistes')
        chistes = c.fetchall()
        lchistes=[]
        for cchiste in chistes:
            chiste = Chiste(cchiste[0],cchiste[1],cchiste[2])
            lchistes.append(chiste)
        return lchistes
    def createChiste(self,autor, chiste):
        row =((autor,chiste))
        self.db.execute('insert into chistes(autor,chiste)values(?,?)',row)
        self.db.commit()
    def delChiste(self, id):
        row=((id))
        self.db.execute('delete from chistes where id=?',row)
        self.db.commit()
def printhelp():
    print("Uso Python cuehchistescontroller.py <comando> <parametros>")
    print("<comando> : createschema (No requiere parametros), insertchiste( requiere 2 parametros autor y chiste)")
    exit(0)
    
def main():
    controller= ChisteController()
    if len(argv)<=1:
        printhelp()
    else:
        command=argv[1]

    if command == 'createschema':
        controller.createSchema()
    elif command == 'insertchiste':
        if(len(argv)<3):
            print('Error; faltan parametros')
            printhelp()
        controller.createChiste(argv[2],argv[3])
    elif command == 'getchistes':
        print(controller.getChistes())
    elif command == 'delchiste':
        if len(argv)<2 :
            print('Error, faltan parametros')
            printhelp()
        id= argv[2]
        controller.delChiste(id)
    else:
        printhelp()
        
if __name__ == '__main__':
    main()