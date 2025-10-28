# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the API key from the environment
api_key = os.environ.get("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY environment variable not set.")

# Configure the client library
genai.configure(api_key=api_key)

# Construct the path to the image file
script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "sample_data", "gemini_logo.png")

# Upload a sample file to the File API
display_name = "Gemini Logo"
sample_file = genai.upload_file(path=file_path, display_name=display_name)
print(f"Uploaded file '{sample_file.display_name}' as: {sample_file.uri}")

# Get the file back from the API
get_file = genai.get_file(name=sample_file.name)
print(f"Retrieved file '{get_file.display_name}' as: {get_file.uri}")


# Generate content using the file
prompt = "Describe the image with a creative description"
model = genai.GenerativeModel(model_name="gemini-1.5-flash")
response = model.generate_content([prompt, sample_file])
print(response.text)

# Delete the file
genai.delete_file(name=sample_file.name)
print(f"Deleted file {sample_file.display_name}")
