def calculate_density(mass, volume):
    try:
        den=mass/volume
    except ZeroDivisionError:
        return "Volume can't be zero"
    except TypeError:
        return "Invalid data type"
    except:
        return "Invalid Input"
    return den
den_value=calculate_density(2000, 'a')
print(den_value)

def calculate_bmi(weight, height):
    try:
        bmi=weight/(height**2)
    except ZeroDivisionError:
        return "Height can't be zero"
    except TypeError:
        return "Invalid data type"
    return bmi
bmi_value= calculate_bmi(75, 5)
print(bmi_value)