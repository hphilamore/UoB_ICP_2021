def new_item():
    with open('price_per_item.csv', 'r+') as file:
        print(file.read()) 
        new_item = input('Enter new food item: ')
        new_price = input('Enter new price: ')
        file.write(new_item + ',' + new_price + '\n')
        file.seek(0)
        print(file.read())
