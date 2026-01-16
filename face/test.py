import FaceRecogniton

im=face_recognition.load_image_file("face.jpg")
face=face_recognition.face_location(im)
print("face found",len(face))