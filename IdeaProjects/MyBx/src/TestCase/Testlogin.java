package TestCase;

import Action.BaiduSearchPageAction;
import Opreate.BaiduSearch;
import Opreate.Login;
import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeTest;
import org.testng.annotations.Test;

import java.io.IOException;

public class Testlogin {
    BaiduSearch testSearch = new BaiduSearch();
    Login loginBy= new Login();
   // @Test
    public void searchHelloWorld() {
        testSearch.search("123");
    }

  //  @Test
    //测试输入随机字符
   // public void searchCode() {
       // testSearch.search("Q￥#@%Y……");
    //}

   // @Test
    //测试留空
   // public void searchBlock() {
     //   testSearch.search("");
    //}

    public void setTestSearch(BaiduSearch testSearch) {
        this.testSearch = testSearch;
    }
    @Test
    public void LoginCaiyun() throws InterruptedException, IOException {

        loginBy.LoginPhone("13738056812","w12345678");

    }
    @AfterClass
    public void tearDown() throws InterruptedException{

        Thread.sleep(2000);
    }
    public void cookielogin() throws InterruptedException {

        loginBy.cookielogin();

    }
}
