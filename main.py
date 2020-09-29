from bs4 import BeautifulSoup as bs
import requests
from datetime import datetime

teamUrl = "https://www.hltv.org/team/6665/astralis"

# hltvUrl = "https://www.hltv.org/"
# source = requests.get(hltvUrl)

def DateToWeekday(date):
     items = date.split("/")
     output = datetime(int(items[2]), int(items[1]), int(items[0])).weekday()
     days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
     output = days[output]
     return output

def Sprint(tupleList):
     """
     Prints tuple gathered from GetInfo() in an orderly manner
     """

     print(
          tupleList[0] +
          " Rank: " +
          tupleList[1] +
          "\nUpcoming match against: " +
          tupleList[3] +
          "\n" +
          DateToWeekday(tupleList[2]) +
          " " + tupleList[2]
     )


def GetInfo(sourceLink):
     """
     Gathers info from any team on hltv.org, from a link as parameter.\n
     returns: teamName, teamRank, upcomingMatchDates, upcomingMatchOpponent
     """
     sourceLink = source

     if source.status_code != 200:
          print("Could not retreive website.")

     soup = bs(sourceLink.content, "lxml") # using source.content to get the html

     teamName = soup.find("h1", class_= "profile-team-name text-ellipsis").text

     teamRank = soup.find("span", class_= "value").text


     upcomingMatchDates = soup.find("td", class_ = "date-cell").text

     upcomingMatchOpponent = soup.find("a", class_ = "team-name team-2").text

     return teamName, teamRank, upcomingMatchDates, upcomingMatchOpponent
     

source = requests.get(teamUrl)

myTuple = GetInfo(source)

Sprint(myTuple)
