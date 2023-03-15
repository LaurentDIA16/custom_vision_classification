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
project_id = '4dc702af-8edf-4742-a0c5-5162d58cd19d'

# Create tags
pizza_tag = trainer.create_tag(project_id, "pizza")
tiramisu_tag = trainer.create_tag(project_id, "tiramisu")


# Upload and tag images
images_folder = os.path.join(os.path.dirname(__file__), "images", "Train")
tags_folder_names = [ "pizza", "tiramisu" ]

print("Adding images...")

for tag_num in range(0, 2):
    if tag_num == 0:
        tag = pizza_tag
    else:
        tag = tiramisu_tag
    for batch_num in range(0, 2):
        image_list = []
        for image_num in range(1, 61):
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

# Training
print ("Training...")
iteration = trainer.train_project(project_id,["pizza", "tiramisu"])
while (iteration.status != "Completed"):
    iteration = trainer.get_iteration(project_id, iteration.id)
    print ("Training status: " + iteration.status)
    print ("Waiting 10 seconds...")
    time.sleep(20)

# Get iteration performance information
threshold = 0.5
iter_performance_info = trainer.get_iteration_performance(project_id, iteration.id, threshold)
print("Iteration Performance:")
print(f"\tPrecision: {iter_performance_info.precision*100 :.2f}%\n"
      f"\tRecall: {iter_performance_info.recall*100 :.2f}%\n"
      f"\tAverage Precision: {iter_performance_info.average_precision*100 :.2f}%")

print("Performance per tag:")
for item in iter_performance_info.per_tag_performance:
    print(f"* {item.name}:")
    print(f"\tPrecision: {item.precision*100 :.2f}%\n"
          f"\tRecall: {item.recall*100 :.2f}%\n"
          f"\tAverage Precision: {item.average_precision*100 :.2f}%")

# Publish the current iteration
print("Publishing the current iteration...")
trainer.publish_iteration(project_id, iteration.id, prediction_resource_id)
print ("Iteration published!")


# Test - Make a prediction
print("Testing the prediction endpoint...")
test_images_folder_path = os.path.join(os.path.dirname(__file__), "images", "Test")
for img_num in range(7,12):
    test_image_filename = str(img_num) + ".jpg"
    with open(os.path.join(test_images_folder_path, test_image_filename), "rb") as image_contents:
        results = predictor.classify_image(project_id, image_contents.read())

        # Display the results
        print(f"Testing image {test_image_filename}...")
        for prediction in results.predictions:
            print(f"\t{prediction.tag_name}: {prediction.probability*100 :.2f}%")
