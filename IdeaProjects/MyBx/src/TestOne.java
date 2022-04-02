import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.firefox.FirefoxDriver;

public class TestOne {

public void login() {
    System.setProperty("webdriver.chrome.driver", "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe");
    WebDriver driver = new ChromeDriver();
    driver.get("http://nvsm.cnki.net/KNS/");
}

    public static void main(String[] args) {
        // TODO Auto-generated method stub
        System.setProperty("webdriver.chrome.driver", "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe");
        WebDriver driver = new ChromeDriver();
        driver.get("https://www.baidu.com/");
        driver.close();

    }
}
