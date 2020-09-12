import json
data = {
    "SKU1001": {
        "name":"ACME Anvils",
        "cost":1200,
        "stock":5
    },
    "ABC101": {
        "name":"ACME Dynamite",
        "cost":1500,
        "stock":7
    },
    "BEN102": {
        "name":"Toilet Roll",
        "cost":10.50,
        "stock":0
    }
}

with open('inventory.json', 'w') as fp:
    json.dump(data, fp)
