from flask import Flask
app =Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World'

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8080, debug=True)
    


runtime: python
env: flex
entrypoint: gunicorn -b :$PORT main:app

runtime_config:
    python_version: 3

manual_scaling:
    instances: 1
resources:
cpu: 1
memory_gb: 0.5
disk_size_gb: 10


Flask==2.0.2
gunicorn==20.1.0
