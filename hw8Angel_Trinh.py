def make_sandwich (*ingredients):
    """Summary of the ordered sandwich"""
  
    print("\nMaking a sandwich with the following ingredients:")
    for ingredient in ingredients:
        print(f"-{ingredient}")

make_sandwich('bread','turkey', 'avocado','lettuce','cheese','mayo')
make_sandwich('bread','meatballs', 'mozzarella cheese','olives','lettuce')


