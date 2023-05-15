from roboflow import Roboflow
rf = Roboflow(api_key="LyJzwGuVAAqXUwBL0kHC")
project = rf.workspace().project("ribworth")
model = project.version(3).model
def weed_locator(image_name):
    k=model.predict("your_image.jpg", confidence=30, overlap=20).json()
    return(k)


# infer on a local image
print(model.predict("your_image.jpg", confidence=30, overlap=20).json())

# visualize your prediction
model.predict("your_image.jpg", confidence=30, overlap=20).save("prediction.jpg")
array=['1','2','3','4','5','6']
for i in range(6):
    image_path="image" + array[i] + ".jpg"
    save_path="prediction" + array[i] + ".jpg"
    # infer on a local image
    print(model.predict(image_path, confidence=10, overlap=10).json())

# visualize your prediction
    model.predict(image_path, confidence=10, overlap=10).save(save_path)

# infer on an image hosted elsewhere
# print(model.predict("URL_OF_YOUR_IMAGE", hosted=True, confidence=40, overlap=30).jsond