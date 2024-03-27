class Contact:
    def __init__(self, name, surname, number, ):
        self.name = name
        self.surname = surname
        self.number = number
        
    def saved():
        print("CONTACTS SAVED: ", end="")
        for j in range(0, len(address_book)):
            print(j, address_book[j].name)
            
    
    def isempty(list):
        if len(list)==0:
            print("NO CONTACT SAVED")
            return True
        return False
        
    def edit_name(self, name):
        self.name = name
        return self.name
    
    def edit_surname(self, surname):
        self.surname = surname
        return self.surname
    
    def edit_number(self, number):
        self.number = number
        return self.number
    
    
class Contact_book(Contact):
    def __init__(self, name, surname, number):
        super().__init__(name, surname, number)
        
    def add( name, surname, number):
        return (name, surname, number)
    
    def summary(index =0):
        if index ==0:
            for j in range(0, len(address_book)):
                print(address_book[j].name, address_book[j].surname, end='/')
                print(address_book[j].number, '/',)
                
            else:
                print(address_book[index].name, address_book[index].surname, end='/')
                print(address_book[index].number,)
            print()
            return None
        

    

address_book = []
msg_error = "{}Invalid option{}".format 

access = input('Press any key to access')

while True:
    print('=CONTACTS MENU=')
    print("""[ 1 ] ADD    [ 3 ] DELETE     [ 5 ] VIEW ALL
    [ 2 ] MODIFY    [ 4 ] VIEW   [ 0 ] FINISH""")

    option = input('>>> ')

    if not option.isnumeric():
        print(msg_error)
        continue
    elif option not in '012345':
        print(msg_error)
        continue

    else:
        option = int(option)
    
    if option ==0:
        print(">>>Program ended\n")
        break
    
    elif option ==1:
        name = input("Name").capitalize().strip()
        surname =input("surname").capitalize().strip()
        number = input("Number: ").strip()
    
        address_book.append(Contact_book.add(name, surname,number))
        print("Contact Saved\n")
    
    elif option == 2:
        if Contact.isempty(address_book):
            continue
        
        Contact.saved()
        name_index = int(input("Modify which name ?"))
        print("Modify which entry ?")
        entry_index = int(input("[1]NAME [2]SURNAME [3]NUMBER\n"))


        if entry_index == 1:
          modification = input('New name: ').capitalize().strip()
          address_book[name_index].edit_name(modification)
          
        elif entry_index == 2:
          modification = input('New surname: ').capitalize().strip()
          address_book[name_index].edit_surname(modification)
          
        elif entry_index == 3:
          modification = input('New number: ').strip()
          address_book[name_index].edit_number(modification)
          
          # Delete a contact
        elif option == 3:
            if Contact.isempty(address_book):
                continue

            Contact.saved()
            name_index = int(input('\nWhich contact delete? '))
            del address_book[name_index]
            print('Contact deleted')
            
          # View specific contact details
        elif option == 4:
            if Contact.isempty(address_book):
                continue

            Contact.saved()
            index = int(input('\nContact position: '))
            Contact.summary(index)

  # View details of all contacts
        elif option == 5:
            if Contact.isempty(address_book):
                continue
            Contact.summary()


          
        

          
        





    
    
            
            
        
                