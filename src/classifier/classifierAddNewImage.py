from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateBatch, ImageFileCreateEntry
from msrest.authentication import ApiKeyCredentials
import os, time

#load the keys and endpoints from the configuration file
training_endpoint=''
training_key=''
prediction_endpoint=''
prediction_key=''
prediction_resource_id=''

#Authenticate the client
credentials = ApiKeyCredentials(in_headers={"Training-key": training_key})
trainer = CustomVisionTrainingClient(training_endpoint, credentials)
prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
predictor = CustomVisionPredictionClient(prediction_endpoint, prediction_credentials)

#Select the project id
project_id = ''

# Create tags
tiramisu_tag = next(t for t in trainer.get_tags(project_id) if t.name == "Tiramisu")
cannoli_tag = next(t for t in trainer.get_tags(project_id) if t.name == "Cannoli")

# Upload and tag images
images_folder = os.path.join(os.path.dirname(__file__), "images", "Train")
tags_folder_names = [ "Tiramisu", "Cannoli" ]

print("Adding images...")

for tag_num in range(0, 2):
    if tag_num == 0:
        tag = tiramisu_tag
    else:
        tag = cannoli_tag
    for batch_num in range(0, 1):
        image_list = []
        for image_num in range(62, 120):
            file_name = f"{tags_folder_names[tag_num]} ({60*batch_num + image_num}).jpg"
            with open(os.path.join(images_folder, tags_folder_names[tag_num], file_name), "rb") as image_contents:
                image_list.append(ImageFileCreateEntry(name=file_name, contents=image_contents.read(), tag_ids=[tag.id]))

        upload_result = trainer.create_images_from_files(project_id, ImageFileCreateBatch(images=image_list))
        if not upload_result.is_batch_successful:
            print("Image batch upload failed.")
            for image in upload_result.images:
                print("Image status: ", image.status)
            exit(-1)
    print(f"{tags_folder_names[tag_num]} Uploaded")
