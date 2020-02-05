import sys
# superglobals
ERROR_FILE = open('error_log.txt', 'a')
def get_number_input(prompt):
    '''
    Use prompt to collect input and return float
    '''

    #initialize value
    value = None
    while type(value) != float:
        try:
            value = float(input(prompt))
            return value

        except KeyboardInterrupt:
            exit()

        except ValueError as e:
            print("Invalid input!!! Input should be number")
            print(e, file=ERROR_FILE)

def  main():
    while True:
        client_name = input('what is the customer\'s name?: ')


        if client_name == '':
            break
        while True:
            product_name = input('what is the product name?: ')
            if product_name == "":
                break
            product_qty = get_number_input(f'How many {product_name} purchased?: ')

            product_price = get_number_input(f'How much is one unit of {product_name}?: ')

if __name__  == '__main__':
    # superglobals
    ERROR_FILE = open('error_log.txt', 'a')

    #the main code
    main()

    ERROR_FILE.close()