from curses.ascii import HT
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404,reverse
from django.http import HttpResponse
from django.contrib import messages
from django.conf import settings
from django.template import loader
from django.shortcuts import render
from django.core.mail import EmailMessage
from django.utils.crypto import get_random_string
from matplotlib.style import context
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Users\suresh\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
from PIL import Image
import cv2
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import imutils
import numpy as np
import easyocr
from adminapp.models import *
from .models import*
import imageio as iio

def police_home(request):
    return render(request, './police/police-home.html')

def upload_challan(request):
    obje = Fines.objects.all()
    
    try :
        obj1 = Vechile_Register.objects.get(vechile_number=request.session["surya"]) 
        if obj1 is None:
            messages.error(request, "Can Not Find The Vehile")
        else:
            context = {
                'view': obj1,
                'view1':obje
            }
    except:
        context={

        }
        if request.method == "POST" and request.FILES["image"] :
            demo = request.FILES['image']
            demo1 = "C:/Users/suresh/Desktop/projects/pro-7/img/"
            file_name = f'{demo}'
            print(file_name)
            img = cv2.imread(demo1+ f'{demo}')
            img_cv = cv2.imread(demo1+ f'{demo}', 0)
            bfilter = cv2.bilateralFilter(img_cv, 11, 17, 17) #Noise reduction
            edged = cv2.Canny(bfilter, 30, 200) #Edge detection
            # plt.imshow(cv2.cvtColor(edged, cv2.COLOR_BGR2RGB))
            
            # window_name2 = "p-image2"
            # cv2.imshow(window_name2, edged)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()
            keypoints = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            contours = imutils.grab_contours(keypoints)
            contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]
            location = None
            for contour in contours:
                approx = cv2.approxPolyDP(contour, 10, True)
                if len(approx) == 4:
                    location = approx
                    break
            mask = np.zeros(img_cv.shape, np.uint8)
            new_image = cv2.drawContours(mask, [location], 0,255, -1)
            new_image = cv2.bitwise_and(img, img, mask=mask)
            # window_name3 = "p-image3"
            # cv2.imshow(window_name3, new_image)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()
            (x,y) = np.where(mask==255)
            (x1, y1) = (np.min(x), np.min(y))
            (x2, y2) = (np.max(x), np.max(y))
            cropped_image  = img_cv[x1:x2+1, y1:y2+1]
            # window_name4 = "image4"
            # cv2.imshow(window_name4, cropped_image )
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()
            # text = tess.image_to_string(new_image)
            # print(text)
            reader = easyocr.Reader(['en'])
            result = reader.readtext(cropped_image, detail = 0)
            view = (' '.join(result))
            v = view.replace(" ", "")
            request.session["demo"] = v
            print(v)
            try:
                data = Vechile_Register.objects.get(vechile_number=request.session["demo"])
               
                context={
                'view' : data,
                'file_name' : file_name,
                'view1':obje
                }   
            except:
                f1 = get_details(request)
                context={
                    'view': f1
                }
            # f1 = get_details(request)
            # print(f1.vechile_number)
            # context={
            #     'view' : "pending",
                
            # }
    
    return render (request, './police/upload-challan.html', context=context)

def get_details(request):
    try:
        if request.method == "POST":
            num = request.POST['num']
            try:
                Vechile_Register.objects.get(vechile_number=num).exists()
                messages.error(request, "We Can Not Find Vechile")
                print("1")
                return redirect("upload_challan")
            except:
                request.session["surya"] = num
                return redirect("upload_challan")
        else:
            pass
    except:
        messages.error(request, "We Can Not Process Pls Enter Number")
        surya= "pending"
    return surya
   

def post(request):
    if request.method == "POST" and request.FILES["f-image"] :
        fname = request.POST['fname']
        lname = request.POST['lname']
        v_type = request.POST['v_type']
        v_year = request.POST['v_year']
        v_make = request.POST['make'] 
        v_color = request.POST['v_color']
        v_num = request.POST['v_num']
        causes = request.POST['fine']
        image = request.FILES["f-image"] 
        data1 = Fines.objects.get(title=causes)
        data = V_Fines.objects.create(user_name=fname, user_lastname=lname, vechile_type=v_type,
        vechile_year=v_year, vechile_make=v_make, vechile_color=v_color,vechile_number=v_num,
        causes=causes, vechile_image=image, user = data1)
        data.save()
        messages.success(request, "successfuly Uploaded")
        try:
            del request.session["surya"]
        except:
            pass
    return redirect("upload_challan")


def cancel(request):
    try:
        del request.session["surya"]
    except:
        del request.session["demo"]
    return redirect("upload_challan")

def p_logout(request):
    return redirect("home")





# def dami(request):
#     obje = Fines.objects.all()
#     try :
#         data = Vechile_Register.objects.get(vechile_number = request.session["data"])
#         image = request.session["image"]
#         print(image)
#         context = {
#             'view':data,
#             'view1':obje,
#             'image':image
#         }
#     except:
#         context={
#             'view': "pending"
#         }
    
#     return render (request, './police/dami.html', context=context)

# def view_details(request): 
    
#     if request.method == "POST" and request.FILES["f-image"] :
#         demo = request.FILES['f-image']
#         demo1 = "C:/Users/suresh/Desktop/projects/pro-7/img/"
#         file_name = f'{demo}'
#         print(file_name)
#         request.session["image"] = f'{demo}'
#         img = cv2.imread(demo1+ f'{demo}')
#         img_cv = cv2.imread(demo1+ f'{demo}', 0)
#         bfilter = cv2.bilateralFilter(img_cv, 11, 17, 17)
#         edged = cv2.Canny(bfilter, 30, 200)
#         keypoints = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#         contours = imutils.grab_contours(keypoints)
#         contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]
#         location = None
#         for contour in contours:
#             approx = cv2.approxPolyDP(contour, 10, True)
#             if len(approx) == 4:
#                 location = approx
#                 break
#         mask = np.zeros(img_cv.shape, np.uint8)
#         new_image = cv2.drawContours(mask, [location], 0,255, -1)
#         new_image = cv2.bitwise_and(img, img, mask=mask)
#         (x,y) = np.where(mask==255)
#         (x1, y1) = (np.min(x), np.min(y))
#         (x2, y2) = (np.max(x), np.max(y))
#         cropped_image  = img_cv[x1:x2+1, y1:y2+1]
#         reader = easyocr.Reader(['en'])
#         result = reader.readtext(cropped_image, detail = 0)
#         view1 = (' '.join(result))
#         v = view1.replace(" ", "")
#         print(v)
#         request.session["data"] = v
      
#     return redirect ("dami")


# def cancel1 (request):
#     del request.session["data"]
#     del request.session["image"]
#     return redirect ("dami")