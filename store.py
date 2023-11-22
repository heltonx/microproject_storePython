
def buy():

    option = '1'
    total = 0
    while True :
        if option == '1':
            value = int (input ("type the value of the product" ) )
            total = total + value
        elif option == '2':
            break
        else:
            print ( "opcao invalida" )
        option = input ( "Keep buying - 1; get out - 2: " )

    print ( total )

def main() :
    buy()

if __name__ == "__main__":
    main()
    
