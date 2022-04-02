package Opreate;

import Action.BaiduSearchPageAction;
import Page.CreateBx;
import org.apache.commons.io.FileUtils;
import org.openqa.selenium.OutputType;
import org.openqa.selenium.TakesScreenshot;

import java.io.File;
import java.io.IOException;

public class CreateOpreate {

     CreateBx create=new CreateBx();
    BaiduSearchPageAction action = new BaiduSearchPageAction();

    public void clickNew() throws IOException, InterruptedException {
        action.click(create.clickNew(Login.driver));
        action.click(create.clickPu(Login.driver));
        File srcFile = ((TakesScreenshot)Login.driver).getScreenshotAs(OutputType.FILE);
        //利用FileUtils工具类的copyFile()方法保存getScreenshotAs()返回的文件对象。
        FileUtils.copyFile(srcFile, new File("create.png"));
        Thread.sleep(1000);
       // action.click(create.close(Login.driver));

    }

    public void clickOut() throws InterruptedException {
        action.click(create.clickNew(Login.driver));
        action.click(create.clickOut(Login.driver));
        Thread.sleep(1000);
        action.click(create.close(Login.driver));
    }
}
