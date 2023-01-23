def to_roman(n):
    
    roman_numerals = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I"
    }

   
    result = ""
    for value, numeral in roman_numerals.items():
        while n >= value:
            result += numeral
            n -= value

    return result


while True:
    input_str = input("Enter a number or array of numbers (1-3999): ")
    if input_str.isdigit():
        # Tek sayı girişi için
        input_int = int(input_str)
        if 1 <= input_int <= 3999:
            print(to_roman(input_int))
            break
        elif input_int<=0 and input_int>3999 :
            print("Number must be between 1 and 3999. Please try again.")
            
        else:
            print("Number must be between 1 and 3999. Please try again.")
    elif input_str==str(input_str) :
        print("Number must be between 1 and 3999. Please try again.")
    else:
        None