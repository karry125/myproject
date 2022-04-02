package Opreate;

import Action.BaiduSearchPageAction;
import Page.BaiduSearchPageElements;
import Page.LoginPage;
import org.apache.commons.io.FileUtils;
import org.openqa.selenium.*;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;

import java.io.File;
import java.io.IOException;

public class Login {
    BaiduSearchPageElements elements = new BaiduSearchPageElements();
    BaiduSearchPageAction action = new BaiduSearchPageAction();
    LoginPage page= new LoginPage();
    //定义浏览器
    public static WebDriver driver;

    //定义百度搜索操作类
    public void LoginPhone(String inputKey,String Password) throws InterruptedException, IOException {
        //配置文件地址

        System.setProperty("webdriver.chrome.driver", "C:\\Program Files (x86)\\Google\\Chrome\\chromeDriver.exe");
        //声明chromeoptions,主要是给chrome设置参数
        ChromeOptions options = new ChromeOptions();
        options.addArguments("disable-infobars","user-data-dir=C:\\Users\\asus\\AppData\\Local\\Google\\Chrome\\User Data\\Default");

    //实例化chrome对象，并加入选项
         driver = new ChromeDriver();
        //打开搜索页
        driver.get("https://web.jituancaiyun.com/#/login");
        Cookie c=new Cookie("_NOWUID","76608960");
        Cookie c1=new Cookie("deviceId","web_30fa2f0faf86e66069c287cf3990c322");
        Cookie c2=new Cookie("mobile","13738056812");
        Cookie c3=new Cookie("token","00276b88e3d6a40f0cc346df74e72321");
        Cookie c4=new Cookie("userId","76608960");
        Cookie c5=new Cookie("timeStamp","1525795372528773");
        Cookie c6=new Cookie("uiapp","%7B%22orgId%22%3A84472%2C%22orgName%22%3A%22%E6%B5%8B%E8%AF%95%E4%BC%81%E4%B8%9A-%E7%8E%8B%E5%B9%BC%E6%95%8F%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8%E5%90%BE%E9%97%AE%E6%97%A0%E4%B8%BA%E8%B0%93%E6%97%A0%22%2C%22name%22%3A%22%E7%8E%8B%E5%B9%BC%E6%95%8F%22%2C%22mobile%22%3A%2213738056812%22%2C%22superAdmin%22%3A0%2C%22subOrg%22%3Afalse%2C%22teamOrg%22%3Afalse%2C%22uid%22%3A%2276608960%22%7D");
        Cookie c7=new Cookie("userInfo","%7B%22orgId%22%3A84472%2C%22orgName%22%3A%22%E6%B5%8B%E8%AF%95%E4%BC%81%E4%B8%9A-%E7%8E%8B%E5%B9%BC%E6%95%8F%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8%E5%90%BE%E9%97%AE%E6%97%A0%E4%B8%BA%E8%B0%93%E6%97%A0%22%2C%22name%22%3A%22%E7%8E%8B%E5%B9%BC%E6%95%8F%22%2C%22mobile%22%3A%2213738056812%22%2C%22superAdmin%22%3A0%2C%22subOrg%22%3Afalse%2C%22teamOrg%22%3Afalse%2C%22uid%22%3A%2276608960%22%7D");
        Cookie c8=new Cookie("userName","%E7%8E%8B%E5%B9%BC%E6%95%8F");
        Cookie c9=new Cookie("sca","99cd01bf");
        Cookie a1=new Cookie("_scn","a24c5df6S24e0ad43S163407dc581Se81c");
        Cookie a2=new Cookie("atpsida","824f43e8fd3b01d984064410_1525795171_1");
        Cookie a3=new Cookie("cna","Y7d4E4C+e2ACAXPHZ/+mvBJ6");


        driver.manage().addCookie(c);
        driver.manage().addCookie(c1);
        driver.manage().addCookie(c2);
        driver.manage().addCookie(c3);
        driver.manage().addCookie(c4);
        driver.manage().addCookie(c5); driver.manage().addCookie(c6);
        driver.manage().addCookie(c7);
        driver.manage().addCookie(c8);
        driver.manage().addCookie(c9);
        driver.manage().addCookie(a1);
        driver.manage().addCookie(a2);
        driver.manage().addCookie(a3);
        driver.navigate().refresh();
        action.click(page.clickBatton(driver));

        //点击搜索按钮
        action.click(page.clickFrame(driver));
        //输入搜索词
        action.input(page.inputAccount(driver),inputKey);
        //点击搜索按钮
        action.input(page.inputPassword(driver),Password);
        action.click(page.clickLoginBatton(driver));
        // wait(10);
        // System.out.print(driver.get());
       Thread.sleep(2000);
        File srcFile = ((TakesScreenshot)driver).getScreenshotAs(OutputType.FILE);
        //利用FileUtils工具类的copyFile()方法保存getScreenshotAs()返回的文件对象。
        FileUtils.copyFile(srcFile, new File("screenshot.png"));
        //((ChromeDriver) driver).getScreenshotAs("/Screenshots/foo.png");
        if(page.clickLOrgn(driver).size() !=0){
            System.out.print(  page.clickLOrgn(driver).size());
            action.click(page.clickLOrgn(driver).get(1));
           //action.click(page.clickLoginOrg(driver));
           // action.click(page.clickLOrgn(driver).get(1));
            action.click(page.clickCaidan(driver));
        }
        Thread.sleep(2000);
        File srcFile1 = ((TakesScreenshot)driver).getScreenshotAs(OutputType.FILE);
        FileUtils.copyFile(srcFile1, new File("screenshot1.png"));
        // 选取警告弹窗
       // Alert alert=driver.switchTo().alert();
        // 点击取消按钮
       // alert.accept();
    }

