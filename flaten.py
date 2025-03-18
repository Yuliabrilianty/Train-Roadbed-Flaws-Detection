import cv2
import numpy as np

# Ganti dengan alamat IP atau URL streaming kamera Anda
video_src = "rtsp://Brillianty:mytapoo@192.168.0.100:554/stream1"

# Baca video dari kamera
cap = cv2.VideoCapture(video_src)

# Parameter intrinsik kamera (jika sudah dikalibrasi)
# fx, fy, cx, cy, distCoeffs = ...
cameraMatrix = [1198.867401715405, 0, 1028.951702159298], [0, 1198.742906815016, 551.6495813405396], [0, 0, 1]
distCoeffs = [-0.3634752204592028, 0.1888997006275953, -0.001205262391897054, -0.001669215669126604, -0.06137070097553191]
# Matriks rotasi dan proyeksi (jika diperlukan)
# R, P = ...

# Buat peta de-warping
map1, map2 = cv2.initUndistortRectifyMap(
    cameraMatrix, distCoeffs, (1280, 720), cv2.CV_32FC1
)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # De-warping frame
    undistorted_frame = cv2.remap(frame, map1, map2, cv2.INTER_LINEAR)

    # Tampilkan hasil
    cv2.imshow("Original Frame", frame)
    cv2.imshow("Undistorted Frame", undistorted_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()