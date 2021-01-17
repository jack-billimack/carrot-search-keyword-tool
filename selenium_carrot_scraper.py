from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import config

# This sets up the Firefox-based webdriver we will use.
# If configured correctly, a blank Firefox browser tab will pop-up.
driver = webdriver.Firefox(executable_path=config.driver_path)
wait = WebDriverWait(driver, 100)

def search_carrot(keyword_input):
    # This is the Carrot Tool URL which we will enter into the browser. We string format the keywords into the URL.
    carrot_search_url = "https://search.carrot2.org/#/search/web/{0}/folders".format(keyword_input)


    # request the url and wait for a specific CSS class to load  
    driver.get(carrot_search_url)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'TopCluster')))


def scrape_keywords():
    # We want to gather keyword terms associated with our keyword input. Here is scaffolding for that dict.
    keyword_dict = {
                'keyword':[], 
                'occurances':[] 
                    }

    # The code below uses a Python "For-Loop" to iterate over the keyword results and write them to our dict.
    table = driver.find_element_by_css_selector(".ClusterList")

    for row in table.find_elements_by_css_selector(".TopCluster"):
        
        kwd = row.find_elements_by_css_selector(".labels")[0].text
        keyword_dict['keyword'].append(kwd)
    
        occurance = row.find_elements_by_css_selector(".meta")[0].text
        keyword_dict['occurances'].append(occurance)

    return keyword_dict


def scrape_sources():
    # We want to gather keyword sources associated with our keyword input. Here is scaffolding for that dict.
    source_dict = {
                    'title':[], 
                    'description':[], 
                    'url':[], 
                    'source':[], 
                    'cluster':[]
                }

    # The code below uses a Python "For-Loop" to iterate over the keyword source links and write them to our dict.
    table = driver.find_element_by_css_selector(".ResultList")
    
    for row in table.find_elements_by_css_selector(".Result"):
        
        title = row.find_element_by_css_selector("strong").text
        source_dict['title'].append(title)

        description = row.find_element_by_css_selector("div").text 
        source_dict['description'].append(description)

        url = row.find_elements_by_css_selector(".url")[0].text
        source_dict['url'].append(url)

        source = row.find_elements_by_css_selector(".sources")[0].text
        source_dict['source'].append(source)

        cluster = row.find_elements_by_css_selector(".ResultClusters")[0].text
        source_dict['cluster'].append(cluster)

    return source_dict

if __name__ == '__main__':
    # This is an input prompt where you tell the code what keyword to look up.
    # Note that you can enter multiple words separated by a comma.
    keyword_input = input("\n PLEASE ENTER KEYWORD PHRASE \n") 

    search_carrot(keyword_input)

    # Assign dictionary variables
    keyword_dictionary = scrape_keywords()
    source_dictionary = scrape_sources()

    # Create Pandas Dataframes from dictionary variables
    import pandas as pd
    keyword_df = pd.DataFrame(keyword_dictionary)
    source_df = pd.DataFrame(source_dictionary)

    print(keyword_df)
    print(source_df)

    # Send our DataFrames to local csv files
    keyword_df.to_csv('./results/keyword_results.csv')
    source_df.to_csv('./results/keyword_source_results.csv')