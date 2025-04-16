import wikipedia
import wikipediaapi



x=input('Enter the word for info:')
search_results=[]
search=wikipedia.search(x)
print(search)
search_results.append(search)

page_summary=wikipedia.summary(x)
print('summary is as follows:',page_summary)

'''
with open('summary.txt','w') as summary:
    summary.writelines(page_summary)
'''

#commenting out the above code cuz i dont want to write the summary again and again 

wiki=wikipediaapi.Wikipedia(user_agent='your-user-agent',language='en')   #selecting english langauge

page=wiki.page(x)

if page.exists():
    print(f'Title: {page.title}')
    print(f'Summary: {page.summary[:1000]}')
else:
    print('page not found')    