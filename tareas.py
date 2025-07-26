from archivo import saving_tasks, tasks
from datetime import datetime

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
            print (f"{i+1}. {task["title"]} -- {task["description"]} -- A completar antes del {task["deadline"]} --({task["status"]})") #por cada par índice-valor, se imprime una cadena, donde aparecerá el índice y el valor que se esté recorriendo en esa iteración.
        print("Selecciona el numero de la tarea a completar. Si no, pulsa enter: ")
        completed_task = input()
        while completed_task != "":
            try: 
                tasks[int(completed_task)-1]["status"] = "Completada"
                saving_tasks()
                print("Tarea completada")
                break
            except (ValueError,IndexError): 
                print("Selecciona una opción válida")
                completed_task = input()
        print("-------")
        print("Filtrar por Completadas:'c', Filtrar por No completadas: 'nc', Ordenar por fecha límite: 'o', Salir a menu: Enter")
        filter_tasks = input()
        if filter_tasks == "c":
            for i, task in enumerate(tasks):
                if task["status"] == "Completada":
                    print (f"{i+1}. {task["title"]} -- {task["description"]} -- A completar antes del {task["deadline"]} --({task["status"]})")
        if filter_tasks == "nc":
            for i, task in enumerate(tasks):
                if task["status"] == "No Completada":
                    print (f"{i+1}. {task["title"]} -- {task["description"]} -- A completar antes del {task["deadline"]} --({task["status"]})")
        if filter_tasks == "o":
            ordered_tasks = sorted(tasks, key=lambda t: datetime.strptime(t["deadline"], "%d/%m/%Y"))
            for i, task in enumerate(ordered_tasks):
                print (f"{i+1}. {task["title"]} -- {task["description"]} -- A completar antes del {task["deadline"]} --({task["status"]})")

        print("Selecciona una nueva acción")

def add_task():
    task_title = input("Escribe una nueva tarea: ")
    task_description = input("Escribe una descripción de la tarea: ")
    while True:
        date_input = input("Escribe la fecha limite para completar esta tarea, en formato dd-mm-aaaa (guiones incluidos): ")
        try: 
            task_deadline = datetime.strptime(date_input, "%d-%m-%Y").strftime("%d/%m/%Y")
            break
        except ValueError:
            print ("Ingrese una fecha válida en formato dd-mm-aaaa (guiones incluidos)")

    tasks.append({"title": task_title, "description": task_description, "deadline": task_deadline, "status": "No Completada"}) #añade bibliotecas a la lista tasks
    saving_tasks()
    print ("Tarea añadida")
    print("-------")
    print ("Selecciona una nueva opción.")

def delete_task():
    while True: #bucle infinito hasta que no se especifique un break que lo haga salir
        if tasks ==[]:
            print("Ninguna tarea disponible para eliminar. volviendo al menú principal")
            break
        try:
            to_delete = input("Selecciona el número de la tarea a eliminar y pulse Enter:")
            try:
                tasks.pop(int(to_delete)-1)
            except ValueError:
                print("Valor inválido. Por favor, seleccione un número válido")
                continue
            saving_tasks()
            print ("Tarea eliminada. Seleccione una nueva opción")
            break #para salir del bucle. solo sale si se selecciona una opcion valida.
        except IndexError:
            print("Valor inválido. Por favor, seleccione un número válido")

if __name__ == "__main__":
    tasks = [{"title": "correr", "description": "correr 100m", "deadline": "02/11/2025", "status": "Completada"}, {"title": "fumar mucho", "description": "fumar mucho mucho", "deadline": "02/03/2026", "status": "No Completada"},{"title": "gritar", "description": "gritR 100m", "deadline": "02/11/2027", "status": "Completada"}]
    see_task()
    while len(tasks) != 0:
        tasks.pop(len(tasks)-1)
    saving_tasks()