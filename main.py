MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_suficiente (order_ingredients):
    """Devolver True cuando la orden se puede realizar y falso cuando no hay suficiente dinero"""
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Lo siento no hay suficiente {item} ")
            is_enough = False
    return is_enough

def process_coins():
    """Devolver el total de las monedas introducidas"""
    print("Por favor inserta monedas")
    total = int(input("Cuantos cuartos?")) * 0.25
    total += int(input("Cuantos dimes?")) * 0.1
    total += int(input("Cuantos nickles?")) * 0.05
    total += int(input("Cuantos pennies?")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    """Devolver True cuando el pago es aceptado o False cuando el dinero es insuficiente"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Aqui tienes tus {change} de cambio ")
        global profit
        profit += drink_cost
        return True
    else:
        print("Lo siento no tienes suficiente dinero para realizar la transaccion")
        return False

def make_coffe(drink_name, order_ingredients):
    """Esta funcion reduce los ingredientes a medida que se van consumiendo"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Aqui tienes tu {drink_name} ☕️")


is_on = True

while is_on:
    choice = input ( "Que tipo de cafe quieres? ( espresso / latte / cappuccino)")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water:{resources ['water']} ml ")
        print(f"Milk: {resources ['milk'] }ml")
        print(f"Coffe: {resources['coffee'] }ml")
        print (f"Money: {profit} ")

    else:
        drink = MENU [choice]
        if is_resource_suficiente(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
               make_coffe(choice, drink ["ingredients"])










#espresso = "50ml water", "18gcafe" price 1,50

#latte = "200ml water", "24gcafe", "150ml milk" price 2,50

#Cappuccino = "250ml water", "24gcafe", "100ml milk" price 3,00


#Suministros

    #water = 300 ml
    #milk = 200 ml
    #cafe = 100g

#Coin operator

    #penny = 0,01
    #dime = 0,1
    #nickel = 0,05
    #quarter = 0,25


# TODO 1 - print record ( cuanta leche queda, cuanto cafe queda etc=

# TODO 2 - Mirar que los recursos que se piden son suficientes checkear si no lo es.

# TODO 3 - Procesar las monedas.
    # cuantos penny
    # cuentos dime
    # cuantos nickel
    # cuantos quarter

# TODO 4 - Checkear que la transaccion fue exitosa.ç
    # si no es dinero suficiente devolverle el dinero.
    # si es suficiente decirle que la transaccion fue exitosa.


