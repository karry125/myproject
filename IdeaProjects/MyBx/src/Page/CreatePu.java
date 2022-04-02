package Page;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;

public class CreatePu {
  public WebElement textcontent(WebDriver driver){
      return driver.findElement(By.xpath("//*[@id=\"appWraper\"]/div[2]/div[1]/div[2]/div/div/div[1]/div/div[2]/span/textarea"));

  }
    public WebElement clicktype(WebDriver driver){
        return driver.findElement(By.xpath("//*[@id=\"appWraper\"]/div[2]/div[1]/div[2]/div/div/div[3]/div[2]/div/span/u"));

    }
    public WebElement clickselef(WebDriver driver){
        return driver.findElement(By.xpath("//*[@id=\"appWraper\"]/div[2]/div[1]/div[2]/div/div/div[3]/div[2]/div/span/span/ul/li[1]"));

    }
public  WebElement clicktypes(WebDriver driver){
      return driver.findElement(By.xpath("//*[@id=\"appWraper\"]/div[2]/div[1]/div[2]/div/div/div[3]/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div[2]/div/a/div[1]"));
}

    public WebElement clicktime(WebDriver driver){
        return driver.findElement(By.xpath("//*[@id=\"appWraper\"]/div[2]/div[1]/div[2]/div/div/div[3]/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/div[2]/span/div/input"));

    }
    public WebElement inputmoney(WebDriver driver){
        return driver.findElement(By.xpath("//*[@id=\"appWraper\"]/div[2]/div[1]/div[2]/div/div/div[3]/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[3]/div/div[2]/input"));

    }
    public  WebElement inputdec(WebDriver driver){
      return driver.findElement((By.xpath("//*[@id=\"appWraper\"]/div[2]/div[1]/div[2]/div/div/div[3]/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[2]/span/textarea")));
    }
    public  WebElement inputphoto(WebDriver driver){
        return driver.findElement((By.xpath("//*[@id=\"F-jh4jkwy77\"]/label")));
    }
    public  WebElement clickture(WebDriver driver){
        return driver.findElement((By.xpath("//*[@id=\"appWraper\"]/div[2]/div[1]/div[2]/div/div/div[3]/div[2]/div/div/div[2]/div/div/div/div[3]/div/button[2]")));
    }

}
