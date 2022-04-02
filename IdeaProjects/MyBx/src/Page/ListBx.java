package Page;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;

public class ListBx {

    public java.util.List<WebElement> clickleft(WebDriver driver) {
        return driver.findElements(By.className(("item-3UUV4")));

    }

}
