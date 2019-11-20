from django.shortcuts import render
from pycricbuzz import Cricbuzz
import json
from bs4 import BeautifulSoup
from .models import News,Imag
import requests
import urllib.request

from django.http import JsonResponse


# Create your views here.
def admin(request):
    return render(request,"cric/admin.html")

def ranking(request):

   
    c = Cricbuzz()       
    matches = c.matches()
    
    page = requests.get('http://www.espncricinfo.com/rankings/content/page/211271.html')
    
    soup = BeautifulSoup(page.text, 'html.parser')
    #p1=soup.prettify()

    #tbl=soup.find_all('table')
    p1=[]
    p2=[]
    p3=[]
    p4=[]
    p5=[]
    zero=soup.find_all('table')[0]
    one=soup.find_all('table')[1]
    two=soup.find_all('table')[2]
    three=soup.find_all('table')[3]
    four=soup.find_all('table')[4]

    for x in zero:
            row=zero.find_all('tr')
            for y in row:
                tt=y.find_all('td')
                for d in tt:
                    p1.append(d.text.strip())

    for x in one:
            row=one.find_all('tr')
            for y in row:
                tt=y.find_all('td')
                for d in tt:
                    p2.append(d.text.strip())

    for x in two:
            row=two.find_all('tr')
            for y in row:
                tt=y.find_all('td')
                for d in tt:
                    p3.append(d.text.strip())
    for x in three:
            row=three.find_all('tr')
            for y in row:
                tt=y.find_all('td')
                for d in tt:
                    p4.append(d.text.strip())
    for x in four:
            row=four.find_all('tr')
            for y in row:
                tt=y.find_all('td')
                for d in tt:
                    p5.append(d.text.strip())
    



    return render(request,"cric/ranking.html",{
        "matches":matches,
        "ad1":p1,
        "ad2":p2,
        "ad3":p3,
        "ad4":p4,
        "ad5":p5,
               
        })


def match_info(request,id,src):
    '''c = Cricbuzz()
    #id=int(id)
    minfo = c.matchinfo(id)
    return render(request,"cric/matchinfo.html",{"minfo":minfo,"id":id})'''
    c = Cricbuzz()
    matches = c.matches()
    #print(json.dumps(matches, indent=4, sort_keys=True))
    return render(request,"cric/home.html",{"matches":matches,})
    #for match in matches:
        
        #if(match['mchstate'] != 'nextlive'):
            #daa=c.livescore(match['22857'])
            #print (c.commentary(match['id']))
            #print (c.scorecard(match['id']))
            #return json
            
    #return JsonResponse({"daa":daa})'''





def matchinfo(request):
    '''c = Cricbuzz()
    #id=int(id)
    minfo = c.matchinfo(id)
    return render(request,"cric/matchinfo.html",{"minfo":minfo,"id":id})'''
    c = Cricbuzz()
    matches = c.matches()
    #print(json.dumps(matches, indent=4, sort_keys=True))
   


    return render(request,"cric/home.html",{"matches":matches,})
    #for match in matches:
        
        #if(match['mchstate'] != 'nextlive'):
            #daa=c.livescore(match['22857'])
            #print (c.commentary(match['id']))
            #print (c.scorecard(match['id']))
            #return json
            
    #return JsonResponse({"daa":daa})'''








def live_score(request,id):
        
    c = Cricbuzz()    
    lscore = c.livescore(id)
    commntry=c.commentary(id)
    
    matches = c.matches()
    #vv=matches[id]['team1']['squad']
    #print(vv)
    #num=len(commntry['commentary'])
    #num=str(num)
    matches = c.matches()
    l1=[]
    l2=[]
    pl1=[]
    pl2=[]
    try:

        for i in range(len(matches)):
        
            if matches[i]['id']== id:
                l1=matches[i]['team1']['squad']
                l2=matches[i]['team2']['squad']
    except:
        print("except")
        l1=[]
        l2=[]
    try:
        if l1:
            for i in range(len(l1)):
                if i==1 or i==2 or i==5 or i==6 or i==9 or i==10:
                    pl1.append(l1[i])
                    pl2.append(l2[i])
        else:
            print("else")
                
    except:
        
        pl1=[]
        pl2=[]

    #return JsonResponse({"commntry":matches})
    overin2=0
    overin3=0
    overin1=0
    overin4=0
    try:

        overin1=lscore['batting']['score'][0]['overs']
        overin3=lscore['bowling']['score'][0]['overs']
        overin2=lscore['batting']['score'][1]['overs']
        overin4=lscore['bowling']['score'][1]['overs']
        
        #['batting']['score'[1]['overs']
        
    except:
        pass    
                           
    id1=str(id)
    
    return render(request,"cric/live.html",{
        "lscore":lscore,
        "pl1":pl1,
        "pl2":pl2,
        "commntry":commntry,        
        "overin2":overin2,
        "overin3":overin3,
        "overin1":overin1,
        "overin4":overin4,
        "id":id1,
        "matches":matches,
        })
        #print(json.dumps(lscore, indent=4, sort_keys=True))
    
      
