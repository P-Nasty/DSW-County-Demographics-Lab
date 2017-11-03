from flask import flask, url_for,render_template, request, Markup, flash
import json
import os
app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)
@app.route("/")
def main():
   return render_template("demographics.html")
   """ with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
        state = get_state_options
    get_state_options(counties)
    fun_fact(state)"""
    

"""def alphabetically_first_county(counties):
    Return the county with the name that comes first alphabetically.
    first = counties[0]["County"]
    for c in counties:
        if c["County"]< first:
            first = c["County"]
    return first


def county_most_under_18(counties):
    first = counties[0]["Age"]["Percent Under 18 Years"]
    second = counties[0]["County"]
    third = counties[0]["State"]
    for c in counties:
        if c["Age"]["Percent Under 18 Years"] > first:
            first = c["Age"]["Percent Under 18 Years"] 
            second = c["County"]
            third = c["State"]
    return second, third
    
    

    
def percent_most_under_18(counties):
    first = counties[0]["Age"]["Percent Under 18 Years"]
    for c in counties:
        if c["Age"]["Percent Under 18 Years"] > first:
            first = c["Age"]["Percent Under 18 Years"]
    return first
  

    
def most_under_18(counties):
    first = counties[0]["Age"]["Percent Under 18 Years"]
    second = counties[0]["County"]
    third = counties[0]["State"]
    for c in counties:
        if c["Age"]["Percent Under 18 Years"] > first:
            first = c["Age"]["Percent Under 18 Years"] 
            second = c["County"]
            third = c["State"]
    fourth = [first,second,third]
    return fourth
    

    
def state_with_most_counties(counties):
    dict = {"AL":0}
    first = counties[0]["State"]
    second = 0
    third = counties[0]["State"]
    for c in counties: 
        first = c["State"]
        if first in dict:
            dict[first] += 1 
        else:
            dict[first] = 1
    for c in dict:
        if dict[c] > second:
            second = dict[c]
            third = c
    return third
            
        
  
    #Make a dictionary that has a key for each state and the values keep track of the number of counties in each state
    
    #Find the state in the dictionary with the most counties
    
    #Return the state with the most counties
    
    
def your_interesting_demographic_function(counties):
    first = counties[0]["Age"]["Percent Under 18 Years"]
    second = counties[0]["County"]
    third = counties[0]["State"]
    for c in counties:
        if c["Age"]["Percent Under 18 Years"] < first:
            first = c["Age"]["Percent Under 18 Years"] 
            second = c["County"]
            third = c["State"]
    return second, third"""
     """Compute and return an interesting fact using the demographic data about the counties in the US."""

"""def get_state_options(counties):
    first = []
    second = ""
    for c in counties:
        first.append(c["state])
    for c in first:
        second += Markup("<option value=\"" + c + "\">" + c + "</option>")
    rendertemplate(demographics.html, list = second)
    return first                  
def fun_fact(state):
    counter = 0;
    for c in counties:
        if c["state"] = states[counter]:
            
             
        for c in first:
            second += second + c
    rendertemplate(demographics.html, first) """                      
                     
  


if __name__=="__main__":
    app.run(debug=False, port=54321)
