import random, time
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.webdriver import WebDriver
from applib.human_pause import human_pause



def human_like_mouse_move(driver: WebDriver, element: WebElement) -> None:
    """
    Move move to the middle of element. with random offset: from -5 to 5 px.
    """
    driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth' });", element)
    
    actions = ActionChains(driver)
    
    print('element size: ', element.size)
    
    actions.move_to_element_with_offset(element, xoffset=random.randint(-5, 5), yoffset=random.randint(-5, 5))
    
    human_pause(0.1, 0.5)


