import cv2

def extract_frames(video_path, output_dir):
  """Mengekstrak frame dari video dan menyimpannya sebagai gambar.

  Args:
    video_path: Path ke file video.
    output_dir: Direktori untuk menyimpan gambar-gambar frame.
  """

  # Buka video
  video = cv2.VideoCapture(video_path)

  # Baca frame video
  success, frame = video.read()
  count = 0

  while success:
    # Simpan frame sebagai gambar
    cv2.imwrite(f"{output_dir}/frame_{count}.jpg", frame)

    # Baca frame selanjutnya
    success, frame = video.read()
    count += 1

  # Tutup video
  video.release()

# Contoh penggunaan
video_path = "D:\BRIGHT\SEMESTER 8\S.Tr.T\_Data\Data\Seepage2.mp4"
output_dir = "D:\BRIGHT\SEMESTER 8\S.Tr.T\_Data\Data\see2"
extract_frames(video_path, output_dir)