    public void cookielogin() throws InterruptedException {
        System.setProperty("webdriver.chrome.driver", "C:\\Program Files (x86)\\Google\\Chrome\\chromeDriver.exe");
        WebDriver driver = new ChromeDriver();
        driver.get("https://web.jituancaiyun.com/#/login");
        Cookie c=new Cookie("_NOWUID","76608960");
        Cookie c1=new Cookie("deviceId","web_30fa2f0faf86e66069c287cf3990c322");
        Cookie c2=new Cookie("mobile","13738056812");
        Cookie c3=new Cookie("token","00276b88e3d6a40f0cc346df74e72321");
        Cookie c4=new Cookie("userId","76608960");
        Cookie c5=new Cookie("timeStamp","1525795372528773");
        Cookie c6=new Cookie("uiapp","%7B%22orgId%22%3A84472%2C%22orgName%22%3A%22%E6%B5%8B%E8%AF%95%E4%BC%81%E4%B8%9A-%E7%8E%8B%E5%B9%BC%E6%95%8F%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8%E5%90%BE%E9%97%AE%E6%97%A0%E4%B8%BA%E8%B0%93%E6%97%A0%22%2C%22name%22%3A%22%E7%8E%8B%E5%B9%BC%E6%95%8F%22%2C%22mobile%22%3A%2213738056812%22%2C%22superAdmin%22%3A0%2C%22subOrg%22%3Afalse%2C%22teamOrg%22%3Afalse%2C%22uid%22%3A%2276608960%22%7D");
        Cookie c7=new Cookie("userInfo","%7B%22orgId%22%3A84472%2C%22orgName%22%3A%22%E6%B5%8B%E8%AF%95%E4%BC%81%E4%B8%9A-%E7%8E%8B%E5%B9%BC%E6%95%8F%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8%E5%90%BE%E9%97%AE%E6%97%A0%E4%B8%BA%E8%B0%93%E6%97%A0%22%2C%22name%22%3A%22%E7%8E%8B%E5%B9%BC%E6%95%8F%22%2C%22mobile%22%3A%2213738056812%22%2C%22superAdmin%22%3A0%2C%22subOrg%22%3Afalse%2C%22teamOrg%22%3Afalse%2C%22uid%22%3A%2276608960%22%7D");
        Cookie c8=new Cookie("userName","%E7%8E%8B%E5%B9%BC%E6%95%8F");
        Cookie c9=new Cookie("sca","99cd01bf");
        Cookie a1=new Cookie("_scn","a24c5df6S24e0ad43S163407dc581Se81c");
        Cookie a2=new Cookie("atpsida","824f43e8fd3b01d984064410_1525795171_1");
        Cookie a3=new Cookie("cna","Y7d4E4C+e2ACAXPHZ/+mvBJ6");


        driver.manage().addCookie(c);
        driver.manage().addCookie(c1);
        driver.manage().addCookie(c2);
        driver.manage().addCookie(c3);
        driver.manage().addCookie(c4);
        driver.manage().addCookie(c5); driver.manage().addCookie(c6);
        driver.manage().addCookie(c7);
        driver.manage().addCookie(c8);
        driver.manage().addCookie(c9);
        driver.manage().addCookie(a1);
        driver.manage().addCookie(a2);
        driver.manage().addCookie(a3);
        driver.navigate().refresh();
        action.click(page.clickBatton(driver));
        wait(3);
        page.clickLOrgn(driver).size();
        action.click(page.clickLOrgn(driver).get(2));
       // driver.get("https://web.jituancaiyun.com/#/login");


    }
}
