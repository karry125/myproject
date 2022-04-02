package Action;

import org.openqa.selenium.WebElement;

import java.util.List;
import java.util.ArrayList;
public class BaiduSearchPageAction {

    //定义输入操作
    public void input(WebElement element, String inputKey){
        element.clear();
        element.sendKeys(inputKey);
    }

    //点击按钮操作
    public void click(WebElement element){
        element.click();
    }
    //点击按钮操作
    public void clicks( List<WebElement> element,int a){
        List<WebElement> elements=new ArrayList<WebElement>();
        // element[a].click();
    }
}
