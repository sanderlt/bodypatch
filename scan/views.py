
from django.shortcuts import render, redirect
from django.core.files.base import ContentFile
from django.conf import settings

from io import BytesIO
from imageio import imread
import base64

import cv2
import numpy as np

from .forms import CanvasImageForm
from .detector import ColorDetection

c1_value = c2_value = c3_value = c4_value = 0
c5_value = c6_value = c7_value = c8_value = 0
c9_value = c10_value = c11_value = c12_value = 0
c13_value = c14_value = c15_value = c16_value = 0

def upload_canvas(request):
    if request.method == 'POST':
        form = CanvasImageForm(request.POST)
        if form.is_valid():
            # Get the base64 data from the form
            base64_data = form.cleaned_data['base64_data']

            # Decode the base64 data and save it as a PNG file
            img_data = base64_data.split(',')[1]  # Remove the data:image/png;base64 prefix

            # using https://pypi.org/project/imageio/ to read base 64data
            img = imread(BytesIO(base64.b64decode(img_data)))

            # finally convert RGB image to BGR for opencv
            img_bgr = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

            img_graph = img_bgr.copy()

            #here we can play with contour color
            img_hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)
            lower = np.array([0, 0, 0])
            upper = np.array([110, 110, 110])
            mask = cv2.inRange(img_hsv, lower, upper)

            detected_circles = cv2.HoughCircles(mask,cv2.HOUGH_GRADIENT,1,20,
                                    param1=10,param2=8,minRadius=22,maxRadius=30)

            #if amount of detected_circles is equals 4:
            if detected_circles is not None and len(detected_circles[0, :]) == 4:
                hide_results = 'display: block'
                scanning_error = False
                not_detected = ''
                # Convert the circle parameters a, b and r to integers.
                detected_circles = np.uint16(np.around(detected_circles))

                сtl = сbl = сtr = сbr = [0,0]
                for pt in detected_circles[0, :]:
                    x, y, r = pt[0], pt[1], pt[2]     # draw the outer circle

                    if x <= 100 and y <= 100:
                        сtl = [x,y] #circle top left

                    if x <= 280 and y >= 60:
                        сtr = [x,y] #circle top right

                    if x >= 100 and y >= 100:
                       сbr = [x,y] #circle bottom right

                    if x >= 100 and y <= 100:
                       сbl = [x,y] #circle bottom left

                    # Draw the circumference of the circle.
                    cv2.circle(img_graph, (x, y), r, (0, 255, 0), 2)

                    # Draw a small circle (of radius 1) to show the center.
                    cv2.circle(img_graph, (x, y), 1, (0, 0, 255), 3)

                # Create point matrix
                point_matrix = np.float32([сtl,сbl,сtr,сbr])
                # Output image size
                width, height = 360,360

                btl = [width/20, height/20]
                bbl = [width-width/20, height/20]
                btr = [height/20, width-width/20]
                bbr = [height - height/20, width-width/20]


                # Convert points
                converted_points = np.float32([btl,bbl,btr,bbr])

                # perspective transform
                perspective_transform = cv2.getPerspectiveTransform(point_matrix,converted_points)
                img_output = cv2.warpPerspective(img_bgr,perspective_transform,(width,height))

                # forensics
                cv2.imwrite(settings.MEDIA_ROOT + '/uploads/' + 'img_graph.png', img_graph)
                cv2.imwrite(settings.MEDIA_ROOT + '/uploads/' + 'img_output.png', img_output)
                cv2.imwrite(settings.MEDIA_ROOT + '/uploads/' + 'img_bgr.png', img_bgr)

                clr_values = list(ColorDetection(img_output))

            else:
                not_detected = 'The Bodypatch is not detected, please try again!'
                scanning_error = True

            if scanning_error==True:

                output_dict = {
                    'form': form,
                    'clr_results': None,
                    'hide_results': None,
                    'not_detected': not_detected,
                }
            else:
                output_dict = {
                    'form': form,
                    'clr_results': clr_values,
                    'hide_results': hide_results,
                    'not_detected': not_detected,
                }


            # Render results and form
            return render(request, 'latest.html', output_dict)

            #return redirect('scan/')  # Redirect to a success page
    else:
        form = CanvasImageForm()
    return render(request, 'latest.html', {'form': form})
