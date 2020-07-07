import database as d

stop = False
passCorrect = False

while stop == False:           
    email = input("Introduce tu email: ")
    if email in d.students1.keys():
        while passCorrect == False:
            password = input("Introduce tu contraseña: ") 
            if d.students1[email] == password:
                print("Bienvenido!")
                #Ejecutar lo deseado
                passCorrect = True
                stop = True
            else: 
                print("La contraseña esta mal introducida")
    else: 
        print("El email no se encuentra en la base de datos, vuelva a intentarlo") 