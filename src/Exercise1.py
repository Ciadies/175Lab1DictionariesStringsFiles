'''
Created on Jan. 15, 2024
Process mary's order at bluebell 
@author: Sebastian
'''
#Bluebell
prices = {
    "daffodil":0.35,
    "tulip":0.33,
    "crocus":0.25,
    "hyacinth":0.75,
    "bluebell":0.50
    }

mary_order = {
    "daffodil":50,
    "tulip":100
    }

def main():
    prices["tulip"] = float('{:.2f}'.format(prices["tulip"]*1.25)) 
    mary_order["hyacinth"] = 30
    
    mary_list = []
    
    for entry in mary_order: #convert to list so I can sort it
        mary_list.append(entry)
        
    mary_list.sort()
    
    total = 0
    bulbs = 0
    
    print("You have purchased the following bulbs:")
    
    for entry in mary_list: #use the sorted mary_list since it contains the indexes of everything in mary_order
        print("%-5s *%4s = $%6.2f"%(entry[0:3].upper(), mary_order[entry], prices[entry] * mary_order[entry]))
        total += prices[entry] * mary_order[entry] #increase the price total
        bulbs += mary_order[entry] #increase count of bulbs purchased 
    
    print(f"Thank you for purchasing %s bulbs from Bluebell Greenhouses.\nYour total comes to $ %6.2f." % (bulbs,total))
    
if __name__ == "__main__":
    main()