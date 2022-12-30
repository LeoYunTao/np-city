class Utlis:
    
    @staticmethod
    def get_int(input_messge):
        mmChoice = input(input_messge)
        if mmChoice.isdigit():
            mmChoice = int(mmChoice)
            return mmChoice
        
        print("Please type in an integer!")
        Utlis.get_int(input_messge)

    
