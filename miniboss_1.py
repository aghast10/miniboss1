tasks = [] #aquí se guardan las tareas que el usuario anote

def printed_menu():
    print ("---MENU---")
    print ("1. Ver tareas")
    print ("2. Añadir tarea")
    print ("3. Eliminar tarea")
    print ("4. Mostrar Menu")
    print ("5. Salir")

def choices():
    choice = "0" #defino la variable choice para activar el bucle a continuación
    while choice != "5":
       
        choice = input("Elige una opción: ") #modifica choice y sigue el script       
        if choice == "1":
            see_task() #activa la funcion see_task(), una vez leida, se reinicia el bucle
        elif choice == "2":
            add_task()      
        elif choice == "3":
            delete_task()
        elif choice == "4":
            printed_menu()
        elif choice == "5":
            print ("Has salido") #como choice es "5", nada más imprimir esto se reinicia el bucle, pero como choice == 3, se sale del bucle y el programa termina (no hay nada más que hacer).
        else:
            print ("Opción no válida. Inténtalo de nuevo.")

def see_task():
    if len(tasks) == 0:
        print("-------")
        print("No hay ninguna tarea guardada. selecciona otra opción")
        
    else:
        for i, task in enumerate(tasks):#enumerará todas las partes de la lista tasks
            print (f"{i+1}. {task["title"]} -- {task["status"]}") #por cada par índice-valor, se imprime una cadena, donde aparecerá el índice y el valor que se esté recorreindo en esa iteración.
        while True:
            completed_task = input("selecciona el numero de la tarea a completar. si no, pulse enter: ")
            try: 
                tasks[int(completed_task)-1]["status"] = "Completada"
                print("Tarea completada")
                break
            except (ValueError,IndexError): 
                print("seleccione una opción válida")
        print("-------")
        print("Selecciona una nueva acción")

def add_task():
    new_task = input("Escribe una nueva tarea: ")
    tasks.append({"title": new_task, "status": "No Completada"}) #añade bibliotecas a la lista tasks
    print ("Tarea añadida")
    print("-------")
    print ("Selecciona una nueva opción.")

def delete_task():
    while True: #bucle infinito hasta que no se especifique un break que lo haga salir
        try:
            to_delete = input("Selecciona el número de la tarea a eliminar y pulse Enter:")
            tasks.pop(int(to_delete)-1)
            print ("Tarea eliminada. Seleccione una nueva opción")
            break #para salir del bucle. solo sale si se selecciona una opcion valida.
        except IndexError:
            print("Valor inválido. Por favor, seleccione un número válido")

printed_menu()
choices()