'''
Created on Jan. 15, 2024

@author: Sebastian
'''

def line_to_list(lines):
    '''
    Takes in a list of lines containing the details of an earthquake and returns it in the form of a list
    eg.
    2.8 2006/10/19 02:02:10 62.391 -149.751 15.0 CENTRAL ALASKA
    returns [2.8, 2006/10/19, 02:02:10, 62.391, -149.751, 15.0, 'CENTRAL', 'ALASKA']
    '''
    list = []
    for line in lines:
        line = line.strip()
        list.append(line.split(" "))
    return list

def main():
    filename = 'earthquake.txt'
    with open(filename, 'r') as file:
        lines = file.readlines()
        
    data_list = line_to_list(lines)
    data_dict = {}    
    
    for entry in data_list:
        if entry[-1] in data_dict:
            data_dict[entry[-1]].append([entry[1], entry[0]]) #appends the list to an already existing entry
        else: #creates an entry if one does not currently exist
            data_dict[entry[-1]] = [] #appends the list to the newly created entry
            data_dict[entry[-1]].append([entry[1], entry[0]])
            
    for item in data_dict :#writes the entry
        to_write = [item] #adds the dictionary key to the start of the list
        
        for entry in data_dict[item]: #appends each list associated the corresponding dictionary key
            to_write.append(entry)
            
        with open("earthquakefmt.txt", "a") as text: 
            text.write(f"{str(to_write)}\n\n")
            
if __name__ == "__main__":
    main()