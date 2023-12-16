filename = 'info.txt'
def write(name, age, sex, phone):
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(name + '|' +  age + '|' + sex + '|' + phone + '\n')

def read():
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            if line.strip():
                name, age, sex, phone = line.split('|')
                print(f'Name: {name}')
                print(f'Age: {age} years')
                print(f'Sex: {"Male" if sex == "M" else "Female"}')
                print(f'Phone: {phone}')

def obtain_by_name(name_interested):
    while name_interested.isdigit():
        name_interested = input('Name cannot be a number, try again: ')
    
    name_interested_list = []
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            if line.strip():
                name, age, sex, phone = line.split('|')
                if name_interested.upper() in name.upper():
                    unique_register_by_name = []
                    unique_register_by_name.append(name)
                    unique_register_by_name.append(age)
                    unique_register_by_name.append(sex)
                    unique_register_by_name.append(phone)

                    name_interested_list.append(unique_register_by_name)

    return name_interested_list

def obtain_by_sex(sex_interested):
    while sex_interested.upper() != 'M' and sex_interested.upper() != 'F':
        sex_interested = input('Sex must be F or M: ').upper()
    sex_interested_list = []

    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            if line.strip():
                name, age, sex, phone = line.split('|')
                if sex_interested.upper() == sex:
                    unique_register_by_sex = []
                    unique_register_by_sex.append(name)
                    unique_register_by_sex.append(age)
                    unique_register_by_sex.append(sex)
                    unique_register_by_sex.append(phone)

                    sex_interested_list.append(unique_register_by_sex)
    
    return sex_interested_list

def obtain_info():  
    while True:
        name = input('Name: ').capitalize()      
        while name.isdigit() and name != '0':
            name = input('Name cannot be a number, try again: ').capitalize()
        while name == '':
            name = input('Name entry empty, try again: ').capitalize()
        if name == '0':
            break
        age = input('Age: ')
        while not age.isdigit():
            age = input('Age must be a integer: ')
        sex = input('Sex: ').upper()
        while sex != 'F' and sex != 'M':
            sex = input('Sex must be F or M: ').upper()
        phone = input('Phone: ')
        while not phone.isdigit():
            phone = input('Phone must be a integer: ')

        write(name, age, sex, phone)
        
#Tete da funçao read
#read()

#Teste de cadastro de pessoas
# obtain_info()

# Teste na buca por sexo
# results_by_sex = obtain_by_sex('m')
# if len(results_by_sex) != 0:
#     for count, item in enumerate(results_by_sex, start=1):
#         print(f'Person {count}: \n') 
#         print(f'Name: {item[0]}')
#         print(f'Age: {item[1]}')
#         print(f'Sex: {item[2]}')
#         print(f'Phone: {item[3]}')
# else:
#     print('No records have been registered with this gender...')

# Teste na busca por nome        
# results_by_name = obtain_by_name('th')
# if len(results_by_name) != 0:
#     for count, item in enumerate(results_by_name, start=1):
#         print(f'Name: {item[0]}')
#         print(f'Age: {item[1]}')
#         print(f'Sex: {item[2]}')
#         print(f'Phone: {item[3]}')
# else:
#     print('No nome detected.')