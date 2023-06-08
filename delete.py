from kubernetes import client, config

# Load Kubernetes configuration
config.load_kube_config()

# Create a Kubernetes API client
api_client = client.ApiClient()

# Delete the existing deployment
api_instance = client.AppsV1Api(api_client)
api_instance.delete_namespaced_deployment(
    name="my-flask-app",
    namespace="default",
    body=client.V1DeleteOptions(propagation_policy='Foreground')
)

print("Existing deployment deleted successfully!")