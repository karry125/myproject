package Opreate;

import Action.BaiduSearchPageAction;
import Page.BaiduSearchPageElements;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.firefox.FirefoxDriver;

public class BaiduSearch {
    //声明元素类和操作类
    BaiduSearchPageElements elements = new BaiduSearchPageElements();
    BaiduSearchPageAction action = new BaiduSearchPageAction();
    //定义浏览器


    //定义百度搜索操作类
    public void search(String inputKey){
        System.setProperty("webdriver.chrome.driver", "C:\\Program Files (x86)\\Google\\Chrome\\chromeDriver.exe");
        WebDriver driver = new ChromeDriver();
        //打开搜索页
        driver.get("http://www.baidu.com");
        //输入搜索词
        action.input(elements.inputFrame(driver),inputKey);
        //点击搜索按钮
        action.click(elements.searchButton(driver));
    }
}
