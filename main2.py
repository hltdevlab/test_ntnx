
import ntnx_clustermgmt_py_client
from ntnx_clustermgmt_py_client.rest import ApiException
from ntnx_config import config
import traceback
# response_type='clustermgmt.v4.config.ListClustersApiResponse'
from ntnx_clustermgmt_py_client.models.OneOfclustermgmt.v4.config.ListClustersApiResponsedata import ListClustersApiResponsedata

if __name__ == "__main__":
    client = ntnx_clustermgmt_py_client.ApiClient(configuration=config)
    clusters_api = ntnx_clustermgmt_py_client.ClustersApi(api_client=client)
    
    page = 0
    
    limit = 50


    try:
        api_response = clusters_api.list_clusters(_page=page, _limit=limit)
        print(api_response)
    except ApiException as e:
        print(e)
    except KeyError as e:
        print(f"The KeyError: {e}")
        traceback.print_exc()

