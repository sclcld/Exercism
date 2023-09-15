
def roman(number):  
    
    if number>=1000:
        unit=number%10
        ten=(number%100)//10
        hundred=(number%1000)//100  
        thousand=number//1000
        roman_units=units(unit)
        roman_tens=tens(ten)        
        roman_hundreds=hundreds(hundred)
        roman_thousands=thousands(thousand)
        return roman_thousands+roman_hundreds+roman_tens+roman_units
    elif number>=100:
        unit=number%10
        ten=(number%100)//10
        hundred=number//100
        roman_units=units(unit)
        roman_tens=tens(ten)               
        roman_hundreds=hundreds(hundred)
        return roman_hundreds+roman_tens+roman_units  
    elif number>=10:
        ten=number//10
        unit=number%10
        roman_units=units(unit)
        roman_tens=tens(ten)        
        return roman_tens+roman_units        
    elif number<10:
        roman_units=units(number)
        return roman_units    

def units(number):
    to_ret=""
    if number<4:
        for index in range(number):
            to_ret=to_ret+"I"            
    elif number==4:
        to_ret= "IV"
    elif number>=5 and number<9:
        to_ret="V"
        if number>5:
            number_range=number-5
            for index in range(number_range):
                 to_ret=to_ret+"I"
    elif number==9:
        to_ret="IX"
    return to_ret
    
def tens(ten):
    to_ret=""
    if ten<4:
        for index in range(ten):
            to_ret=to_ret+"X"            
    elif ten==4:
        to_ret= "XL"
    elif ten>=5 and ten<9:
        to_ret="L"
        if ten>5:
            ten_range=ten-5
            for index in range(ten_range):
                 to_ret=to_ret+"X"
    elif ten==9:
        to_ret="XC"
    return to_ret                       

def hundreds(hundred):    
    to_ret=""
    if hundred<4:
        for index in range(hundred):
            to_ret=to_ret+"C"            
    elif hundred==4:
        return "CD"
    elif hundred>=5 and hundred<9:
        to_ret="D"
        if hundred>5:
            hundred_range=hundred-5
            for index in range(hundred_range):
                 to_ret=to_ret+"C"
    elif hundred==9:
        return "CM"
    return to_ret                       

def thousands(thousand):    
    to_ret=""
    for index in range(thousand):
        to_ret=to_ret+"M"            
    return to_ret                       
    
    