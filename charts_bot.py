import requests


def get_response(story_type):
	url = 'https://hacker-news.firebaseio.com/v0/' + story_type + 'stories.json'
	response = requests.get(url)
    story_id_data = response.json()

# To make HTTP calls we will use the requests library for python. Requests is an incredible library which makes it a cakewalk for making HTTP calls (GET,POST,etc) in python.

# In the above lines, first we import the requests library and declare a method get_response(story_type). Inside this method, we construct the url for making the requests. The variable story_type will take a value amongst new,top,best,show,jobs. To make a HTTP GET request we need to use the GET method of the requests library which takes the URL as input. The response.json() extracts the information and returns it in the form of a JSON.


def get_story_ids(stories, size):
    story_ids_reqd = list()
    for i in range(0, size):
        story_ids_reqd.append(stories[i])
    return story_ids_reqd

# This method extracts only the required number of Story IDs from the JSON response we have got earlier.

# We initially create an empty list story_ids_reqd which will contain the IDs of the stories we need. The argument size specifies the number of IDs we want from the response. So, we iterate size number of times and append the story IDs to the list and return the list. We could have included this logic in the first method itself, but for separation of concerns and better modularity I have extracted it as a different function. IMHO, I think a function should do exactly one thing and do it well.


def get_story_data(story_ids):
        stories = dict()

        for story_id in story_ids:
            url = 'https://hacker-news.firebaseio.com/v0/item/' + str(story_id) + '.json'
            story_response = requests.get(url)
            story_data = story_response.json()

            story_by = get_field_data(story_data,'by')
            story_title = get_field_data(story_data,'title')
            story_url = get_field_data(story_data,'url')
            story_score = get_field_data(story_data,'score')

            story_data_values = '{};{};{};{}'.format(story_by,story_title,story_url,story_score)
            stories[story_id] = story_data_values
            # In these two lines, we construct a semicolon delimited string which contains the information about the story. We assign this string as the value to story_id key of the stories dictionary.

        return stories

# This method extracts the actual story details using the story IDs we have extracted.

# The information for each of the stories is present at the API endpoint of the form https://hacker-news.firebaseio.com/v0/item/id.json. We will define a dictionary named stories which will contain the story ID as key and required information about the story as it’s value. If you are from a Java background, dictionaries are similar to Maps. We loop through each story ID present in the list of story IDs. We will again use the requests.get() method to get the response from the endpoint and convert it to JSON using the response.json() method.


def get_field_data(story_data, field):
        if field not in story_data:
            response = ''
        else:
            response = story_data[field]
        return response

# We will define a helper function called get_field_data which will fetch the field specific information from the JSON response. The information we associate with each of the stories: Story author, Story title, Story URL and it’s score.

# If the requested field is present in the data, then we return the info. If not, we will return an empty string. JSON in python3 is by default represented as a dict. We can access the objects in a dict using the square bracket notation ‘[]’. For example we have a dict say person, whose key is the Social Security Number and value name, then we can access the name like person[SSN] where SSN would be replaced by the actual social security number.

stories_all = get_response(type)
stories_reqd = get_story_ids(stories_all,size=5)
stories_data = get_story_data(stories_reqd)
print(stories_data)

# Now that we have got the required data for each story ID, the next step in would be to compose this into a flask application and deploy it on PythonAnywhere.


# Source: https://techthorpe.in/articles/2017-05/telegram-bot-part1
