from django.shortcuts import render,redirect
from django.contrib import messages
from decimal import *
import math
from numericalunits import  m, mm, um, L, cm, mL
import pint
from .unit import *
import numpy as np



def angular_resolution(request):
    try:
    
        if request.method == "POST":
            typec = Type()
            unit = Unit()
            w = request.POST.get('w')
            ad = request.POST.get('ad')
            r = request.POST.get('r')
            
            
            given_data = request.POST['given_data']
            print(given_data)
            print("Res",w, "voltage", ad,"current", r)

            if given_data == "form1" and ad and w:
                ad = typec.type_conversion(request.POST['ad'])
                print(type(ad))
                ad_op = request.POST['ad_op']   #voltage
                print("unit is ",ad_op)         #voltage unit
                w = typec.type_conversion(request.POST['w'])   #resistance
                w_op = request.POST['w_op']
                print("unit is ",w_op)                  #resistance unit

                resistance = 0.0  #w
                voltage = 0.0   #ad
                if(ad_op == "m"):
                    voltage = ad
                elif(ad_op == "mm"):
                    voltage = ad*0.001
                elif(ad_op == "km"):
                    voltage = ad*1000
                elif(ad_op == "mi"):
                    voltage = ad*1000000

                resistance = 0.0
                if(w_op == "m"):
                    resistance = w*0.001
                elif(w_op == "nm"):
                    resistance = w
                elif(w_op == "um"):
                    resistance = w*1000
                elif(w_op == "cm"):
                    resistance = w*1000000

                curr = voltage/resistance
                power = float(round((Decimal(curr)* Decimal(voltage)),2))
                powerall = {
                    "picowatt":power*1000000000000, 
                    "nanowatt" :power*1000000000,
                    "microwatt":power*1000000,
                    "kilowatt":power*0.001,
                    "megawatt":power*0.000001,
                    "gigawatt":power/1000000000,
                    "terawatt":power/1000000000000,
                    "petawatt":power/1000000000000000,
                }

                flag="form1"
                context = {
                    "w":w,
                    "res":resistance,
                    "vol":voltage,
                    "flag":flag,
                    "power":power,
                    "powerall":powerall,
                    'given_data':given_data

                }

                return render(request,"Physics/angular_resolution.html",context)

                
            elif given_data == "form2" and w and r:
                r = typec.type_conversion(request.POST['r'])  #current
                r_op = request.POST['r_op']   #current unit
                w = typec.type_conversion(request.POST['w'])
                w_op = request.POST['w_op']   #resistance unit

                r, text_r = unit.check('rad',r,r_op,' resolution')
                w, text_w = unit.check('m',w,w_op,'Wavelength')

                text_aperture_diameter = f"1.22 * {w} / {r}"
                ad = 1.22 * w / r
                
                resistance = 0.0   #w
                if(w_op == "m"):
                    resistance = w*0.001
                elif(w_op == "nm"):
                    resistance = w
                elif(w_op == "um"):
                    resistance = w*1000
                elif(w_op == "cm"):
                    resistance = w*1000000

                current = 0.0     #r
                if(r_op == 'rad'):
                    current = r
                elif(r_op == 'deg'):
                    current = r*0.001
                elif(r_op == 'gon'):
                    current = r*0.000001
                

                vol = resistance*current
                power = int(current*vol)

                powerall = {
                    "picoowatt":power*1000000000000, 
                    "nanowatt" :power*1000000000,
                    "microwatt":power*1000000,
                    "kilowatt":power*0.001,
                    "megawatt":power*0.000001,
                    "gigawatt":power/1000000000,
                    "terawatt":power/1000000000000,
                    "petawatt":power/1000000000000000,
                    }


                r = unit.conversion(r_op,r,'rad')
                w = unit.conversion(w_op,w,'m')

                context = {
                    "w":w,
                    "res":resistance,
                    "power":power,
                    "powerall":powerall,
                    'given_data':given_data

                }

                return render(request,"Physics/angular_resolution.html",context)

            elif given_data == "form3" and ad and r:
                ad = typec.type_conversion(request.POST['ad'])
                ad_op = request.POST['ad_op']
                r = typec.type_conversion(request.POST['r'])
                r_op = request.POST['r_op']

                voltage = 0.0   #ad
                if(ad_op == "m"):
                    voltage = ad
                elif(ad_op == "mm"):
                    voltage = ad*0.001
                elif(ad_op == "km"):
                    voltage = ad*1000
                elif(ad_op == "mi"):
                    voltage = ad*1000000
                

                current = 0.0     #r
                if(r_op == 'rad'):
                    current = r
                elif(r_op == 'deg'):
                    current = r*0.001
                elif(r_op == 'gon'):
                    current = r*0.000001

                power = voltage*current
                powerall = {
                    "picoowatt":power*1000000000000, 
                    "nanowatt" :power*1000000000,
                    "microwatt":power*1000000,
                    "kilowatt":power*0.001,
                    "megawatt":power*0.000001,
                    "gigawatt":power/1000000000,
                    "terawatt":power/1000000000000,
                    "petawatt":power/1000000000000000,
                    }

                context = {

                    "w":w,
                    "r":r,
                    "ad":ad,
                    "power":power,
                    "powerall":powerall,
                    'given_data':given_data
                    
                    

                }

                return render(request,"Physics/angular_resolution.html",context)


            else:
                return render(request,"Physics/angular_resolution.html",{'given_data':given_data})

        
    
        else:
            return render(request,"Physics/angular_resolution.html",{'given_data':'form1'})

   
    except (ZeroDivisionError):
        if given_data == "form1" :
                context = {
                    'ad':round(ad,9),
                    'ad_op':ad_op,
                    'w':round(w,9),
                    'w_op':w_op,
                    'text_ad':text_ad,
                    'text_w':text_w,
                    'r':'NaN',
                    'text_resolution':text_resolution,
                    'given_data':given_data

                }

                return render(request,"Physics/angular_resolution.html",context)
        
        elif given_data == "form2":
            context = {
                    'r':round(r,9),
                    'r_op':r_op,
                    'ad':'NaN',
                    'w_op':w_op,
                    'text_r':text_r,
                    'text_w':text_w,
                    'w':round(w,9),
                    'text_aperture_diameter':text_aperture_diameter,
                    'given_data':given_data

                }


            return render(request,"Physics/angular_resolution.html",context)

        else:
            messages.error(request, "Can't divide by 0")
            return render(request,"Physics/angular_resolution.html",{'given_data':given_data})


    except:
        messages.error(request, "Please enter valid data")
        return render(request,"Physics/angular_resolution.html",{'given_data':given_data})