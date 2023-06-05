# # import subprocess
# # from pathlib import Path
# # BASE_DIR = Path(__file__).resolve().parent.parent
# # ccext_loc = f'C:\Program Files (x86)\CCextractor\ccextractor'
# # # command = '8849331ddae9c3169024d569ce17b9a4fdd917401cd6c6bfb8dc1fd59c6af21e.mp4'
# # cdd = "-out=txt"+str(BASE_DIR)+ '/videos/' + "8849331ddae9c3169024d569ce17b9a4fdd917401cd6c6bfb8dc1fd59c6af21e.mp4 -o outputvids"
# # subprocess.run(ccext_loc+' '+cdd)
# # # # ccextractor
# #
# # # subprocess.
# with open(r'C:\Users\xmate\PycharmProjects\eco\eco\videos\8849331ddae9c3169024d569ce17b9a4fdd917401cd6c6bfb8dc1fd59c6af21e.srt', 'r') as file:
#     text = file.readlines()
#     for i in text:
#         print(i)
import re

def btaunga(file_path, phrase):
    with open(file_path, 'r') as f:
        content = f.read()
    phrase = phrase.upper()
    # pattern = r'\d+\n(\d+:\d+:\d+,\d+) --> (\d+:\d+:\d+,\d+)\n(.+)?{}'.format(phrase)
    matches = re.findall(r'\d+\n\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}\n(.+?)\n\n', content, re.DOTALL)

    results  = []

    for match in matches:
        timestamps = re.search(r'(\d{2}:\d{2}:\d{2},\d{3}) --> (\d{2}:\d{2}:\d{2},\d{3})', match)
        results.append((timestamps, match.strip()))

    return results

file_path = r'C:\Users\xmate\PycharmProjects\eco\eco\Outputvids'
phrase = 'hi'

timest = btaunga(file_path, phrase)
print(timest)