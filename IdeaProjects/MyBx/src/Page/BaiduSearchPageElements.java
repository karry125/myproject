package Page;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;

public class BaiduSearchPageElements {

    //封装搜索关键字输入框
    public WebElement inputFrame(WebDriver driver){
        return driver.findElement(By.id("kw"));
    }

    //封装搜索按钮
    public WebElement searchButton(WebDriver driver){
        return driver.findElement(By.id("su"));
    }
}
