
from selenium.webdriver.common.by import By
class StudentLocator:
  all_student_loc=(By.XPATH,'//li[contains(@class,"all")]')
  sen_student_loc =(By.XPATH,'//div[@class="all-list"]//li[2]')
  msg_loc = (By.XPATH,'//div[@class="all-list"]//li[2]//a[@class="call"]')
  chat_input_loc =(By.XPATH,'//textarea[@class="ps-container"]')
  send_msg_loc = (By.XPATH,'//div[@class="btn-group"]//a[text()="发送"]')
  error_toast_loc= (By.XPATH,'//div[@class="gTips"]//span')
  msg_list_loc=(By.XPATH,'//div[@class="m-message ps-container"]//li')
  close_chat_loc =(By.XPATH,'//a[@class="layui-layer-ico layui-layer-close layui-layer-close2"]')