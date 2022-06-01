import json

fruits = int(input('number of fruits: '))
fruits_name = [input(f'name of fruit according to number {i + 1}: ') for i in range(fruits)]
fruits_price = [float(input(f'fruits price {froutName}: ')) for froutName in fruits_name]
fruit_dictionary = dict(zip(fruits_name, fruits_price))

if (__name__ == '__main__'):
    print(fruit_dictionary)

    fruits_json = json.dumps(fruit_dictionary)
    with open('fruit.json', 'w') as f:
        f.write(fruits_json)
