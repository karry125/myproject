package Page;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;

public class CreateBx {
    public WebElement clickNew(WebDriver driver){
        return driver.findElement(By.xpath("//*[@id=\"appWraper\"]/div[2]/div[1]/div[2]/div/div/div/div[1]/div[1]/span/u"));
    }
    public WebElement clickPu(WebDriver driver){

        return  driver.findElement(By.xpath("//*[@id=\"appWraper\"]/div[2]/div[1]/div[2]/div/div/div/div[1]/div[1]/span/span/ul/li[1]"));
    }
    public WebElement clickOut(WebDriver driver){
        return driver.findElement(By.xpath("//*[@id=\"appWraper\"]/div[2]/div[1]/div[2]/div/div/div/div[1]/div[1]/span/span/ul/li[2]"));
    }

    public WebElement close(WebDriver driver){
        return driver.findElement(By.xpath("//*[@id=\"appWraper\"]/div[2]/div[1]/div[2]/div/h3/i"));
    }

}
