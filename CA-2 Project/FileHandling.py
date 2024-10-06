def LoadData():
    try:
        file = open('users.csv', 'r')
        header = file.readline().split(',')
        users = []
        for line in file:
            values = line.split(',')
            user = {}
            for i in range(len(header)):
                user[header[i]] = values[i]
            users.append(user)
        file.close()
        return users
    except FileNotFoundError:
        return []

def SaveData(users):
    file = open('users.csv', 'w')
    file.write('Username,EmailAddress,PhoneNumber,SecurityQuestion,SecurityAnswer,Wpassword\n')
    for user in users:
        line = f"{user['Username']},{user['EmailAddress']},{user['PhoneNumber']},{user['SecurityQuestion']},{user['SecurityAnswer']},{user['Wpassword']}\n"
        file.write(line)
    file.close()



