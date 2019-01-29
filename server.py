from flask import Flask, Response, send_from_directory
import subprocess

app = Flask(__name__)


@app.route('/gpu_processes')
def gpu_processes():
  out = subprocess.Popen(['nvidia-smi', '--query-compute-apps=pid,process_name,used_memory', '--format=csv'],
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)

  stdout, stderr = out.communicate()

  return Response(stdout, mimetype='text')

@app.route('/gpu_utilization')
def gpu_utilization():
  out = subprocess.Popen(['nvidia-smi', '--query-gpu=temperature.gpu,memory.total,memory.used,memory.free,timestamp', '--format=csv'],
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)

  stdout, stderr = out.communicate()

  return Response(stdout, mimetype='text')

@app.route('/')
def index():
    return send_from_directory('page', 'index.html')

@app.route('/<path>')
def send_js(path):
    return send_from_directory('page', path)



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=6050)
