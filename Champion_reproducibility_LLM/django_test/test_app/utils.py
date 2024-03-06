import openai
import os
import time
from datetime import datetime
from django import forms

class MethodForm(forms.Form):
    method_text = forms.CharField(widget=forms.Textarea)

def count_total_words(text):
    words = text.split()
    total_words = len(words)
    return total_words
def generate_method_section(message):
    openai.api_key = "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"
    message1 = "please generate a method section that ensures that the following result and \
        discussion section is reproducible. Only output the method section, \
        no need to write my result section nor the discussion and conclusion section again."

    message1 += message

    # max_tokens = 4097
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": message1}],
        max_tokens = 4096-1000-count_total_words(message1)
    )
    return response.choices[0].message.content.strip()

def generate_original_score(message):
    openai.api_key = "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"
    message1 = "please score the following method section based on how well the following result and discussion section \
        can be reproduced on a scale 0-1 with 0 meaning that the result can't be reproduced and 1 meaning that the result can be reproduced perfectly. \
            please put the score on first line,and add <br> behind the score, and put the rest of the content after the second line"

    message1 += message

    # max_tokens = 4097
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": message1}],
        max_tokens = 4096-1000-count_total_words(message1)
    )
    return response.choices[0].message.content.strip()

def generate_score(message):
    openai.api_key = "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"
    message1 = "please score the following method section based on how well the following result and discussion section \
        can be reproduced on a scale 0-1 with 0 meaning that the result can't be reproduced and 1 meaning that the result can be reproduced perfectly. \
            please put the score on first line,and add <br> behind the score, and put the rest of the content after the second line"

    message1 += message

    # max_tokens = 4097
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": message1}],
        max_tokens = 4096-1000-count_total_words(message1)
    )
    return response.choices[0].message.content.strip()


# user_input = input("> ")

# timestamp1 = datetime.now().strftime("%Y%m%d%H%M%S%f")[:-3]  # Current time in YYYYMMDDHHMMSSmmm format
# response1 = generate_method_section(user_input)
# timestamp2 = datetime.now().strftime("%Y%m%d%H%M%S%f")[:-3]  # Current time in YYYYMMDDHHMMSSmmm format
# # wait_and_display_countdown(30)
# response2 = generate_sscore(response1)
# # wait_and_display_countdown(30)

# file_name1 = f"{timestamp1}method_section.txt"
# with open(file_name1, "w") as file:
#     file.write(response1)

# file_name2 = f"{timestamp2}score.txt"
# with open(file_name2, "w") as file:
#     file.write(response2)

# print("Generated method section: {}".format(response1))
# print("The reproducible score is: {}".format(response2))