def see_task(tasks):
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

def add_task(tasks):
    new_task = input("Escribe una nueva tarea: ")
    tasks.append({"title": new_task, "status": "No Completada"}) #añade bibliotecas a la lista tasks
    print ("Tarea añadida")
    print("-------")
    print ("Selecciona una nueva opción.")

def delete_task(tasks):
    while True: #bucle infinito hasta que no se especifique un break que lo haga salir
        try:
            to_delete = input("Selecciona el número de la tarea a eliminar y pulse Enter:")
            tasks.pop(int(to_delete)-1)
            print ("Tarea eliminada. Seleccione una nueva opción")
            break #para salir del bucle. solo sale si se selecciona una opcion valida.
        except IndexError:
            print("Valor inválido. Por favor, seleccione un número válido")
