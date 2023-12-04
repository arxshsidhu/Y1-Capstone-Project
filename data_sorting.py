import csv #credits to a random stack overflow post with a similar issue that helped me utilize this lol, it was too confusing without it
import random 

data = []
type_data = {}
coromon_data = {}
avg_hp = {}
avg_attack = {}
avg_special_attack = {}
avg_defense = {}
avg_special_defense = {}
avg_speed = {}

#open the file and turn it into a data list
with open('CoromonDataset.csv',newline='') as file:
    lines = csv.DictReader(file)
    for row in lines:
        coromon = row['Coromon']
        type = row['Type']
        hp = row['Health Points']
        attack = row['Attack']
        special_attack = row['Special Attack']
        defense = row['Defense']
        special_defense = row['Special Defense']
        speed = row['Speed']
        stamina = row['Stamina Points']
        data.append(f'Coromon: {coromon}, Type: {type}, Health Points: {hp}, Special Defense: {special_defense}, Speed:{speed}, Stamina Points: {stamina}')
        coromon_data[row['Coromon']] = row #this adds each coromons data to coromon dict
        if row['Type'] not in type_data:
            type_data[row['Type']] = [row]
        else:
            type_data[row['Type']].append(row) #this if else saves type data to the type_data dict

#For each Common type display the average value for each of its properties across all of the Coromon that belong to that type.
#In the world of Coromon, there are 8 elemental Coromon Types: Normal, Electric, Ghost, Sand, Fire, Ice, Water, and Dark Magic.

for type, coromons in type_data.items(): 
    #the extremely repetitive definitions that definitely have a easier way to prepare averaging each property 
    hp_tot = sum(int(coromon['Health Points']) for coromon in coromons)
    attack_tot = sum(int(coromon['Attack']) for coromon in coromons)
    special_attack_tot = sum(int(coromon['Special Attack']) for coromon in coromons)
    defense_tot = sum(int(coromon['Defense']) for coromon in coromons)
    special_defense_tot = sum(int(coromon['Special Defense']) for coromon in coromons)
    speed_tot = sum(int(coromon['Speed']) for coromon in coromons)
    stamina_tot = sum(int(coromon['Stamina Points']) for coromon in coromons)
    print(f'For Type {type}:') #prepare for a tornado of yap (i am going insane but happy thanksgiving ig) prints all the averages future arash do not touch these bcs they work perfectly fine and it will take you a not o(n) amount of hours to fix it
    print(f'Average HP: {hp_tot / len(coromons)}, Average Attack: {attack_tot / len(coromons)}, Average Special Attack: {special_attack_tot / len(coromons)}, Average Defense: {defense_tot / len(coromons)},Average Special Defense: {special_defense_tot / len(coromons)},Average Speed: {special_attack_tot / len(coromons)},Average Stamina: {stamina_tot / len(coromons)}')
    avg_hp[type] = hp_tot / len(coromons)
    avg_attack[type] = attack_tot / len(coromons)
    avg_special_attack[type] = special_attack_tot / len(coromons)
    avg_defense[type] = defense_tot / len(coromons)
    avg_special_defense[type] = special_defense_tot / len(coromons)
    avg_speed[type] =speed_tot / len(coromons)

max_hp_type = max(avg_hp, key=avg_hp.get)
min_hp_type = min(avg_hp, key=avg_hp.get)
max_attack_type = max(avg_attack, key=avg_attack.get)
min_attack_type = min(avg_attack, key=avg_attack.get)
max_special_attack_type = max(avg_special_attack,key=avg_special_attack.get)
min_special_attack_type = min(avg_special_attack, key=avg_special_attack.get)
max_defense_type = max(avg_defense, key=avg_defense.get)
min_defense_type = max(avg_defense, key=avg_defense.get)
max_special_defense_type = max(avg_special_defense, key=avg_special_defense.get)
min_special_defense_type = max(avg_special_defense, key=avg_special_defense.get)
max_speed_type = max(avg_speed, key=avg_speed.get)
min_speed_type = min(avg_speed, key=avg_speed.get)

#print the min max averages jhit!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

print('|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')
#hp min max
print(f'The Coromon type with the highest average HP is {max_hp_type} with {avg_hp[max_hp_type]} points.')
print(f'The Coromon type with the lowest average HP is {min_hp_type} with {avg_hp[min_hp_type]} points.')
#attack min max
print(f'The Coromon type with the highest average Attack is {max_attack_type} with {avg_attack[max_attack_type]} points.')
print(f'The Coromon type with the lowest average Attack is {min_attack_type} with {avg_attack[min_attack_type]} points.')
#special attack min max
print(f'The Coromon type with the highest average Special Attack is {max_special_attack_type} with {avg_special_attack[max_special_attack_type]} points.')
print(f'The Coromon type with the lowest average Special Attack is {min_special_attack_type} with {avg_special_attack[min_special_attack_type]} points.')
#defense min max
print(f'The Coromon type with the highest average Defense is {max_defense_type} with {avg_defense[max_defense_type]} points.')
print(f'The Coromon type with the lowest average Defense is {min_defense_type} with {avg_defense[min_defense_type]} points.')
#special defense min max
print(f'The Coromon type with the highest average Special Defense is {max_special_defense_type} with {avg_special_defense[max_special_defense_type]} points.')
print(f'The Coromon type with the lowest average Special Defense is {min_special_defense_type} with {avg_special_defense[min_special_defense_type]} points.')
#speed min max
print(f'The Coromon type with the highest average Speed is {max_speed_type} with {avg_speed[max_speed_type]} points.')

print('|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')

print(f'Theres {len(coromon_data)} Coromons.') 
#prints the total number coromons

print('|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')

random_coromon = random.choice(list(coromon_data.values()))
print(f'Random Coromon: {random_coromon}') #prints random coromane (gucci mane reference(this is a cry for help(joke)))

print('|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')
print(f'Different types of Coromons: {list(type_data.keys())}')
#shows different types of corosdmflwakdfjmasdldfkamons

print('|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')

#print('\n'.join(data)) #to test data just untag it
