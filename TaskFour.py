# define a class named Circle
class Circle:


    # class variable
    __pi = 3.14


    # constructor
    def __init__(self, radius):
        self.radius = radius


    # instance method
    def area_of_circle(self):
        area = self.__pi * self.radius * self.radius
        return area


    # instance method
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
