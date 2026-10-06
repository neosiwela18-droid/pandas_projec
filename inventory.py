import pandas as pd

data = {
    "location": [
        "Staten Island", "Staten Island", "Staten Island", "Staten Island",
        "Staten Island", "Staten Island", "Staten Island", "Staten Island",
        "Staten Island", "Staten Island", "Brooklyn", "Brooklyn", "Brooklyn",
        "Brooklyn", "Brooklyn", "Brooklyn", "Brooklyn", "Brooklyn", "Brooklyn",
        "Brooklyn"
    ],
    "product_type": [
        "seeds", "seeds", "seeds", "garden tools", "garden tools", "garden tools",
        "pest_control", "pest_control", "planter", "planter", "seeds", "seeds",
        "seeds", "garden tools", "garden tools", "garden tools", "pest_control",
        "pest_control", "planter", "planter"
    ],
    "product_description": [
        "daisy", "calla lily", "tomato", "rake", "wheelbarrow", "spade",
        "insect killer", "weed killer", "20 inch terracotta planter",
        "8 inch plastic planter", "daisy", "calla lily", "tomato", "rake",
        "wheelbarrow", "spade", "insect killer", "weed killer",
        "20 inch terracotta planter", "8 inch plastic planter"
    ],
    "quantity": [
        4, 46, 85, 4, 0, 93, 74, 8, 0, 53,
        50, 0, 0, 15, 82, 36, 80, 76, 5, 26
    ],
    "price": [
        6.99, 19.99, 13.99, 13.99, 89.99, 19.99, 12.99, 23.99, 17.99, 3.99,
        6.99, 19.99, 13.99, 13.99, 89.99, 19.99, 12.99, 23.99, 17.99, 3.99
    ]
}

inventory = pd.DataFrame(data)

staten_island = inventory.head(10)
product_request = staten_island['product_description']
seed_request = inventory[(inventory['location'] == 'Brooklyn') & (inventory['product_type'] == 'seeds')]
inventory['in_stock'] = (inventory['quantity'].apply(lambda x: True if x > 0 else False))

inventory['total_value'] = inventory.apply(lambda row: row.price * row.quantity,axis=1)

combine_lambda = lambda row: \
    '{} - {}'.format(row.product_type,
                     row.product_description)

inventory['full_description'] = inventory.apply(combine_lambda,axis =1)

print(inventory)
