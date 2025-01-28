while True:
    try:
        MeasurementType = input("Please enter measurement type (M for Metric/I for Imperial): ")
    except (ValueError, MeasurementType != "m", MeasurementType !='i', MeasurementType != "metric", MeasurementType != "imperial") :
        print("Please provide valid input.")
        continue
    else:
        try:
            Height = float(input("Please enter your height: "))
            Weight = float(input("Please enter your weight: "))
        except ValueError:
                print("Please provide valid input.")
                continue
        else:
            if Height <= 0 or Weight <= 0:
                    print("Input cannot be 0 or less")
                    continue
            else:
                if MeasurementType == "m" or MeasurementType == "metric":
                    BMIIndex = round(Weight / (Height * Height), 2)
                    print("Your Body Mass Index is: ", BMIIndex)

                    if BMIIndex < 18.5:
                        print("Underweight.")
                    elif BMIIndex <= 24.9:
                        print("Normal.")
                    elif BMIIndex <= 29.9:
                        print("Overweight.")
                    else:
                        print("Obese.")
                
                elif MeasurementType == "i" or MeasurementType == "imperial":
                    BMIIndex = round(Weight / (Height * Height) * 703, 2)
                
                    print("Your Body Mass Index is: ", BMIIndex)

                    if BMIIndex < 18.5:
                        print("Underweight.")
                    elif BMIIndex <= 24.9:
                        print("Normal.")
                    elif BMIIndex <= 29.9:
                        print("Overweight.")
                    else:
                        print("Obese.")
            break