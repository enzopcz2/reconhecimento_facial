import face_recognition
import cv2
import os
import numpy as np

# Carregar rostos conhecidos
known_face_encodings = []
known_face_names = []

for file in os.listdir("rostos"):
    image = face_recognition.load_image_file(f"rostos/{file}")
    encoding = face_recognition.face_encodings(image)[0]   
    known_face_encodings.append(encoding)
    name = os.path.splitext(file)[0]  # Remove .jpg
    known_face_names.append(name)

# Iniciar webcam
video_capture = cv2.VideoCapture(0)

while True:
    status, frame = video_capture.read()
    if not status:
        print("❌ Falha ao capturar o frame.")
        break
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)  # Reduz a imagem
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Desconhecido"
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        color = (0, 0, 255)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]
            distance = face_distances[best_match_index]
            confidence = 1 - distance
            confidence_percent = round(confidence * 100, 2)
            name += f" ({confidence_percent}%)"
            color = (0, 255, 0)
        # Redimensiona coordenadas para imagem original
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4
        # Desenha retângulo e nome
        cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)
    # Exibe o vídeo
    cv2.imshow('Reconhecimento Facial', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()