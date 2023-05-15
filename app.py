import os
import subprocess
import urllib.request
import contextlib
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        url = request.form.get("url")
        download_file(url)
    return render_template("index.html")

def download_file(url):
    home = os.path.expanduser("~")
    ocr_path = f"{home}/.ipython/ocr.py"
    if not os.path.exists(ocr_path):
        hCode = "https://raw.githubusercontent.com/biplobsd/OneClickRun/master/res/ocr.py"
        urllib.request.urlretrieve(hCode, ocr_path)

    # Perform MEGA installation if necessary
    if not os.path.exists("/usr/bin/mega-cmd"):
        loadingAn()
        print("Installing MEGA ...")
        runSh('sudo apt-get -y update')
        runSh('sudo apt-get -y install libmms0 libc-ares2 libc6 libcrypto++6 libgcc1 libmediainfo0v5 libpcre3 libpcrecpp0v5 libssl1.1 libstdc++6 libzen0v5 zlib1g apt-transport-https')
        runSh('sudo curl -sL -o /var/cache/apt/archives/MEGAcmd.deb https://mega.nz/linux/MEGAsync/Debian_9.0/amd64/megacmd-Debian_9.0_amd64.deb', output=True)
        runSh('sudo dpkg -i /var/cache/apt/archives/MEGAcmd.deb', output=True)
        print("MEGA is installed.")
        clear_output()

    output_path = "downloads"
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    newlines = ['\n', '\r\n', '\r']

    def unbuffered(proc, stream='stdout'):
        stream = getattr(proc, stream)
        with contextlib.closing(stream):
            while True:
                out = []
                last = stream.read(1)
                # Don't loop forever
                if last == '' and proc.poll() is not None:
                    break
                while last not in newlines:
                    # Don't loop forever
                    if last == '' and proc.poll() is not None:
                        break
                    out.append(last)
                    last = stream.read(1)
                out = ''.join(out)
                yield out

    def transfare():
        import codecs
        decoder = codecs.getincrementaldecoder("UTF-8")()
        cmd = ["mega-get", url, output_path]
        proc = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            # Make all end-of-lines '\n'
            universal_newlines=True,
        )
        for line in unbuffered(proc):
            print(line)

    transfare()

if __name__ == "__main__":
    app.run()
