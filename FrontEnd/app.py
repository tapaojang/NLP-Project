from flask import Flask, render_template, request
import os

app = Flask(__name__)

# หน้าแรก
@app.route('/')
def upload_file():
    return render_template('upload.html')

# ฟังก์ชันรับไฟล์ที่อัปโหลด
@app.route('/uploader', methods=['POST'])
def uploader():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filepath = os.path.join('uploads', file.filename)
            file.save(filepath)
            return 'File uploaded successfully'
    return 'No file uploaded'

if __name__ == '__main__':
    app.run(debug=True)
