# import requests

# url = "http://52.42.17.90/segment"

# data_dict = {"bounding_box": [[ 1261, 511, 1493, 1032]], "input_video":"https://skoutwatch-videos.s3.eu-north-1.amazonaws.com/1739012950196_2932301-uhd_4096_2160_24fps.mp4"}
# response = requests.post(url, json=data_dict).json()
# print(response)


import requests

url = "http://34.209.240.233//api/v1/books/40"


response = requests.get(url)
print(response)

print(response.json())
