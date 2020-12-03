from flask import Flask, render_template, Response
import cv2
from fd_class import tes
from fr_class import deteksi

app = Flask(__name__)

camera = cv2.VideoCapture(0)  # use 0 for web camera
#  for cctv camera use rtsp://username:password@ip_address:554/user=username_password='password'_channel=channel_number_stream=0.sdp' instead of camera

def gen_frames():  # generate frame by frame from camera
    while True:
        # Capture frame-by-frame
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    hasil = Response(tes(), mimetype='multipart/x-mixed-replace; boundary=frame')
    print(hasil)
    # return Response(kelas.initialize(), mimetype='multipart/x-mixed-replace; boundary=frame')
    return hasil


@app.route('/video_feed_fr')
def video_feed_fr():

    

    """Video streaming route. Put this in the src attribute of an img tag."""
    hasil = Response(deteksi(), mimetype='multipart/x-mixed-replace; boundary=frame')

    print("")
    print("isi deteksi")
    print(hasil)
    print("")

    # return Response(kelas.initialize(), mimetype='multipart/x-mixed-replace; boundary=frame')
    return hasil

@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

