from flask import Flask, render_template
import subprocess

app = Flask(__name__)

@app.route("/")
def dashboard():
    vm_name = subprocess.getoutput("hostname")
    cpu_info = subprocess.getoutput("nproc")
    ram_info = subprocess.getoutput("free -h | grep Mem")
    disk_info = subprocess.getoutput("df -h / | tail -1")
    
    return render_template("vm_dashboard.html",
                           vm_name=vm_name,
                           cpu=cpu_info,
                           ram=ram_info,
                           disk=disk_info)

if __name__ == "__main__":
    app.run(debug=True)
