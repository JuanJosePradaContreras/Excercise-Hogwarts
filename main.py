#Ejercicio Sombrero seleccionador

import random

houses = {
    "Gryffindor": {"points": 0 },
    "Slytherin": {"points": 0 },
    "Hufflepuff": {"points": 0 },
    "Ravenclaw": {"points": 0 }
}

questions = [

    {
        "question": "¿Cuál es tu valor más importante?",
        "options": [
            ("A) Ser valiente", "Gryffindor"),
            ("B) Tener ambición", "Slytherin"),
            ("C) Ser leal", "Hufflepuff"),
            ("D) Ser inteligente", "Ravenclaw")
        ]
    },
    {
        "question": "¿Cómo te gustaría ser recordado?",
        "options": [
            ("A) Como un héroe", "Gryffindor"),
            ("B) Como un líder", "Slytherin"),
            ("C) Como un amigo fiel", "Hufflepuff"),
            ("D) Como un pensador", "Ravenclaw")
        ]
    },
    {
        "question": "¿Qué actividad prefieres?",
        "options": [
            ("A) Aventuras", "Gryffindor"),
            ("B) Competencias", "Slytherin"),
            ("C) Trabajar en equipo", "Hufflepuff"),
            ("D) Leer un buen libro", "Ravenclaw")
        ]
    },
    {
        "question": "Si encuentras un objeto mágico, ¿qué harías?",
        "options": [
            ("A) Usarlo para ayudar a otros", "Gryffindor"),
            ("B) Usarlo para conseguir poder", "Slytherin"),
            ("C) Usarlo para hacer nuevos amigos", "Hufflepuff"),
            ("D) Estudiarlo para aprender más", "Ravenclaw")
        ]
    },
    {
        "question": "¿Cómo manejas un desafío?",
        "options": [
            ("A) Enfrentándolo con valor", "Gryffindor"),
            ("B) Planeando estratégicamente", "Slytherin"),
            ("C) Buscando apoyo de otros", "Hufflepuff"),
            ("D) Analizando cada detalle", "Ravenclaw")
        ]
    }
]

def ask_questions():
    for q in questions:
        while True:  
            print(q["question"])
            for option in q["options"]:
                print(option[0])

            response = input("Elige una opción (A, B, C, D): ").strip().upper()
            
            
            if response in ['A', 'B', 'C', 'D']:
                for option in q["options"]:
                    if response == option[0][0]:
                        house_name = option[1]
                        houses[house_name]["points"] += 1
                        break
                break  
            else:
                print("Respuesta inválida. Por favor, solo responde A, B, C o D.")
                
def determine_house():
    max_points = max(house["points"] for house in houses.values())
    potential_houses = [house for house, info in houses.items() if info["points"] == max_points]

    if len(potential_houses) > 1:
        return random.choice(potential_houses)  # Elegir al azar en caso de empate
    else:
        return potential_houses[0]

def main():
    print("Bienvenido al Sombrero Seleccionador de Hogwarts!")
    ask_questions()
    selected_house = determine_house()
    print(f"\n¡Felicidades! Has sido asignado a la casa: {selected_house}!")

if __name__ == "__main__":
    main()