#Dictionary of responses
intent_response_dict = {
    "intro": ["I am GSU bot.  I answer your queries related to Georgia State University.  I can provide information"
              "related to location, CS department location, area, GSU university type, cost of attendance, Chair-person"
              "of CS department, Machine learning professor, departments at GSU"],
    "greet":["Hi","Hello","What's up","Hey","How are you","How are you doing"],
    "goodbye":["Bye","See you","Bye! Have a good one!","It was nice talking to you!"],
    "affirm":["Hey"]
}

gsu_info_dict = {
    "location": "Downtown Atlanta GA USA is the location of Georgia State University",
    "cs-location": "25 Park Pl Atlanta GA USA is address of Computer Science department",
    "area": "518 Acres is the total area",
	"type": "Public University",
	"cost": "$48000 is the cost of attendance",
	"chair-person": "Dr. Yi Pan is the chair-person",
	"professor": "Dr. Zhipeng Cai is the machine learning professor",
    "faq_link": "https://www.gsu.edu",
    "departments":"Computer Science, Political Science, History, Physics, Biology, Maths, many more",
    "gsu-intro":"Georgia State University is a public research university situated in Downtown, Atlanta, USA"
}

def gsu_info(entities):
    entity_value = entities[0].get('type')
    print(entity_value)
    for key,value in gsu_info_dict.items():
        if key == entity_value:
           return(value)
           flag = 'yes'
    if(flag != 'yes'):
       return "Please refer to " + gsu_info_dict["faq_link"]
