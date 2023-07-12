import nltk
import spacy
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
# Set up the WebDriver
driver = webdriver.Chrome("chromedriver.exe")  # Replace with the path to your ChromeDriver executable

# Log in to LinkedIn
driver.get('https://www.linkedin.com/')
sleep(2)  # Wait for the page to load

email_input = driver.find_element(By.ID, 'session_key')

email_input.send_keys('----@gmail.com')  # Replace with your LinkedIn email
password_input = driver.find_element(By.ID, 'session_password')
password_input.send_keys('password')  # Replace with your LinkedIn password
sleep(5)
login_button = driver.find_element(By.CSS_SELECTOR, '[data-id="sign-in-form__submit-btn"]')
login_button.click()
sleep(15)  # Wait for the login to complete
#
# Navigate to competitor's profile
competitor_profile_url = 'https://www.linkedin.com/in/abhie16/'  # Replace with the URL of the competitor'
driver.get(competitor_profile_url)
sleep(6)  # Wait for the profile page to load
#
# Access competitor's connections
connect_button = driver.find_element(By.CSS_SELECTOR, 'a[href*="/search/results/people/?connectionOf"]')
connect_button.click()
sleep(5)  # Wait for the connections page to load

# # Extract new connections
new_connections = driver.find_elements(By.CLASS_NAME, 'scaffold-layout__main')
print(new_connections)

# Initialize NLP tools
nltk.download('punkt')
nlp = spacy.load('en_core_web_sm')
#
for connection in new_connections:
    # Extract relevant details of the connection
    connection = driver.find_element (By.CSS_SELECTOR, "--")
    profile_url = connection.get_attribute ('href')

    print (profile_url)    # You can extract additional information about the connection here
#
    # Analyze connection profile
    driver.get(profile_url)
    sleep(2)  # Wait for the profile page to load

    # Extract relevant information from the connection's profile
    about_section = driver.find_element (By.CSS_SELECTOR,'--').text
    print(about_section)
    job_description = driver.find_element (By.CSS_SELECTOR,'').text
    print (job_description)
    name_element = driver.find_element (By.CSS_SELECTOR,'--')
    connection_name = name_element.text
    print (connection_name)

    # Perform NLP analysis on the extracted information
    about_section_keywords = nltk.word_tokenize(about_section)
    print (about_section_keywords)

    job_description_keywords = nltk.word_tokenize(job_description)
    print (job_description_keywords)

    # Generate personalized message based on the extracted keywords
    message = f"Hi {connection_name},\n\n"
    message += "I noticed that in your 'About Us' section, you mentioned keywords such as "
    message += ", ".join(about_section_keywords[:3])  # Include the first 3 keywords
    message += ". It's great to see your focus on these areas.\n\n"
    message += "In your job description, I found keywords like "
    message += ", ".join(job_description_keywords[:3])  # Include the first 3 keywords
    message += ". I'm particularly interested in these aspects as well.\n\n"
    message += "I believe our shared interests and expertise could lead to valuable insights and collaboration. "
    message += "Let's connect and explore potential synergies.\n\n"
    message += "Looking forward to connecting with you!\n\n"
    message += "Best regards,\n"
    message += "[your Name]"



# Send connection request
    connect_button = driver.find_element (By.CLASS_NAME, '--')
    connect_button.click ()

    sleep(1)  # Wait for the connection request modal to open

    add_note_button = driver.find_element (By.CSS_SELECTOR, '--')
    add_note_button.click ()
    sleep (1)  # Wait for the note section to load

    note_input = driver.find_element (By.CSS_SELECTOR, '--')
    note_input.send_keys (message)  # Replace with your personalized message
    send_button = driver.find_element (By.CSS_SELECTOR, '--')
    send_button.click ()
    sleep (2)  # Wait for the connection request to be sent


# Close the WebDriver
driver.quit()