def alldetail(request,id):
    c = Cricbuzz()    
    #print (c.scorecard(match['id']))
    alldetail = c.scorecard(id)
    
    matches = c.matches()
    bat1=0
    bowl1=0
    fall_wickets1=0
    #return JsonResponse({"alldetail":alldetail})
    try:
        bat=alldetail['scorecard'][0]['batcard']
        bowl=alldetail['scorecard'][0]['bowlcard']
        fall_wickets=alldetail['scorecard'][0]['fall_wickets']
    except:
        pass
    try:
        bat1=alldetail['scorecard'][1]['batcard']
        bowl1=alldetail['scorecard'][1]['bowlcard']
        fall_wickets1=alldetail['scorecard'][1]['fall_wickets']
    except:
        pass
        



    lscore = c.livescore(id)
    overin2=0
    overin3=0
    overin1=0
    overin4=0
    try:
        overin1=lscore['batting']['score'][0]['overs']
        overin3=lscore['bowling']['score'][0]['overs']
        overin2=lscore['batting']['score'][1]['overs']
        overin4=lscore['bowling']['score'][1]['overs']
        
    except:
        pass    

    #return JsonResponse({"bat1":fall_wickets1})

    return render(request,"cric/scorecard2.html",{
        "alldetail":alldetail,
        "bat":bat,
        "bowl":bowl,
        "fall_wickets":fall_wickets,

        "bat1":bat1,
        "bowl1":bowl1,
        "fall_wickets1":fall_wickets1,
        "lscore":lscore,
        "overin2":overin2,
        "overin3":overin3,
        "overin1":overin1,
        "overin4":overin4,
        "matches":matches,
        
        })
    
def apitest(request):
    
    c = Cricbuzz()
    matches = c.matches()
    news=News.objects.all()
    img=Imag.objects.all()
    

    #print(json.dumps(matches, indent=4, sort_keys=True))
    #return JsonResponse({"daa":news})
    return render(request,"cric/index2.html",{
        "matches":matches,
        "news":news,
        "img":img,
        })


    '''c = Cricbuzz()
    matches = c.matches()
    for match in matches:
        
        if(match['mchstate'] != 'nextlive'):
            daa=c.livescore(match['22857'])
            #print (c.commentary(match['id']))
            #print (c.scorecard(match['id']))
            #return json
            
    return JsonResponse({"daa":daa})
    '''

  
    
    #print (json.dumps(matches,indent=4)) #for pretty prinitng
    #return JsonResponse({"minfo":matches})


    #print(json.dumps(minfo, indent=4, sort_keys=True))

    
def scorelive(request):
    c = Cricbuzz() 
    id=request.POST.get("id")   
    lscore = c.livescore(id)
    commntry=c.commentary(id)
    #num=len(commntry['commentary'])
    #num=str(num)
    #return JsonResponse({"commntry":lscore})

    matches = c.matches()
    l1=[]
    l2=[]
    pl1=[]
    pl2=[]
    try:

        for i in range(len(matches)):
        
            if matches[i]['id']== id:
                l1=matches[i]['team1']['squad']
                l2=matches[i]['team2']['squad']
    except:
        print("except")
        l1=[]
        l2=[]
    try:
        if l1:
            for i in range(len(l1)):
                if i==1 or i==2 or i==5 or i==6 or i==9 or i==10:
                    pl1.append(l1[i])
                    pl2.append(l2[i])
        else:
            print("else")
                
    except:
        
        pl1=[]
        pl2=[]


    overin2=0
    overin3=0
    overin1=0
    overin4=0
    try:
        overin1=lscore['batting']['score'][0]['overs']
        overin3=lscore['bowling']['score'][0]['overs']
        overin2=lscore['batting']['score'][1]['overs']
        overin4=lscore['bowling']['score'][1]['overs']
        
        
        
        #['batting']['score'[1]['overs']
        
    except:
        pass    
                           
    id1=str(id)
    return render(request,"cric/refreshlive.html",{
        "lscore":lscore,
        "commntry":commntry,   
        "pl1":pl1,
        "pl2":pl2,     
        "overin2":overin2,
        "overin3":overin3,
        "overin1":overin1,
        "overin4":overin4,
        "id":id1,
        })
        
    
def calender(request):
    
    url="http://cricapi.com/api/matchCalendar"

    data=requests.get(url).json()
    return JsonResponse({"data":data})

