from tareas import see_task, add_task, delete_task
def printed_menu():
    print ("---MENU---")
    print ("1. Ver tareas")
    print ("2. Añadir tarea")
    print ("3. Eliminar tarea")
    print ("4. Mostrar Menu")
    print ("5. Salir")

def choices():
    tasks = [] #aquí se guardan las tareas que el usuario anote
    choice = "0" #defino la variable choice para activar el bucle a continuación
    while choice != "5":
       
        choice = input("Elige una opción: ") #modifica choice y sigue el script       
        if choice == "1":
            see_task(tasks) #activa la funcion see_task(), una vez leida, se reinicia el bucle
        elif choice == "2":
            add_task(tasks)      
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            printed_menu()
        elif choice == "5":
            print ("Has salido") #como choice es "5", nada más imprimir esto se reinicia el bucle, pero como choice == 3, se sale del bucle y el programa termina (no hay nada más que hacer).
        else:
            print ("Opción no válida. Inténtalo de nuevo.")

printed_menu()
choices()