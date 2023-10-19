import cv2 
  
# Setting parameter values 
t_lower = 30  # Lower Threshold 
t_upper = 100  # Upper threshold 
  
# Applying the Canny Edge filter 

cap = cv2.VideoCapture(0)  # 0 for the default camera

while True:
    ret, frame = cap.read()
    
    if not ret:
        break
    
    # Detect and outline shapes
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian blur to reduce noise and improve shape detection
    blurred = cv2.GaussianBlur(gray,(5,5),cv2.BORDER_CONSTANT)
    frame1 =  cv2.Canny(blurred, t_lower, t_upper,apertureSize=3) 
    
    # Display the resulting frame
    cv2.imshow('canny', frame1)
    cv2.imshow('canny 1', blurred)
    cv2.imshow('Shape Detection', frame)
    
    if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()

