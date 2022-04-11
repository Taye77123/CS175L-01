import matplotlib

def main():
    with open('expenses.txt', 'r') as f:
        
        lines = f.readlines()
        d = dict()
        for line in lines:
            
            line = line.strip() 
            key, value = line.split(':')[0], int(line.split(':')[1])
            d[key] = value
        expenses, costs = d.keys(), d.values()
        print(expenses) 
        print(costs)    
        
