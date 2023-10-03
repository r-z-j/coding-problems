n, m = map(int, input().split())
ticket_prices = [int(i) for i in input().split()]
customer_max_prices = [int(i) for i in input().split()]

ticket_prices.sort(reverse=True)

for max_price in customer_max_prices:
    price_match = False
    for price in ticket_prices:
        if price <= max_price:
            print(price)
            ticket_prices.remove(price)
            price_match = True
            break

    if not price_match:
        print(-1)

