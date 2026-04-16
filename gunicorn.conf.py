# gunicorn.conf.py — tuned for t3.micro (1 vCPU, 1 GB RAM)
bind = "0.0.0.0:5000"
workers = 2          # 2 * CPUs is enough; keep RAM free
threads = 2
worker_class = "sync"
timeout = 90         #
keepalive = 5
max_requests = 500   # recycle workers to avoid memory leaks
max_requests_jitter = 50
accesslog = "-"
errorlog = "-"
loglevel = "info"
