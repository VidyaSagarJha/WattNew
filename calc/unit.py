import pint
u = pint.UnitRegistry()
Q = u.Quantity

class Unit:
    
    def conversion(self,unit,num,u):
        distance = Q(num,u)
        num = distance.to(unit)
        return (num.magnitude)
    
   
    def check(self,conv_unit,value,unit,name):
        if unit != conv_unit:
            changed_value = self.conversion(conv_unit,value,unit)
            text = f"{name} in {conv_unit} is {changed_value}"
            return changed_value,text
        
        else:
            return value,''

    




    
class Type:  
    def type_conversion(self,num):
            if num.isdigit():
                Number = int(num)
            
            else:
                Number = float(num)

            return Number


 
 


            

