package Opreate;

import Action.BaiduSearchPageAction;
import Page.CreatePu;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.Select;

public class CreatePuOpreate {

    CreatePu create=new CreatePu();
    BaiduSearchPageAction action = new BaiduSearchPageAction();


    public void create(){
       action.input(create.textcontent(Login.driver),"123");
       action.click(create.clicktype(Login.driver));
       action.click(create.clickselef(Login.driver));
        Select selectAge = new Select(create.clicktypes(Login.driver));
        selectAge.selectByIndex(2);
       String js_value = "document.getElementsByClassName('text-input-2JzoH')[0].value='行政采购/办公用品'";
        ((ChromeDriver) Login.driver) .executeScript(js_value);
        //String js = "document.getElementsByClassName('.ant-calendar-picker-input.ant-input')[0].removeAttribute('readonly')";
       // ((ChromeDriver) Login.driver).executeScript(js);
        String js_valuee = "document.getElementsByClassName('.ant-calendar-picker-input.ant-input')[0].value='2018/05/13'";

        ((ChromeDriver) Login.driver) .executeScript(js_valuee);
        action.input(create.inputmoney(Login.driver),"5.5");
        action.input(create.inputdec(Login.driver),"456");
        action.click(create.clickture(Login.driver));
    }
}
