levels = {
    1: "Піти на кухню",
    2: "Підійти до тумбочки",
    3: "Подивитись в телефон",
}

def show_level_select():


    print("Твій вибір:")
    for key, value in levels.items():
        print(f'{key} - {value}')

    while True:
       try:
           level_choice = int(input())
    
           if level_choice in levels:
               print(f'Ти вибрав: {level_choice}')
               break
           else:
               raise Exception()
       except:
           print("Неправильний вибір")
           
    return level_choice 