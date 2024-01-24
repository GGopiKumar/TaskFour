'''
Author : G Gopi Kumar
Date : 24/01/2024

Program : 1)Create a Python Class called Circle with Constructor which will take a 
List as an argument for the task. The List is [10, 501, 22, 37, 100, 999, 87, 351)
2)Create proper member variables inside the task if required and use them when necessary. 
For example for this task create a class private variable named pl = 3.141
3)From the given List create two class Methods Area and Perimeter which will be going to calculate the Area and Perimeter.

Logic : Here i have created a class name circle which contain one private variable , Constructor , 2 Class method to calculate 
the area and permiter of the area and using for loop i have created object for the given list in the main function
'''

# define a class named Circle
class Circle:


    # private class variable
    __pi = 3.14


    # constructor
    def __init__(self, radius):
        self.radius = radius


    # class method for area 
    def area_of_circle(self):
        area = self.__pi * self.radius * self.radius
        return area


    # class method permiter for circle
    def perimeter_of_circle(self):
        perimeter = 2 * self.__pi * self.radius
        return perimeter
   

if __name__ == "__main__":   
   Radius_list = [10, 501, 22, 37, 100, 999, 87, 351] 
   for radius in Radius_list:
    circle = Circle(radius)
    print("The Radius of the Circle is : " + str(radius))
    print("The area of the circle is : " + str(circle.area_of_circle()))
    print("The perimeter of the circle is : " + str(circle.perimeter_of_circle()))
    print("-" * 25)


'''
Author : G Gopi Kumar
Date : 24/01/2024

Program : convert the UML diagram of TV into a Python Class and its methods

'''
class TV:
    def __init__(self, brand):
        #Below are the properties of the TV Mentioned in the UML diagram 
        self.brand = brand
        self.channel = 1
        self.price = None  
        self.inches = None  
        self.on_off_status = True
        self.volume = 50

    def increase_volume(self):
        #Volume Can't never be above 100 so using if conditon if volume incraesed above 100 then setting it to 100 only and returning false
        if self.volume > 100:
            self.volume = 100
            return False
        return True
    def decrease_volume(self):
        #Volume Can't never be below 0 so using if conditon if volume decresed below 0 then setting it to 0 only and returning false
        if self.volume < 0:
            self.volume = 0
            return False
        return True

    def set_channel(self, channel):
        #Channel has default have 1 and max value 50 so used below if condition
        if 1 <= channel <= 50:
            self.channel = channel

    def reset_tv(self):
        self.channel = 1
        self.volume = 50

    def get_status(self):
        return self.brand + " at channel " + str(self.channel) + ", volume " + str(self.volume)


class LedTV(TV):
    def __init__(self, brand, screen_thickness, energy_usage, lifespan, refresh_rate):
        super().__init__(brand)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate
        self.viewing_angle = None  
        self.backlight = None 
        
    def display_details(self):
        return (
                "Screen Thickness: " + str(self.screen_thickness) + ", " +
                "Energy Usage: " + str(self.energy_usage) + ", " +
                "Lifespan: " + str(self.lifespan) + ", " +
                "Refresh Rate: " + str(self.refresh_rate) + ", " +
                "Viewing Angle: " + str(self.viewing_angle) + ", " +
                "Backlight: " + str(self.backlight)
                )


class PlasmaTV(TV):
    def __init__(self, brand, screen_thickness, energy_usage, lifespan, refresh_rate):
        super().__init__(brand)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate
        self.display_details = None  

    def display_details(self):
       return (
                "Screen Thickness: " + str(self.screen_thickness) + ", " +
                "Energy Usage: " + str(self.energy_usage) + ", " +
                "Lifespan: " + str(self.lifespan) + ", " +
                "Refresh Rate: " + str(self.refresh_rate) + ", " +
                "Display Details: " + str(self.display_details)
            )





