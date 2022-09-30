# Josue Lopez.
# Created November 25th,
# Last Edited 9:28 AM

from bs4 import BeautifulSoup
import requests

# Main link for scraping
main_page = 'https://www.misabueso.com/esoterica/suenos/'
obtain_main_page = requests.get(main_page).text
second_main_page = 'https://misabueso.com/'

# Invoke beautiful soup
main_soup = BeautifulSoup(obtain_main_page, 'lxml')

# Obtaining main links of all letters of the alphabet
alphabet = main_soup.find('ul', class_='alfalist')

# Data gatherer to obtain all of the word links
alphabet_getter = [x['href'] for x in alphabet.find_all('a', href=True)]

# Loop to obtain all links
for x in range(len(alphabet_getter)):
    # Add the main_page (link) to the alphabet getter obtained link completion.
    full_alphabet_link = main_page + alphabet_getter[x]
    # print(full_alphabet_link)

    # Part of the loop to obtain all of the sublinks.
    obtain_second_main_page = requests.get(full_alphabet_link).text
    second_main_soup = BeautifulSoup(obtain_second_main_page, 'lxml')
    links_of_the_alphabet = second_main_soup.find('div', class_='paginator')
    links_of_the_alphabet_getter = [x['href'] for x in links_of_the_alphabet.find_all('a', href=True)]

    # Main subLoop to obtain all sublinks
    for xx in range(len(links_of_the_alphabet_getter)):
        full_sub_alphabet_link = second_main_page + links_of_the_alphabet_getter[xx]
        # print(full_sub_alphabet_link)
        # SubSubLoop to obtain all pre finalizing links EVERYTHING WORKS TILL HERE
        for xxx in range(len(full_sub_alphabet_link)):
            obtain_third_main_page = requests.get(full_alphabet_link).text
            obtain_fourth_main_page = requests.get(full_sub_alphabet_link).text

            third_main_soup = BeautifulSoup(obtain_third_main_page, 'lxml')
            fourth_main_soup = BeautifulSoup(obtain_fourth_main_page, 'lxml')
            extracting_pre_final_links_part_one = third_main_soup.find('ul', class_='drms-list')
            extracting_pre_final_links_part_two = fourth_main_soup.find('ul', class_='drms-list')

            storing_epflp_part_one = [x['href'] for x in extracting_pre_final_links_part_one.find_all('a', href=True)]
            storing_epflp_part_two = [x['href'] for x in extracting_pre_final_links_part_two.find_all('a', href=True)]
            for xxxx in range(len(storing_epflp_part_one)):
                full_store_epflp = second_main_page + storing_epflp_part_one[xxxx]
                print(full_store_epflp)
            for xxxxx in range(len(storing_epflp_part_two)):
                full_store_epflp = second_main_page + storing_epflp_part_one[xxxxx]
                print(full_store_epflp)