from flask import Flask, render_template, Response, redirect, request
import fd_class
import fr_class
from datetime import datetime

app = Flask(__name__)

@app.route('/video_feed_fd')
def video_feed_fd():
    """Video streaming route. Put this in the src attribute of an img tag."""
    hasil = Response(fd_class.deteksi_masker(), mimetype='multipart/x-mixed-replace; boundary=frame')
    return hasil

@app.route('/video_feed_fr')
def video_feed_fr():
    """Video streaming route. Put this in the src attribute of an img tag."""
    hasil = Response(fr_class.identifikasi_wajah(), mimetype='multipart/x-mixed-replace; boundary=frame')
    return hasil

@app.route('/face_recognition_result')
def face_recognition_result():
    return  Response(fr_class.get_result())

@app.route('/mask_detection_result')
def mask_detection_result():
    return  Response(fd_class.get_result())

@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/face_recognition')
def face_recognition():
    return render_template('face_recognition.html')

@app.route('/mask_detection')
def mask_detection():
    fr_class.result = ""
    return render_template('mask_detection.html')

@app.route('/about')
def about():
    fr_class.result = ""
    fd_class.md_result = ""
    return render_template('about.html')

@app.route('/person')
def person():
    daftar_siswa = {
        'Andree': {
            'nama': 'Andree Meilio Caniago',
            'kelas': 'XI RPL 3',
            'nisn': '1920118137',
            'no_absen': '04',
            },
        'Puji': {
            'nama': 'Puji Saefuloh',
            'kelas': 'XI RPL 3',
            'nisn': '1920118160',
            'no_absen': '27',
            },
        'Shafa': {
            'nama': 'Shafa Firazty Rahadatul \'Aisy',
            'kelas': 'XI RPL 3',
            'nisn': '1920118166',
            'no_absen': '33',
            },
        'Dwi': {
            'nama': 'Mochammad Dwi Putra Julian',
            'kelas': 'XI RPL 3',
            'nisn': '1920118151',
            'no_absen': '18',
            },
        }

    siswa = request.args.get('name')
    fr_class.result = ""
    fd_class.md_result = ""
    now = datetime.now()
    waktu_absen = now.strftime("%H:%M")

    return render_template('person.html', waktu_absen = waktu_absen, photo = siswa, nama = daftar_siswa[siswa]['nama'], kelas = daftar_siswa[siswa]['kelas'], nisn = daftar_siswa[siswa]['nisn'], no_absen = daftar_siswa[siswa]['no_absen'])

if __name__ == '__main__':
    app.run(debug=True)

