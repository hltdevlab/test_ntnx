import ntnx_clustermgmt_py_client

config = ntnx_clustermgmt_py_client.Configuration()
config.scheme = "http"
# IPv4/IPv6 address or FQDN of the cluster
config.host = "127.0.0.1"
# Port to which to connect to
config.port = 9440
# Max retry attempts while reconnecting on a loss of connection
config.max_retry_attempts = 3
# Backoff factor to use during retry attempts
config.backoff_factor = 3
# UserName to connect to the cluster
config.username = "admin"
# Password to connect to the cluster
config.password = "password123"

config.logger_file = "log.txt"
