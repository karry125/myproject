package Page;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
 import  java.util.List;
public class LoginPage {

    //封装搜索关键字输入框
    public WebElement clickFrame(WebDriver driver){
        return driver.findElement(By.xpath("//*[@id=\"app\"]/div/div[2]/div[2]/div/div/div[1]/div/label[2]/span[2]"));
    }

    public WebElement inputAccount(WebDriver driver){
        return  driver.findElement(By.xpath("//*[@id=\"app\"]/div/div[2]/div[2]/div/div/div[2]/div/div/div[1]/input"));
    }
    public WebElement inputPassword(WebDriver driver){
        return  driver.findElement(By.xpath("//*[@id=\"app\"]/div/div[2]/div[2]/div/div/div[2]/div/div/div[2]/input"));
    }
    public WebElement clickBatton(WebDriver driver){
        return driver.findElement(By.xpath("//*[@id=\"app\"]/div/div[2]/div[2]/div/div/div[3]/span/span"));
    }
    public WebElement clickLoginBatton(WebDriver driver){
        return driver.findElement(By.xpath("//*[@id=\"app\"]/div/div[2]/div[2]/div/div/div[2]/div/div/button"));
    }
    //java.util.List<WebElement>
    public java.util.List<WebElement> clickLOrgn(WebDriver driver){
       return driver.findElements(By.className("item-368vZ"));
        //return driver.findElements(By.xpath("//*[@id=\"app\"]/div/div[2]/div/div/div"));
        //return driver.findElement(By.xpath("//*[text()='测试王幼敏']']"));
}
 public java.util.List<WebElement>  Clickorg(WebDriver driver){
        return driver.findElements(By.className("dropitem-RB6Po item-3-fsO"));
 }
    public WebElement clickLoginOrg(WebDriver driver){
        return driver.findElement(By.xpath("//*[@id=\"appWraper\"]/div[1]/div/div[1]/div/div/div[1]/div/span"));
    }
    public WebElement clickCaidan(WebDriver driver){
        return driver.findElement(By.xpath("//*[@id=\"appWraper\"]/div[1]/div/div[2]/a[7]/span/span/span"));
    }

}
