import face_recognition
image_of_gates = face_recognition.load_image_file('./img/known/bill-gates.jpg')
gates_face_encoding = face_recognition.face_encodings(image_of_gates)[0]

unknown_image = face_recognition.load_image_file('./img/unknown/iphone360_236749.jpg')
unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]

unknown_image2 = face_recognition.load_image_file('./img/unknown/PROD-86th-Annual-Academy-Awards-Arrivals_ED.jpg')
unknown_face_encoding2 = face_recognition.face_encodings(unknown_image2)[0]

results = face_recognition.compare_faces([gates_face_encoding],unknown_face_encoding)
results2 = face_recognition.compare_faces([gates_face_encoding],unknown_face_encoding2)
if(results[0]):
    print('First image is Bill Gates')
else:
    print('First image not Bill Gates')
if(results2[0]):
    print('Second iamge is Bill Gates')
else:
    print('Second iamge is not Bill Gates')