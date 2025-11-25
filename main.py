import urllib3
from ntnx_clustermgmt_py_client import ApiClient, Configuration
# from ntnx_clustermgmt_py_client.api import ClusterApi
from ntnx_clustermgmt_py_client.rest import ApiException
from ntnx_clustermgmt_py_client.api import ClustersApi

# Suppress SSL warnings for insecure connections (for testing/dev only)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# --- Configuration ---
# Replace with your Prism Central IP/FQDN, username, and password
PC_IP = "127.0.0.1"
USERNAME = "admin"
PASSWORD = "password123"

# --- API Client Setup ---
config = Configuration()
# config.host = f"http://{PC_IP}:9440/api/clustermgmt/v4.0" # Adjust API version if needed
config.scheme = "http"
config.host = PC_IP
config.username = USERNAME
config.password = PASSWORD
config.verify_ssl = False # Set to True in production and provide certs if needed

api_client = ApiClient(config)

# --- Cluster API Instance ---
cluster_api = ClustersApi(api_client)
# cluster_api_instance = ntnx_clustermgmt_py_client.api.ClusterApi(api_client=api_client)


try:
    # --- Get a list of all clusters ---
    # You can add parameters like 'count', 'offset', 'filter', etc.
    # For example, to get details of a specific cluster by its external ID:
    # cluster_details = cluster_api.get_cluster(extId="your_cluster_ext_id")
    
    cluster_list_response = cluster_api.list_clusters()
    
    print("List of Clusters:")
    for cluster in cluster_list_response.data:
        print(f"  Name: {cluster.name}, External ID: {cluster.ext_id}")

    # --- Example: Get details of the first cluster found ---
    if cluster_list_response.data:
        first_cluster_ext_id = cluster_list_response.data[0].ext_id
        print(f"\nDetails for Cluster (External ID: {first_cluster_ext_id}):")
        cluster_details = cluster_api.get_cluster(extId=first_cluster_ext_id)
        print(f"  Cluster Name: {cluster_details.data.name}")
        print(f"  Number of Nodes: {cluster_details.data.nodes.number_of_nodes}")
        # Add more details as needed
        
except ApiException as e:
    print(f"Error calling Nutanix API: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
