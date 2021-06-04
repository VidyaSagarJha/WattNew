from django.shortcuts import render,redirect

# Create your views here.


def check(request):
    # try:
        if request.method=="POST":
            anode = int(request.POST['anode'])
            cathode = int(request.POST['cathode'])
            a = anode
            c = cathode
            op = request.POST['operation']
            opa = request.POST['operationanode']
            opc = request.POST['operationcathode']
            
            if opa == 'mv':
                a = a*1000

            if opa == 'kv':
                a = a / 1000

            if opa == 'mv1':
                a = a / 1000000

            if opc == 'mv':
                c = c*1000

            if opc == 'kv':
                c = c / 1000

            if opc == 'mv1':
                c = c / 1000000

            result = cathode - anode
            
            if op == 'v':
                result =  result

            if op == 'kv':
                result = result / 1000

            if op == 'mv':
                result = result * 1000

            if op == 'mv1':
                result = result / 1000000


                
                    
                

           
            context = {"op":op,'a':a,'c':c,'result':result,'opc':opc,'opa':opa}
            return render(request,"home.html",context)

        else:
            return render(request,"home.html")


    # except:
    #     return render(request,"home.html")

def calc(request,anode,op,cathode):
    op=op
    a = int(anode)
    c = int(cathode)
    
    context = {"op":op,"result":result,'a':a,'c':c}
    return render(request,"home.html",context)