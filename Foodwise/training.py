# Importing libraries
from clarifai_grpc.channel.clarifai_channel import ClarifaiChannel
from clarifai_grpc.grpc.api import service_pb2_grpc
from clarifai_grpc.grpc.api import service_pb2, resources_pb2
from clarifai_grpc.grpc.api.status import status_code_pb2
from json import loads
from dotenv import dotenv_values

stub = service_pb2_grpc.V2Stub(ClarifaiChannel.get_grpc_channel())
config = dotenv_values()
TOP_K = 5

# Get .env values
authentication = config["AUTH"]
modelID = config["MODEL_ID"]
# Authenticating key
metadata = (('authorization', authentication),)

def predict(file_bytes):
    """
    Predict the foods in the fridge with a multiclass visual classifier model
    """
    # Making a call to server
    request = service_pb2.PostModelOutputsRequest(
        # Food model ID
        model_id = modelID,
        inputs = [
            resources_pb2.Input(data=resources_pb2.Data(image=resources_pb2.Image(base64=file_bytes)))
        ])

    # Getting model response
    response = stub.PostModelOutputs(request, metadata=metadata)

    # Raising exception if key fails
    if response.status.code != status_code_pb2.SUCCESS:
        raise Exception("Request failed, status code: " + str(response.status.code))

    # Debug: Dump outputs
    #jsonFile = open("examples/trainresponse3.json", "w")
    #jsonFile.write(str(response))
    #jsonFile.close()
    #print(response)
    #print(name)

    # Get top k foods
    i = TOP_K
    arr_food = []
    
    for food in response.outputs[0].data.concepts:
        if i == 0:
            break
        arr_food.append(food.name)
        i -= 1
    
    return arr_food

"""
#request("https://previews.123rf.com/images/bazru/bazru1712/bazru171200015/91310895-juicy-ripe-fruits-on-a-table-in-garden.jpg")

with open("examples/foodimg1.jpg", "rb") as f:
    file_bytes = f.read()
    request(file_bytes)
"""