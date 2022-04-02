package TestCase;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.annotations.Test;

public class TestOther {
    @Test
    public void TestClose(){
        System.setProperty("webdriver.chrome.driver", "C:\\Program Files (x86)\\Google\\Chrome\\chromeDriver.exe");
        WebDriver driver = new ChromeDriver();
       // driver = webdriver.Firefox()
        driver.get("http://www.runoob.com/try/try.php?filename=tryjs_alert");
        driver.switchTo().frame("iframeResult");
        ((ChromeDriver) driver).findElementByXPath("html/body/input").click();
         driver.switchTo().alert().accept();
    }

    @Test
    public void JsTest(){
        System.setProperty("webdriver.chrome.driver", "C:\\Program Files (x86)\\Google\\Chrome\\chromeDriver.exe");
        WebDriver driver = new ChromeDriver();

        driver.get("https://kyfw.12306.cn/otn/index/init");
        //去掉元素的readonly属性
        String js = "document.getElementById('train_date').removeAttribute('readonly')";
        ((ChromeDriver) driver).executeScript(js);
// 用js方法输入日期
        String js_value = "document.getElementById('train_date').value='2016-12-25'";
        ((ChromeDriver) driver).executeScript(js_value);
    }
}
