class VOITURE:
    """
        This is the class to manage a car
    """

#  public
# _ private
# __ protected

    def __init__(self, color2):
        """
            Init a class with only color passed by argument
        """

        self.color = color2
        self._prixInterne = 300000
        self.__nbr_defaut = 3

 
    def clsGoToDestination(self, dest):
        """
            print where you wanna go

        """
        print("Going to " +  dest + " with a "+ self.color +" car")
        self.clsStopCar()
        

    def clsStopCar(self):
        """
            Used to stop the car
        """
        print ("STOOOOOP")

    def _clsClean(self):
        print("car is clean")


    def clsNBR_Defauts(self):
        print(self.__nbr_defaut)






myCar = VOITURE("blue")
print(myCar.color)                # Public
print(myCar._prixInterne)         # Privé (juste pour informer)
print(myCar.__nbr_defaut)         # Pas touche !!!


myCar.clsGoToDestination("Beziers")
myCar.clsStopCar()
myCar._clsClean()

