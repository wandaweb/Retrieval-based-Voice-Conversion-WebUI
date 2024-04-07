import os
import sys
from infer.modules.uvr5.modules import uvr

path = os.environ["UVR_FILE"]
model = os.environ["UVR_MODEL"] 
output_folder = os.environ["UVR_OUT"]
format = os.environ["UVR_FORMAT"]

print("Splitting into vocals and instrumentals:", path)

obj = type('obj', (object,), {'name' : path})
for i in uvr(model, "", output_folder, [obj], output_folder, "10", format):
    print(i)
        
print("Finished.")

