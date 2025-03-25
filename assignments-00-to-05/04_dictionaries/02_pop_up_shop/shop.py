def main():

    fruit_prices = {
        'apple': 1.5,
        'durian': 50,
        'jackfruit': 80,
        'kiwi': 1,
        'rambutan': 1.5,
        'mango': 5
    }
    
    total_cost = 0 


    for fruit, price in fruit_prices.items():
        quantity = int(input(f"How many {fruit}s do you want to buy?: "))
        total_cost += quantity * price

    print(f"\nTotal cost of your purchase is: ${total_cost:.2f}")


if __name__ == '__main__':
    main()